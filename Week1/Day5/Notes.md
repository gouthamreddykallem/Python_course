Day 5: Functions and Methods
Teaching Content (30 minutes):

Defining Functions:

Function syntax
Parameters and arguments
Return statements


Function Types:

Functions with no parameters
Functions with multiple parameters
Functions with default parameters


Built-in Functions:

print(), len(), type(), int(), str(), etc.


Methods:

String methods (upper(), lower(), strip(), etc.)
List methods (append(), remove(), sort(), etc.)



Code Examples:

# Defining a function
def greet(name):
    return f"Hello, {name}!"

# Function with multiple parameters
def add_numbers(a, b):
    return a + b

# Function with default parameter
def power(base, exponent=2):
    return base ** exponent

# Using built-in functions
numbers = [1, 2, 3, 4, 5]
print(len(numbers))
print(max(numbers))

# Using methods
text = "   Python Programming   "
print(text.strip().upper())

fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits.sort()
print(fruits)

# Week 1, Day 5: Functions and Methods - Alternative Lab Exercises

## Lab Work (15 minutes):

### Exercise 1: Temperature Converter
Create a function called `convert_temperature` that takes three parameters:
- `temperature`: the temperature value to convert
- `input_scale`: the current scale of the temperature ('C' for Celsius, 'F' for Fahrenheit)
- `output_scale`: the desired scale to convert to ('C' or 'F')

The function should return the converted temperature. Use this function to convert:
1. 32°F to Celsius
2. 100°C to Fahrenheit
3. Ask the user for a temperature, input scale, and output scale, then display the result

### Exercise 2: Password Strength Checker
Write a function called `check_password_strength` that takes a password as a parameter and returns a strength rating ('Weak', 'Medium', or 'Strong'). Use the following criteria:
- Weak: Less than 8 characters
- Medium: 8-12 characters with a mix of letters and numbers
- Strong: More than 12 characters with a mix of letters, numbers, and special characters

Test the function with at least 3 different passwords and print the results.

### Exercise 3: List Manipulation
Create the following functions and use them in a simple program:
1. `get_unique_elements(list)`: Returns a new list with duplicate elements removed
2. `get_common_elements(list1, list2)`: Returns a list of elements that appear in both input lists
3. `sort_list(list, reverse=False)`: Returns the sorted list in ascending or descending order based on the `reverse` parameter

Use these functions with sample lists and display the results.

### Exercise 4: Simple Calculator
Implement a calculator with the following functions:
1. `add(a, b)`
2. `subtract(a, b)`
3. `multiply(a, b)`
4. `divide(a, b)` (remember to handle division by zero)

Create a main function that asks the user for two numbers and an operation, then calls the appropriate function and displays the result.

### Exercise 5: String Analyzer
Write a function called `analyze_string` that takes a string as input and returns a dictionary with the following information:
- Number of characters (including spaces)
- Number of words
- Number of unique words (case-insensitive)
- Most frequent word and its count

Test this function with a sample paragraph and print the results.

### Bonus (if time allows):
Create a simple game of Hangman:
1. Write a function to choose a random word from a list of words
2. Write a function to display the current state of the word (with underscores for unguessed letters)
3. Write a function to check if a guessed letter is in the word
4. Use these functions in a main game loop that allows the user to play Hangman