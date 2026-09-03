'''Total Quantity Per Product ⭐⭐

Expected:

{
    "Laptop": 5,
    "Mouse": 4
}'''

orders = [
    {"customer": "Amit", "product": "Laptop", "quantity": 2},
    {"customer": "Sara", "product": "Mouse", "quantity": 3},
    {"customer": "Amit", "product": "Mouse", "quantity": 1},
    {"customer": "John", "product": "Laptop", "quantity": 1},
    {"customer": "Sara", "product": "Laptop", "quantity": 2},
    {"customer": "Amit", "product": "Laptop", "quantity": 1}
]

def total_revenue(sales):
    result = {}

    for sal in orders:
        product = sal.get("product")
        quantity = sal.get("quantity")
        price = sal.get("price")

        result[product] = result.get(product, 0) + quantity

    return result

print(total_revenue(orders))
