tup=(1,2,3,4,5,6,7,8,9,10)
tup1=()
tup1=list(tup1)
for i in tup:
    if i%2==0:
        tup1.append(i)
tup1=tuple(tup1)
print(tup1)
