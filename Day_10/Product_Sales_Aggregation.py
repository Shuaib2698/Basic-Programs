'''Product Sales Aggregation ⭐⭐

Given:

sales = [
    {"product": "Laptop", "quantity": 2, "price": 50000},
    {"product": "Mouse", "quantity": 3, "price": 500},
    {"product": "Laptop", "quantity": 1, "price": 50000},
    {"product": "Keyboard", "quantity": 2, "price": 1000},
    {"product": "Mouse", "quantity": 2, "price": 500}
]

Calculate the total revenue for each product.

Remember:

revenue = quantity × price

Expected:

{
    "Laptop": 150000,
    "Mouse": 2500,
    "Keyboard": 2000
}'''


sales = [
    {"product": "Laptop", "quantity": 2, "price": 50000},
    {"product": "Mouse", "quantity": 3, "price": 500},
    {"product": "Laptop", "quantity": 1, "price": 50000},
    {"product": "Keyboard", "quantity": 2, "price": 1000},
    {"product": "Mouse", "quantity": 2, "price": 500}
]

def total_revenue(sales):
    result = {}

    for sal in sales:
        product = sal.get("product")
        quantity = sal.get("quantity")
        price = sal.get("price")

        result[product] = result.get(product, 0) + quantity*price

    return result

print(total_revenue(sales))
