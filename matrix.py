mat = [[1, 2, 3], 
       [4, 5, 6],
       [7, 8, 9]]

aux = mat[1][1]
c = aux * 2
mat[1][1] = c

for i in mat:
    print(i)