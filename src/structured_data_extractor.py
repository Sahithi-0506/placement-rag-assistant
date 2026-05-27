import pdfplumber

PDF_PATH = "data/Placement_RAG_Dataset_Enhanced.pdf"

def extract_company_records():
    records = []

    with pdfplumber.open(PDF_PATH) as pdf:
        page = pdf.pages[1]
        tables = page.extract_tables()

        for table in tables:
            for row in table[1:]:
                if row and row[0]:
                    records.append({
                        "company": row[0],
                        "min_cgpa": float(row[1]),
                        "max_backlogs": int(row[2]),
                        "package_lpa": float(row[3]),
                        "bond_years": int(row[4]),
                        "key_topics": row[5],
                        "tech_focus": row[6]
                    })

    return records