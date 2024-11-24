trycount = 0
for i in range(1, 4):
    trycount += 1
    user = input("请输入您的账号：")
    pswd = input("请输入您的密码：")
    if user == "admin":
        # 当if判断错误时，执行else
        if pswd == "admin888":
            print("登陆成功")
            break
        else:
            print("密码错误")
            print(f"还有{3 - trycount}次机会")
    if trycount == 3:
        print("请稍后再试")
    else:
        print(f"还有{3 - trycount}次机会")
