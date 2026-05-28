import pdfplumber

PDF_PATH = "data/Placement_RAG_Dataset_Enhanced.pdf"


def extract_company_records():
    records = []
    with pdfplumber.open(PDF_PATH) as pdf:
        table = pdf.pages[1].extract_tables()[0]
        for row in table[1:]:
            if row and row[0]:
                records.append({
                    "company": row[0].replace(";", "").strip(),
                    "min_cgpa": float(row[1]),
                    "max_backlogs": int(row[2]),
                    "package_lpa": float(row[3]),
                    "bond_years": int(row[4]),
                    "key_topics": row[5].strip(),
                    "tech_focus": row[6].strip()
                })
    return records


def extract_hiring_records():
    records = []
    with pdfplumber.open(PDF_PATH) as pdf:
        for page_index in [5, 6]:
            tables = pdf.pages[page_index].extract_tables()
            for table in tables:
                for row in table[1:]:
                    if row and row[0]:
                        records.append({
                            "company": row[0].replace(";", "").strip(),
                            "sde": int(row[1]),
                            "analyst": int(row[2]),
                            "officer": int(row[3]),
                            "intern": int(row[4]),
                            "total": int(row[5])
                        })
    return records


def extract_trend_records():
    records = []
    with pdfplumber.open(PDF_PATH) as pdf:
        table = pdf.pages[8].extract_tables()[0]
        for row in table[1:]:
            if row and row[0]:
                records.append({
                    "company": row[0].strip(),
                    "2021": float(row[1]),
                    "2022": float(row[2]),
                    "2023": float(row[3]),
                    "2024": float(row[4]),
                    "trend": row[5]
                })
    return records


def extract_conflict_records():
    records = []
    with pdfplumber.open(PDF_PATH) as pdf:
        table = pdf.pages[9].extract_tables()[0]
        for row in table[1:]:
            if row and row[0]:
                records.append({
                    "company": row[0].strip(),
                    "official_cgpa": float(row[1]),
                    "portal_cgpa": float(row[2]),
                    "official_package": row[3],
                    "portal_package": row[4],
                    "conflict": row[5]
                })
    return records


def extract_statistics_records():
    records = []
    with pdfplumber.open(PDF_PATH) as pdf:
        table = pdf.pages[10].extract_tables()[0]
        for row in table[1:]:
            if row and row[0]:
                records.append({
                    "company": row[0].replace(";", "").strip(),
                    "avg_package": float(row[1]),
                    "max_offers": int(row[2]),
                    "min_offers": int(row[3]),
                    "avg_cgpa_cutoff": float(row[4]),
                    "bond_free": row[5].strip().lower() == "yes"
                })
    return records