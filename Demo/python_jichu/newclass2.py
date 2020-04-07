# author:lyr time:2019-10-17
# from random import randint#随机数包
# print(randint(0,1))
class Tigter:
    def rora(self):
        print('父类t属性')
    @staticmethod
    def tell():
        print('父类t静态属性')
class Tigter2:
    def rora(self):
        print('父类t2属性')
    @staticmethod
    def tell():
        print('父类t2静态属性')
class Sheep:
    def rora(self):
        print('父类s属性')
    @staticmethod
    def tell():
        print('父类s静态属性')

#基础子类基础父类
class Sou(Tigter2,Tigter,Sheep):
    #子类自己的方法
    def rora(self):
        print('子类jc属性')

    @staticmethod
    def tell():
        print('子类jc静态属性')

s1=Sou()#创建子类对象
s1.rora()#调用的是子类自己的属性

#注，根据子类继承的顺序进行调用的
super(Sou,s1).rora()#super调用父类的一个继承类的属性
#super调用父类的二个继承类的属性顺序少一个比如调用子类对象点方法，则调用继承父类的第一个类方法
super(Tigter,s1).tell()
# super(Tigter2,s1).rora()