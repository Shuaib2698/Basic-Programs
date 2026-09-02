# '''🐍 PART B — List of Dictionaries
#
# Use this data for Q9–Q12:
#
# employees = [
#     {"name": "Amit", "salary": 50000, "department": "IT"},
#     {"name": "Sara", "salary": 60000, "department": "HR"},
#     {"name": "John", "salary": 75000, "department": "IT"},
#     {"name": "Ali", "salary": 45000, "department": "Finance"},
#     {"name": "Ravi", "salary": 55000, "department": "HR"},
#     {"name": "Kiran", "salary": 65000, "department": "Finance"}
# ]
# Filter Employees ⭐
#
# Find all employees who:
#
# work in IT
# AND have salary greater than 50000
#
# Expected:
#
# [
#     {"name": "John", "salary": 75000, "department": "IT"}
# ]'''
#
# employees = [
#     {"name": "Amit", "salary": 50000, "department": "IT"},
#     {"name": "Sara", "salary": 60000, "department": "HR"},
#     {"name": "John", "salary": 75000, "department": "IT"},
#     {"name": "Ali", "salary": 45000, "department": "Finance"},
#     {"name": "Ravi", "salary": 55000, "department": "HR"},
#     {"name": "Kiran", "salary": 65000, "department": "Finance"}
# ]
#
# def filter_emp(employees):
#     result = []
#
#     for emp in employees:
#         if emp["department"] == 'IT'  and emp["salary"] > 50000:
#             result.append(emp)
#     return False
#
# print(filter_emp(employees))
#
#
#
