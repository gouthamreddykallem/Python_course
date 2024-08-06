
## Day 2: Inheritance and Polymorphism

### Teaching Content (30 minutes):
1. Inheritance
   - Concept of base class (parent) and derived class (child)
   - Syntax for creating a derived class
   - Method overriding
   - The `super()` function

2. Polymorphism
    - Duck Typing
    - Method Overriding(same as inheritance)
    - Method Overloading (achieved through default arguments)
    - Operator Overloading

3. Abstract Base Classes
   - The `abc` module
   - Abstract methods

### Code Example:
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Usage
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(f"Area: {shape.area()}")
```


Day 2: Inheritance and Polymorphism
Exercise 1: Shape Hierarchy
Create a base class Shape with a method area(). Then create subclasses Circle, Rectangle, and Triangle that inherit from Shape and implement their specific area calculations.
Exercise 2: Employee Management System
Create a base class Employee with attributes name and ID. Then create subclasses Manager, Developer, and Salesperson with specific attributes and methods. Implement a method calculate_bonus() in each subclass that calculates bonus differently based on the employee type.