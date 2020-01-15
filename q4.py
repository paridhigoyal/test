lst=[]
tup=()
s=''
n=input()
for i in n:
    if i==',':
        lst.append(s)
        tup=tup+(s ,)
        s=''
        continue

    else:
        s = s + i
lst.append(s)
tup = tup +(s ,)
print(lst)
print(tup)
