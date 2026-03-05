# Invoice Copilot

Invoice Copilot is a Python + Streamlit project that automatically extracts structured data from invoices (PDFs, including Greek text), computes features, and generates Excel reports.

---

## Features

- Extract invoice fields using an LLM (OpenRouter free model `arcee-ai/trinity-large-preview:free`)
- Handle multiple items per invoice
- Include product codes, descriptions, quantities, prices, and totals
- Generate Excel reports with structured rows per product
- Streamlit web interface for PDF upload and Excel download

---

## Setup Instructions


1. Clone the repo:

   ```bash
    git clone https://github.com/gvellos/PdfAfent.git
    cd PdfAfent

2. Create a virtual environment and activate it:
   
    python3 -m venv .venv
   
    source .venv/bin/activate  # Linux / macOS
   
    .venv\Scripts\activate     # Windows

3. Install dependencies:
   
    pip install --upgrade pip
   
    pip install -r requirements.txt

4.  Set up environment variables:

    Create a .env file in the root directory with:

    OPENROUTER_API_KEY=your_openrouter_api_key

5. Run the Streamlit App
   
   streamlit run app.py
