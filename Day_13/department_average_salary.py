employees = {
    "Amit": {
        "department": "IT",
        "salary": 60000
    },
    "Sara": {
        "department": "HR",
        "salary": 55000
    },
    "John": {
        "department": "IT",
        "salary": 75000
    },
    "David": {
        "department": "Finance",
        "salary": 70000
    },
    "Mike": {
        "department": "IT",
        "salary": 65000
    },
    "Priya": {
        "department": "HR",
        "salary": 65000
    }
}

'''{
    "IT": 66666.67,
    "HR": 60000.0,
    "Finance": 70000.0
}'''

def department_average_salary(employees):
    data = {}

    for name, details in employees.items():
        department = details["department"]
        salary = details["salary"]

        if department not in data:
            data[department] = {
                "total": salary,
                "count": 1
            }
        else:
            data[department]["total"] += salary
            data[department]["count"] += 1

    average = {}
    for key, value in data.items():
        average[key] = value["total"]/value["count"]

    return average

print(department_average_salary(employees))