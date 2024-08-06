# Week 1, Day 3: Control Flow - Updated Homework

1. Enhanced Grade Calculator
   Extend the grade calculator from the lab to include plus and minus grades:
   - A+: 97-100
   - A: 93-96
   - A-: 90-92
   - B+: 87-89
   - B: 83-86
   - B-: 80-82
   (Continue this pattern for C and D grades)
   - F: Below 60

   Ask the user to input a numerical grade and print the corresponding letter grade.

2. Password Strength Checker
   Create a function that takes a password as input and returns its strength as "Weak", "Medium", or "Strong". Use the following criteria:
   - Weak: Less than 8 characters
   - Medium: 8 or more characters, with at least one number and one letter
   - Strong: 8 or more characters, with at least one number, one uppercase letter, one lowercase letter, and one special character (!@#$%^&*)

   Test your function with at least 5 different passwords and print the results.

3. ATM Simulator
   Create a simple ATM simulator with the following features:
   - Start with a balance of $1000
   - Present a menu to the user with options: Check Balance, Deposit, Withdraw, Exit
   - Use a while loop to keep the program running until the user chooses to exit
   - For withdrawals, check if there's enough balance. If not, print an error message
   - For deposits and withdrawals, ensure the amount is positive

4. Rock, Paper, Scissors, Lizard, Spock Game
   Extend the Rock, Paper, Scissors game to include Lizard and Spock. The rules are:
   - Scissors cuts Paper
   - Paper covers Rock
   - Rock crushes Lizard
   - Lizard poisons Spock
   - Spock smashes Scissors
   - Scissors decapitates Lizard
   - Lizard eats Paper
   - Paper disproves Spock
   - Spock vaporizes Rock
   - Rock crushes Scissors

   Implement this game where the user plays against the computer. Keep track of the score and allow the user to play multiple rounds until they choose to quit.

5. Number Guessing Game
   Create a number guessing game with the following features:
   - The computer chooses a random number between 1 and 100
   - The user has 7 attempts to guess the number
   - After each guess, tell the user if their guess was too high or too low
   - If the user guesses correctly, congratulate them and tell them how many attempts it took
   - If the user doesn't guess correctly after 7 attempts, reveal the number

6. Bonus Challenge: Simple Adventure Game
   Create a text-based adventure game where the player navigates through a series of rooms. Each room should present a choice to the player (e.g., "go left", "go right", "open door"). Use nested if-elif statements to determine the outcome of each choice. Include at least 5 rooms with different scenarios. The game should end when the player either wins (reaches a treasure room) or loses (enters a room with a monster).

Remember to use appropriate variable names, include comments in your code, and handle potential errors (like invalid inputs) where necessary. Test your code with different inputs to ensure it works correctly.