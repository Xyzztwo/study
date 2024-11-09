# i控制列（竖）
i = 1
while i <= 9:
    # j控制行（横）
    j = 1
    while j <= i:
        print(f"{j}*{i}={i*j} ", end="")
        j += 1
    print("")
    i += 1
