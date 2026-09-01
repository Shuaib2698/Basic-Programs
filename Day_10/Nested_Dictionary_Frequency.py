'''Nested Dictionary Frequency ⭐⭐

Let's change the type of thinking now.

Given:

orders = [
    {"customer": "Amit", "product": "Laptop", "quantity": 2},
    {"customer": "Sara", "product": "Mouse", "quantity": 3},
    {"customer": "Amit", "product": "Mouse", "quantity": 1},
    {"customer": "John", "product": "Laptop", "quantity": 1},
    {"customer": "Sara", "product": "Laptop", "quantity": 2},
    {"customer": "Amit", "product": "Laptop", "quantity": 1}
]
Task

Calculate the total quantity purchased by each customer.

Expected:

{
    "Amit": 4,
    "Sara": 5,
    "John": 1
}

Because:

Amit → Laptop 2 + Mouse 1 + Laptop 1 = 4
Sara → Mouse 3 + Laptop 2 = 5
John → Laptop 1 = 1
Rules
Core Python only
Function + loops + dictionary
No Counter
No Pandas
No sum()
Hint

This is similar to your frequency dictionary:

freq[i] = freq.get(i, 0) + 1

But instead of adding 1, you're adding the employee/order's quantity.

Think:

customer = emp.get("customer")
quantity = emp.get("quantity")

Then somehow update:

result[customer]'''

orders = [
    {"customer": "Amit", "product": "Laptop", "quantity": 2},
    {"customer": "Sara", "product": "Mouse", "quantity": 3},
    {"customer": "Amit", "product": "Mouse", "quantity": 1},
    {"customer": "John", "product": "Laptop", "quantity": 1},
    {"customer": "Sara", "product": "Laptop", "quantity": 2},
    {"customer": "Amit", "product": "Laptop", "quantity": 1}
]

def total_quantity(orders):
    result = {}

    for cus in orders:
        customers = cus.get("customer")
        quantity = cus.get("quantity")

        result[customers] = result.get(customers, 0) + quantity


        # if customers not in result:
        #     result[customers] = quantity
        #
        # else:
        #     result[customers] += quantity

    return result

print(total_quantity(orders))