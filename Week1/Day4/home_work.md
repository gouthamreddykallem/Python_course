# Week 1, Day 4: Loops - Updated Homework

1. Advanced Fibonacci Sequence
   Extend the Fibonacci sequence generator from the lab. Write a program that:
   a) Asks the user for a maximum value
   b) Generates the Fibonacci sequence up to (but not exceeding) that maximum value
   c) Prints the sequence and the total count of numbers in the sequence

   Example:
   ```
   Enter maximum value: 100
   Fibonacci Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
   Total numbers in sequence: 12
   ```

2. Multiplication Table Generator with Formatting
   Enhance the multiplication table generator to create a formatted table for numbers 1 through 10. The table should be aligned and easy to read.

   Example output:
   ```
     1   2   3   4   5   6   7   8   9  10
   --------------------------------------
   1| 1   2   3   4   5   6   7   8   9  10
   2| 2   4   6   8  10  12  14  16  18  20
   3| 3   6   9  12  15  18  21  24  27  30
   ...
   ```

3. List Comprehension Practice
   Given the following list of numbers:
   ```python
   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
   ```
   Use list comprehensions to create the following new lists:
   a) A list of squares of even numbers
   b) A list of numbers divisible by 3
   c) A list of numbers that are both even and greater than 5

4. Password Generator
   Create a function that generates a random password. The function should:
   a) Accept parameters for password length and whether to include numbers, uppercase letters, and special characters
   b) Use loops and conditional statements to build the password
   c) Ensure the password meets the specified criteria
   
   Test your function by generating 5 different passwords with various criteria.

5. Prime Factorization
   Write a program that performs prime factorization on a given number. The program should:
   a) Ask the user for a number
   b) Use loops to find all prime factors of the number
   c) Print the prime factors

   Example:
   ```
   Enter a number: 84
   Prime factors: 2 x 2 x 3 x 7
   ```

6. Nested Loops Pattern
   Write a program that uses nested loops to print the following pattern:
   ```
   *
   **
   ***
   ****
   *****
   ****
   ***
   **
   *
   ```
   The program should ask the user for the maximum number of stars in a row.

      *
     ***
    *****
   *******

7. Bonus Challenge: Conway's Game of Life
   Implement a simple version of Conway's Game of Life. For those unfamiliar, it's a cellular automaton where cells in a grid evolve over time based on simple rules. Here's a simplified version:
   
   a) Create a 10x10 grid of cells (0 for dead, 1 for alive)
   b) Randomly initialize the grid
   c) Implement the rules:
      - Any live cell with fewer than two live neighbors dies
      - Any live cell with two or three live neighbors lives
      - Any live cell with more than three live neighbors dies
      - Any dead cell with exactly three live neighbors becomes a live cell
   d) Use nested loops to apply these rules to each cell in the grid
   e) Print the grid after each generation
   f) Run the simulation for 5 generations

   This is a complex challenge that combines nested loops, conditional statements, and 2D list manipulation.

Remember to use appropriate variable names, include comments in your code, and handle potential errors (like invalid inputs) where necessary. Test your code with different inputs to ensure it works correctly.