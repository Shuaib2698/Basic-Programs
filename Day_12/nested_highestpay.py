'''Question 2 ⭐⭐

Now let's make it slightly harder.

Given:

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
    }
}

Write:

def highest_paid_employee(employees):
    # your code
Expected output
John
Rules

Don't use:

max()
sorted()
list comprehensions

Use only:

for
.items()
dictionary access
if
comparison
variables
💡 Hint

This is almost the same pattern as Question 1.

But this time, ask yourself:

What should I compare?'''

def highest_paid_employee(employees):
    highest_pay = 0
    employee = ""

    for keys, values in employees.items():
        if values["salary"] > highest_pay:
            highest_pay = values["salary"]
            employee = keys
    return employee

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
    }
}

print(highest_paid_employee(employees))