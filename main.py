from turtle import *

bgcolor('black') # цвет фона
color('cyan') # цвет кружков
speed(11) # скорость
right(45) # угол

for i in range(150):
  circle(30)
  if 7 < i < 62:
    left(5)
  if 80 < i < 133:
    right(5)
  if i < 80:
    forward(10)
  else:
    forward(5)