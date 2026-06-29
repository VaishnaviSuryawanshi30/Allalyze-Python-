import PyPDF2
from nltk.tokenize import sent_tokenize, word_tokenize

def analyze_pdf(path):
    reader = PyPDF2.PdfReader(path)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + " "

    # Case: Scanned or image-based PDF
    if not text.strip():
        return {
            "pages": len(reader.pages),
            "error": "No extractable text found (possibly scanned PDF)"
        }

    try:
        words = word_tokenize(text.lower())
        sentences = sent_tokenize(text)
    except LookupError:
        # Fallback if NLTK data is missing
        words = text.lower().split()
        sentences = text.split(".")

    return {
        "pages": len(reader.pages),
        "word_count": len(words),
        "sentence_count": len(sentences),
        "character_count": len(text),
        "text_preview": text[:500] + "..."
    }