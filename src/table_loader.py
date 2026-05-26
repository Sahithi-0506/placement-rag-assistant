import pdfplumber
from langchain_core.documents import Document

PDF_PATH = "data/Placement_RAG_Dataset_Enhanced.pdf"

def load_company_table():
    documents = []

    with pdfplumber.open(PDF_PATH) as pdf:
        page = pdf.pages[1]  # page 2 has company eligibility table
        tables = page.extract_tables()

        for table in tables:
            for row in table[1:]:
                if row and row[0]:
                    text = f"""
Company: {row[0]}
Minimum CGPA: {row[1]}
Maximum Backlogs: {row[2]}
Package: {row[3]} LPA
Bond: {row[4]} years
Key Topics: {row[5]}
Tech Focus: {row[6]}
"""
                    documents.append(
                        Document(
                            page_content=text,
                            metadata={"section": "company_eligibility", "company": row[0]}
                        )
                    )

    return documents