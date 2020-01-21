class gen:
    def divisible_7(num):
        for i in range(0,n+1):
            if(i%7==0):
                yield i
n=int(input())
g=gen.divisible_7(n)
for i in g:
  print(i)
