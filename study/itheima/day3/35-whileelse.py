# i = 0
# while i < 5:
#     print("错了")
#     i += 1
## 当while正常执行后才执行else(break不执行else，continue跳过后继续执行)
# else:
#     print("ok")


# i = 0
# while i < 5:
#     print("错了")
#     i += 1
#     if i == 3:
#         print("够了")
#         break
# else:
#     print("ok")


i = 1
while i < 5:
    print("错了")
    i += 1
    if i == 3:
        print("不够真诚")
        continue
else:
    print("ok")
