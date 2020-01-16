s=input()
digits=0
alpha=0
for i in range(len(s)):
    if(s[i].isnumeric()):
        digits+=1
    if(s[i].isalpha()):
        alpha+=1
print("DIGITS", digits)
print("LETTERS", alpha)
