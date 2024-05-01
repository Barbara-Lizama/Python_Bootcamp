##Numeric Data Types

## Data types
print(type(5))
print(type(2.5))
print(type(True))

## Mathematical operations
value1 = 4.5
value2 = 3.2
print(value1 + value2)  
print(value1 - value2)  

value1 = 4.5
i = 10
print(i + value1)
print(i - value1)
print(i / value1) 
print(i % value1)

## Coding Exercise: Calculate simple interest
## In this exercise, your task is to create a Python function named "calculate_simple_interest" that calculates the total amount after a given duration with the specified interest rate(principal 10000, interest 5, duration 5 years).
def calculate_simple_interest(principal, interest, duration):
    total_amount = principal + (principal * interest * 0.01 * duration)
    return total_amount
    
print(calculate_simple_interest(10000, 5, 5))

## Perfoming integer division
number1 = 5
number2 = 2
print(number1 // number2)

## Exponentiation
print(5 ** 3)
print(pow(5,3))

## Rounding numbers
print(round(5.6))
print(round(5.67, 1))
print(round(5.678, 2))

## Coverting int to float
print(float(5))

## Playing with decimal
import decimal
from decimal import Decimal
value1 = Decimal('4.5')
value2 = Decimal('3.2')
result = value1 - value2  
print(result)

## Boolean Types
i = 10
print(i > 15)
print(i < 15)
print(i >= 15)
print(i == 11) 

## Playing with Data Types
x = 5
y = 3.5
z = True
print(type(x))
print(type(y))
print(type(z))

is_raining = True
int_value = int(is_raining)
print(int_value)
 
str_num = "123"
num = int(str_num)
print(num)

## Coding Exercise: Library Access Permission
## In a local library, there's a specific section that only allows members who are 18 years old or older to enter. You need to create a function can_access_library  to return if a member can access this section.
def can_access_library(age):
    Check = age >= 18 
    return Check
    
print(can_access_library(17))
print(can_access_library(19))

## Coding Exercise: Vehicle Eligibility for Race
## A city is hosting a car race. However, only cars that have a maximum speed of exactly 200 km/h are allowed to participate. You need to create a function is_eligible_for_race(max_speed) to return if a car is eligible to participate.
def is_eligible_for_race(max_speed):
    Check = max_speed == 200
    return Check

print(is_eligible_for_race(150))
print(is_eligible_for_race(200))
