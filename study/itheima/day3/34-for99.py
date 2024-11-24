for i in range(1, 10):
    # 序列中，第一位要小于第二位才可以继续执行
    # for顾头不顾尾，且要小于第二位才可执行下去（while顾尾）
    for j in range(1, i + 1):
        print(f"{j}*{i}={i*j} ", end="")
    print("")
