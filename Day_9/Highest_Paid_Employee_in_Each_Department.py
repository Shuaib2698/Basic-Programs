'''Find the Highest-Paid Employee in Each Department ⭐⭐

This is a step up from the previous question because now you need to compare values while grouping.

Given:

employees = [
    {"name": "Amit", "salary": 50000, "department": "IT"},
    {"name": "Sara", "salary": 60000, "department": "HR"},
    {"name": "John", "salary": 75000, "department": "IT"},
    {"name": "Ali", "salary": 45000, "department": "Finance"},
    {"name": "Ravi", "salary": 55000, "department": "HR"},
    {"name": "Kiran", "salary": 65000, "department": "Finance"}
]
Task

Find the highest-paid employee in each department.

Expected output:

{
    "IT": "John",
    "HR": "Sara",
    "Finance": "Kiran"
}
Rules
Use only core Python.
Use a function.
Use loops.
Use dictionaries.
No Pandas.
No max().
No sorted().
No defaultdict().
💡 Hint

You need to maintain something like:

result = {}

As you go through each employee, ask:

Does this department already exist in result?
If not, this employee becomes the highest-paid employee for that department.
If yes, compare the current employee's salary with the salary you previously stored.

The tricky part is deciding what you should store in result.

For example, you could temporarily have:

{
    "IT": {"name": "Amit", "salary": 50000},
    ...
}

Then compare salaries.'''

employees = [
    {"name": "Amit", "salary": 50000, "department": "IT"},
    {"name": "Sara", "salary": 60000, "department": "HR"},
    {"name": "John", "salary": 75000, "department": "IT"},
    {"name": "Ali", "salary": 45000, "department": "Finance"},
    {"name": "Ravi", "salary": 55000, "department": "HR"},
    {"name": "Kiran", "salary": 65000, "department": "Finance"}
]

def high_salary(employees):
    result = {}

    for emp in employees:
        department = emp.get("department")
        name = emp.get("name")
        salary = emp.get("salary")

        if department not in result:
            result[department] = {
                "name": name,
                "salary" : salary
            }
        elif salary > result[department]["salary"]:
            result[department] = {
                "name" : name,
                "salary": salary
            }

    final_result = {}

    for department, employee in result.items():
        final_result[department] = employee["name"]


    return final_result

print(high_salary(employees))

