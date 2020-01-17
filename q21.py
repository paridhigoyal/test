import math
n=int(input())
up,down,left,right,a,b,c=0,0,0,0,0,0,0
lst=[]
for i in range(n):
    s=input("\n")
    lst=s.split(" ")
    if lst[0]=="LEFT":
        left+=int(lst[1])
    elif lst[0]=="RIGHT":
        right+=int(lst[1])
    elif lst[0]=="UP":
        up+=int(lst[1])
    elif lst[0]=="DOWN":
        down+=int(lst[1])
if(left>right):
    a=left-right
else:
    a=right-left
if(up>down):
    b=up-down
else:
    b=down-up
c=round(math.sqrt(a*a+b*b))
print(c)
