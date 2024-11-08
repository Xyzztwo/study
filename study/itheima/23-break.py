i = 1
while i <= 5:
    if i == 4:
        print("不吃了，等会再吃")
        i += 1
        continue
    print(f"吃{i}个")
    if i == 5:
        print("吃饱了")
        break
    i += 1
