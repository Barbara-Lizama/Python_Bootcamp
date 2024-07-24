### Time Complexity Made Easy
## Time complexity measures how the runtime of an algorithm grows as the size of the input grows.
# CONSTANT TIME COMPLEXITY - O(1) : means that the running time of the algorithm does not depend on the size of the input.

def get_first_element(arr):
    return arr[0]

print(get_first_element([1, 2, 3]))

# LINEAR TIME COMPLEXITY - O(n): means the running time grows linearly with the size of the input.
def find_max(arr):
 
    max_val = arr[0]
 
    for num in arr:
        if num > max_val:
            max_val = num
 
    return max_val
    
print(find_max([1, 2, 3]))

# QUADRATIC TIME COMPLEXITY - O(n^2): means the running time grows with the square of the size of the input.
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)

print_pairs([1, 2, 3])

## Introduction to Recursion in Python
# CODE EXAMPLE: FACTORIAL USING RECURSION
def factorial(n):
    print(f"Calculating factorial of {n}")
    if n == 1:
        print("Reached base case: factorial of 1 is 1")
        return 1
    result = n * factorial(n - 1)
    print(f"factorial of {n} is {result}")
    return result
result = factorial(3)
print(f"Final Output: Factorial of 3 is {result}")

## Sum of a List using Recursion
def sum_of_list(lst, n):
    print(f"Calculating sum of first {n} elements of {lst}")
    if n == 0:
        print("Reached base case: sum is 0")
        return 0
    result = lst[n-1] + sum_of_list(lst, n-1)
    print(f"Sum of first {n} elements is {result}")
    return result
 
# Running the step-by-step example
result = sum_of_list([1, 2, 3], 3)
print(f"Final Output: Sum of list is {result}")

