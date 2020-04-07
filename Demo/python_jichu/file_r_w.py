fildir='D:\SQ\log.txt'#查询某结尾，的数值总和
filer_R=open(fildir,'r')
lines=filer_R.read().splitlines()#读取所有信息并去除所以换行符
del lines[0],lines[-1]#去除头和尾
res=[]#保存类型，个数
for line in lines:
    r_s=line.split('\t')
    file_Type=r_s[0].split('.')[-1].strip()#获取下标0的元素，在通过.截取，获取最后一个元素，去除空格
    file_Size=int(r_s[1].strip())#获取第二个元素去除空格，最后要加，所以要转换类型
    inFlag=False
    for one in res:
        if file_Type==one[0]:
            one[1]+=file_Size#累加文件数
            inFlag=True
            break
    if inFlag==False:
        res.append([file_Type,file_Size])
print(res)

