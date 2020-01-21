rows,columns=(3,5)
arr = [[ 0 for i in range(columns)] for j in range(rows)]
for i in range(rows):
    for j in range(columns):
        arr[i][j]=i*j
print(arr)

