## Coding Exercise: Find Intersection Between Multiples of Two Numbers
# In this exercise, you are tasked with determining the intersection of the multiples of two numbers within a given range. This is a classic problem of set intersection, which can be approached using set operations.

def find_intersection(num1, num2, limit):
    if num1 == 0 or num2 == 0:
        return set()
        
    multiples_num1 = {i for i in range(num1, limit + 1, num1)}
    multiples_num2 = {i for i in range(num2, limit + 1, num2)}

    result = set(multiples_num1) & set(multiples_num2)

    return result

print(find_intersection(4, 6, 30))  # Output: {12, 24}
print(find_intersection(3, 5, 20))  # Output: {12, 24}
print(find_intersection(9, 11, 50))
print(find_intersection(7, 13, 100))

## Coding Exercise: Identify Unique Colors
# In this exercise, you're tasked with creating a Python function named unique_colors that identifies and returns the colors that are unique to two different sets of color palettes.

def unique_colors(palette1, palette2):
    if not palette1:
        return palette2
    if not palette2:
        return palette1
    
    result1 = (palette1 | palette2) - (palette1 & palette2)
    return result1
       
print(unique_colors({"red", "blue"}, {"blue", "green"}))         
print(unique_colors({"purple", "yellow"}, {"yellow", "pink"}))   
print(unique_colors({"orange", "cyan"}, {"cyan", "magenta"}))    

## Coding Exercise: Merge Multiple Shopping Lists
# In this exercise, your task is to create a Python function named merge_shopping_lists that merges any number of shopping lists into one consolidated list, ensuring that there are no duplicate items.

def merge_shopping_lists(*lists):
    if not lists:
        return set()
        
    union_result = set.union(*lists) 
    return union_result
      
list1 = {"apples", "bananas", "cherries"}
list2 = {"bananas", "dates", "eggs"}
list3 = {"cherries", "dates", "figs"}
print(merge_shopping_lists(list1, list2, list3))

list4 = {"bread", "milk"}
list5 = {"milk", "eggs", "juice"}
print(merge_shopping_lists(list4, list5))

