# Q44. Final Challenge — Employee Processing
# Given:
# employees = [    {"name": "Rahul", "department": "IT", "salary": 45000, "skills": ["Python", "Django"]},    {"name": "Aman", "department": "HR", "salary": 55000, "skills": ["Excel", "Communication"]},    {"name": "Priya", "department": "IT", "salary": 75000, "skills": ["Python", "Django", "React"]},    {"name": "Sneha", "department": "Finance", "salary": 65000, "skills": ["Excel", "Power BI"]},    {"name": "Arjun", "department": "IT", "salary": 85000, "skills": ["Python", "Django", "React", "SQL"]}]
#
#
# Build a program that:
# 1. Finds employees who know "Python".
# 2. Finds employees whose salary is above 60000.
# 3. Finds the highest-paid employee.
# 4. Groups employees by department.
# 5. Calculates the average salary.
# 6. Sorts employees by salary descending.
# 7. Creates a new list containing employee names in uppercase.
# 8. Uses appropriate functions/lambda/map/filter/sorted where they make sense.
# This is the final challenge, so don't worry if you cannot complete every part perfectly.


employees = [
    {"name": "Rahul", "department": "IT", "salary": 45000, "skills": ["Python", "Django"]},
    {"name": "Aman", "department": "HR", "salary": 55000, "skills": ["Excel", "Communication"]},
    {"name": "Priya", "department": "IT", "salary": 75000, "skills": ["Python", "Django", "React"]},
    {"name": "Sneha", "department": "Finance", "salary": 65000, "skills": ["Excel", "Power BI"]},
    {"name": "Arjun", "department": "IT", "salary": 85000, "skills": ["Python", "Django", "React", "SQL"]}
]

# 1. Finds employees who know "Python"
python_devs = list(filter(lambda emp: "Python" in emp["skills"], employees))

# 2. Finds employees whose salary is above 60000
high_earners = list(filter(lambda emp: emp["salary"] > 60000, employees))

# 3. Finds the highest-paid employee (using max with a lambda key)
top_earner = max(employees, key=lambda emp: emp["salary"])

# 4. Groups employees by department
grouped_by_dept = {}
for emp in employees:
    dept = emp["department"]
    if dept not in grouped_by_dept:
        grouped_by_dept[dept] = []
    grouped_by_dept[dept].append(emp["name"])

# 5. Calculates the average salary
average_salary = sum(emp["salary"] for emp in employees) / len(employees)

# 6. Sorts employees by salary descending
sorted_by_salary = sorted(employees, key=lambda emp: emp["salary"], reverse=True)

# 7. Creates a new list containing employee names in uppercase
uppercase_names = list(map(lambda emp: emp["name"].upper(), employees))

# --- Printing Results ---
print("1. Python Developers:", [emp["name"] for emp in python_devs])
print("2. Salary > 60000:", [emp["name"] for emp in high_earners])
print("3. Highest Paid:", top_earner["name"])
print("4. Grouped by Department:", grouped_by_dept)
print("5. Average Salary:", average_salary)
print("6. Sorted by Salary:", [f"{emp['name']} ({emp['salary']})" for emp in sorted_by_salary])
print("7. Uppercase Names:", uppercase_names)