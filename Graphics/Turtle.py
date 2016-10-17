import turtle


def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    my_turtle = turtle.Turtle()
    my_turtle.shape('turtle')

    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)

    window.exitonclick()

draw_square()
