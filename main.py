from turtle import Turtle, Screen

mpapi = Turtle()
chacha = Screen()

mpapi.color('green')

def move():
    mpapi.forward(500)
    mpapi.left(50)
    mpapi.forward(40)
    mpapi.left(69)

move()
move()

chacha.exitonclick()  # باش تبقى النافذة مفتوحة #fix