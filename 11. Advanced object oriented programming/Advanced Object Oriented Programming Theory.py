## OOP Basics revisited
# The objective of this learning lab is to delve into advanced aspects of Object-Oriented Programming (OOP) in Python. Topics like object composition, inheritance, and class design will be explored.

# Define the Fan class
class Fan:
# Constructor to initialize the fan
    def __init__(self, make, radius, color):
        self.make = make
        self.radius = radius
        self.color = color
        self.speed = 0  # Initial speed is 0
        self.is_on = False  # Fan is initially off
 
# Method to represent the Fan object as a string
    def __repr__(self):
        return repr((self.make, self.radius, self.color, self.speed, self.is_on))

# Method to switch the fan on
    def switch_on(self):
        self.is_on = True
        self.speed = 3  # Set initial speed to 3

# Method to switch the fan off
    def switch_off(self):
        self.is_on = False
        self.speed = 0  # Reset speed to 0
 
# Method to increase the fan speed
    def increase_speed(self):
        if self.is_on and self.speed < 5:  # Max speed is 5
            self.speed += 1
 
# Method to decrease the fan speed
    def decrease_speed(self):
        if self.is_on and self.speed > 0:  # Min speed is 0
            self.speed -= 1
 
# Create a Fan object and test the methods
fan = Fan('Manufacturer 1', 5, 'Green')
print(fan)  # Output: ('Manufacturer 1', 5, 'Green', 0, False)
 
fan.switch_on()
print(fan)  # Output: ('Manufacturer 1', 5, 'Green', 3, True)
 
fan.increase_speed()
print(fan)  # Output: ('Manufacturer 1', 5, 'Green', 4, True)
 
fan.switch_off()
print(fan)  # Output: ('Manufacturer 1', 5, 'Green', 0, False)

## Exploring object composition in OOP
# we will explore the concept of object composition by creating two related classes: Book and Review. This is to demonstrate how a class can contain objects from another class, further exemplifying the concept of object composition.

# Define the Book class
class Book(object):
    # Constructor to initialize the Book
    def __init__(self, id, name, author):
        self.id = id
        self.name = name
        self.author = author
        self.reviews = []  # Empty list for storing reviews
 
    # Representation method for printing the Book object
    def __repr__(self):
        return repr((self.id, self.name, self.author, self.reviews))

# Create a Book instance
book = Book(123, 'Object Oriented Programming with Python', 'Ranga')
print(book) 

## Creating the Review Class

# Define the Review class
class Review:
    # Constructor to initialize the Review
    def __init__(self, id, description, rating):
        self.id = id
        self.description = description
        self.rating = rating
 
    # Representation method for printing the Review object
    def __repr__(self):
        return repr((self.id, self.description, self.rating))
    
review = Review(10, 'Great Book', 5)
print(review)  # Output: (10, 'Great Book', 5)

# Add the add_review method to the Book class
def add_review(self, review):
    self.reviews.append(review)

# Attach this method to the Book class
setattr(Book, 'add_review', add_review)
 
# Add reviews to the book
book.add_review(Review(10, 'Great Book', 5))
book.add_review(Review(101, 'Awesome', 5))
print(book)

## Exploring Inheritance in Object-Oriented Programming (OOP)
# we will look into why and when we might need inheritance in object-oriented programming. We’ll demonstrate this by creating a simple example involving two classes: Animal and Pet.

# Define Animal class with a bark method
class Animal:
    def bark(self):
        print("bark")
 
# Create an instance of Animal and call its bark method
animal = Animal()
animal.bark()

class Pet(Animal):
    def groom(self):
        print("groom")
 
# Create an instance of Pet
dog = Pet()
 
# Check if inheritance works
dog.bark()  # Output: bark
dog.groom()  # Output: groom

## Exploring object Class
# we’ll delve into the concept of Python’s object class, which serves as a base for all other Python classes. We’ll learn how Python’s inheritance from the object class influences the default behavior of our classes and instances.

# Define a Book class with no methods or properties
class Book(): pass
 
# Create an instance of Book and print it
book = Book()
print(book)  # Output: <__main__.Book object at some_memory_location>

# Define a Book class with a custom __repr__ method
class Book():
    def __repr__(self):
        return repr('new book')
 
# Create an instance of Book and print it
book = Book()
print(book)  

## Exploring Multiple Inheritance
# Multiple inheritance allows a single class to inherit from more than one class. We’ll look at a real-world example by creating classes for LandAnimal, WaterAnimal, and Amphibian.

class LandAnimal: 
    def __init__(self):
        super().__init__()
        self.walking_speed = 5
    def increase_walking_speed(self, how_much):
        self.walking_speed += how_much
        
class WaterAnimal:
    def __init__(self):
        super().__init__()
        self.swimming_speed = 10
    def increase_swimming_speed(self, how_much):
        self.swimming_speed += how_much

class Amphibian(WaterAnimal, LandAnimal):
    def __init__(self):
        super().__init__()
 
amphibian = Amphibian()

amphibian.increase_walking_speed(50)
amphibian.increase_swimming_speed(25)

print(amphibian.walking_speed)  
print(amphibian.swimming_speed)  

## Understanding Abstract Classes
# The objective of this step is to delve into abstract classes in Python’s Object-Oriented Programming (OOP). We will create an abstract class and discuss how and why you should use them.

from abc import ABC, abstractmethod
 
class AbstractAnimal(ABC):
    @abstractmethod
    def bark(self): pass

# Attempting to instantiate an abstract class will result in an error
# animal = AbstractAnimal()  
# TypeError: Can't instantiate abstract class AbstractAnimal with abstract methods bark
 
# Implementing the abstract method in a subclass
class Dog(AbstractAnimal):
    def bark(self):
        print("Bow Bow")
 
Dog().bark()  # Output: "Bow Bow"

## Using Template Method Pattern in Object-Oriented Programming (OOP)
# The objective of this step is to dive into a specific design pattern known as the Template Method Pattern. This pattern is particularly useful when you want to define the structure of an algorithm but allow subclasses to implement specific steps.

from abc import ABC, abstractmethod
 
class AbstractRecipe(ABC):
 # step 1
    def execute(self):
        self.prepare()
        self.recipe()
        self.cleanup()
 
 # step 2
    @abstractmethod
    def prepare(self): pass
 
    @abstractmethod
    def recipe(self): pass
 
    @abstractmethod
    def cleanup(self): pass 

# Example Recipe1
class Recipe1(AbstractRecipe):
 
    def prepare(self):
        print('do the dishes')
        print('get raw materials')
 
    def recipe(self):
        print('execute the steps')
 
    def cleanup(self): pass
 
Recipe1().execute()

# Example Recipe2
class MicrowaveRecipe(AbstractRecipe):
 
    def prepare(self):
        print('do the dishes')
        print('get raw materials')
        print('switch on microwave')
 
    def recipe(self):
        print('execute the steps')
 
    def cleanup(self):
        print('switch off microwave')
 
MicrowaveRecipe().execute()

## Understanding Polymorphism
# Polymorphism makes your code easy to manage and update. It lets you write a piece of code that can work with objects of different types, which makes your program flexible and reusable.

# Defining the shape class (the parent class)
class Shape:
    def area(self):
        pass

# Defining Subclasses
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# Demostrating polymorphism
shapes = [Circle(5), Square(4), Rectangle(2, 5)]

for shape in shapes:
    print(f"The area of {shape} is {shape.area()}")

