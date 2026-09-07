"""
Day 2 Practice: String Manipulation and Slicing
Goal: Practice string concatenation, formatting (f-strings), and extracting substrings using string slicing.
"""
# Build an employee profile generator

# String Concatenation and Modification:

first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
address = '123 Main Street'
address += ', Apartment 4B'

# Type Casting to String:

employee_age = 28
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)
experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)

# String Formatting using F-Strings:

position = 'Data Analyst'
salary = 75000
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)

# String Slicing :

employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3]
print(department)
year_code = employee_code[4:8]
print(year_code)
initials = employee_code[9:11]
print(initials)
last_three=employee_code[-3:]
print(last_three)