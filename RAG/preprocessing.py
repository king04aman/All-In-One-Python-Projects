import nltk
from nltk.tokenize import sent_tokenize
from PyPDF2 import PdfReader
from io import BytesIO
from docx import Document

nltk.download('punkt')

def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ''
    for page in reader.pages:
        text += page.extract_text() + '\n'
    return text

def extract_text_from_txt(txt_file_path):
    with open(txt_file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    paragraphs = [paragraph.text for paragraph in doc.paragraphs]
    text = '\n'.join(paragraphs)
    return text

def chunk_text(text, chunk_size=5):
    sentences = sent_tokenize(text)
    return [' '.join(sentences[i:i + chunk_size]) for i in range(0, len(sentences), chunk_size)]
