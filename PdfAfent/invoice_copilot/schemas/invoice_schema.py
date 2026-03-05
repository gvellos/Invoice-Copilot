from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    product_code: str
    description: str
    quantity: float
    unit_price: float

class InvoiceSchema(BaseModel):
    invoice_number: str
    invoice_date: str      # ISO format: YYYY-MM-DD
    due_date: str          # ISO format: YYYY-MM-DD
    vendor_name: str
    vendor_vat: str
    currency: str
    subtotal: float
    tax_amount: float
    total_amount: float
    items: List[Item]