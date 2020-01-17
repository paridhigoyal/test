tup=()
lst=list(tup)
def n():
    for i in range(1, 21):
        lst.append(i * i)
    return tuple(lst)
print(n())
