import docx

# agents/breakdown_agent.py

def breakdown_doc(doc):
    """
    Break down the document into sections (paragraphs, tables, etc.)
    For now, we will just return a list of paragraphs.
    """
    sections = []
    for para in doc.paragraphs:
        if para.text.strip():
            sections.append({"type": "paragraph", "content": para.text})
    return sections

