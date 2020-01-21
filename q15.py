n=int(input())
a=int(input())
sum=0
lst=[]
for i in range(0,n):
    sum+=a*pow(10,i)
    lst.append(sum)
sum=0
for i in lst:
    sum+=i
print(sum)
