## Implementing 2D List
# A 2D list appears as a grid with rows and columns:
rows = 3
cols = 4
 
two_d_list = []
 
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(i * 10 + j)
    two_d_list.append(row)
 
two_d_list[2][3] = two_d_list[2][3] * 2  # 46
 
two_d_list[1][2] = two_d_list[1][2] * 2  # 24

print(two_d_list)
 
two_d_list[0][0] = 1
two_d_list[0][1] = 2
two_d_list[1][2] = 3
two_d_list[2][3] = 4
 
#print(two_d_list)
 
for i in range(rows):
    for j in range(cols):
        print(two_d_list[i][j], end=' ')
    print()

