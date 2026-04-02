from turtle import Turtle, Screen
import random
# الشاشة
windowe = Screen()
windowe.setup(width=400, height=600)
windowe.bgcolor('black')
windowe.title('hamouda')

# السلاحف
hamouda = Turtle()
mpape=Turtle()
wes= Turtle()
colors = ['red','blue','green','yellow','white','purple','pink','brown','gray']
shapes = ['arrow','turtle','circle','square','triangle']
angles = [0, 90, 180, 270]
steps = [10,20,30,40,50,60,70,80,90,100]
# 🎯 حركة عامة
def drawe_circles():
    hamouda.goto(100,150)
    hamouda.pensize(3)
    hamouda.shape(random.choice(shapes))
    hamouda.color(random.choice(colors))
    for i in range(9):
        hamouda.circle(30)
        hamouda.left(40)
def drawe_square():
    mpape.goto(0,0)
    mpape.color(random.choice(colors))
    mpape.shape(random.choice(shapes))
    mpape.pensize(3)
    for i in range(12):
        for y in range(4):
            mpape.forward(50)
            mpape.left(90)
        mpape.left(30)
def drawe_triangle():
    wes.goto(-150,-200)
    wes.color(random.choice(colors))
    wes.shape(random.choice(shapes))
    wes.pensize(3)
    for y in range(18):
        for i in range(1):
            wes.forward(80)
            wes.left(60)
            wes.forward(60)
            wes.left(500)
            wes.forward(120)
            wes.left(20)
# textinput() opens a Tkinter dialog that does not trigger the mobile keyboard
# inside the VNC window. Using input() in the console works on every device,
# including mobile, because the console input field handles keyboard focus correctly.
print("╔══════════════════════════════╗")
print("║  Type your name in the       ║")
print("║  CONSOLE below, then Enter.  ║")
print("╚══════════════════════════════╝")
user_name = input("Enter your first name: ").strip() or "Guest"

# Write the name onto the turtle canvas so it appears in the VNC window
nametag = Turtle()
nametag.hideturtle()
nametag.penup()
nametag.color('white')
nametag.goto(0, 250)
nametag.write(f"Hello, {user_name}!", align="center", font=("Arial", 16, "bold"))

drawe_square()
drawe_circles()
drawe_triangle()
windowe.exitonclick()