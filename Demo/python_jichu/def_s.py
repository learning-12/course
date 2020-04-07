#再识函数
# x=1
# def pay():
#     global x#global定义全局变量
#     x=3
#     print("---------1111",x)
# pay()
#
#
# print("---------22222222",x)
# print(1,2,3,4,sep='')
# re=open()

# def xhdy(*alist):
#     d_list=0
#     print(type(alist))
#     for one in alist:
#         d_list+=one
#     return d_list
# # print(xhdy(*[1,2,3,4,5]))
# print(xhdy(1,2,3,4,5))
#关键字可变参数可缺省（在需要传入参数以字典形式存储可用这个）

# largs = {'a': 3, 'name': 'Nqq', 'age': 13}
def testnew(*a, **b):

    print(a,b)
# test1(1,2,3,**largs)
if __name__=='__main__':
    testnew(1, 2)
    # print(__name__)
# def func(a,b,c=0,*d,**e):
#     return a,b,c,d,e
# print(func(1,2,c=8))




