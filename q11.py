num=[]
num1=[]

n=input()
s=''
for i in n:
    if i==',':
        num1.append(int(s))
        s=''
    else:
        s=s+i
num1.append(int(s))
#print (num1)
for i in num1:
    c=0
    sum=0
    i1 = i
    while i1!=0:

        r=i1%10
        sum+= r*pow(2,c)
        c+=1
        i1=i1//10

    if (sum %5)==0:
        num.append(i)
for i in num:

 print(i,end =" ,")



