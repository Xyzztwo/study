# 梯形的面积=（上底+下底）*高/2
upper = int(input("请输入上底："))
down = int(input("请输入下底："))
tall = int(input("请输入高："))

sum = (upper + down) * tall / 2

print(f"梯形的面积为：{sum}")

print(type(sum))
