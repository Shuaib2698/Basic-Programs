'''

Group Employees ⭐⭐

Create:

{
    "IT": ["Amit", "John"],
    "HR": ["Sara", "Ravi"],
    "Finance": ["Ali", "Kiran"]
}

Important: Don't hard-code the department names.
'''

employees = [
    {"name": "Amit", "salary": 50000, "department": "IT"},
    {"name": "Sara", "salary": 60000, "department": "HR"},
    {"name": "John", "salary": 75000, "department": "IT"},
    {"name": "Ali", "salary": 45000, "department": "Finance"},
    {"name": "Ravi", "salary": 55000, "department": "HR"},
    {"name": "Kiran", "salary": 65000, "department": "Finance"}
]

def group_employees(employees):
    result = {}

    for emp in employees:
        department = emp.get("department")
        # name = emp.get("name")

        if department  in result:
            result[department].append(emp.get("name"))
        else:
            result[department] = [emp.get("name")]
    return result

print(group_employees(employees))