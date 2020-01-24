import re

p = list(input().split(","))

for i in p:
    if (len(i) < 6 or len(i) > 12):
        break
    elif not re.search("[a-z]", i):
        break
    elif not re.search("[0-9]", i):
        break
    elif not re.search("[A-Z]", i):
        break
    elif not re.search("[$#@]", i):
        break
    elif re.search("\s", i):
        break
    else:
        print(i)
