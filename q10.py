lst=[]
s=''
n=input()
for i in n:
    if(i ==" "):
        lst.append(s)
        s=''
        continue
    else:
        s=s+i
lst.append(s)
lst=list(dict.fromkeys(lst))
lst.sort()
for i in lst:
    print(i,end=' ')
