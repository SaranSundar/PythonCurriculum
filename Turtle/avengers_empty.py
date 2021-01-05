import turtle

screen: turtle.Screen
pencil: turtle.Turtle
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
ANIMATION_SPEED = 0


def create_screen():
    """Creates a non resizable screen with a white background color"""
    global screen
    global SCREEN_WIDTH
    global SCREEN_HEIGHT

    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.cv._rootwindow.resizable(False, False)
    # turtle.screensize(SCREEN_WIDTH, SCREEN_HEIGHT, "white")
    # https://trinket.io/docs/colors - find colors for turtle or just use r,g,b values
    screen.bgcolor("white")


def create_pencil():
    """Sets properties that allows our pencil to draw on the screen"""
    global pencil
    global ANIMATION_SPEED

    pencil = turtle.Turtle()
    # https://trinket.io/docs/colors - find colors for turtle or just use r,g,b values
    pencil.color("black")
    # ['arrow', 'blank', 'circle', 'classic', 'square', 'triangle', 'turtle']
    pencil.shape("arrow")
    pencil.pensize(1)
    pencil.speed(ANIMATION_SPEED)


def draw_avengers_logo():
    """Will draw an avengers logo on the screen"""
    global pencil


def main():
    global pencil

    create_screen()
    create_pencil()

    draw_avengers_logo()

    pencil.hideturtle()

    # Needed to make sure the turtle window doesn't close after the drawing is finished
    turtle.done()


if __name__ == '__main__':
    main()
