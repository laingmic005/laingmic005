'''
This program will ask the user one question: "What colour is
thy blade, O, adventurer?" The user may input the name of a
color (most colors in the Python Turtle module will work,
however some will not due to the blade being two toned).
Turtle graphics will then draw a sword with a blade of the
color inputted by the user. If the user enters an invalid
color, the message "We beg thee pardon, goodly adventurer,
metal of that colour is not found in these lands," will be
displayed, and the program will start back from the
first question.

After drawing the sword, the Turtle will etch a tiny
sword into the pommel of the big sword.
'''

import turtle

def main():
    '''
    Program starts here.
    '''
    try:
        width = 500
        height = 500
        color_val = input("What colour is thy blade, O, adventurer? ")

        screen = turtle.Screen()
        screen.setup(width, height, 0, 0)

        space = turtle.Turtle()
        space.speed(3)


        #right side of blade
        space.penup()
        space.color("black", color_val)
        space.goto(0,230)
        space.pendown()
        space.begin_fill()
        space.rt(70)
        space.forward(50)
        space.rt(20)
        space.forward(225)
        space.rt(90)
        space.forward(17)
        space.rt(90)
        space.forward(270)
        space.end_fill()

        #left side of blade
        space.penup()
        space.color("black",f"{color_val}1")
        space.goto(0,230)
        space.pendown()
        space.begin_fill()
        space.lt(70+90)
        space.forward(50)
        space.lt(20)
        space.forward(225)
        space.lt(90)
        space.forward(17)
        space.lt(90)
        space.forward(270)
        space.end_fill()

        #handle
        space.penup()
        space.goto(0,-45)
        space.color("black","chocolate")
        space.pendown()
        space.begin_fill()
        space.rt(90)
        space.fd(15)
        space.rt(95)
        space.fd(75)
        space.rt(85)
        space.fd(17)
        space.rt(85)
        space.fd(75)
        space.rt(95)
        space.fd(15)
        space.end_fill()

        #crossguard right
        space.penup()
        space.goto(0,-35)
        space.color("black","DarkGoldenRod3")
        space.pendown()
        space.begin_fill()
        space.rt(5)
        space.forward(60)
        space.rt(85)
        space.forward(10)
        space.rt(85)
        space.forward(60)
        space.rt(95)
        space.forward(25)
        space.end_fill()

        #crossguard left
        space.penup()
        space.goto(0,-35)
        space.color("black","DarkGoldenRod1")
        space.pendown()
        space.begin_fill()
        space.lt(5+90)
        space.forward(60)
        space.lt(85)
        space.forward(10)
        space.lt(85)
        space.forward(60)
        space.lt(95)
        space.forward(25)
        space.end_fill()

        #pommell outer
        space.penup()
        space.goto(19,-130)
        space.color("black","DarkGoldenRod2")
        space.pendown()
        space.begin_fill()
        space.circle(20)
        space.end_fill()

        #pommell mid
        space.penup()
        space.goto(19,-130)
        space.color("DarkGoldenRod3")
        space.pendown()
        space.begin_fill()
        space.circle(20)
        space.end_fill()

        #pommell inner
        space.penup()
        space.goto(19,-130)
        space.color("Black","DarkGoldenRod1")
        space.pendown()
        space.begin_fill()
        space.circle(20)
        space.end_fill()

        #SMALL SWORD / DAGGER
        #right side of blade
        space.penup()
        space.color("black", "darkgoldenrod")
        space.goto(0,-150)
        space.pendown()
        space.begin_fill()
        space.rt(70+90+180)
        space.forward(8.33)
        space.rt(20)
        space.forward(15.833)
        space.rt(90)
        space.forward(2.833)
        space.rt(90)
        space.forward(23.33)
        space.end_fill()

        #left side of blade
        space.penup()
        space.color("black","Darkgoldenrod2")
        space.goto(0,-150)
        space.pendown()
        space.begin_fill()
        space.lt(70+90)
        space.forward(8.33)
        space.lt(20)
        space.forward(15.833)
        space.lt(90)
        space.forward(2.833)
        space.lt(90)
        space.forward(23.33)
        space.end_fill()

        #handle
        space.penup()
        space.goto(0,-125)
        space.color("black","darkgoldenrod1")
        space.pendown()
        space.begin_fill()
        space.rt(90)
        space.fd(3)
        space.rt(95)
        space.fd(10)
        space.rt(85)
        space.fd(4)
        space.rt(85)
        space.fd(10)
        space.rt(95)
        space.fd(3)
        space.end_fill()

        #crossguard right
        space.penup()
        space.goto(0,-126)
        space.color("Black","DarkGoldenRod3")
        space.pendown()
        space.begin_fill()
        space.rt(5)
        space.forward(10)
        space.rt(85)
        space.forward(1.75)
        space.rt(85)
        space.forward(10)
        space.rt(95)
        space.forward(4.33)
        space.end_fill()

        #crossguard left
        space.penup()
        space.goto(0,-126)
        space.color("black","DarkGoldenRod1")
        space.pendown()
        space.begin_fill()
        space.lt(5+90)
        space.forward(10)
        space.lt(85)
        space.forward(1.75)
        space.lt(85)
        space.forward(10)
        space.lt(95)
        space.forward(4.33)
        space.end_fill()

        #pommell outer
        space.penup()
        space.goto(-3.69,-113)
        space.color("black","DarkGoldenRod2")
        space.pendown()
        space.begin_fill()
        space.circle(4)
        space.end_fill()
        turtle.done()

    except turtle.TurtleGraphicsError:
        print("We beg thee pardon, goodly adventurer, metal of that colour is not found in these lands.")
        main()
    else:
        print("Behold thy blade!")

if __name__ == "__main__":
    main()
