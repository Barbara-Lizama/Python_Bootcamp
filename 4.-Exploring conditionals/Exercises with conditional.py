## Coding exercise: Are both numbers even
# In this exercise, your task is to create a Python function named are_both_even that checks if both input integers are even.
def are_both_even(i,j):
    i = i % 2 == 0
    j = j % 2 == 0
    
    return i and j
    
print(are_both_even(4, 2))
print(are_both_even(3, 4))

## Coding exercise: Check if a Year is a Leap Year
# Your task is to complete the implementation of the method is_leap_year to determine if a given year is a leap year.
# A year is a leap year in the Gregorian calendar if:
# It is divisible by 4 (AND)
# It is NOT divisible by 100 (except when it is divisible by 400)
# Not Divisible by 4 - NOT Leap Year (2041)
# Divisible by 4 and NOT divisible by 100 - Leap Year (2048)
# Divisible by 4 and divisible by 100 - Additional check needed
# Divisible by 4, divisible by 100, divisible by 400 - Leap Year (2000, 2400)
# Divisible by 4, divisible by 100, NOT divisible by 400 - NOT Leap Year (2100, 2200, 2300)

def is_leap_year(year):
    
    if year <= 0:
        return False
        
    if not year % 4 == 0:
        return False

    if not year % 100 == 0:
        return True
        
    if year % 400 == 0:
        return True
        
    return False

print(is_leap_year(2000))
print(is_leap_year(1900))

## Coding Exercise: Is it a Right Angled Triangle?
# In this exercise, your task is to create a Python function named is_right_angled_triangle that determines whether the given lengths of three sides form a right-angled triangle or not.
# As per the Pythagorean theorem, in a right-angled triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides.
# If any side has a non-positive length, it's not considered a valid triangle.

def is_right_angled_triangle(side1,side2,side3):
    if side1 <= 0:
        return False
        
    if side2 <= 0:
        return False    
    
    if side3 <= 0:
        return False
        
    if (side3 * side3  == side1 * side1 + side2 * side2):
       return True
    if (side2 * side2  == side1 * side1 + side3 * side3):
        return True
    if (side1 * side1  == side3 * side3 + side2 * side2):
        return True
        
    return False
    
print(is_right_angled_triangle(3, 4, 5))

## Playing with Conditionals
number = 5
if(number%2==0):
   isEven = True
else:
   isEven = False
print(isEven)

x = 10
y = 5
if x > 5 and y < 10:
    print("Condition 1")
elif x == 10 or y == 5:
    print("Condition 2")
else:
    print("Condition 3")

## Coding exercise: Student Grades A to F based on Marks
# In this exercise, your task is to create a Python function named assign_grade that assigns a grade (A to F) to a student based on the marks they received.
# Here is the grade assignment criteria:
# If marks are 90 or more, grade is 'A' / If marks are 80 or more but less than 90, grade is 'B' / If marks are 70 or more but less than 80, grade is 'C'
# If marks are 60 or more but less than 70, grade is 'D'/ If marks are 50 or more but less than 60, grade is 'E'/ If marks are less than 50, grade is 'F'

def assign_grade(marks):
    if marks >= 90:
       return ('A')
    elif marks >= 80:
         return('B') 
    elif marks >= 70:
         return('C')
    elif marks >= 60:
         return('D')
    elif marks >= 50:
         return('E')
    else :
         return('F')
         
    return grade
         
print(assign_grade(65))  

## Coding Exercise: Weather Advisor
# In this exercise, your task is to create a Python function named provide_weather_advisory that provides a weather advisory message based on the current temperature.
# Here is the advisory message criteria:
# If the temperature is below 0, return "It's freezing! Wear a heavy coat." / If the temperature is between 0 and 10 (inclusive), return "It's cold! Bundle up."
# If the temperature is between 11 and 20 (inclusive), return "It's cool! A light jacket will do." / If the temperature is above 20, return "It's warm! Enjoy the day."

def provide_weather_advisory(temperature):
    if temperature < 0:
        return ("It's freezing! Wear a heavy coat.")
    elif temperature <=10:
        return("It's cold! Bundle up.")
    elif temperature <=20:
        return("It's cool! A light jacket will do.")
    else :
        return ("It's warm! Enjoy the day.")
        
        return message
        
print(provide_weather_advisory(25))