import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()
noofsides=6
sidelenght=70
angle=360/noofsides
for i in range(noofsides):
    polygon.forward(sidelenght)
    polygon.right(angle)
turtle.done()