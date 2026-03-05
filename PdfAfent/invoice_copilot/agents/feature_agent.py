import pandas as pd
from datetime import datetime

class InvoiceFeatureAgent:
    def run(self, invoice):
        # Safe parsing of invoice_date
        invoice_date = None
        if invoice.invoice_date:
            try:
                invoice_date = datetime.fromisoformat(invoice.invoice_date)
            except ValueError:
                invoice_date = None

        # Safe parsing of due_date
        due_date = None
        if invoice.due_date:
            try:
                due_date = datetime.fromisoformat(invoice.due_date)
            except ValueError:
                due_date = None

        features = {
            "total_amount": invoice.total_amount,
            "subtotal": invoice.subtotal,
            "tax_amount": invoice.tax_amount,
            "num_items": len(invoice.items),
            "invoice_day": invoice_date.day if invoice_date else None,
            "invoice_month": invoice_date.month if invoice_date else None,
            "invoice_year": invoice_date.year if invoice_date else None,
            "due_day": due_date.day if due_date else None,
            "due_month": due_date.month if due_date else None,
            "due_year": due_date.year if due_date else None,
        }

        return features