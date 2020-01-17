s=input()
upper=0
lower=0
for i in range(len(s)):
    a=ord(s[i])
    if (a >= 65 and a <= 90) :
        upper+=1
    if(a>=97 and a<=112):
        lower+=1
print("UPPER CASE", upper)
print("LOWER CASE", lower)


