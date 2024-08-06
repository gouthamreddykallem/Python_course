# Week 2: Intermediate Python - Updated Daily Content

## Day 1: Object-Oriented Programming Basics

### Teaching Content (30 minutes):
1. Introduction to Object-Oriented Programming (OOP)
   - What is OOP?
   - Benefits of OOP: encapsulation, abstraction, inheritance, polymorphism

2. Classes and Objects
   - Defining a class
   - Creating instance attributes
   - Creating methods
   - The `__init__` method (constructor)
   - Creating objects (instances) of a class

3. Encapsulation
   - Public vs private attributes
   - Getter and setter methods

4. The `__str__` method for string representation

### Code Example:
```python
class BankAccount:
    def __init__(self, account_number, balance, owner_name):
        self.account_number = account_number
        self._balance = balance  # Using underscore for pseudo-private attribute
        self.owner_name = owner_name

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

    def get_balance(self):
        return self._balance

    def __str__(self):
        return f"Account {self.account_number} owned by {self.owner_name}, balance: ${self._balance}"

# Usage
account = BankAccount("123456", 1000, "John Doe")
account.deposit(500)
print(account)
```


Day 1: Object-Oriented Programming Basics
Exercise 1: Create a Bank Account Class
Create a BankAccount class with the following features:

Attributes: account_number, balance, owner_name
Methods:

deposit(amount)
withdraw(amount)
get_balance()
str() to print account info

Create multiple accounts and perform various transactions.



Exercise 2: Implement a Simple Library System
Create two classes: Book and Library:

Book: title, author, ISBN
Library: books (list of Book objects), add_book(), remove_book(), find_book_by_title()

Demonstrate adding books, removing books, and finding books in the library.