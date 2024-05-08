## Logical operators - and, or, not, logical^(XOR)
## The and operator returns True only when both operands are True. 
print(True and True)           
print(True and False)          
print(False and False)  

## The or operator returns True if at least one of the operands is True. 
print(True or False)            
print(False or False)       

## The not operator returns the negation of the bool value.
print(not True)
print(not False)

## The ^ operator, also known as the exclusive or (xor) operator, returns True when the operands have different boolean values.
print(True ^ True)
print(True ^ False)

## Logical Operations - NOT and NOT EQUAL TO
## NOT and !=
#In this section, we'll look at not operator and != operator to evaluate conditions that are not equal to a specific value.
x = 5
if x != 6:
    print("This")

## ANY NON-ZERO VALUE IS TRUE
# Here's an interesting fact about boolean values in Python: any non-zero value is considered True, while 0 is the only integer value which is considered False.
print(bool(6))  
print(bool(-6))  
print(bool(0))  

## If, Else, and Elif 
# The if statement checks a specific condition. If the condition is true, it executes the code block underneath it.
i = 2
if i%2 == 0:
    print("i is even");

# The else statement provides an alternative code block that will execute if the if statement's condition is not met (i.e., if it's false).
i = 3
if i%2 == 0:
    print("i is even");
else:
    print("i is odd");

# elif stands for "else if". This statement allows us to check multiple conditions. If the if condition is false, the program checks the elif condition. If the elif condition is true, it executes the code block underneath it.
i = 3
if i==1:
    print("i is 1")
elif i==2:
    print("i is 2")
else:
    print("i is not 1 or 2")


 



