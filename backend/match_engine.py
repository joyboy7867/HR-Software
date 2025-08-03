from sentence_transformers import SentenceTransformer, util
from extract import extract_text
import pandas as pd
import os
# Load once
def matching():
    model = SentenceTransformer('intfloat/e5-base-v2')

# Extract text
    resumes = [f for f in os.listdir("resumes") if f.endswith((".pdf", ".docx"))]
    jds = [f for f in os.listdir("jds") if f.endswith((".pdf", ".docx"))]

    jd_data = []
    for jd in jds:
        text = extract_text(os.path.join("jds", jd))
        if text.strip():
            emb = model.encode(f"passage: {text}", convert_to_tensor=True)
            jd_data.append((jd, emb))

    results = []
    for res in resumes:
        res_text = extract_text(os.path.join("resumes", res))
        if not res_text.strip():
            continue
        res_emb = model.encode(f"query: {res_text}", convert_to_tensor=True)

        for jd_name, jd_emb in jd_data:
            score = util.cos_sim(res_emb, jd_emb)[0][0].item()
            results.append({
                "Resume": res,
                "JD": jd_name,
                "Match %": round(score * 100, 2)
            })

    # --- Show table ---
    df = pd.DataFrame(results).sort_values(by="Match %", ascending=False)
    df.reset_index(drop=True, inplace=True)
    print(df)
    return(df)