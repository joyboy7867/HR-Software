import pdfplumber
import docx
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            return " ".join(p.extract_text() or "" for p in pdf.pages)
    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        return " ".join([p.text for p in doc.paragraphs])
    return ""
