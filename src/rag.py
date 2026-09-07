"""
RAG (Retrieval-Augmented Generation) module for EcoMind AI.
Retrieves context from sustainability guidelines and campus energy policy documents.
"""

import os
import glob
import re

def load_knowledge_base(kb_dir: str = "data/knowledge_base") -> list[dict]:
    """
    Load text and markdown policy documents from knowledge base directory.
    """
    documents = []
    if not os.path.exists(kb_dir):
        return documents

    files = glob.glob(os.path.join(kb_dir, "*.txt")) + glob.glob(os.path.join(kb_dir, "*.md"))
    
    for filepath in files:
        if os.path.basename(filepath) == "README.md":
            continue
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                filename = os.path.basename(filepath)
                # Split document into sections by headers or paragraphs
                sections = [sec.strip() for sec in content.split("\n\n") if len(sec.strip()) > 30]
                for idx, sec in enumerate(sections):
                    documents.append({
                        "filename": filename,
                        "section_id": f"{filename}#sec-{idx+1}",
                        "content": sec,
                    })
        except Exception as e:
            continue

    return documents

def retrieve_context(query: str, kb_dir: str = "data/knowledge_base", top_k: int = 3) -> list[dict]:
    """
    Retrieve top_k relevant policy/guideline snippets using lightweight term frequency scoring.
    """
    documents = load_knowledge_base(kb_dir)
    if not documents:
        return []

    # Clean query terms
    query_terms = set(re.findall(r"\w+", query.lower()))
    stop_words = {"what", "is", "the", "a", "an", "and", "or", "in", "on", "at", "to", "for", "of", "with", "how", "can", "we", "should"}
    query_terms = query_terms - stop_words

    if not query_terms:
        return documents[:top_k]

    scored_docs = []
    for doc in documents:
        text = doc["content"].lower()
        score = 0
        for term in query_terms:
            count = len(re.findall(r"\b" + re.escape(term) + r"\b", text))
            score += count * 2.0
            if term in doc["filename"].lower():
                score += 1.0

        if score > 0:
            scored_docs.append((score, doc))

    scored_docs.sort(key=lambda x: x[0], reverse=True)
    return [doc for score, doc in scored_docs[:top_k]]
