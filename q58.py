lst1=[]
lst=[12,24,35,24,88,120,155,88,120,155]
for i in range(len(lst)):
    if lst[i] not in lst1:
        lst1.append(lst[i])
print(lst1)
