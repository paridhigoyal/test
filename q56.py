def div(num):
    num=0
    while num<=n:
        if num%5==0 and num%7==0:
            yield num
        num+=1
n=int(input())
f=div(n)
for i in f:
    print(i, end=",")

