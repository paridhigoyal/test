items=set()
s=''
n=input()
for i in n:
    if i==" ":
        items.add(s)
        s=''
        continue
    else:
        s=s+i
items.add(s)
lst=list(items)
lst.sort()
for i in lst:
    print(i, end=" ")
