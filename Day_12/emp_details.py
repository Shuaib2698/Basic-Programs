'''def employee_report(name, *salaries, **details):

Given:

employee_report(
    "Amit",
    40000,
    45000,
    50000,
    department="IT",
    experience=3
)

Return:

{
    "name": "Amit",
    "total_salary": 135000,
    "average_salary": 45000,
    "department": "IT",
    "experience": 3
}

No sum().'''

def employee_report(name, *salary, **details):
    total = 0

    for i in salary:
        total+=i

    average = total/len(salary)

    report = {
        "Name" : name,
        "Total_salary" : total,
        "Average_salary" : average,
        "Department" : details.get("department"),
        "Experience" : details.get("experience")
    }

    return report

print(employee_report(
    "Amit",
    40000,
    45000,
    50000,
    department="IT",
    experience=3
))