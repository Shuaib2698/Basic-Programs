'''{
    "IT": 260000,
    "HR": 5000,
    "Finance": 8000
}'''

sales = {
    "Amit": {
        "department": "IT",
        "product": "Laptop",
        "quantity": 3,
        "price": 50000
    },
    "Sara": {
        "department": "HR",
        "product": "Mouse",
        "quantity": 5,
        "price": 1000
    },
    "John": {
        "department": "IT",
        "product": "Laptop",
        "quantity": 2,
        "price": 50000
    },
    "David": {
        "department": "Finance",
        "product": "Keyboard",
        "quantity": 4,
        "price": 2000
    },
    "Mike": {
        "department": "IT",
        "product": "Mouse",
        "quantity": 10,
        "price": 1000
    }
}

def department_revenue(sales):
    dept_revenue = {}

    for key, value in sales.items():
        department = value["department"]
        revenue = value["quantity"] * value["price"]

        dept_revenue[department] = dept_revenue.get(department, 0) + revenue

    return dept_revenue

print(department_revenue(sales))

