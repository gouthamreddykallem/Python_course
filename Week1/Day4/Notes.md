Day 4: Loops
Teaching Content (30 minutes):

For Loops:

Iterating over sequences (lists, strings)
Using range() function
Nested for loops


While Loops:

Basic while loop structure
Using break and continue statements


Loop Control Statements:

break: exit the loop
continue: skip to the next iteration
pass: do nothing (placeholder)



Code Examples:

# For loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using range()
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Break and continue
for i in range(10):
    if i == 3:
        continue
    if i == 8:
        break
    print(i)


# Week 1, Day 4: Loops - Alternative Lab Exercises

## Lab Work (15 minutes):

### Exercise 1: Fibonacci Sequence Generator
Write a program that generates the Fibonacci sequence up to a specified number of terms. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones. Ask the user how many terms they want to generate, then use a loop to create and print the sequence.

Example output:
```
How many Fibonacci terms do you want? 8
Fibonacci Sequence: 0, 1, 1, 2, 3, 5, 8, 13
```

### Exercise 2: Multiplication Table Generator
Create a program that generates a multiplication table for a given number. Ask the user for a number, then use a loop to print the multiplication table for that number from 1 to 10.

Example output:
```
Enter a number: 7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
...
7 x 10 = 70
```

### Exercise 3: Password Attempt Limiter
Implement a program that gives a user three attempts to enter the correct password. Use a while loop to control the number of attempts. If the correct password is entered, print "Access granted." If three incorrect attempts are made, print "Access denied."

### Exercise 4: List Element Counter
Given a list of items and a specific item to search for, use a for loop to count how many times that item appears in the list. 

Example:
```python
items = ['apple', 'banana', 'orange', 'apple', 'mango', 'apple']
search_item = 'apple'
# Your code here should print: 'apple appears 3 times in the list.'
```

### Exercise 5: Prime Number Checker
Write a function that takes a number as input and returns True if it's prime, and False otherwise. Then use a loop to check and print all prime numbers between 1 and 50.

### Bonus (if time allows):
Create a simple number guessing game:
1. Generate a random number between 1 and 100.
2. Use a while loop to repeatedly ask the user for guesses.
3. Provide "too high" or "too low" feedback after each guess.
4. When the correct number is guessed, print a congratulatory message and the number of attempts made.
5. Ask if the user wants to play again, and if so, restart the game.