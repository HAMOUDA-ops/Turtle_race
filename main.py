from turtle import Turtle, Screen
import time

# انتظر 5 ثوانٍ قبل البدء لتعطي فرصة للشاشة لتفتح
time.sleep(5)
def move():
  hamouda = Turtle()
  hamouda.shape('turtle')
  hamouda.color('green')
  hamouda.forward(100)
  hamouda.left(45)
  hamouda.forward(50)
  hamouda.right(90)
move()
Screen().exitonclick()