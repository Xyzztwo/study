# 判断是否为三角形
a = int(input("请输入a边："))
b = int(input("请输入b边："))
c = int(input("请输入c边："))
# and的话，如果全为真，则返回最后一个值（True）。如果其中有一个为假，则返回该假值
# or的话，如果有一个为真，则返回第一个真值。 如果全为假，则返回最后一个假值
#! if (a + b > c) or (b + c > a) or (c + a > b):
if (a + b > c) and (b + c > a) and (c + a > b):
    print("是一个合法三角形")
else:
    print("错误！")
