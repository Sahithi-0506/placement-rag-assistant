from src.structured_data_extractor import extract_company_records

records = extract_company_records()

print(f"Total records extracted: {len(records)}")

for record in records:
    print(record)