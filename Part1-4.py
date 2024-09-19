import turtle
import random


"""PUT YOUR FUNCTIONS HERE"""

def draw_pumpkin(t, x, y, radius):
    """Draws a pumpkin (orange circle) at the given (x, y) location with a green stem."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_stem (t, radius):
    # Drawing the stem
    t.fillcolor("green")
    t.begin_fill()
    t.left(90)  # Point upwards
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius // 5)
    t.left(90)
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius // 5)
    t.end_fill()

def draw_eye(t, x, y, size):
        """Draws one triangular eye at the given (x, y) position."""
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.fillcolor("yellow")
        t.begin_fill()
        draw_polygon(t, 3, size)
        t.end_fill()

def draw_polygon(t, n, length):
            angle = 360 / n
            for i in range(n):
                t.forward(length)
                t.left(angle)

def draw_mouth(t, x, y, width):
        """Draws a jagged mouth using a series of connected lines."""
        t.penup()
        t.goto(x, y)
        t.right(60)
        t.pendown()
        t.fillcolor("yellow")
        t.begin_fill()
        for _ in range(5):  # Create a simple zigzag mouth
            t.forward(width // 5)
            t.left(120)
            t.forward(width // 5)
            t.right(120)
        t.end_fill()

def draw_jackolantern():
    draw_stem(t, 100)
    draw_pumpkin(t, -10, -199, 100)
    draw_eye(t, -65, -70, 35)
    draw_eye(t, 10, -70, 35)
    draw_mouth(t, -70, -115, 120)

def draw_star(t, x, y, size):
    """Draws a star at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)  # 144 degrees is the angle to form a star
    t.end_fill()

def draw_sky(t, num_stars):
    """Draws a starry sky with the given number of stars."""
    for _ in range(num_stars):
        x = random.randint(-300, 300)
        y = random.randint(0, 300)
        size = random.randint(10, 30)
        draw_star(t, x, y, size)




# Create a turtle object
t = turtle.Turtle()

# Hide the turtle and set speed
t.speed(10)  # 1 is slow, 10 is fast, 0 is instant
t.hideturtle()

# Create a window to draw in
# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("darkblue")
# Set the width and height of the screen
screen.setup(width=600, height=600)


"""PUT YOUR DRAW CALLS TO FUNCTIONS HERE"""
draw_jackolantern()
draw_sky(t, 100)  # Draw 20 stars




# Close the turtle graphics window when clicked
turtle.exitonclick()