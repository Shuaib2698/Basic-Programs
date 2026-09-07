'''Employee Salary Report ⭐⭐⭐

Given:

employees = [
    {"name": "Amit", "salary": 50000},
    {"name": "Sara", "salary": 60000},
    {"name": "John", "salary": 75000},
    {"name": "Ali", "salary": 45000}
]

Return:

{
    "total": 230000,
    "average": 57500,
    "highest": "John",
    "lowest": "Ali"
}

Restrictions:

Core Python
loops
dictionaries
no sum()
no max()
no min()'''

employees = [
    {"name": "Amit", "salary": 50000},
    {"name": "Sara", "salary": 60000},
    {"name": "John", "salary": 75000},
    {"name": "Ali", "salary": 45000}
]

def sal_report(employees):

    total = 0
    highest_salary = 0
    lowest_salary = 0
    highest_name = ""
    lowest_name = ""

    for emp in employees:
        salary = emp.get("salary")
        name = emp.get("name")

        # Total
        total += salary

        # Highest
        if salary > highest_salary:
            highest_salary = salary
            highest_name = name

        # Lowest
        if lowest_salary == 0 or salary < lowest_salary:
            lowest_salary = salary
            lowest_name = name

    average = total / len(employees)

    result = {
        "total": total,
        "average": average,
        "highest": highest_name,
        "lowest": lowest_name
    }

    return result


print(sal_report(employees))