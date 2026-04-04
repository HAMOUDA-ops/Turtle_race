import turtle
import random

# ─────────────────────────────────────────────
# WHY textinput() FAILS ON MOBILE / VNC
# ─────────────────────────────────────────────
# textinput() creates a small Tkinter pop-up dialog.
# The VNC viewer streams the remote desktop as pixels,
# so when that dialog opens the mobile OS has no way to
# know a text field is waiting — it never raises the
# soft keyboard. The fix: replace the dialog with
# clickable turtle buttons. Taps/clicks are forwarded
# correctly through VNC, so the user just taps a color.
# ─────────────────────────────────────────────

COLORS = ["red", "blue", "green"]
FINISH_X = 280
START_X  = -280

screen = turtle.Screen()
screen.setup(width=700, height=500)
screen.title("Turtle Race")
screen.bgcolor("black")
screen.tracer(0)

# ── helper: draw a filled rounded-ish rectangle button ──
def draw_button(pen, cx, cy, color):
    w, h = 110, 45
    pen.penup()
    pen.goto(cx - w // 2, cy - h // 2)
    pen.setheading(0)
    pen.color("white", color)
    pen.pensize(2)
    pen.begin_fill()
    for length in [w, h, w, h]:
        pen.forward(length)
        pen.left(90)
    pen.end_fill()
    pen.penup()
    pen.goto(cx, cy - 8)
    pen.color("white")
    pen.write(color.upper(), align="center", font=("Arial", 15, "bold"))

# ── draw the three bet buttons ──
btn_pen = turtle.Turtle()
btn_pen.hideturtle()
btn_pen.speed(0)

BTN_Y = 30
BTN_POSITIONS = [(-210, BTN_Y), (0, BTN_Y), (210, BTN_Y)]

for col, pos in zip(COLORS, BTN_POSITIONS):
    draw_button(btn_pen, pos[0], pos[1], col)

# ── instruction label ──
msg = turtle.Turtle()
msg.hideturtle()
msg.penup()
msg.color("white")
msg.goto(0, 130)
msg.write("Tap a color to place your bet:", align="center",
          font=("Arial", 16, "bold"))

screen.update()

# ─────────────────────────────────────────────
# RACE
# ─────────────────────────────────────────────
def start_race(bet):
    screen.tracer(0)
    btn_pen.clear()
    msg.clear()

    # draw finish line
    finish_pen = turtle.Turtle()
    finish_pen.hideturtle()
    finish_pen.penup()
    finish_pen.goto(FINISH_X, -200)
    finish_pen.setheading(90)
    finish_pen.color("white")
    finish_pen.pensize(2)
    finish_pen.pendown()
    finish_pen.forward(400)

    # place turtles on the track
    racers = []
    for idx, color in enumerate(COLORS):
        t = turtle.Turtle()
        t.shape("turtle")
        t.color(color)
        t.penup()
        t.goto(START_X, -80 + idx * 80)
        racers.append(t)

    screen.update()
    screen.tracer(1)

    # race loop
    winner = None
    while winner is None:
        for t in racers:
            t.forward(random.randint(1, 10))
            if t.xcor() >= FINISH_X:
                winner = t.pencolor()
                break

    # result banner
    screen.tracer(0)
    banner = turtle.Turtle()
    banner.hideturtle()
    banner.penup()
    banner.goto(0, -210)
    if bet == winner:
        banner.color("gold")
        banner.write(f"YOU WON!  {winner.upper()} wins!",
                     align="center", font=("Arial", 18, "bold"))
    else:
        banner.color("tomato")
        banner.write(f"YOU LOST.  {winner.upper()} won.",
                     align="center", font=("Arial", 18, "bold"))

    print(f"\nResult: {winner.upper()} won. Your bet: {bet.upper()}.")
    if bet == winner:
        print("You WON!")
    else:
        print("You lost.")

    screen.update()

# ─────────────────────────────────────────────
# CLICK HANDLER  — detects which button was tapped
# ─────────────────────────────────────────────
def on_click(x, y):
    for color, (cx, cy) in zip(COLORS, BTN_POSITIONS):
        if abs(x - cx) < 55 and abs(y - cy) < 22:
            screen.onclick(None)   # stop listening for more clicks
            msg.clear()
            msg.goto(0, 130)
            msg.color("yellow")
            msg.write(f"Bet placed: {color.upper()}!  Racing...",
                      align="center", font=("Arial", 16, "bold"))
            screen.update()
            start_race(color)
            return

screen.onclick(on_click)
screen.listen()
turtle.done()
