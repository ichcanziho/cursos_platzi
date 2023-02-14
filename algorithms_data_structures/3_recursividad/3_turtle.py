import turtle


def draw(my_turtle, length):
    if length:
        my_turtle.forward(length)
        my_turtle.left(123)
        draw(my_turtle, length - 2)


if __name__ == "__main__":
    pencil = turtle.Turtle()
    screen = turtle.Screen()

    colors = (
        '#006699',
        '#006666',
        '#660066',
        '#990000',
        '#ad3270',
        '#e65100',
        '#1a237e',
        '#827717',
        '#006064',
        '#f57f17',
        '#d50000',
        '#4a148c',
    )

    for color in colors:
        pencil.pencolor(color)
        draw(pencil, 100)

    screen.exitonclick()
