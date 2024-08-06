
## Day 3: File Handling and Exception Handling

### Teaching Content (30 minutes):
1. File Handling
   - Opening and closing files
   - Reading from files (read(), readline(), readlines())
   - Writing to files
   - The `with` statement

2. Working with CSV files
   - The `csv` module
   - Reading and writing CSV files

3. Exception Handling
   - Try-except blocks
   - Handling specific exceptions
   - The `finally` clause
   - Raising exceptions
   - Creating custom exceptions

### Code Example:
```python
import csv

class InvalidAgeError(Exception):
    pass

def process_ages(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                age = int(row[1])
                if age < 0 or age > 120:
                    raise InvalidAgeError(f"Invalid age: {age}")
                print(f"Valid age: {age}")
            except ValueError:
                print(f"Invalid data: {row}")
            except InvalidAgeError as e:
                print(str(e))

# Usage
process_ages('ages.csv')
```


Day 3: File Handling and Exception Handling
Exercise 1: CSV Data Processor
Write a program that reads a CSV file containing student data (name, age, grade) search online for dataset, processes the data (e.g., calculate average grade), and writes the results to a new CSV file. Handle potential file I/O exceptions.
Exercise 2: Custom Exception for Data Validation
Create a custom exception called InvalidAgeError. Write a function that reads ages from a file and raises this exception if an age is negative or unreasonably high (e.g., > 80). Use try-except blocks to handle these exceptions.