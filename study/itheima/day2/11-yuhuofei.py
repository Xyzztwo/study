# 逻辑表达式（与或非）
# and 只要有一个为假，则返回为假

print(True and True)
print(True and False)
print(False and False)

print("-" * 20)
# or 有一个为真，则返回为真
print(True or True)
print(False or True)
print(False or False)

print("-" * 20)
# not 就是取反
print(not False)
print(not True)

#! 数字也可以对比，
#! 其中“空字符串”和“0”以及“None”看为False
#! 其他数值和非空字符串看为True

#! python布尔运算中，只要能提前确定计算结果，则不会继续往下算
