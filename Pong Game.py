import turtle

wn = turtle.Screen()
wn.title("Pong by @TokyoEdTech")
wn.bgcolor("black")
wn.setup(width=800, height=600) #these mean +400 on the left and -400 on the right. Also +300 on top, -300 on bottom
wn.tracer(0)

#Score
score_a = 0
score_b = 0

#Adding Paddle A and B along with a Ball

paddle_a = turtle.Turtle() #this make it an object.
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() #stops it from drawing a line, which apparently turtles do
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle() #this make it an object.
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() #stops it from drawing a line, which apparently turtles do
paddle_b.goto(350, 0)

ball = turtle.Turtle() #this make it an object.
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup() #stops it from drawing a line, which apparently turtles do
ball.goto(0, 0)
ball.dx = 0.15 #d means delta, or change. this is the speed the ball moves. varrys by computer
ball.dy = 0.15 #these mean that every time the ball moves, it moves two pixes.

# Pen (for scoring)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier",24,"normal"))

#Creating functions for paddle movement
def paddle_a_up():
    y = paddle_a.ycor() #assigning y cordinate to a vairable, y
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() #assigning y cordinate to a vairable, y
    y -= 20
    paddle_a.sety(y)
    
def paddle_b_up():
    y = paddle_b.ycor() #assigning y cordinate to a vairable, y
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() #assigning y cordinate to a vairable, y
    y -= 20
    paddle_b.sety(y)

wn.listen()#tells to listen for keyboard input
wn.onkeypress(paddle_a_up, "w") #call the function with w key
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up") #call the fuction with up arrow
wn.onkeypress(paddle_b_down, "Down")

#Main Game Loop
while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #this reverses the direction. if dy is 2 then it becomes -2. if it's -2, it becomes 2.
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390: #We do 90instead of the full 400 and 300 because that is the point where it is past the paddle
        ball.goto(0, 0) #back to center
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier",24,"normal"))
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier",24,"normal"))

    # Paddle and ball collissions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1

    
