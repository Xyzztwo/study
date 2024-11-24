import turtle

turtle.pensize(10)
turtle.begin_fill()
turtle.pencolor("red")
turtle.fillcolor("yellow")
for i in range(5):
    turtle.forward(200)
    turtle.right(144)

# 填充需要结束绘画
turtle.end_fill()
turtle.hideturtle()
# 停止绘画，窗口不关闭
turtle.done()
