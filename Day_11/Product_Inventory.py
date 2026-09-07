'''Product Inventory ⭐⭐⭐

Given:

products = [
    {"name": "Laptop", "price": 50000, "stock": 5},
    {"name": "Mouse", "price": 500, "stock": 20},
    {"name": "Keyboard", "price": 1000, "stock": 10}
]

Calculate the total inventory value.

Formula:

price × stock

Expected:

270000

Do it manually with loops.'''

products = [
    {"name": "Laptop", "price": 50000, "stock": 5},
    {"name": "Mouse", "price": 500, "stock": 20},
    {"name": "Keyboard", "price": 1000, "stock": 10}
]

def total_inventory(products):
    result = {}

    for i in products:
        name = i.get("name")
        stock = i.get("stock")
        price = i.get("price")

        result[name] = result.get(name, 0) + stock*price

    final_result = 0

    for keys, values in result.items():
        final_result+= result[keys]
    return final_result

print(total_inventory(products))