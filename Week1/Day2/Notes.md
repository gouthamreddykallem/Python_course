Day 2: Python Object and Data Structure Basics
Teaching Content (30 minutes):
Variables and Basic Data Types:

Premitive datatypes

Declaring and assigning variables
Naming conventions (lowercase, underscores for spaces)
Dynamic typing in Python
Integers, floats, strings, and booleans


Data Structures:

Lists: ordered, mutable collections
Dictionaries: key-value pairs, unordered, mutable


Basic Operations:

Arithmetic operations (+, -, *, /, **, //)
String operations (concatenation, repetition)
Type conversion (int(), float(), str(), bool())


Working with Lists:

Creating lists
Accessing elements (indexing)
Basic list methods (append, insert, remove, sort)


Working with Dictionaries:

Creating dictionaries
Accessing and modifying values
Adding and removing key-value pairs


String Manipulation:

String methods (upper(), lower(), strip(), replace())
String formatting (f-strings)

Code Examples:

# Variables and basic data types
name = "Alice"
age = 30
height = 1.75
is_student = True

# List operations
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
numbers.insert(0, 0)
numbers.remove(30)
numbers.sort(reverse=True)
print(numbers)

# Dictionary operations
personal_info = {
    "name": "Bob",
    "age": 25,
    "height": 1.80,
    "favorite_color": "blue",
    "is_student": False
}
print(personal_info["favorite_color"])
personal_info["occupation"] = "Engineer"

# String manipulation
text = "Python programming is fun!"
print(len(text))
print(text.upper())
print("fun" in text)
new_text = text.replace("fun", "awesome")
print(new_text)

# Type conversion
num_string = "42"
float_num = 3.14
bool_val = True

print(int(num_string), float(num_string))
print(int(float_num), str(float_num))
print(int(bool_val), str(bool_val))

# User input and calculations
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Quotient: {num1 / num2}")
print(f"Exponent: {num1 ** num2}")


Lab Work (15 minutes):

# Week 1, Day 2: Python Object and Data Structure Basics - Alternative Lab Exercises

## Lab Work (15 minutes):

### Exercise 1: Personal Information Dictionary
Create a dictionary called `personal_info` that contains the following information about you:
- Name
- Age
- Height (in meters)
- Favorite color
- Is_student (boolean)

Print the entire dictionary, then access and print your favorite color separately.

### Exercise 2: List Operations
Create a list called `numbers` with the values [10, 20, 30, 40, 50]. Perform the following operations:
1. Append 60 to the list
2. Insert 0 at the beginning of the list
3. Remove the number 30 from the list
4. Sort the list in descending order
5. Print the final list

### Exercise 3: String Manipulation
Given the string `"Python programming is fun!"`, perform the following operations:
1. Print the length of the string
2. Convert the string to uppercase and print it
3. Check if the string contains the word "fun" and print the result
4. Replace "fun" with "awesome" and print the new string

### Exercise 4: Basic Calculations
Ask the user to input two numbers. Convert these inputs to floats and perform the following operations:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponentiation (first number raised to the power of the second number)

Print the results of all operations.

### Exercise 5: Type Conversion
Create the following variables:
- `num_string = "42"`
- `float_num = 3.14`
- `bool_val = True`

Convert each of these to the other two types (where possible) and print the results. For example:
- Convert `num_string` to an integer and a float
- Convert `float_num` to an integer and a string
- Convert `bool_val` to an integer and a string

### Bonus (if time allows):
Create a list of your three favorite fruits. Ask the user to input a fruit name. Check if the fruit is in your list of favorites. If it is, print "This is one of my favorite fruits!" If not, append it to the list and print the updated list.