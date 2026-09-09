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

'''Expected output
Amit

Because:

Amit  → 3 × 50000 = 150000
John  → 2 × 50000 = 100000
Mike  → 10 × 1000 = 10000
Sara  → 5 × 1000 = 5000
David → 4 × 2000 = 8000

Amit has the highest individual revenue.'''

def highest_revenue_employee(sales):
    highest = {}
    emp = ""

    for name, details in sales.items():
        highest[name] = details["quantity"] * details["price"]

    high_sale = 0
    for name, sale in highest.items():
        if high_sale < highest[name]:
            high_sale = highest[name]
            emp = name

    return emp

print(highest_revenue_employee(sales))