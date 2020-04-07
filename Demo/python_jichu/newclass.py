# author:lyr time:2019-10-16
#创建一个类
class Tigter:
    tname='老虎'#属性
    #实例属性init称为静态方法
    def __init__(self,weights=200):
        # print(self.writh+'的体重'+str(inweight))
        self.weights=weights

    #实例方法 叫
    def roar(self):
        self.weights-=5
        print('wow!叫一次体重减少5斤')
    #喂食
    def feed(self,food):
        if food=='肉':
            self.weights+=10
        else:
            self.weights-=10
 #房间，房间编号，动物
class Room:
    def __init__(self,sbh,animal):
        self.num=sbh
        self.animal=animal

class Sleep:
    tname = '羊'  # 属性

    # 实例属性init称为静态方法
    def __init__(self, weights=100):
        # print(self.writh+'的体重'+str(inweight))
        self.weights = weights

    # 实例方法 叫
    def roar(self):
        self.weights -= 5
        print('mie!叫一次体重减少5斤')

    # 喂食
    def feed(self, food):
        if food == '草':
            self.weights += 10
        else:
            self.weights -= 10#创建的实例
t1=Tigter()
t2=Sleep()
# t1.roar()
# t1.feed('肉')
t2.roar()
t2.feed('草')
print(t1.weights,t2.weights)

from random import randint
roomlist=[]#可存放任意类型
for one in range(1,11):
    if randint(0,1)==0:
        ani=Tigter(200)
    else:
        ani=Sleep(100)
    room=Room(one,ani)
    roomlist.append(room)
