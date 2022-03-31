import turtle

def draw_square():

    i = 0
    while True:
        window = turtle.Screen()
        window.bgcolor('purple')

        john = turtle.Turtle()
        john.settiltangle(30.0)

        john.shape('arrow')
        john.color('green')
        john.settiltangle(30.0)
        john.speed(5)
        john.forward(150)
        john.right(90)
        john.forward(150)
        john.right(90)
        john.forward(150)
        john.right(90)
        john.forward(150)
        john.right(90)

        andy = turtle.Turtle()
        andy.shape('circle')
        andy.speed(2)
        andy.color('yellow')
        andy.forward(75)
        andy.right(90)
        andy.forward(75)
        andy.right(90)
        andy.forward(75)
        andy.right(90)
        andy.forward(75)
        andy.right(90)

        woody = turtle.Turtle()
        woody.color("blue")
        woody.speed(4)
        woody.circle(100)

    window.exitonclick()


draw_square()
