lst=[]
lst1=[]
def lst_gen():
    for i in range(1,21):
        lst.append(i*i)
    for j in range(15,20):
        lst1.append(lst[j])
    return lst1
print(lst_gen())
