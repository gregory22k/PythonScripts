#classic pong game


#part 1: imports
import turtle

#part 2: set the window properties
wn = turtle.Screen()
wn.title("Pong by Gregory")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#set paddles, ball and pen properties

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=4,stretch_len=1)
paddle_a.penup()  #doesnt draw line while moving
paddle_a.goto(-390,0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=4,stretch_len=1)
paddle_b.penup()
paddle_b.goto(390,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.08
ball.dy = -0.08


#pen to keep track of score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align = "center", font = (("Courier"), 24, "normal"))


#Score initilization
player_a = 0
player_b = 0

#paddle movement

def paddle_a_up():
	y = paddle_a.ycor()
	y += 30
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	y -= 30
	paddle_a.sety(y)


def paddle_b_up():
	y = paddle_b.ycor()
	y += 30
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y -= 30
	paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddle_a_up,'w')
wn.onkeypress(paddle_a_down,'s')

wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down,'Down')

#main game loop
while True:

	wn.update()


#move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)


#border checking
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1

	if ball.ycor()<-290:
		ball.sety(-290)
		ball.dy *= -1

	if ball.xcor()>390:
		ball.goto(0,0)
		ball.dy *= 1
		ball.dx*=-1
		ball.clear()
		player_a+=1
		pen.clear()
		pen.write("Player A: {}  Player B: {}".format(player_a, player_b), align = "center", font = (("Courier"), 24, "normal"))
		

	if ball.xcor()<-390:
		ball.goto(0,0)
		ball.dy *= -1
		ball.dx *=-1
		ball.clear()
		player_b += 1
		pen.clear()
		pen.write("Player A: {}  Player B: {}".format(player_a, player_b), align = "center", font = (("Courier"), 24, "normal"))


#paddle and ball collision
	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor()+40 and ball.ycor() > paddle_b.ycor()-40):
		ball.setx(340)
		ball.dx*=-1
        
	if (ball.xcor() <- 340 and ball.xcor() >-350) and (ball.ycor() < paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor()-40):
		ball.setx(-340)
		ball.dx*=-1

