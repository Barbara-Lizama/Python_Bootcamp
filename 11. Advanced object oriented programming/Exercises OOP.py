## Coding Exercise: Implementing Car with Multiple Inheritance
# You are tasked with implementing a Car class that inherits from two other classes: Engine and Wheels.

class Engine:
    def start_engine(self): 
        return "Engine started"
    
class Wheels:
    def number_of_wheels(self): 
        return 4

class Car (Engine , Wheels): 
    def drive(self):
        return "Car is driving"
    
vehicle = Car()

result_start = vehicle.start_engine()
print(result_start)

result_drive = vehicle.drive()
print(result_drive)

num_wheels = vehicle.number_of_wheels()  
print(num_wheels)

## Coding Exercise: Create Abstract Class Shape Implementations
# You are tasked with creating a program that models shapes. You will need to define an abstract class Shape with two abstract methods: area and perimeter.

from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Rectangle class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
      return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Circle class inheriting from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius * self.radius)

    def perimeter(self):
        return 2 * 3.14 * self.radius

shapes = [Circle(5), Rectangle(2, 5)]

for shape in shapes:
   print(f"The area of {shape} is {shape.area()}")
   print(f"The perimeter of {shape} is {shape.perimeter()}")


    