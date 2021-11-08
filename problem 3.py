# miguel jusino
import turtle
#defined
sides = int(input("How many sides?"))
lenght = int(input("what is the lenght of the side?"))
line_c = (input("what color are the sides?"))
shape_c = (input("what color should we fill the shape?"))

wn = turtle.Screen()
alex = turtle.Turtle()

#start of drawing

alex.begin_fill()

for i in range(sides):
    alex.fillcolor(shape_c)
    alex.pencolor(line_c)
    alex.pensize(5)
    alex.forward(lenght)
    alex.left(360/sides)
alex.end_fill()


wn.exitonclick()



