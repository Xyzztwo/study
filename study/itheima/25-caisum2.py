import random

i = 1
computer = random.randint(1, 10)
while i <= 3:
    user = int(input("请输入您才的数字1-10（3次机会哦）："))
    if user == computer:
        print("恭喜你猜对啦")
        break
    elif user < computer:
        print(f"猜小咯，在{user}-10来一次吧")
    elif user > computer:
        print(f"猜大咯，在1-{user}来一次吧")
    i += 1
