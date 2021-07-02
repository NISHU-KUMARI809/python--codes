 # import the turtle library for drawing the required curves ....
import turtle as t
# set the background color as black
#pensize as 2 and speed of drawing curve as 10 ......
t.bgcolor('black')
t.pensize (2)
t.speed(10)
# iterate 20  times in total ......
for i in range (20):
    # choose your color combination
    for color in('violet','indigo','blue','green','yellow','orange','red'):
        t.color(color)
        # draw a circle of choosen radius 100 here
        t.circle(100)
        # move 10 pixels left to draw another circle ......
        t.left(10)
# hide the turtle
        t.hideturtle()

