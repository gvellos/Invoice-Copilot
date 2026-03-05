import pdfplumber

class InvoiceIngestionAgent:

    def run(self, file_path: str) -> dict:
        text = ""

        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        if not text.strip():
            raise ValueError(f"No text found in PDF: {file_path}. Is it a scanned PDF?")

        return {"raw_text": text}