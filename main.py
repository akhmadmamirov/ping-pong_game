from turtle import Screen
from padlet import Padlet
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(800,600)
screen.bgcolor('red')
screen.title('Pong')
screen.tracer(0)

left_padlet = Padlet((-350,0))
right_padlet = Padlet((350, 0))

ball = Ball()
scoreboard = Scoreboard()




screen.listen()
screen.onkey(right_padlet.go_up, 'Up')
screen.onkey(right_padlet.go_down, 'Down')

screen.onkey(left_padlet.go_up, 'w')
screen.onkey(left_padlet.go_down, 's')


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
 
    #Detect the Collision with the Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #Detect collision with the paddl. 
    if ball.distance(right_padlet) <50 and ball.xcor() > 320 or ball.distance(left_padlet) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    #Detec right paddle misses the ball 
    if ball.xcor() >380:
        ball.reset_position()
        scoreboard.l_point()
    
    #Detect left paddle misses the ball
    if ball.xcor() < - 380:
        ball.reset_position()
        scoreboard.r_point()
screen.exitonclick()
