'''Group Employees by Department ⭐

Now let's make the list-of-dictionaries problem slightly harder.

Given:

employees = [
    {"name": "Amit", "salary": 50000, "department": "IT"},
    {"name": "Sara", "salary": 60000, "department": "HR"},
    {"name": "John", "salary": 75000, "department": "IT"},
    {"name": "Ali", "salary": 45000, "department": "Finance"},
    {"name": "Ravi", "salary": 55000, "department": "HR"}
]

Create a dictionary grouping the employee names by department.

Expected:

{
    "IT": ["Amit", "John"],
    "HR": ["Sara", "Ravi"],
    "Finance": ["Ali"]
}'''

employees = [
    {"name": "Amit", "salary": 50000, "department": "IT"},
    {"name": "Sara", "salary": 60000, "department": "HR"},
    {"name": "John", "salary": 75000, "department": "IT"},
    {"name": "Ali", "salary": 45000, "department": "Finance"},
    {"name": "Ravi", "salary": 55000, "department": "HR"}
]

def dict_list(employees):
    result = {
        "IT" : [],
        "HR" : [],
        "Finance" : []
    }

    for emp in employees:
        department = emp.get("department")
        if department in result:
            result[department].append(emp.get("name"))

    return result

print(dict_list(employees))

