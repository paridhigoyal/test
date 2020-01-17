lst=[]
def lst_gen():
    for i in range(1,21):
        lst.append(i*i)
    return lst
print(lst_gen())
