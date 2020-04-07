fildir='D:\SQ\log.txt'
r_Open=open(fildir,'r')
jpgCount=0
preMsg=''
#判断这个字在文件中出现的总次数
for r_o in r_Open:
    if preMsg in r_o:
        jpgCount+=1
    else:
        if len(preMsg)>0:
            print(preMsg,jpgCount)
        preMsg=r_o
        jpgCount=1

