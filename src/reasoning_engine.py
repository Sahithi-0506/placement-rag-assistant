from src.structured_data_extractor import extract_company_records


def get_records():
    return extract_company_records()


def format_company_list(records):
    if not records:
        return "I don't have enough information in the provided document."

    return ", ".join(record["company"] for record in records)


def companies_above_cgpa(threshold):
    records = get_records()

    result = [
        record for record in records
        if record["min_cgpa"] > threshold
    ]

    return format_company_list(result)


def companies_allowing_backlogs(min_backlogs):
    records = get_records()

    result = [
        record for record in records
        if record["max_backlogs"] >= min_backlogs
    ]

    return format_company_list(result)


def bond_free_companies():
    records = get_records()

    result = [
        record for record in records
        if record["bond_years"] == 0
    ]

    return format_company_list(result)


def python_focused_companies():
    records = get_records()

    result = [
        record for record in records
        if record["tech_focus"].lower() == "python"
    ]

    return format_company_list(result)


def highest_package_python_focused():
    records = get_records()

    python_records = [
        record for record in records
        if record["tech_focus"].lower() == "python"
    ]

    if not python_records:
        return "I don't have enough information in the provided document."

    best = max(python_records, key=lambda record: record["package_lpa"])

    return f"{best['company']} offers the highest package among Python-focused companies with {best['package_lpa']} LPA."


def zero_bond_above_package(package_threshold):
    records = get_records()

    result = [
        record for record in records
        if record["bond_years"] == 0 and record["package_lpa"] > package_threshold
    ]

    if not result:
        return "I don't have enough information in the provided document."

    return ", ".join(
        f"{record['company']} ({record['package_lpa']} LPA)"
        for record in result
    )


def highest_paying_for_student(cgpa, backlogs):
    records = get_records()

    eligible = [
        record for record in records
        if record["min_cgpa"] <= cgpa and record["max_backlogs"] >= backlogs
    ]

    if not eligible:
        return "No company in the provided document matches the student's eligibility."

    best = max(eligible, key=lambda record: record["package_lpa"])

    return f"{best['company']} is the highest-paying eligible company with {best['package_lpa']} LPA."