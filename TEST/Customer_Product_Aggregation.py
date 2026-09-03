'''Customer + Product Aggregation ⭐⭐⭐

Now make it more difficult.

Calculate how many of each product each customer purchased.

Expected:

{
    "Amit": {
        "Laptop": 3,
        "Mouse": 1
    },
    "Sara": {
        "Mouse": 3,
        "Laptop": 2
    },
    "John": {
        "Laptop": 1
    }
}

This is the first question where I want to see whether you can independently build a nested dictionary.'''

orders = [
    {"customer": "Amit", "product": "Laptop", "quantity": 2},
    {"customer": "Sara", "product": "Mouse", "quantity": 3},
    {"customer": "Amit", "product": "Mouse", "quantity": 1},
    {"customer": "John", "product": "Laptop", "quantity": 1},
    {"customer": "Sara", "product": "Laptop", "quantity": 2},
    {"customer": "Amit", "product": "Laptop", "quantity": 1}
]

def cus_product_agg(orders):
    result = {}

    for names in orders:
        customer = names.get("customer")
        product = names.get("product")
        quantity = names.get("quantity")

        if customer not in result:
            result[customer] = {}

        if product in result[customer]:
            result[customer][product] += quantity
        else:
            result[customer][product] = quantity

    return result

print(cus_product_agg(orders))