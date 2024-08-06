## Day 5: Functional Programming and List Comprehensions

1. Implement a data processing pipeline using functional programming concepts:
   - Start with a list of dictionaries containing student data (name, age, grades)
   - Use `map` to calculate the average grade for each student
   - Use `filter` to select students with an average grade above 80
   - Use `reduce` to find the student with the highest average grade
   - Implement this both with and without lambda functions

2. Create a module with higher-order functions for common list operations:
   - `sort_by(list, key_func)`
   - `group_by(list, key_func)`
   - `find_first(list, predicate_func)`
   - Demonstrate the use of these functions with different key and predicate functions

3. Use list comprehensions to perform the following tasks:
   - Create a multiplication table (10x10 matrix)
   - Generate a list of prime numbers up to 100
   - Flatten a list of lists into a single list
   - Create a dictionary mapping numbers to their squares for numbers 1 to 20

4. Implement a simple text analysis tool using functional programming and list comprehensions:
   - Read a text file
   - Use list comprehensions to:
     - Extract all unique words
     - Find all words longer than a given length
   - Use `map` and `reduce` to:
     - Convert all words to lowercase
     - Calculate the average word length
   - Use `filter` to remove common stop words (provide a list of stop words)

Remember to use appropriate variable names, include comments in your code, and handle potential errors where necessary. Test your code with different inputs to ensure it works correctly.