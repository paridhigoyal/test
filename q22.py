import operator
string=input()
a =string.split(" ")
dicty={}
for i in a:
    dicty[i]=a.count(i)
dict_list = sorted(dicty.items(), key=operator.itemgetter(0,1))
new_dict = dict(dict_list)
for i,j in dict_list:
  print(i ,":",j )
