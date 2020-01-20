lst=[]
for i in range(1,21):
    lst.append(i)
a=list(filter(lambda x:x%2==0,lst))
print(a)
