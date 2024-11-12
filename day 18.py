from turtle import Turtle, Screen
timmy_the_turle=Turtle()
#timmy_the_turle.shape("Circle")
timmy_the_turle.color("Red")
import random
timmy_the_turle.speed("fastest")
# timmy_the_turle.colormode(255)

# def random_color():
#     global r,g,b
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
# my_tuple=(r,g,b)
# timmy_the_turle.color(my_tuple)
r=50
n=2
for _ in range(180):
 timmy_the_turle.circle(r)
 timmy_the_turle.right(n)
 n+=2











screen=Screen()
screen.exitonclick()