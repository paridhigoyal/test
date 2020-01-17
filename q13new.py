s=input()
digits=0
alpha=0
for i in range(len(s)):
    a=ord(s[i])
    if(a>=48 and a<= 57):
        digits+=1
    if((a>=65 and a<=90) or (a>=97 and a<=112)):
        alpha+=1
print("DIGITS", digits)
print("LETTERS", alpha)
