# 数据类型
# 数值（整型、浮点型）、布尔（真、假）、字符串、列表、元组、集合、字典
#! num(int、float)、True\False、str、list、tuple、set、dict

# 判断变量是那种数据类型
name = "xuhaoran"
print(f"{name}的数据类型为{type(name)}")
num1 = 123
print(f"{num1}的数据类型为{type(num1)}")
# 判断name变量是否为？类型，是返回True，否返回False
print(isinstance(name, str))
print(isinstance(name, int))

flag = isinstance(name, int)

# 布尔类型
# flag = False
print(flag)
print(f"{flag}的数据类型为{type(flag)}")


# 列表
list1 = [1, 2, 3]
# 元组
set1 = (1, 2, 3)
# 集合(去重)
tuple1 = {1, 2, 3, 1, 2}
print(tuple1)
# 字典类型(查询，搜索)  key:value
dict1 = {"name": "xuhaoran", "age": "22"}
print(dict1)
