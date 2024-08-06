# Week 1, Day 5: Functions and Methods - Updated Homework

1. Advanced Temperature Converter
   Extend the temperature converter function from the lab to include Kelvin. Create a function `convert_temperature(temperature, input_scale, output_scale)` that can convert between Celsius, Fahrenheit, and Kelvin. Then write a program that:
   a) Converts 0°C to Fahrenheit and Kelvin
   b) Converts 98.6°F to Celsius and Kelvin
   c) Converts 300K to Celsius and Fahrenheit
   d) Allows the user to input a temperature, input scale, and output scale, then displays the result

2. Text Analyzer
   Create a function called `analyze_text(text)` that takes a string as input and returns a dictionary with the following information:
   - Word count
   - Character count (excluding spaces)
   - Average word length
   - Most common word and its frequency
   - Number of sentences
   - Unique words (case-insensitive)
   
   Use this function to analyze a paragraph of text (you can use a famous quote or passage from a book). Print the results in a formatted manner.

3. List Operations
   Create the following functions:
   a) `merge_sorted_lists(list1, list2)`: Merges two sorted lists into a single sorted list
   b) `find_median(numbers)`: Finds the median of a list of numbers
   c) `remove_outliers(numbers, n)`: Removes the n smallest and n largest values from the list
   
   Write a program that demonstrates the use of these functions with sample data.

4. Password Generator and Validator
   Create two functions:
   a) `generate_password(length, use_uppercase, use_numbers, use_special_chars)`: Generates a random password based on the specified criteria
   b) `validate_password(password)`: Checks if a password meets the following criteria:
      - At least 8 characters long
      - Contains at least one uppercase letter, one lowercase letter, one number, and one special character
      - Returns True if the password is valid, False otherwise
   
   Use these functions to generate 5 random passwords and validate them. Print the passwords and whether they are valid.

5. Simple Encryption/Decryption
   Implement a simple Caesar cipher encryption and decryption:
   a) Create a function `encrypt(message, shift)` that encrypts a message by shifting each letter by the specified amount
   b) Create a function `decrypt(encrypted_message, shift)` that decrypts an encrypted message
   c) Demonstrate the use of these functions by encrypting and then decrypting a sample message

6. Math Functions Library
   Create a module called `math_functions.py` with the following functions:
   a) `factorial(n)`: Calculates the factorial of a number
   b) `fibonacci(n)`: Returns the nth Fibonacci number
   c) `is_prime(n)`: Checks if a number is prime
   d) `gcd(a, b)`: Finds the greatest common divisor of two numbers
   
   In a separate file, import this module and demonstrate the use of each function with appropriate examples.

7. Bonus Challenge: Tic-Tac-Toe Game
   Implement a Tic-Tac-Toe game using functions. Create the following functions:
   a) `initialize_board()`: Creates an empty 3x3 board
   b) `print_board(board)`: Prints the current state of the board
   c) `is_winner(board, player)`: Checks if the specified player has won
   d) `is_board_full(board)`: Checks if the board is full (tie game)
   e) `get_player_move(player)`: Asks the player for their move
   f) `make_move(board, player, position)`: Places the player's mark on the board
   
   Use these functions to create a main game loop that allows two players to play Tic-Tac-Toe.

Remember to use appropriate variable names, include comments in your code, and handle potential errors (like invalid inputs) where necessary. Test your code with different inputs to ensure it works correctly.