import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen. bgcolor("tan")

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-80,15)
t.pendown()
t.pencolor("blue")
t.circle(35)

t.penup()
t.goto(-48,-20)
t.pendown()
t.pencolor("yellow")
t.circle(35)

t.penup()
t.goto(-20,15)
t.pendown()
t.pencolor("black")
t.circle(35)


t.penup()
t.goto(10,-20)
t.pendown()
t.pencolor("green")
t.circle(35)

t.penup()
t.goto(35,15)
t.pendown()
t.pencolor("red")
t.circle(35)

t.pencolor("purple")
t.penup()
t.goto(0,200)
t.pendown()
t.write("Winter Olympics",font=("arial",30,"bold"),align="center")

t.pencolor("purple")
t.penup()
t.goto(0,-200)
t.pendown()
t.write("2026",font=("arial",20,"bold"),align="center")



turtle.done()