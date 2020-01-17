lst=[]
s=''
n=input()
for i in n:
    if i==',':
        lst.append(int(s))
        s=''
        continue

    else:
        s = s + i
lst.append(int(s))

for i in lst:
    if((i%2)!=0):
       print(i,end=",")
