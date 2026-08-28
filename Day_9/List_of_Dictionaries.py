'''Transform a List of Dictionaries ⭐

Now let's move into something much closer to real-world Python/data processing.

Given:

employees = [
    {"name": "Amit", "salary": 50000, "department": "IT"},
    {"name": "Sara", "salary": 60000, "department": "HR"},
    {"name": "John", "salary": 75000, "department": "IT"},
    {"name": "Ali", "salary": 45000, "department": "Finance"}
]
Task

Find all employees from the IT department whose salary is greater than 50,000.

Expected output:

["John"]
Conditions
Use a function.
Use a loop.
Don't use pandas.
Don't use filter() yet.

This is a very useful pattern because you'll frequently encounter lists containing dictionaries when working with JSON/API responses.'''

employees = [
    {"name": "Amit", "salary": 50000, "department": "IT"},
    {"name": "Sara", "salary": 60000, "department": "HR"},
    {"name": "John", "salary": 75000, "department": "IT"},
    {"name": "Ali", "salary": 45000, "department": "Finance"}
]

def list_dict(employees):
    result = []

    #  Best method to work on json data it handles keyerror and returns none if any key not present in dictionary.
    for emp in employees:
        if emp.get("department") == "IT" and emp.get("salary") > 50000:
            result.append(emp.get("name"))
    return result

    # This is another method but it raises keyError if any key doesn't exists in dictionary.
    # example if "name":"salary" not present in any 1 dictionary then emp["salary"] throughs keyerror.
    # for emp in employees:
    #     if emp["department"] == "IT" and emp["salary"] > 50000:
    #         result.append(emp["name"])
    # return result

print(list_dict(employees))