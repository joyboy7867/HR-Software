from sentence_transformers import SentenceTransformer, util
from extract import extract_text
import os

model = SentenceTransformer('intfloat/e5-base-v2')

def smart_query(user_query, top_k=10):
    query_emb = model.encode(f"query: {user_query}", convert_to_tensor=True)

    resumes = [f for f in os.listdir("resumes") if f.endswith((".pdf", ".docx"))]
    scored = []

    for res in resumes:
        text = extract_text(os.path.join("resumes", res))
        if not text.strip():
            continue
        res_emb = model.encode(f"passage: {text}", convert_to_tensor=True)
        score = util.cos_sim(query_emb, res_emb)[0][0].item()
        scored.append({
            "Resume": res,
            "Score": round(score * 100, 2)
        })

    return sorted(scored, key=lambda x: x["Score"], reverse=True)[:top_k]