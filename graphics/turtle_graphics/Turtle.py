import turtle


def draw_square(artist):
    for x in range(1, 5):
        artist.forward(100)
        artist.right(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    my_turtle = turtle.Turtle()
    my_turtle.shape('turtle')
    for i in range(1, 37):
        draw_square(my_turtle)
        my_turtle.right(10)

    window.exitonclick()


draw_art()
