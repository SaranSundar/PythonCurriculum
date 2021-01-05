import turtle

screen: turtle.Screen
pencil: turtle.Turtle

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
ANIMATION_SPEED = 0


def create_screen():
    global screen
    global SCREEN_WIDTH
    global SCREEN_HEIGHT

    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.cv._rootwindow.resizable(False, False)
    screen.bgcolor("white")


def create_pencil():
    global pencil
    global ANIMATION_SPEED

    pencil = turtle.Turtle()
    pencil.color("black")
    pencil.pensize(1)
    pencil.speed(ANIMATION_SPEED)


def draw_square():
    global pencil

    pencil.penup()
    pencil.goto(0, 0)
    pencil.pendown()
    # pencil.fillcolor("red")
    # pencil.begin_fill()
    # pencil.goto(100, 0)
    # pencil.goto(100, 100)
    # pencil.goto(0, 100)
    # pencil.goto(0, 0)
    # pencil.end_fill()

    # for i in range(0, 4):
    #     pencil.forward(100)
    #     pencil.right(90)

    pencil.fillcolor("red")
    pencil.pencolor("blue")
    pencil.begin_fill()
    pencil.circle(100)
    pencil.end_fill()

    pencil.fillcolor("green")
    pencil.pencolor("yellow")
    pencil.begin_fill()
    pencil.circle(50)
    pencil.end_fill()


def main():
    create_screen()
    create_pencil()

    draw_square()

    turtle.done()


if __name__ == '__main__':
    main()
