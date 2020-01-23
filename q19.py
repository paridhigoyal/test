import operator
n=int(input())
tup=()
lst1=[]
for i in range(n):
  
    tup=tuple(input().split(","))

    lst1.append(tup)
lst=sorted(lst1,key=lambda tu:tu[2])
lst=sorted(lst1,key=lambda tu:tu[1])
lst=sorted(lst1,key=lambda tu:tu[0])

print(lst)
