i = 5
while i > -1:
    print("* ", end="")
    j = 0
    # while j < i 正三角
    while j < i:
        print("* ", end="")
        j += 1
    print("")
    i -= 1
