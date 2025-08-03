from flask import Flask, request, jsonify
from match_engine import matching
from werkzeug.utils import secure_filename
from flask_cors import CORS
from smart import smart_query
from flask import send_from_directory

import os 
app = Flask(__name__)
CORS(app)
# Configure folders
RESUME_FOLDER = 'resumes'
JD_FOLDER = 'jds'

os.makedirs(RESUME_FOLDER, exist_ok=True)
os.makedirs(JD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'pdf', 'docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route("/Existing",methods=["GET"])
def check():
    df = matching()
    results = df.to_dict(orient="records")

    return jsonify({
        "message": "match done",
        "results": results
    })


@app.route('/upload', methods=['POST'])
def upload():
    # Save resumes and JDs
    # Call scoring function
    
    if not any(key in request.files for key in ['resumes', 'jds']):
        return jsonify({"error": "No resumes or JDs uploaded"}), 400

    # Save resumes
    resume_files = request.files.getlist("resumes")
    for file in resume_files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(RESUME_FOLDER, filename))
            print(f"Saved resume: {filename}")

    # Save JDs
    jd_files = request.files.getlist("jds")
    for file in jd_files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(JD_FOLDER, filename))
            print(f"Saved JD: {filename}")
    df = matching()

    # Convert it to list of dicts so Flask can jsonify it
    results = df.to_dict(orient="records")

    return jsonify({
        "message": "Upload and match done",
        "results": results
    })

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    query = data.get('query', '')
    if not query:
        return jsonify({"error": "Query is required"}), 400

    results = smart_query(query)
    return jsonify({"results": results})

@app.route('/resumes/<filename>')
def download_resume(filename):
    return send_from_directory('resumes', filename, as_attachment=True)
if __name__ == '__main__':
    app.run(debug=True)
