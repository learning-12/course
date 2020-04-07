def sort(list):
    newList=[]
    while len(list)>0:
        mixVal=list[0]#假设是个最小值
        mixZB=0#最小值的下标
        id_mix=0#当前循环的下标
        for lists in list:
            if mixVal>lists:#判断假设最小值是否大于循环的列表值大于的话，接着比较,表示没有找到当前最小值
                mixVal=lists#把最小值的坐标赋值给坐标最小的值
                mixZB=id_mix#把当前最小值的坐标赋值给一个变量用于后来移除
            id_mix+=1#否则下个坐标与列表继续相比

        list.pop(mixZB)#移除最小值pop根据下标移除
        newList.append(mixVal)#重新添加在新的列表里
    return newList

print(sort(list([2,11,3,14,15,7])))

