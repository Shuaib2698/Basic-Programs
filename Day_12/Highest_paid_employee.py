'''Given:

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
    }
}

Write:

def highest_paid_by_department(employees):
    # your code
Expected output
{
    "IT": "John",
    "HR": "Sara",
    "Finance": "David"
}'''

def highest_paid_by_department(employees):
    data = {}

    for keys, values in employees.items():
        department = values["department"]
        name = keys
        salaries = values["salary"]
        if department not in data:
            data[department] = {
                "name" : name,
                "salary" : salaries
            }

        elif salaries > data[department]["salary"]:
            data[department] = {
                "name" : name,
                "salary": salaries
            }

    final_data = {}

    for department, employee in data.items():
        final_data[department] = employee["name"]

    return final_data


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
    }
}

print(highest_paid_by_department(employees))