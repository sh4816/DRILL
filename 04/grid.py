import turtle
# 2018182009 김승환 - DRILL 04
turtle.left(90)

xPos = -200
yPos = -200

turtle.penup()
count = 0
while(count <= 5):
    turtle.goto(xPos, yPos)
    turtle.write('(' + str(xPos) + ', '+ str(yPos) + ')')
    turtle.pendown()
    turtle.forward(500)
    xPos = xPos + 100
    turtle.penup()
    count = count + 1

turtle.penup()
turtle.right(90)
xPos = -200
while(count > 0):
    turtle.goto(xPos, yPos)
    turtle.write('(' + str(xPos) + ', '+ str(yPos) + ')')
    turtle.pendown()
    turtle.forward(500)
    yPos = yPos + 100
    turtle.penup()
    count = count - 1

turtle.exitonclick()
