## Print Sum of squares of first 10 numbers
sum_of_squares = 0
for i in range(1,11):
    sum_of_squares = (i * i) + sum_of_squares
    
print(sum_of_squares)

## Print Factorial of 6
factorial = 1
for i in range(1,7):
    factorial = i * factorial
    
print(factorial)

## Introduction to Nested for loops
# Define the outer loop
for i in range(1, 3):
 
    # Define the inner loop
    for j in range(1, 3):
    
        print(f"i = {i}, j = {j}")

