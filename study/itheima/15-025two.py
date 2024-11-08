import random

player = int(input("请输入石头剪刀布（对应1/2/3）："))
computer = random.randint(1, 3)
if (
    (player == 1 and computer == 2)
    or (player == 2 and computer == 3)
    or (player == 3 and computer == 1)
):
    print("玩家获胜")
elif player == computer:
    print("平局")
else:
    print("电脑获胜")
