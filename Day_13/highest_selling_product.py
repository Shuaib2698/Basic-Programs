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
    },
    "Mike": {
        "product": "Mouse",
        "quantity": 10,
        "price": 1000
    }
}

'''Expected output
Mouse

Because total quantities are:

Laptop   → 3 + 2  = 5
Mouse    → 5 + 10 = 15
Keyboard → 4      = 4

So Mouse has the highest quantity sold.'''

def highest_selling_product(sales):
    products = {}

    for product, quants in sales.items():
        product = quants["product"]
        item = quants["quantity"]

        products[product] = products.get(product, 0) + item

    high_product = ""
    high_val = 0

    for key, value in products.items():
        if high_val < products[key]:
            high_val = products[key]
            high_product = key

    return high_product

print(highest_selling_product(sales))

