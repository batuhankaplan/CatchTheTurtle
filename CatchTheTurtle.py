import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("CatchTurtleIfYouCan")

# Skorbord
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 320)
score_display.color("white")
score_display.write("Score: 0", align="center", font=("Comic Sans MS", 22, "normal"))

# Süre
timer_display = turtle.Turtle()
timer_display.hideturtle()
timer_display.penup()
timer_display.goto(0, 360)
timer_display.color("green")
timer_display.write("Time left: 10", align="center", font=("Comic Sans MS", 22, "normal"))

time_left = 10
score = 0


# Kaplumbağa
def draw_turtle():
    kaplumbaga.clear()
    kaplumbaga.penup()
    kaplumbaga.goto(0, 0)
    kaplumbaga.pendown()


kaplumbaga = turtle.Turtle()
kaplumbaga.shape("turtle")
kaplumbaga.color("green")
kaplumbaga.penup()
kaplumbaga.speed(0)
kaplumbaga.hideturtle()


# Kaplumbağa hareketleri
def move_turtle():
    y_movement = random.choice([-50, 50])
    kaplumbaga.sety(kaplumbaga.ycor() + y_movement)

    if kaplumbaga.ycor() > 180:
        kaplumbaga.sety(180)
    elif kaplumbaga.ycor() < -180:
        kaplumbaga.sety(-180)

    x_movement = random.choice([-20, 20])
    kaplumbaga.setx(kaplumbaga.xcor() + x_movement)

    screen.ontimer(move_turtle, 500)


# Kaplumbağaya tıklama fonksiyonu
def click_turtle(x, y):
    global score
    if kaplumbaga.distance(x, y) < 20:
        score += 1
        update_score()
        move_turtle()


# Skor
def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Comic Sans MS", 22, "normal"))


# Gerisayım
def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        timer_display.clear()
        timer_display.write(f"Time left: {time_left}", align="center", font=("Comic Sans MS", 22, "normal"))
        screen.ontimer(countdown, 1000)
    else:
        check_win_or_lose()


#Win/Lose
def check_win_or_lose():
    kaplumbaga.hideturtle()
    message_display = turtle.Turtle()
    message_display.hideturtle()
    message_display.penup()
    message_display.goto(0, 200)

    if score >= 10:
        message_display.color("Green")
        message_display.write("You caught the turtle! YOU WIN!", align="Center", font=("Comic Sans MS", 24, "Bold"))

    else:
        message_display.color("Red")
        message_display.write("GAME OVER!", align="center", font=("Comic Sans MS", 24, "normal"))



kaplumbaga.showturtle()
move_turtle()
screen.ontimer(countdown, 1000)

screen.onscreenclick(click_turtle)

screen.mainloop()
