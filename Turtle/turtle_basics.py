import turtle
import os

screen: turtle.Screen
pencil: turtle.Turtle


def create_screen():
    global screen
    screen = turtle.Screen()
    # https://trinket.io/docs/colors - find colors for turtle or just use r,g,b values
    screen.bgcolor("white")

    # Shows all shapes available for pencil on line 26 - pencil.shape("arrow")
    print(screen.getshapes())

    # Just a trick to be used on Mac OS only that makes sure turtle window is always in the foreground
    os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')


def create_pencil():
    global pencil
    pencil = turtle.Turtle()
    # https://trinket.io/docs/colors - find colors for turtle or just use r,g,b values
    pencil.color("black")
    pencil.shape("arrow")
    pencil.pensize(1)
    pencil.speed(0)


def draw_advanced_avengers_logo():
    global pencil

    start_x = -100
    start_y = -200

    # Creates circle
    pencil.penup()
    pencil.goto(start_x, start_y)
    pencil.pendown()
    pencil.begin_fill()
    pencil.setheading(-30)
    pencil.circle(255, 330)
    pencil_position = pencil.position()
    pencil.goto(pencil_position[0] - 29, pencil_position[1] - 45)
    pencil.setheading(123)
    pencil.circle(-300, 335)
    pencil.goto(start_x, start_y)
    pencil.end_fill()
    pencil.hideturtle()

    pencil.penup()
    pencil.goto(start_x - 200, start_y - 100)
    pencil.pendown()
    pencil.begin_fill()
    pencil.goto(start_x + 200, start_y + 550)
    pencil.goto(start_x + 250, start_y + 553)
    pencil.goto(start_x + 250, start_y + 150)
    pencil.goto(start_x + 170, start_y + 210)
    pencil.goto(start_x + 180, start_y + 370)
    pencil.goto(start_x + 80, start_y + 150)
    pencil.end_fill()


def draw_basic_avengers_logo():
    global pencil
    pencil.penup()
    pencil.goto(0, -150)
    pencil.pendown()
    pencil.circle(200, 300)
    pencil.penup()
    pencil.goto(-100, -150)
    pencil.pendown()
    pencil.goto(30, 300)
    pencil.goto(60, -30)
    pencil.penup()
    pencil.goto(-30, 30)
    pencil.pendown()
    pencil.goto(50, 30)


def main():
    create_screen()
    create_pencil()
    draw_advanced_avengers_logo()
    # draw_basic_avengers_logo()
    # Needed to make sure the turtle window doesn't close after the drawing is finished
    turtle.done()


if __name__ == '__main__':
    main()
