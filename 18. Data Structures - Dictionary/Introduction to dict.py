## Introduction To dict
# A dictionary in Python is a collection of key-value pairs.
occurances = dict(a=5, b=6, c=8)
print(occurances)  
print(type(occurances))  

# ACCESSING AND MODIFYING VALUES
occurances['d'] = 15
print(occurances)  
occurances['d'] = 10
print(occurances)  
print(occurances['d'])  

# print(occurances['e']) # KeyError: 'e': To avoid this, use the get() method

print(occurances.get('d'))  
print(occurances.get('e'))  
print(occurances.get('e', 10)) 

# EXPLORING DICTIONARY METHODS
print(occurances.keys())  
print(occurances.values())  
print(occurances.items())  

# ITERATING A DICTIONARY
for (key, value) in occurances.items():
    print(f"{key} {value}")  

# DELETING FROM A DICTIONARY
occurances['a'] = 0
del occurances['a']
print(occurances)  

# Examples

user_info = {'name': 'John', 'age': 30, 'city': 'New York'}
user_info['age'] = 31
print(user_info)
 
text = "hello"
char_count = {}
for char in text:
   if char in char_count:
       char_count[char] += 1
   else:
       char_count[char] = 1
print(char_count)
 
dict_1 = {'a': 1, 'b': 2, 'c': 3}
dict_2 = {'c': 3, 'd': 4, 'e': 5}
common_keys = set(dict_1.keys()) & set(dict_2.keys())
print(common_keys)
 
keys = ['a', 'b', 'c']
values = [1, 2, 3]
result = {k: v for k, v in zip(keys, values)}
print(result)
 
users = {
   'user1': {'name': 'John', 'age': 30},
   'user2': {'name': 'Jane', 'age': 25}
}
print(users['user1']['name'])
 
squares = {x: x**2 for x in range(1, 6)}
print(squares)
 
students = {"Alice": {"Math", "English"}, "Bob": {"Math", "Science"}}
common_subjects = set.intersection(*students.values())
print(common_subjects)

