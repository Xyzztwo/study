# 字符串的格式化
name = "xuhaoran"
age = 22
print("我叫%s.今年%d岁了" % (name, age))
price = 3.1415
print("保留小数点%f" % (price))
print("保留小数点%.4f" % (price))
num1 = 1
print("保留小数点%d" % (num1))
print("保留小数点%06d" % (num1))

str1 = "Xyzztwo"
# {}对应后续变量
print("ID是{}".format(str1))


# 格式化转义符
# \t    一个tab（四个空格）
# \n    换行
# end = '' 不换行，或使用三引号
print("***")
print("*\t*\t*")
print("*\n*")
# 不换行
print("嘿嘿", end="")
print(f"{name}\n{age}")
print(
    """
    1
    2
    3
    """
)
