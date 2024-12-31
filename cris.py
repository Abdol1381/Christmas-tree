import turtle
import random
import time
import numbers 


def draw_tree_base(t, levels, base_width, height_step):
    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.color("green")
    for i in range(levels):
        t.fillcolor("green")
        t.begin_fill()
        t.goto(-base_width // 2 + i * 10, -250 + i * height_step)
        t.goto(base_width // 2 - i * 10, -250 + i * height_step)
        t.goto(0, -250 + (i + 1) * height_step)
        t.goto(-base_width // 2 + i * 10, -250 + i * height_step)
        t.end_fill()

def draw_trunk(t):
    t.penup()
    t.goto(-20, -250)
    t.pendown()
    t.fillcolor("brown")
    t.begin_fill()
    for _ in range(2):
        t.forward(40)
        t.left(90)
        t.forward(60)
        t.left(90)
    t.end_fill()

def draw_star(t):
    t.penup()
    t.goto(0, 120)
    t.setheading(-90)
    t.pendown()
    t.color("yellow")
    t.fillcolor("yellow")
    t.begin_fill()
    for _ in range(5):
        t.forward(50)
        t.right(144)
    t.end_fill()

def add_decorations(t, num_decorations):
    colors = ["red", "blue", "gold", "white", "pink"]
    for _ in range(num_decorations):
        x = random.randint(-100, 100)
        y = random.randint(-200, 90)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(random.randint(10, 20), random.choice(colors))

def glowing_message(t, text, position):
    
    colors = ["white", "yellow", "gold", "pink"]
    for _ in range(10):
        t.penup()
        t.goto(position)
        t.color(random.choice(colors))
        t.write(text, align="center", font=("Arial", 18, "bold"))
        time.sleep(0.2)
        t.undo()

def draw_christmas_tree():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Christmas Tree with Glowing Message")

    t = turtle.Turtle()
    t.speed(0)

    draw_tree_base(t, levels=8, base_width=200, height_step=30)
    draw_trunk(t)
    add_decorations(t, num_decorations=30)
    draw_star(t)
    glowing_message(t, "Merry Christmas!", (0, -320))

    t.hideturtle()
    screen.mainloop()

draw_christmas_tree()
