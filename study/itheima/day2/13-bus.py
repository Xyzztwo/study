money = int(input("请投币（1为有，0为没有）："))
# 1有空座
seat = int(input(("查看是否有空座？（1为有，0为没有）")))
if money == 1:
    print("可以上车")
    # 如果以上结果为True则执行以下语句
    if seat == 1:
        print("有座位，可以做")
    else:
        print("没座位，站着吧哥们")
else:
    print("没钱还想上车？跑起来吧！")
