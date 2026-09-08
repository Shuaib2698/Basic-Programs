'''{
    "Amit": 150000,
    "Sara": 5000,
    "John": 100000,
    "David": 8000
}'''

sales = {
    "Amit": {
        "product": "Laptop",
        "quantity": 3,
        "price": 50000
    },
    "Sara": {
        "product": "Mouse",
        "quantity": 5,
        "price": 1000
    },
    "John": {
        "product": "Laptop",
        "quantity": 2,
        "price": 50000
    },
    "David": {
        "product": "Keyboard",
        "quantity": 4,
        "price": 2000
    }
}

def calculate_sales(sales):
    revenue = {}

    for name, details in sales.items():
        revenue[name] = revenue.get(name, 0) + details["quantity"] * details["price"]


    return revenue

print(calculate_sales(sales))