import math

c=50
h=30
d=''
m= input( )
for i in range(len(m)):
    if m[i]==',':
         q = round(math.sqrt((2*c*int(d))//h))
         print(q, sep=",")
         d = ''
    else:
        d=d+m[i]
q = round(math.sqrt((2 * c * int(d)) // h))
print(q)
