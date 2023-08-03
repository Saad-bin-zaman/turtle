from turtle import *
from random import randint

speed(10)
penup()
goto(-140, 140)

for step in range(21):
    write(step, align='center')
    right(90)
    for num in range(8):
        penup()
        forward(10)
        pendown()
        forward(10)
    penup()
    backward(160)
    left(90)
    forward(20)

a = Turtle()
a.color('purple')
a.shape('turtle')

a.penup()
a.goto(-160, 100)
a.pendown()

b = Turtle()
b.color('blue')
b.shape('turtle')

b.penup()
b.goto(-160, 70)
b.pendown()

c = Turtle()
c.color('green')
c.shape('turtle')

c.penup()
c.goto(-160, 40)
c.pendown()

for turn in range(10):
    a.right(36)

for turn in range(100):
    a.forward(randint(1, 8))
    b.forward(randint(1, 8))
    c.forward(randint(1, 8))

done()
