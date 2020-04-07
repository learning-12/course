'''
1.程序开始的时候提示用户输入学生年龄信息 格式如下：
Jack Green ,   21  ;  Mike Mos, 9;
我们假设 用户输入 上面的信息，必定会遵守下面的规则：
  学生信息之间用分号隔开（分号前后可能有不定数量的空格），
  每个学生信息里的 姓名和 年龄之间用 逗号隔开（逗号前后可能有不定数量的空格）
2. 程序随后将输入的学生信息分行显示，格式如下
Jack Green :   21;
Mike Mos   :   09;
学生的姓名要求左对齐，宽度为20， 年龄信息右对齐，宽度为2位，不足前面补零
'''
format_w=input('请输入：')
str_sp=format_w.split(";")#以；分割
print(str_sp)
for str_f in str_sp:#循环输入的值
    if ',' not in str_f:
        continue

    name,age=str_f.split(',')#分割以，
    name=name.strip()#得到name的值，并去除前后空格
    age=age.strip()

    if not age.isdigit():#判断是否是数字
        continue
    age=int(age)

    print(f'{name:20}:{age:02}')#输出