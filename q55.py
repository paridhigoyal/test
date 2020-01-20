def all_even(a):
    n = 0
    while n%2==0:
        if n<=a:
          yield n
          n=n+2
a=int(input())
f=all_even(a)
for i in f:
   print(i)
