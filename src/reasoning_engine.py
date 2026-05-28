from src.structured_data_extractor import (
    extract_company_records,
    extract_hiring_records,
    extract_trend_records,
    extract_conflict_records,
    extract_statistics_records,
)


def names(records):
    return ", ".join(r["company"] for r in records) if records else "I don't have enough information in the provided document."


def companies_above_cgpa(threshold):
    return names([r for r in extract_company_records() if r["min_cgpa"] > threshold])


def companies_allowing_backlogs(min_backlogs):
    return names([r for r in extract_company_records() if r["max_backlogs"] >= min_backlogs])


def bond_free_companies():
    return names([r for r in extract_company_records() if r["bond_years"] == 0])


def python_focused_companies():
    return names([r for r in extract_company_records() if r["tech_focus"].lower() == "python"])


def highest_package_python_focused():
    records = [r for r in extract_company_records() if r["tech_focus"].lower() == "python"]
    best = max(records, key=lambda r: r["package_lpa"])
    return f"{best['company']} offers the highest package among Python-focused companies with {best['package_lpa']} LPA."


def zero_bond_above_package(package_threshold):
    records = [
        r for r in extract_company_records()
        if r["bond_years"] == 0 and r["package_lpa"] > package_threshold
    ]
    return ", ".join(f"{r['company']} ({r['package_lpa']} LPA)" for r in records)


def highest_paying_for_student(cgpa, backlogs):
    eligible = [
        r for r in extract_company_records()
        if r["min_cgpa"] <= cgpa and r["max_backlogs"] >= backlogs
    ]
    best = max(eligible, key=lambda r: r["package_lpa"])
    return f"{best['company']} is the highest-paying eligible company with {best['package_lpa']} LPA."


def company_with_most_interns():
    best = max(extract_hiring_records(), key=lambda r: r["intern"])
    return f"{best['company']} hires the most interns with {best['intern']} intern roles."


def compare_sde_amazon_google():
    records = {r["company"]: r for r in extract_hiring_records()}
    return f"Amazon hires {records['Amazon']['sde']} SDEs, while Google hires {records['Google']['sde']} SDEs."


def largest_package_growth():
    records = extract_trend_records()
    best = max(records, key=lambda r: r["2024"] - r["2021"])
    growth = round(best["2024"] - best["2021"], 1)
    return f"{best['company']} showed the largest package growth: {growth} LPA from 2021 to 2024."


def amazon_cgpa_conflict():
    for r in extract_conflict_records():
        if r["company"].lower() == "amazon":
            return f"There are conflicting records for Amazon. Official CGPA is {r['official_cgpa']}, while portal CGPA is {r['portal_cgpa']}."


def companies_with_conflicting_cgpa():
    return names([r for r in extract_conflict_records() if r["official_cgpa"] != r["portal_cgpa"]])


def best_package_to_cgpa_ratio():
    records = extract_company_records()
    best = max(records, key=lambda r: r["package_lpa"] / r["min_cgpa"])
    ratio = round(best["package_lpa"] / best["min_cgpa"], 2)
    return f"{best['company']} has the best package-to-CGPA ratio: {ratio}."


def rank_eligible_zero_backlog_8_plus():
    records = [
        r for r in extract_company_records()
        if r["min_cgpa"] >= 8.0 and r["max_backlogs"] == 0
    ]
    records.sort(key=lambda r: r["package_lpa"], reverse=True)
    return ", ".join(f"{r['company']} ({r['package_lpa']} LPA)" for r in records)


def compare_google_amazon():
    data = {r["company"]: r for r in extract_company_records()}
    google = data["Google"]
    amazon = data["Amazon"]
    return (
        f"Google: CGPA {google['min_cgpa']}, package {google['package_lpa']} LPA, "
        f"backlogs {google['max_backlogs']}, bond {google['bond_years']} year, tech focus {google['tech_focus']}. "
        f"Amazon: CGPA {amazon['min_cgpa']}, package {amazon['package_lpa']} LPA, "
        f"backlogs {amazon['max_backlogs']}, bond {amazon['bond_years']} years, tech focus {amazon['tech_focus']}."
    )