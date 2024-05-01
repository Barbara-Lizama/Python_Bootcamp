## Creating a Functions
def print_hello_world_once():
    print("Hello World")

print_hello_world_once()

## Function can have parameters
def print_hello_world(no_of_times):
    print(no_of_times)
print_hello_world(5)

## Function with multiple parameters
def product_of_two_numbers(a,b):
    print(a * b)
product_of_two_numbers(1,2)

## Built in function returning a value
maximum = max(1,2,3,4)
print(maximum)
print(maximum * 5)

## Creating a function returning a value
def product_of_two_numbers(a,b):
    product = a * b;
    return product
 
print(product_of_two_numbers(2,3))

## The result can be stored in variable and used later
product_result = product_of_two_numbers(2,3)
print(product_result)
print(product_result * 10)

## Calculate sum of three numbers
def calculate_sum_of_three_numbers(a, b, c):
    sum = a + b + c
    return sum

print(calculate_sum_of_three_numbers(2,3,4))

## Calculate the cube of a number
def cube_of_number (n):
    cube = n * n * n
    return cube
    
print(cube_of_number(3))
    
## Calculate the third angle of a triangle
def calculate_third_angle (first_angle, second_angle):
    third_angle = 180 - (first_angle + second_angle)
    return third_angle
    
print(calculate_third_angle(15, 60))

## Calculate the sum of squares of first n even numbers
def sum_of_squares (n):
    sum = 0
    for i in range (2, n * 2 + 1, 2):
        sum = (i * i) + sum
    return sum
        
print(sum_of_squares(5))