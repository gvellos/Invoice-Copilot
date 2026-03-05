from invoice_copilot.agents.ingestion_agent import InvoiceIngestionAgent
from invoice_copilot.agents.extraction_agent import InvoiceExtractionAgent 
from invoice_copilot.agents.feature_agent import InvoiceFeatureAgent
from invoice_copilot.agents.excel_agent import ExcelReportAgent


class InvoiceCopilot:

    def __init__(self):

        # Initialize agents
        self.ingestion = InvoiceIngestionAgent()
        self.extraction = InvoiceExtractionAgent()
        self.features = InvoiceFeatureAgent()
        self.excel = ExcelReportAgent()

    def process(self, pdf_path: str, output_path: str):
        """
        Full pipeline:
        PDF → Text → Structured Invoice → Features → Excel
        """

        print("📄 Reading PDF...")
        raw_data = self.ingestion.run(pdf_path)

        print("🧠 Structuring invoice with LLM...")
        structured = self.extraction.run(raw_data)

        print("📊 Computing features...")
        features = self.features.run(structured)

        print("📁 Writing Excel...")
        self.excel.run(structured, features, output_path)

        print("✅ Pipeline completed")

        return structured, features