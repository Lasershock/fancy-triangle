import turtle

def draw_sierpinski_triangle(turtle, order, size):
    if order == 0:
        for _ in range(3):
            turtle.forward(size)
            turtle.left(120)
    else:
        draw_sierpinski_triangle(turtle, order - 1, size / 2)
        turtle.forward(size / 2)
        draw_sierpinski_triangle(turtle, order - 1, size / 2)
        turtle.backward(size / 2)
        turtle.left(60)
        turtle.forward(size / 2)
        turtle.right(60)
        draw_sierpinski_triangle(turtle, order - 1, size / 2)
        turtle.left(60)
        turtle.backward(size / 2)
        turtle.right(60)

if __name__ == "__main__":
    window = turtle.Screen()
    window.bgcolor("white")

    sierpinski_turtle = turtle.Turtle()
    sierpinski_turtle.speed(0)

    initial_order = 5
    initial_size = 700


    sierpinski_turtle.penup()
    sierpinski_turtle.goto(-initial_size / 2, -initial_size / 2 / 1.732)
    sierpinski_turtle.pendown()


    draw_sierpinski_triangle(sierpinski_turtle, initial_order, initial_size)


    sierpinski_turtle.hideturtle()
    window.mainloop()


wn.exitonclick()
