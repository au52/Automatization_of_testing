# from turtle import *
#
# my_turtle = Turtle()
# my_turtle.speed(0)
# my_turtle.screen.setup(1200, 800)
#
# # Нарисовать квадрат
# def draw_rect(t):
#     for x in range(0, 4):
#         t.right(90)
#         t.forward(100)
#
# # Рисует квадраты в цикле
# for x in range(0, 360):
#     draw_rect(my_turtle)
#     my_turtle.right(1)
#
# # Необходимо, чтобы окно не закрывалось само, а только по клику
# my_turtle.screen.exitonclick()
# my_turtle.screen.mainloop()

# Вот животное:

# Рисовать голову кошки

import turtle
import math

window = turtle.Screen()
window.bgcolor("blue")

cursor = turtle.Turtle()
cursor.shape()
cursor.color("yellow")
cursor.speed(12)
cursor.pensize(7)


def movePen(cursor, x, y):
  cursor.penup()
  cursor.setposition(x, y)
  cursor.pendown()

def movePenX(cursor, x):
  cursor.penup()
  cursor.setx(x)
  cursor.pendown()

def movePenY(cursor, y):
  cursor.penup()
  cursor.sety(y)
  cursor.pendown()

def positionAlongCircle(x, y, radius, angle):
  radians = math.radians(angle)
  return [x + (radius*math.sin(radians)),
            y + (radius*math.cos(radians))]

# Рисовать круг

movePenY(cursor, -150)
cursor.circle(150)

# Рисовать нос

noseMouthOffset = -15

movePenY(cursor, -20 + noseMouthOffset)
cursor.circle(20)
#
# # Рисовать рот

movePen(cursor, -100, -20 + noseMouthOffset)
cursor.right(90)
cursor.circle(50, 180)
cursor.left(180)
cursor.circle(50, 180)

# Рисовать глаза

eyeSpacingX = 30
eyePosY = 40
eyeRadius = 30

# Правый

movePen(cursor, eyeSpacingX, eyePosY)
cursor.right(180)
cursor.circle(eyeRadius, -180)

# Левый

movePen(cursor, -eyeSpacingX, eyePosY)
cursor.circle(eyeRadius, 180)

# Рисовать язык

movePen(cursor, -20, -60 + noseMouthOffset)
cursor.circle(20, 180)

# Рисовать уши
#
# Правое

earBeginAngle = 25
earSize = 85
earWidth = 22
positionA = positionAlongCircle(0, 0, 150, earBeginAngle)
movePen(cursor, positionA[0], positionA[1])

positionB = positionAlongCircle(0, 0, 150 + earSize, earBeginAngle + earWidth)
cursor.setposition(positionB[0], positionB[1])

positionC = positionAlongCircle(0, 0, 150, earBeginAngle + earWidth * 2)
cursor.setposition(positionC[0], positionC[1])

# Левое
#
positionA = positionAlongCircle(0, 0, 150, -earBeginAngle)
movePen(cursor, positionA[0], positionA[1])

positionB = positionAlongCircle(0, 0, 150 + earSize, -earBeginAngle + -earWidth)
cursor.setposition(positionB[0], positionB[1])

positionC = positionAlongCircle(0, 0, 150, -earBeginAngle + -earWidth * 2)
cursor.setposition(positionC[0], positionC[1])

# Рисовать усы

whiskerLength = 180

# Правые усы

movePen(cursor, 50, -15)
cursor.setheading(0)
cursor.forward(whiskerLength)

movePen(cursor, 50, 0)
cursor.left(5)
cursor.forward(whiskerLength)

# Левые усы

movePen(cursor, -50, -15)
cursor.setheading(180)
cursor.forward(whiskerLength)

movePen(cursor, -50, 0)
cursor.left(-5)
cursor.forward(whiskerLength)

window.exitonclick()
