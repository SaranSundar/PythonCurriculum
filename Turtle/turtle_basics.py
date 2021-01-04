import turtle
import os

screen: turtle.Screen
pencil: turtle.Turtle


def create_screen():
    global screen
    screen = turtle.Screen()
    # https://trinket.io/docs/colors - find colors for turtle or just use r,g,b values
    screen.bgcolor("white")
    screen.onscreenclick(print_mouse_click_coordinates)

    # Shows all shapes available for pencil on line 26 - pencil.shape("arrow")
    print(screen.getshapes())

    # Just a trick to be used on Mac OS only that makes sure turtle window is always in the foreground
    os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')


def print_mouse_click_coordinates(x, y):
    print(f"({x},{y}),")
    draw_circle(x, y, 2, should_fill=True)


def create_pencil():
    global pencil
    pencil = turtle.Turtle()
    # https://trinket.io/docs/colors - find colors for turtle or just use r,g,b values
    pencil.color("black")
    pencil.shape("arrow")
    pencil.pensize(1)
    pencil.speed(0)


def draw_polygon(coordinates, should_fill=False, pen_color="black", fill_color="black"):
    """Input should be counter clock wise starting from bottom left"""
    global pencil

    pencil.penup()
    pencil.pencolor(pen_color)
    pencil.fillcolor(fill_color)

    if len(coordinates) > 0:
        coordinates.append(coordinates[0])

    if should_fill:
        pencil.begin_fill()

    for points in coordinates:
        x, y = points
        pencil.goto(x, y)
        pencil.pendown()

    if should_fill:
        pencil.end_fill()


def draw_circle(x, y, radius, should_fill=False, pen_color="black", fill_color="black"):
    global pencil

    pencil.penup()
    pencil.goto(x, y - radius)
    pencil.pendown()
    pencil.pencolor(pen_color)
    pencil.fillcolor(fill_color)

    if should_fill:
        pencil.begin_fill()

    pencil.circle(radius)

    if should_fill:
        pencil.end_fill()


def draw_avengers_logo():
    global pencil

    start_x, start_y = 0, 0

    inner_circle_radius = 325
    outer_circle_radius = inner_circle_radius + 45

    draw_circle(x=start_x, y=start_y, radius=outer_circle_radius, should_fill=True)
    draw_circle(x=start_x, y=start_y, radius=inner_circle_radius, should_fill=True, fill_color="white")

    white_out_coordinates = [(-286.0, -293.0),
                             (-235.0, -193.0),
                             (-143.0, -255.0),
                             (-193.0, -337.0)]
    draw_polygon(white_out_coordinates, should_fill=True, pen_color="white", fill_color="white")

    left_A_coordinates = [(-306.0, -374.0),
                          (122.0, 414.0),
                          (199.0, 422.0),
                          (-235.0, -376.0)]
    draw_polygon(left_A_coordinates, should_fill=True)

    right_A_coordinates = [(119.0, 118.0),
                           (116.0, 302.0),
                           (199.0, 419.0),
                           (200.0, 47.0)]
    draw_polygon(right_A_coordinates, should_fill=True)

    draw_polygon([(2.0, 65.0),
                  (117.0, 66.0),
                  (113.0, 2.0),
                  (-40.0, 3.0)], should_fill=True)

    draw_polygon([(117.0, 96.0),
                  (112.0, -21.0),
                  (212.0, 19.0)], should_fill=True)

    draw_polygon([(115.0, -38.0),
                  (200.0, -4.0),
                  (202.0, -45.0)], should_fill=True)


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
