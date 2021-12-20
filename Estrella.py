import random
import turtle

puntas = int(input("Eliga el número de puntas de su estrella a dibujar: "))
def turtle_star(puntas, tamaño = 100):
    dim_angulo = 360 / puntas
    turtle.fillcolor('black')
    turtle.begin_fill()