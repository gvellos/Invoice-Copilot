# agents/excel_agent.py
import pandas as pd

class ExcelReportAgent:
    def run(self, invoice, features, output_path):
        # Flatten invoice for Excel: one row per item
        rows = []
        for item in invoice.items:
            row = {
                # "invoice_number": invoice.invoice_number,
                # "invoice_date": invoice.invoice_date,
                # "due_date": invoice.due_date,
                # "vendor_name": invoice.vendor_name,
                # "vendor_vat": invoice.vendor_vat,
                # "currency": invoice.currency,
                # "subtotal": invoice.subtotal,
                # "tax_amount": invoice.tax_amount,
                # "total_amount": invoice.total_amount,
                # Item-specific fields using dot notation
                "item_product_code": item.product_code,
                "item_description": item.description,
                "item_quantity": item.quantity,
                "item_unit_price": item.unit_price,
            }
            rows.append(row)

        df = pd.DataFrame(rows)

        # Write to Excel
        df.to_excel(output_path, index=False, engine="openpyxl")
        print(f"✅ Excel report saved to {output_path}")