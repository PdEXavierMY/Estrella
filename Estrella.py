import turtle
turtle.showturtle()
turtle.shape("classic")

puntas = int(input("Eliga el número de puntas de su estrella a dibujar: "))
def turtle_star(puntas, tamaño = 100):
    dim_angulo = 360 / puntas
    turtle.fillcolor('black')
    turtle.begin_fill()
    if puntas % 2 == 0:
        pclave = []
        for i in range(0, puntas):
            turtle.penup()
            pclave.append(turtle.pos())
            turtle.circle(tamaño, dim_angulo)
        for j in range(0, len(pclave)):
            if j % 2 == 0:
                turtle.pendown()
                turtle.goto(pclave[j][0], pclave[j][1])
            else:
                continue
        turtle.goto(pclave[0][0], pclave[0][1])
        turtle.penup()
        for k in range(0, (len(pclave) + 1)):
            if k % 2 != 0:
                turtle.goto(pclave[k][0], pclave[k][1])
                turtle.pendown()
            else:
                continue
        turtle.goto(pclave[1][0], pclave[1][1])
    else:
        angulo = 180 - (180 / puntas)
        for z in range(puntas):
            turtle.forward(tamaño)
            turtle.right(angulo)
        turtle.end_fill()

turtle_star(puntas)