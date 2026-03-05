import streamlit as st
import tempfile
from invoice_copilot.main import InvoiceCopilot


st.title("AI Invoice Copilot")

uploaded_file = st.file_uploader("Upload invoice", type=["pdf"])

if uploaded_file:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

    copilot = InvoiceCopilot()

    if st.button("Process Invoice"):

        structured, features = copilot.process(pdf_path, "output.xlsx")

        st.success("Invoice processed!")

        # st.json(structured.model_dump())

        with open("output.xlsx", "rb") as f:
            st.download_button(
            "Download Excel",
            data=open("output.xlsx", "rb"),
            file_name="invoice.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )