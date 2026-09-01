'''Find the Department With the Highest Total Salary ⭐⭐

Now we're going to combine two levels of aggregation.

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

Calculate the total salary paid by each department, then return the department with the highest total salary.

Expected:

IT → 125000
HR → 115000
Finance → 110000

Therefore:

IT
Expected output
"IT"'''

employees = [
    {"name": "Amit", "salary": 50000, "department": "IT"},
    {"name": "Sara", "salary": 60000, "department": "HR"},
    {"name": "John", "salary": 75000, "department": "IT"},
    {"name": "Ali", "salary": 45000, "department": "Finance"},
    {"name": "Ravi", "salary": 55000, "department": "HR"},
    {"name": "Kiran", "salary": 65000, "department": "Finance"}
]

def dept_highest_sal(employees):
    result = {}


    for emp in employees:
        department = emp.get("department")
        salary = emp.get("salary")

        result[department] = result.get(department, 0) + salary
    return max(result, key = result.get)

    # max_sal = 0
    # dept = ""

    # for emp in employees:
    #     if department not in result:
    #         result[department] = salary
    #     else:
    #         result[department] += salary
    #
    # for keys, values in result.items():
    #     if values > max_sal:
    #         max_sal = values
    #         dept = keys
    # return dept

print(dept_highest_sal(employees))