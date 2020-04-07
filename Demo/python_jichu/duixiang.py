import copy
alist=[1,2,3,['a','n']]
b=copy.copy(alist)

alist[3].append('b')
alist.append(1)
alist=[1,2,3,['a','b']]
b=copy.copy(alist)
b[-1].append('c')
print(alist)
print(b)
print(id(alist))
print(id(b))
