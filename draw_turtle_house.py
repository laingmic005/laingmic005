import turtle

def main():
    turtle.speed(0)

    def draw_rectangle(w,h):
        for i in range(2):
            turtle.forward(w)
            turtle.lt(90)
            turtle.forward(h)
            turtle.lt(90)

  # Draw a rectangle with width 100 and height 100       
    draw_rectangle(100,100)

  # Move the turtle to (100, 100) to start the roof
    turtle.penup()
    turtle.goto(100, 100)
    turtle.setheading(0)
    turtle.pendown()


  # Draw a triangle with sides of length 100
    for i in range(3):
        turtle.lt(120)
        turtle.forward(100)

  # Move the turtle to (40, 0) to start the door
    turtle.penup()
    turtle.goto(40, 0)
    turtle.setheading(0)
    turtle.pendown()

  # Draw a rectangle with width 20 and height 40
    draw_rectangle(20,40) 

  # Move the turtle to (10, 50) to start the left window
    turtle.penup()
    turtle.goto(10, 50)
    turtle.setheading(0)
    turtle.pendown()

  # Draw a rectangle with width 20 and height 20
    draw_rectangle(20,20)

  # Move the turtle to (70, 50) to start the right window
    turtle.penup()
    turtle.goto(70, 50)
    turtle.setheading(0)
    turtle.pendown()

  # Draw a rectangle with width 20 and height 20
    draw_rectangle(20,20)

    turtle.mainloop()

if __name__ == '__main__':
  main()
