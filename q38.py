lst=[]
def lst_gen():
    for i in range(1,21):
        lst.append(i*i)
    return lst[0],lst[1],lst[2],lst[3],lst[4]
print(lst_gen())
