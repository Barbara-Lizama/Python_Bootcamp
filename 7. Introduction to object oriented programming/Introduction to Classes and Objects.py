##  Introduction To Object-Oriented Programming (OOP)
# STRUCTURED PROGRAMMING: code is organized around functions.
def login(username, password):
    pass
 
def logout():
    pass

# OBJECT ORIENTED PROGRAMMING: code is organized around classes and objects.
class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

## Introduction To Classes and Objects in Python 
# Creating an Empty Class
class Country:
    pass

# Creating an Instance of a Class
india = Country()
usa = Country()
netherlands = Country()

# Adding State to Objects
india.name = 'India'
india.capital = 'New Delhi'
 
usa.name = 'USA'
usa.capital = 'Washington'
 
netherlands.name = 'Netherlands'
netherlands.capital = 'Amsterdam'

# Accessing Object Attributes
print(india.name)  
print(usa.capital)  

## Exercise create class
class Book:
    pass

first_book = Book()
second_book = Book()
third_book = Book()

first_book.name = 'A name unknown'
second_book.name = 'Powerless'
third_book.name = 'Bride'
 
print(first_book.name)
print(second_book.name)
print(third_book.name)

## Constructor 
# When you create instances of a class, sometimes you want to set an initial state for those instances. This is where constructors come into play.

class MotorBike:
    def __init__(self):
        print("MotorBike instance created")

honda = MotorBike()

# We can add parameters to the constructor to accomplish this.

class MotorBike:
    def __init__(self, speed):
        print(speed)
 
honda = MotorBike(50)

# the Book class with a constructor so we can create books with names

class Book:
    def __init__(self, name):
        self.name = name
 
learning_python = Book('Learning Python In 100 Steps')
print(learning_python.name) 

# It’s a good practice to define and initialize all instance attributes in the constructor.

class Planet:
    def __init__(self, name="Earth"):
        self.name = name
        self.speed = 10
        self.distance_from_sun = 10000
 
planet = Planet()
 
print(planet.speed) 
print(planet.distance_from_sun) 

##  Introducing Methods and Encapsulation
# In this lab, we’ll discuss the object-oriented principle of encapsulation and learn how to encapsulate behavior within a class using instance methods. We’ll build upon our MotorBike class to add methods that allow for the changing of a motorbike’s speed.

class MotorBike:
    def __init__(self, speed):
        self.speed = speed

# Adding instance methods to modify attributes (add behavior)

    def increase_speed(self, how_much):
        self.speed += how_much

    def decrease_speed(self, how_much):
        self.speed -= how_much

ducati = MotorBike(250)
print(ducati.speed)

ducati.increase_speed(25)
print(ducati.speed)

ducati.decrease_speed(25)
print(ducati.speed)  

## Everything is an Object
# Understanding data types of basic values. Python treats even basic data types like integers, booleans, strings, and floats as objects. That means they are instances of classes.

print(type(7))  
print(type(True))  
print(type('Hawaii'))  
print(type(2.5))  

## Even a function is an object
# In Python, functions are also treated as objects. This allows you to assign functions to variables and pass them around, giving you a lot of flexibility.

def do_something():
    print("something")
 
# Functions as objects
print(do_something)

# Assigning functions to variables
test = do_something
test() 


