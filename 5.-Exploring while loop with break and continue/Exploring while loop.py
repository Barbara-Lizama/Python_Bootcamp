## Basic for loop 
# Consider you want to print numbers from 1 to 10. You can use the for loop along with the range function for this purpose.
for i in range(1, 11):
    print(i)

## Introducing the while loop
# In a while loop, we specify a logical condition. While the condition is true, the loop continues running.
 # example 
   # i = 0
   # while i < 5:
   # print(i) (infinite loop)

## Incrementing inside while LOOP
# To avoid the infinite loop problem, it's essential to increment the value of i inside the loop:
i = 0
while i < 5:
  print(i)
  i = i + 1

## Loops - Break and Continue
# The break keyword
 # The break statement is used to exit a loop when a specific condition is met. (different form)
for i in range(1, 11):
    if i == 5:
       break
    print(i, end=' ')
print("done")

i = 1
while i < 11:
    if i == 5:
        break
    print(i, end=' ')
    i += 1
print("done")

# The continue keyword
 # The continue statement is used to skip the current iteration of a loop and proceed to the next iteration.
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=' ')
print("done")

i = 1
while i < 11:
    if i % 2 == 0:
        i += 1
        continue
    print(i, end=' ')
    i += 1
print("done")
