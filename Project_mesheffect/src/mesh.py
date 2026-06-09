import turtle

def setup_screen():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("black")
    screen.title("Mesh Effect")
    return screen

def setup_turtle():
    t = turtle.Turtle()
    t.speed(20)
    t.width(5)
    return t

def draw_mesh_effect(t):
    colors = ["red","purple","blue","cyan","green", "yellow", "orange"]
    for i in range(150):
        t.color(colors[i % 7])
        t.circle(i, 180)
        t.left(90)
        t.forward(i)
        t.left(45)
def main():
    screen = setup_screen()
    screen.tracer(1)

    t = setup_turtle()
    draw_mesh_effect(t)

    screen.update()
    screen.exitonclick()

main()