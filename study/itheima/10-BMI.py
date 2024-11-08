# 求BMI （kg*m的平方）
kg = int(input("请输入您的体重（kg）："))
m = float(input("请输入您的身高（m）："))
sum = kg / m**2
print(f"BMI为：{sum}")
