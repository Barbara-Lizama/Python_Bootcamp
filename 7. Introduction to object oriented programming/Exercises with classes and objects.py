## Coding Exercise: Inches to Object
# In this problem, you have to complete the implementation of a Dimension class in Python that represents measurements in feet and inches. One foot is equal to 12 inches

class Dimension:
    def __init__(self, inches): #convert given inches into feet and inches
        if inches >= 0:
            self.inches = inches % 12
            self.feet = inches//12
        else:
            self.inches = -1
            self.feet = -1
        
dim1= Dimension(25) 
print(dim1.feet)  
print(dim1.inches) 

dim2= Dimension(-1)
print(dim2.feet)  
print(dim2.inches) 

## Coding Exercise: Create Square with Area and Perimeter Methods
# In this exercise, you're tasked with implementing a class called Square in Python. This class is responsible for modeling a geometric shape - a square.
# A Square object has one attribute, side (of type int), which denotes the length of a side of the square.
# The Square class has a constructor that takes an integer argument. This argument should be used to initialize the side attribute.
# This class also includes two methods:
# calculate_area(): This method calculates and returns the area of the square. The area of a square is given by the formula: side * side. However, in the real world, a square cannot have a side length of zero or less. So, if side is less than or equal to zero, this method should return -1 to indicate an invalid value.
# calculate_perimeter(): This method calculates and returns the perimeter of the square. The perimeter of a square is given by the formula: 4 * side. Similar to the above, if side is less than or equal to zero, this method should return -1 to indicate an invalid value.
# Your task is to complete the implementation of the constructor and these two methods.

class Square:
    def __init__(self, side): 
        self.side = side
        
    def calculate_area(self):
        if self.side <= 0 :
            return -1
        return self.side * self.side
        
    def calculate_perimeter(self):
        if self.side <= 0:
            return -1
        return 4 * self.side 
            
square = Square (12)
print(square.calculate_area())
print(square.calculate_perimeter())
    
square_with_zero_side = Square(-3)
print(square_with_zero_side.calculate_area()) 
print(square_with_zero_side.calculate_perimeter())
    
## Coding Exercise: Create a Point class with 2 d co-ordinates x,y
# In this exercise, you're tasked with completing the implementation of the Point class in Python. A point represents a location in a two-dimensional space, characterized by its x and y coordinates.

import math

class Point:

    def __init__(self, x, y): 
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx * dx + dy * dy)
    
## Playing with object oriented programming
# Organizing code as classes helps us make code more maintainable.
    
class Car:
    pass
my_car = Car()
print(type(my_car))
 
class MyClass:
    def empty_method(self):
        pass
my_instance = MyClass()
my_instance.empty_method()
 
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
 
    def area(self):
        return self.length * self.width
 
my_rect = Rectangle(5, 3)
print(my_rect.area())
 

class BankAccount:
    def __init__(self):
        self.balance = 0
 
    def deposit(self, amount):
        self.balance += amount
 
    def withdraw(self, amount):
        self.balance -= amount
 
    def get_balance(self):
        return self.balance
 
my_account = BankAccount()
my_account.deposit(100)
my_account.withdraw(30)
print(my_account.get_balance())

## Coding Exercise: RGB Color Class
# The Red-Green-Blue (RGB) model is a popular way to represent colors in computer systems. In this model, each color is represented as a combination of the primary colors red, green, and blue. Each of these primary colors can have intensity values ranging from 0 to 255.
# In this exercise, you are tasked with completing the RGBColor class that models a color in the RGB model. The class has attributes for the red, green, and blue intensities, and methods to get these values. Additionally, there's an invert method that changes the color to its complementary color (the inverse color on a color wheel).

class RGBColor:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
        
    def invert(self):
        self.red = (255 - self.red)
        self.green = (255 - self.green)
        self.blue = (255 - self.blue)
    
color = RGBColor(255, 0, 0)
color.invert()
print(color.red)   
print(color.green) 
print(color.blue)  