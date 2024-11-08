while True:
    player = int(input("请输入石头剪刀布（对应0/2/5）："))
    computer = int(input("请输入石头剪刀布（对应0/2/5）："))
    if (
        (player == 0 and computer == 2)
        or (player == 2 and computer == 5)
        or (player == 5 and computer == 0)
    ):
        print("玩家胜利")
    elif player != (0, 2, 5):
        player = int(input("player请输入石头剪刀布（对应0/2/5）："))
        computer = int(input("computer请输入石头剪刀布（对应0/2/5）："))
    elif player == computer:
        print("平局")
