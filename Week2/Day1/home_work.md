## Day 1: Object-Oriented Programming Basics

1. Create a `Vehicle` class with the following features:
   - Attributes: make, model, year, fuel_efficiency (miles per gallon)
   - Methods:
     - `__init__` (constructor)
     - `fuel_needed(miles)`: calculates fuel needed for a given distance
     - `__str__`: returns a string representation of the vehicle

2. Create a `Garage` class that can store multiple `Vehicle` objects:
   - Methods:
     - `add_vehicle(vehicle)`
     - `remove_vehicle(vehicle)`
     - `get_vehicles_by_make(make)`
     - `total_fuel_needed(miles)`: calculates total fuel needed for all vehicles to travel the given miles

3. Create several `Vehicle` objects and a `Garage` object. Demonstrate the use of all methods.

