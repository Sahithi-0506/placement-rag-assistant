from src.structured_data_extractor import (
    extract_company_records,
    extract_hiring_records,
    extract_trend_records,
    extract_conflict_records,
    extract_statistics_records,
)


def names(records):
    if not records:
        return "I don't have enough information in the provided document."

    return ", ".join(r["company"] for r in records)


def companies_above_cgpa(threshold):
    records = [
        r for r in extract_company_records()
        if r["min_cgpa"] > threshold
    ]

    return names(records)


def companies_allowing_backlogs(min_backlogs):
    records = [
        r for r in extract_company_records()
        if r["max_backlogs"] >= min_backlogs
    ]

    return names(records)


def bond_free_companies():
    records = [
        r for r in extract_company_records()
        if r["bond_years"] == 0
    ]

    return names(records)


def python_focused_companies():
    records = [
        r for r in extract_company_records()
        if r["tech_focus"].lower() == "python"
    ]

    return names(records)


def highest_package_python_focused():
    records = [
        r for r in extract_company_records()
        if r["tech_focus"].lower() == "python"
    ]

    if not records:
        return "I don't have enough information in the provided document."

    best = max(records, key=lambda r: r["package_lpa"])

    return (
        f"{best['company']} offers the highest package among "
        f"Python-focused companies with {best['package_lpa']} LPA."
    )


def zero_bond_above_package(package_threshold):
    records = [
        r for r in extract_company_records()
        if r["bond_years"] == 0 and r["package_lpa"] > package_threshold
    ]

    if not records:
        return "I don't have enough information in the provided document."

    return ", ".join(
        f"{r['company']} ({r['package_lpa']} LPA)"
        for r in records
    )


def highest_paying_for_student(cgpa, backlogs):
    eligible = [
        r for r in extract_company_records()
        if r["min_cgpa"] <= cgpa and r["max_backlogs"] >= backlogs
    ]

    if not eligible:
        return "No company in the provided document matches the student's eligibility."

    best = max(eligible, key=lambda r: r["package_lpa"])

    return (
        f"{best['company']} is the highest-paying eligible company "
        f"with {best['package_lpa']} LPA."
    )


def company_with_most_interns():
    records = extract_hiring_records()

    if not records:
        return "I don't have enough information in the provided document."

    best = max(records, key=lambda r: r["intern"])

    return f"{best['company']} hires the most interns with {best['intern']} intern roles."


def compare_sde_amazon_google():
    records = {r["company"]: r for r in extract_hiring_records()}

    if "Amazon" not in records or "Google" not in records:
        return "I don't have enough information in the provided document."

    return (
        f"Amazon hires {records['Amazon']['sde']} SDEs, "
        f"while Google hires {records['Google']['sde']} SDEs."
    )


def role_hiring_count(company_name, role):
    records = extract_hiring_records()
    role_key = role.lower()

    for record in records:
        if record["company"].lower() == company_name.lower():
            if role_key in record:
                return (
                    f"{record['company']} hires {record[role_key]} "
                    f"{role.upper()} roles."
                )

    return "I don't have enough information in the provided document."


def largest_package_growth():
    records = extract_trend_records()

    if not records:
        return "I don't have enough information in the provided document."

    best = max(records, key=lambda r: r["2024"] - r["2021"])
    growth = round(best["2024"] - best["2021"], 1)

    return (
        f"{best['company']} showed the largest package growth: "
        f"{growth} LPA from 2021 to 2024."
    )


def amazon_cgpa_conflict():
    for r in extract_conflict_records():
        if r["company"].lower() == "amazon":
            return (
                f"There are conflicting records for Amazon. "
                f"Official CGPA is {r['official_cgpa']}, "
                f"while portal CGPA is {r['portal_cgpa']}."
            )

    return "I don't have enough information in the provided document."


def companies_with_conflicting_cgpa():
    records = [
        r for r in extract_conflict_records()
        if r["official_cgpa"] != r["portal_cgpa"]
    ]

    return names(records)


def best_package_to_cgpa_ratio():
    records = extract_company_records()

    if not records:
        return "I don't have enough information in the provided document."

    best = max(records, key=lambda r: r["package_lpa"] / r["min_cgpa"])
    ratio = round(best["package_lpa"] / best["min_cgpa"], 2)

    return f"{best['company']} has the best package-to-CGPA ratio: {ratio}."


def rank_eligible_zero_backlog_8_plus():
    records = [
        r for r in extract_company_records()
        if r["min_cgpa"] >= 8.0 and r["max_backlogs"] == 0
    ]

    records.sort(key=lambda r: r["package_lpa"], reverse=True)

    if not records:
        return "I don't have enough information in the provided document."

    return ", ".join(
        f"{r['company']} ({r['package_lpa']} LPA)"
        for r in records
    )


def compare_google_amazon():
    data = {r["company"]: r for r in extract_company_records()}

    if "Google" not in data or "Amazon" not in data:
        return "I don't have enough information in the provided document."

    google = data["Google"]
    amazon = data["Amazon"]

    return (
        f"Google: CGPA {google['min_cgpa']}, "
        f"package {google['package_lpa']} LPA, "
        f"backlogs {google['max_backlogs']}, "
        f"bond {google['bond_years']} year, "
        f"tech focus {google['tech_focus']}. "
        f"Amazon: CGPA {amazon['min_cgpa']}, "
        f"package {amazon['package_lpa']} LPA, "
        f"backlogs {amazon['max_backlogs']}, "
        f"bond {amazon['bond_years']} years, "
        f"tech focus {amazon['tech_focus']}."
    )