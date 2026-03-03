# Activity 1: 
# PART 1 – Variables

name = "Aiman"
age = 20
city = "Peshawar"

print("Name:", name)
print("Age:", age)
print("City:", city)

num1 = 10
num2 = 5

print("Sum:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

# PART 2 - Input and Output

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print("Hello", user_name + ", you are", user_age, "years old")

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

print("Addition:", n1 + n2)
print("Subtraction:", n1 - n2)

# PART 3 - Comments

# This is a single line comment
# It includes variables, input, conditions and loops
# Created for Activity-01 Lab

"""
This program performs different tasks:
1. Works with variables
2. Takes user input
3. Uses conditions and loops
4. Demonstrates functions
"""
# PART 4 - Type Check

int_var = 10
float_var = 10.5
string_var = "Python"
bool_var = True

print("Type of int_var:", type(int_var))
print("Type of float_var:", type(float_var))
print("Type of string_var:", type(string_var))
print("Type of bool_var:", type(bool_var))

# PART 5 - Data Type

age_input = int(input("Enter your current age: "))
print("After 10 years, you will be:", age_input + 10)

marks1 = float(input("Enter marks 1: "))
marks2 = float(input("Enter marks 2: "))
marks3 = float(input("Enter marks 3: "))

average_marks = (marks1 + marks2 + marks3) / 3
print("Average Marks:", average_marks)

# TASK1 Even or Odd

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
    
# Task 2 – Grade System

marks = int(input("Enter your marks: "))

if marks >= 80:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Fail")
    
#Task 3 – Voting Eligibility

age_vote = int(input("Enter your age: "))

if age_vote >= 18:
    print("You can vote")
else:
    print("Not eligible")
    
#Task 4  Print Numbers 1 to 10

for i in range(1, 11):
    print(i)
    
# Task 5 – Multiplication Table

table_num = int(input("Enter number for table: "))

for i in range(1, 11):
    print(table_num, "x", i, "=", table_num * i)
    
# Task 6 – Sum of First 10 Numbers

total = 0

for i in range(1, 11):
    total = total + i

print("Sum of first 10 numbers:", total)

# Task 7 – Password Checker

correct_password = "admin1234"
entered_password = ""

while entered_password != correct_password:
    entered_password = input("Enter password: ")

print("Access Granted!")

# Task 8 – Function

def average(a, b, c):
    return (a + b + c) / 3

result = average(10, 20, 30)
print("Average using function:", result)

