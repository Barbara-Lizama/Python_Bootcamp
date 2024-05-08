## Basic for loop
for i in range(1,10):
    print(i)

## Perfoming operation within for loop
for i in range(1,11):
    print(i * i)

## Calculating Sum with for loop
sum = 0
for i in range(1,11):
    sum = sum + i
    print(sum) ## print the sum number by number
print(sum) ## print the total sum 

## Multiplication Table
for i in range(1,11):
    print(f"5 * {i} = {5 * i}") ## example: 5 * 1 = 5 

## Counting Down with for loop
for i in range(10,0,-1):
    print(i)