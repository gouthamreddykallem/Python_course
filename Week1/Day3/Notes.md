Day 3: Control Flow
Teaching Content (30 minutes):

Conditional Statements:

if statement
if-else statement
if-elif-else statement


Comparison Operators:

==, !=, <, >, <=, >=


Logical Operators:

and, or, not


Indentation in Python

Code Examples:


# Conditional statements
age = 20

if age < 18:
    print("You are a minor")
elif age >= 18 and age < 65:
    print("You are an adult")
else:
    print("You are a senior citizen")

# Comparison and logical operators
x = 5
y = 10

if x < y and x > 0:
    print("x is positive and less than y")

is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("You can relax today!")



# Week 1, Day 3: Control Flow - Alternative Lab Exercises

## Lab Work (15 minutes):

### Exercise 1: Grade Calculator
Write a program that asks the user to input a numerical grade (0-100). Use if-elif-else statements to convert the numerical grade to a letter grade according to the following scale:
- A: 90-100
- B: 80-89
- C: 70-79
- D: 60-69
- F: Below 60

Print the corresponding letter grade.

### Exercise 2: Leap Year Checker
Create a function called `is_leap_year` that takes a year as input and returns True if it's a leap year, and False otherwise. A leap year is divisible by 4, except for century years, which must be divisible by 400. Use this function to check if the years 2000, 2100, and 2024 are leap years.

### Exercise 3: Login System
Implement a simple login system:
1. Create two variables: `correct_username = "python_user"` and `correct_password = "code123"`
2. Ask the user to input a username and password
3. Use logical operators to check if both the username and password are correct
4. If both are correct, print "Login successful!"
5. If the username is correct but the password is wrong, print "Incorrect password"
6. If the username is wrong, print "User not found"

### Exercise 4: Number Classifier
Write a program that asks the user to input a number. Then, use nested if statements to classify the number as follows:
- Positive or Negative
- Even or Odd
- If positive, also classify as:
  - Small (1-50)
  - Medium (51-100)
  - Large (>100)

Print all applicable classifications for the number.

### Exercise 5: Rock, Paper, Scissors Game
Create a simple Rock, Paper, Scissors game:
1. Ask the user to choose Rock, Paper, or Scissors
2. Generate a random choice for the computer (you can use `import random` and `random.choice(['Rock', 'Paper', 'Scissors'])`)
3. Use if-elif statements to determine the winner based on the game rules
4. Print the computer's choice and the result (Win, Lose, or Tie)

### Bonus (if time allows):
Implement a simple calculator that asks the user for two numbers and an operation (+, -, *, /). Use if-elif statements to perform the correct operation and print the result. Include error handling for division by zero.