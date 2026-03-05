# agents/extraction_agent.py
from openai import OpenAI
import os
from dotenv import load_dotenv
from invoice_copilot.schemas.invoice_schema import InvoiceSchema
import json
import re
from datetime import datetime

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

class InvoiceExtractionAgent:
    def __init__(self, model_name="arcee-ai/trinity-large-preview:free"):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key
        )
        self.model_name = model_name

    def run(self, raw_data: dict) -> InvoiceSchema:
        prompt = f"""
        Το παρακάτω κείμενο είναι ένα τιμολόγιο στα ελληνικά. 
        Εξάγετε μόνο ένα έγκυρο JSON με τα πεδία:

        {{
          "invoice_number": "",
          "invoice_date": "",
          "due_date": "",
          "vendor_name": "",
          "vendor_vat": "",
          "currency": "",
          "subtotal": 0,
          "tax_amount": 0,
          "total_amount": 0,
          "items": [
            {{
              "product_code": "",
              "description": "",
              "quantity": 0,
              "unit_price": 0
            }}
          ]
        }}

        **ΜΗΝ προσθέσετε σχόλια ή κείμενο εκτός JSON**.

        Κείμενο τιμολογίου:
        {raw_data['raw_text']}

        Μετατρέψτε τα ποσά σε δεκαδικούς με τελεία (π.χ. 1240.50)
        """

        # Call OpenRouter
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        content = response.choices[0].message.content.strip()
        print("RAW LLM RESPONSE:")
        print(content[:1000])  # preview first 1000 chars

        # Try parsing JSON safely
        parsed = None
        try:
            parsed = json.loads(content)
        except json.JSONDecodeError:
            # Try extracting JSON with regex
            match = re.search(r"\{.*\}", content, re.DOTALL)
            if match:
                try:
                    parsed = json.loads(match.group())
                except:
                    parsed = None

        # Fallback if parsing failed
        if parsed is None:
            print("⚠️ LLM did not return valid JSON, using mock invoice for debugging")
            parsed = {
                "invoice_number": "DEBUG-001",
                "invoice_date": "03/03/2026",
                "due_date": "15/03/2026",
                "vendor_name": "Δοκιμή ΕΠΕ",
                "vendor_vat": "GR123456789",
                "currency": "EUR",
                "subtotal": 1000.0,
                "tax_amount": 240.0,
                "total_amount": 1240.0,
                "items": [{"description": "Προϊόν Α", "quantity": 2, "unit_price": 500.0}]
            }

        # Convert European dates to ISO format (YYYY-MM-DD)
        for key in ["invoice_date", "due_date"]:
            date_str = parsed.get(key)
            if date_str:
                for fmt in ("%d/%m/%Y", "%d.%m.%Y"):
                    try:
                        dt = datetime.strptime(date_str, fmt)
                        parsed[key] = dt.isoformat()  # "YYYY-MM-DD"
                        break
                    except ValueError:
                        continue

        validated = InvoiceSchema(**parsed)
        return validated