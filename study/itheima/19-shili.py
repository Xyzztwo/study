# 世界杯总成绩

me = int(input("请输入你队伍的实力："))
a = int(input("请输入a队伍的实力："))
b = int(input("请输入b队伍的实力："))
c = int(input("请输入c队伍的实力："))
mevsa = (me > a) * 3 + (me == a) * 1
mevsb = (me > b) * 3 + (me == a) * 1
mevsc = (me > c) * 3 + (me == a) * 1

sum1 = mevsa + mevsb + mevsc
print(f"总成绩为{sum1}")

#! True/int(True) = 1，False /int(False) = 0
print(int(True))
print(int(False))
