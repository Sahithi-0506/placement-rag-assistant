from src.reasoning_engine import (
    companies_above_cgpa,
    companies_allowing_backlogs,
    bond_free_companies,
    python_focused_companies,
    highest_package_python_focused,
    zero_bond_above_package,
    highest_paying_for_student,
)

print("CGPA above 8.0:", companies_above_cgpa(8.0))
print("At least 2 backlogs:", companies_allowing_backlogs(2))
print("Bond-free:", bond_free_companies())
print("Python-focused:", python_focused_companies())
print("Highest Python package:", highest_package_python_focused())
print("Zero bond above 40:", zero_bond_above_package(40))
print("Student 7.6 CGPA, 1 backlog:", highest_paying_for_student(7.6, 1))