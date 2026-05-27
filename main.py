from turtle import Turtle,Screen
import random
import time
CHACHA=Screen()
CHACHA.bgcolor('navy')
CHACHA.setup(width=380,height=600)
# انشاء كلاس للأزرار المرتبطة بكل سلحفاة
#تكتب تورتل بين قوسين في الكلاس ازرار لتصريح بإن الكلاس  يرث من المكتبة  تورتل خصائصها فهو كلاس غير عادي
class Button(Turtle):
    def __init__(self,colore,location_X,name):
        #امر الكلاس ان ترث من مكتبة تورتل 
        super().__init__()
        self.colore=colore
        self.location_X=location_X
        self.location_y=0
        self.shape("square")
        self.penup()
        location_y=0
        self.goto(self.location_X,location_y)
        self.shapesize(stretch_wid=2.5, stretch_len=4)
        #هنا يتم تحديد لون كل زرار
        #الون لاول لابيض للحروف والون الثاني للخلفية
        self.color('black',self.colore)
# انشاء كلاس كسلاحفات ثم اخفائها للكتابة على الشاشة
        self.rsam=Turtle()
#اخفئها لأجل الكتابة على الشاشة
        self.rsam.hideturtle()
        
        self.rsam.color('white')
        self.rsam.penup()
#يدخلهاالسلاحفات المخفية في موقع الزرار
        self.rsam.goto(location_X,location_y)
# كتابة اسم كل زرار بستخدام دالة الكتابة
        self.rsam.write(name,align='center',font=('Arial',12,'normal'))
#دالة محو السلاحفات المخفية الخاصة بلنص
    def destroy(self):
                self.rsam.clear()
# انشاء زرار واحد من كلاس الزرار
red_button=Button("red",100,'red')
green_button=Button("green",0,"green")
yello_button=Button("yellow",-100,'yello')

#اخفاء السلاحفات المخفية
#
hamouda=Turtle()
hamouda.shape("turtle")
hamouda.color("red")
hamouda.hideturtle()
#
anis=Turtle()
anis.shape("turtle")
anis.color("green")
anis.hideturtle()
#
iyad=Turtle()
iyad.shape("turtle")
iyad.color("yellow")
iyad.hideturtle()
#دالة اظهار السلاحفاة بعد نقر المستخدم على الزرار
def show_turtle():
        hamouda.showturtle()
        anis.showturtle()
        iyad.showturtle()
#دالة اخفاء لأزرار"وليس نص"بعد نقر المستخدم على الزرار
def hide_button():
        red_button.hideturtle()
        green_button.hideturtle()
        yello_button.hideturtle()
#دالة المكملة لدالةمحو السلاحفات المخفية الخاصة بلنص 
def hide_text():
        red_button.destroy()
        green_button.destroy()
        yello_button.destroy()
#دالة انقر المستخدم على الزرار
def user_click(x,y):
        print(x,y)
        user_bet=None
        def turtle_writer_winer():
                hakma=Turtle()
                hakma.hideturtle()
                hakma.write('you win',align='center',font=('Arial',12,'normal'))
        def turtle_writer_loser():
                hakma=Turtle()
                hakma.hideturtle()
                hakma.write('you lose',align='center',font=('Arial',12,'normal'))

        if 60<x<140 and -25<y<25:
                user_bet='red'
                hide_text()
                red_button.destroy()
        elif -40<x<40 and -25<y<25:
                user_bet='green'
                show_turtle()
                hide_button()
                hide_text()
        elif -140<x<-60 and -25<y<25:
                user_bet='yello'
                show_turtle()
                hide_button()
                hide_text()
        hamouda.penup()
        hamouda.goto(-175,250)
        anis.penup()
        anis.goto(-175,100)
        iyad.penup()
        iyad.goto(-175,-50)
        #حركة السلاح
        def move_turtle():
                show_turtle()
                for i in range(random.randint(20,150)):
                        
                        hamouda.forward(random.randint(10,40))
                        anis.forward(random.randint(10,40))
                        iyad.forward(random.randint(10,40))
                        time.sleep(0.01)
                        
                        if hamouda.xcor()>iyad.xcor() and hamouda.xcor()>anis.xcor() and hamouda.xcor()>=180:
                                print('hamouda is winner')
                                if user_bet=='red':
                                        CHACHA.bgcolor('green')
                                        turtle_writer_winer()
                                else:
                                        CHACHA.bgcolor('red')
                                        turtle_writer_loser()
                                break
                        elif iyad.xcor()>hamouda.xcor() and iyad.xcor()>anis.xcor() and iyad.xcor()>=180:
                                
        
                                print('iyad is winner')
                                if user_bet=='yello':
                                        CHACHA.bgcolor('green')
                                        turtle_writer_winer()
                                else:
                                        CHACHA.bgcolor('red')
                                        turtle_writer_loser()
                                break
                        elif anis.xcor()>iyad.xcor() and anis.xcor()>hamouda.xcor() and anis.xcor()>=180:
                                print('anis is winner')
                        
                                if user_bet=='green':
                                        CHACHA.bgcolor('green')
                                        turtle_writer_winer()
                                else:
                                        CHACHA.bgcolor('red')
                                        turtle_writer_loser()
                                break
        move_turtle()

#شارة البدء 
#دالة انقر المستخدم على الشاشة
CHACHA.onscreenclick(user_click)
CHACHA.mainloop()