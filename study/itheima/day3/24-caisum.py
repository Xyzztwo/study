import random

while True:
    computer = random.randint(1, 10)
    user = int(input("请输入您才的数字1-10（输入0结束）："))
    if user == computer:
        print("运气不错哦~")
    elif user == 0:
        break
    # 当if和elif都不成立时执行else
    else:
        print("运气差了点")
