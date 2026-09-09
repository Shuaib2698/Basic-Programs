sales = {
    "Amit": {
        "product": "Laptop",
        "quantity": 3
    },
    "Sara": {
        "product": "Mouse",
        "quantity": 5
    },
    "John": {
        "product": "Laptop",
        "quantity": 2
    },
    "David": {
        "product": "Keyboard",
        "quantity": 4
    },
    "Mike": {
        "product": "Mouse",
        "quantity": 10
    }
}

'''
{
    "Laptop": 5,
    "Mouse": 15,
    "Keyboard": 4
}'''

def product_quantity(sales):
    products = {}

    for product, quants in sales.items():
        product = quants["product"]
        revenue = quants["quantity"]

        products[product] = products.get(product, 0) + revenue

    return products

print(product_quantity(sales))