
## Day 5: Functional Programming and List Comprehensions

### Teaching Content (30 minutes):
1. Functional Programming Concepts
   - First-class functions
   - Pure functions
   - Higher-order functions

2. Lambda Functions

3. Map, Filter, and Reduce
   - Using `map()` for transformations
   - Using `filter()` for filtering data
   - Using `functools.reduce()` for aggregations

4. List Comprehensions
   - Basic syntax
   - Conditional list comprehensions
   - Nested list comprehensions

5. Generator Expressions

### Code Example:
```python
from functools import reduce

# Map, Filter, Reduce
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
sum_all = reduce(lambda x, y: x + y, numbers)

print(f"Squared: {squared}")
print(f"Evens: {evens}")
print(f"Sum: {sum_all}")

# List comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Flattened matrix: {flattened}")

# Generator expression
sum_of_squares = sum(x**2 for x in range(1, 101))
print(f"Sum of squares from 1 to 100: {sum_of_squares}")
```

Day 5: Functional Programming and List Comprehensions
Exercise 1: Data Transformation Pipeline
Create a pipeline of functions that transform a list of dictionaries containing personal information. Use map(), filter(), and reduce() to:

Filter out people under 18
Transform dates to a standard format
Calculate the average age of the remaining people

Exercise 2: Matrix Operations with List Comprehensions
Implement the following matrix operations using list comprehensions:

Matrix addition
Matrix transposition
Flattening a 2D matrix to a 1D list