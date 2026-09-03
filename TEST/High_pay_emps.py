'''Highest-Paid Employee Per Department ⭐⭐

Expected:

{
    "IT": "John",
    "HR": "Sara",
    "Finance": "Kiran"
}

Restrictions:

No max()
No sorted()
No Pandas
Use loops and dictionaries.'''

employees = [
    {"name": "Amit", "salary": 50000, "department": "IT"},
    {"name": "Sara", "salary": 60000, "department": "HR"},
    {"name": "John", "salary": 75000, "department": "IT"},
    {"name": "Ali", "salary": 45000, "department": "Finance"},
    {"name": "Ravi", "salary": 55000, "department": "HR"},
    {"name": "Kiran", "salary": 65000, "department": "Finance"}
]

def high_pay(employees):
    result = {}

    for emp in employees:
        department = emp.get("department")
        salary = emp.get("salary")
        name = emp.get("name")

        if department not in result:
            result[department] = {
                "name" : name,
                "salary" : salary
            }

        if salary > result[department]["salary"] :
            result[department] = {
                "name" : name,
                "salary" : salary
            }

    final_result = {}

    for department, employee in result.items():
        final_result[department] = employee["name"]

    return final_result

print(high_pay(employees))

