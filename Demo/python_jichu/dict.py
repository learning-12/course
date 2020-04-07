dicts={'name':'lily','age':18}
dicts['hight']=180
d_k=dicts.keys()
print(dicts.keys())#类列表不是列表
for dic,a in dicts.items():#相当于dic是key，a是值
     print(dic,a)
     print('--------------------')
# for dic in dicts:
#     print(dic,dicts[dic])

print(list(d_k))#从新赋值成为列表不会对原对象产生影响
print(d_k)
print(dicts.items())
dicts['hight']=190
print(dicts.items())
print(id(dicts))
dicts.update({'name2':'array2'})
print((dicts))