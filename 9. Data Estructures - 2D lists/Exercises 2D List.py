## Coding Exercise: Search for an Element in a 2D List and Return Its Index
# In this exercise, you are given the task of writing a Python function that searches for an element in a 2D list (list of lists) and returns its index. If the element is not present, the function should return (-1, -1).

def search_element(list_2D, target):
    
    for i in range(len(list_2D)):
        for j in range(len(list_2D[i])):
            if list_2D[i][j] == target:
                return (i, j)
        
    return (-1, -1)     
            
print(search_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5))  
print(search_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10))  
print(search_element([[2, 4, 6], [8, 12, 16], [23, 25, 27]], 23)) 

## Coding Exercise: Find the Sum of Each Row in a 2D List
# Calculate the sum of each row in a 2D list and store the results in a new list.

def sum_of_rows(list_2D):
    row_sums = []
    
    for i in range(len(list_2D)):
          row_sum = 0
          for j in range(len(list_2D[i])):
              row_sum += list_2D[i][j]
          row_sums.append(row_sum)
        
    return row_sums

print(sum_of_rows([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  
print(sum_of_rows([[1], [2], [3]]))  
print(sum_of_rows([[], [], []]))  

## Coding Exercise: Add Two Matrices of the Same Size
# In this exercise, you are tasked with writing a Python function that adds two matrices of the same size. If either of the matrices is empty, return an empty list.
def add_matrices(matrix1, matrix2):
    row_sums = []
    for i in range(len(matrix1)):
          row_sum = []
          for j in range(len(matrix1[0])):
              row_sum.append (matrix1[i][j] + matrix2[i][j])
          row_sums.append(row_sum)

    return row_sums

print(add_matrices([[1, 3], [2, 4]], [[5, 7], [6, 8]]))
print(add_matrices([[11, 3], [13, 4]], [[5, 15], [6, 17]]))

