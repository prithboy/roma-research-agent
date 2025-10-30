from roma import tool
from PyPDF2 import PdfReader

@tool("read_pdf", description="Reads text from a local PDF file.")
def read_pdf(path: str):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text[:4000]  # limit text length for brevity
