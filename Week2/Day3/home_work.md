## Day 3: File Handling and Exception Handling

1. Create a program that reads a CSV file containing product data (name, price, quantity). The program should:
   - Calculate the total value of inventory (price * quantity for each product)
   - Write a new CSV file with product name, price, quantity, and total value
   - Handle potential exceptions:
     - FileNotFoundError
     - ValueError (for invalid numeric data)
     - A custom exception `NegativeValueError` for negative prices or quantities

2. Implement a logging system that writes any exceptions encountered to a log file, including timestamp and error details.

3. Create a function `validate_product_data(name, price, quantity)` that raises appropriate exceptions for invalid data (e.g., empty name, negative price/quantity).

4. Use a `try`-`except`-`finally` structure to ensure the files are properly closed even if an exception occurs.

