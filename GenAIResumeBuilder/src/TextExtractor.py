import pythoncom
import win32com.client
from docx import Document
import PyPDF2
import easyocr
import re
import os
import textract

from src.constants import Config


class TextExtractor:
    def __init__(self, file_path):
        self.file_path = file_path

    def extract_text(self) -> str:
        extension = self.file_path.split(".")[-1].lower()
        if extension in Config.ALLOWED_EXTENSIONS:
            if extension == "docx":
                text = self.extract_text_from_docx()
            elif extension == "doc":
                text = self.extract_text_from_doc()
            elif extension == "pdf":
                text = self.extract_text_from_pdf()
            elif extension == "jpeg" or extension == "jpg":
                text = self.extract_text_from_image()

        return text

    def extract_text_from_docx(self) -> str:
        doc = Document(self.file_path)
        text = "\n\n".join([paragraph.text for paragraph in doc.paragraphs])
        text = re.sub("\s[,.]", ",", text)
        text = re.sub("[\n]+", "\n", text)
        text = re.sub("[\s]+", " ", text)
        text = re.sub("http[s]?(://)?", "", text)
        text = text.replace("\\", "")

        return text

    def extract_text_from_doc(self) -> str:
        text = textract.process(self.file_path).decode()
        text = re.sub("\s[,.]", ",", text)
        text = re.sub("[\n]+", "\n", text)
        text = re.sub("[\s]+", " ", text)
        text = re.sub("http[s]?(://)?", "", text)
        text = text.replace("\\", "")

        return text.strip()

    def extract_text_from_pdf(self) -> str:
        with open(self.file_path, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            num_pages = len(reader.pages)
            text = ""
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text += page.extract_text()
        return text

    def extract_text_from_image(self) -> str:
        reader = easyocr.Reader(["en"])
        result = reader.readtext(self.file_path)

        text = "\n".join([text_info[1] for text_info in result])
        return text