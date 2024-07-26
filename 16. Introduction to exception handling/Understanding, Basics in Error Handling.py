## Basics of Error Handling - try and except
# Python provides the try-except block for exception handling. You wrap the code that could potentially throw an exception inside a try block, and the code that handles the exception goes into the except block.

try:
    i = 0
    j = 10/i
except:
    print("Exception caught!")
    j = 0
print(j)

## Handling Multiple Errors With Multiple except Blocks
# When you use a general except block, it catches all types of exceptions. While this can be useful, it can also be ambiguous. You don’t know what exactly went wrong.
# If you need more granularity in your error-handling mechanism, Python allows you to specify different except blocks for different exceptions.
# Here’s how you can differentiate between a TypeError and a ZeroDivisionError:

try:
    i = 0  # Change this value to see different outcomes
    j = 10/i
    values = [1, '1']
    print(sum(values))
except TypeError:
    print("TypeError")
    j = 0
except ZeroDivisionError:
    print("ZeroDivisionError")
    j = 0
print(j)
print("End")

try:
    i = 1  # Change this value to see different outcomes
    j = 10/i
    values = [1, 2]
    print(sum(values))
except TypeError:
    print("TypeError")
    j = 0
except ZeroDivisionError:
    print("ZeroDivisionError")
    j = 0
print(j)
print("End")

## Error Handling - finally and else
# In the previous steps, we have focused mainly on the try and except blocks. Now, let’s explore two more components that can be part of a try-except block: the else and finally clauses.

try:
    i = 1  # Simulating input from user
    j = 10/i
except Exception as error:
    print(error)
    j = 0
else:
    print("Else")
finally:
    print("Finally")
 
print(j)
print("End")

# What happens when an exception is thrown?

try:
    i = 0  # Simulating input from user
    j = 10/i
except Exception as error:
    print(error)
    j = 0
else:
    print("Else")
finally:
    print("Finally")
 
print(j)
print("End")




