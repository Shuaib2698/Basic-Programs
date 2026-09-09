'''Convert this normal function into a lambda:

def multiply(a, b):
    return a * b'''

multiply = lambda a, b: a*b

print(multiply(5, 6))

students = [
    {"name": "Amit", "marks": 85},
    {"name": "Sara", "marks": 92},
    {"name": "John", "marks": 78}
]

print(sorted(students, key= lambda students: students["marks"]))

employees = [
    {"name": "Amit", "salary": 60000},
    {"name": "Sara", "salary": 55000},
    {"name": "John", "salary": 75000},
    {"name": "David", "salary": 70000}
]

print(sorted(employees, key = lambda employee : employee["salary"], reverse = True))

salaries = [30000, 45000, 60000, 75000]

inc = list(map(lambda salary: salary + (salary * 10/100), salaries))

print(inc)

new = list(filter(lambda salary: salary > 50000, salaries))
print(new)

ans = list(map(lambda salary: salary * 1.10,filter(lambda salary:  salary > 50000, salaries)))
print(ans)