"""
পতাকাটি জাতীয় পতাকার স্ট্যান্ডার্ড মাপ দিয়ে তৈরি করা হয়েছে। 
তবে খুঁটিতে কোন সঠিক মাপ দেয়া হয়নি।
_____________________________________
The flag is made to the standard size of the national flag.
However, no exact dimensions of the hut have been given.
"""






import turtle


t = turtle.Turtle()
t.pensize(1)
t.screen.bgcolor("black")
t.color("green")
t.shape("turtle")
t.speed(5)


#position
t.penup()
t.forward(-280)
t.left(90)
t.forward(600)
t.right(90)
t.pendown()

#rectangle
t.begin_fill()
t.forward(570)
t.right(90)
t.forward(342)
t.right(90)
t.forward(570)
t.right(90)
t.forward(342)
t.end_fill()


#position for circle
t.penup()
t.color("red")
t.right(90)
t.forward(256.5)
t.right(90)
t.forward(171)
t.pendown()

#circle
t.begin_fill()
t.left(90)
t.forward(128.25)
t.left(90)
t.circle(114)
t.end_fill()


#next position for bamboo
t.penup()
t.color("grey")
t.forward(171)
t.left(90)
t.forward(385) #384.75px for flag 0.25px more just for bamboo
t.right(90)
t.pendown()


#bamboo
t.begin_fill()
t.forward(15)
t.forward(-1130)
t.left(90)
t.forward(20)
t.right(90)
t.forward(1130)
t.right(90)
t.forward(20)
t.end_fill()


#position of the base
t.right(90)
t.forward(1130)
t.left(90)

#smallest base
t.begin_fill()
t.color("silver")
t.forward(50)
t.forward(-164)
t.right(90)
t.forward(30)
t.left(90)
t.forward(164)
t.left(90)
t.forward(30)
t.end_fill()


#2nd smallest base
t.begin_fill()
t.forward(-30)
t.right(90)
t.forward(40)
t.right(90)
t.forward(30)
t.right(90)
t.forward(244)
t.right(90)
t.forward(30)
t.right(90)
t.forward(40)
t.end_fill()


#bigest base
t.begin_fill()
t.forward(204)
t.right(90)
t.forward(30)
t.left(90)
t.forward(40)
t.right(90)
t.forward(30)
t.right(90)
t.forward(324)
t.right(90)
t.forward(30)
t.right(90)
t.forward(40)
t.end_fill()


#style position 
t.penup()
t.pensize(5)
t.color("maroon")
t.forward(136)
t.left(90)
t.forward(80)
t.right(90)
t.pendown()

#start style
t.forward(18)
t.left(90)
t.penup()
t.forward(70)
t.left(90)
t.pendown()

t.forward(18)
#2nd
t.right(90)
t.penup()
t.forward(70)
t.left(90)
t.pendown()

t.forward(-18)
#3rd
t.right(90)
t.penup()
t.forward(70)
t.left(90)
t.pendown()

t.forward(18)
#4th
t.right(90)
t.penup()
t.forward(70)
t.left(90)
t.pendown()

t.forward(-18)
#5th
t.right(90)
t.penup()
t.forward(70)
t.left(90)
t.pendown()

t.forward(18)
#6th
t.right(90)
t.penup()
t.forward(70)
t.left(90)
t.pendown()

t.forward(-18)
#7th
t.right(90)
t.penup()
t.forward(70)
t.left(90)
t.pendown()

t.forward(18)
#8th
t.right(90)
t.penup()
t.forward(70)
t.left(90)
t.pendown()

t.forward(-18)
#9th
t.right(90)
t.penup()
t.forward(70)
t.left(90)
t.pendown()

t.forward(18)
#10th
t.right(90)
t.penup()
t.forward(70)
t.left(90)
t.pendown()

t.forward(-18)
#11th
t.right(90)
t.penup()
t.forward(70)
t.left(90)
t.pendown()

t.forward(18)
#12th
t.right(90)
t.penup()
t.forward(70)
t.left(90)
t.pendown()

t.forward(-18)
#13th
t.right(90)
t.penup()
t.forward(70)
t.left(90)
t.pendown()

t.forward(18)
#14th
t.right(90)
t.penup()
t.forward(70)
t.left(90)
t.pendown()

t.forward(-18)
#15th
t.right(90)
t.penup()
t.forward(70)
t.left(90)
t.pendown()

t.forward(18)
#16th
t.right(90)
t.penup()
t.forward(60)
t.left(90)
t.pendown()

t.forward(-18)


#position of "বাংলাদেশ"
t.color("white")
t.penup()
t.forward(-230)
t.left(90)
t.forward(1300)
t.left(180)
t.pensize(10)
t.pendown()

# ব
t.forward(100)
t.right(140)
t.forward(120)
t.left(90)
t.forward(120)
t.left(140)
t.forward(150)
t.penup()

#া
t.forward(20)
t.right(90)
t.pendown()
t.forward(30)
t.right(90)
t.forward(170)
t.forward(-130)
t.right(140)
t.forward(35)

#next position
t.penup()
t.forward(-35)
t.right(40)
t.forward(40)
t.right(90)
t.forward(30)

#ং
t.right(55)
t.forward(20)
t.pendown()
t.forward(110)
t.right(7)
t.forward(70)
t.penup()
t.right(35)
t.forward(-110)
t.left(90)
t.forward(-30)
#o
t.pendown()
t.circle(25, 360)
t.penup()

#next position
t.forward(70)
t.left(97)
t.forward(65)
t.right(90)
t.pendown()

#ল
t.forward(130)
t.right(90)
t.forward(170)
t.forward(-20)
t.right(180)
t.circle(30, 180)
t.forward(20)
t.forward(-20)
t.right(180)
t.circle(30, 180)
t.forward(20)
t.circle(5)

#next position
t.penup()
t.forward(-170)
t.left(90)
t.forward(120)
t.pendown()

#া
t.forward(30)
t.right(90)
t.forward(170)
t.forward(-130)
t.right(140)
t.forward(35)

#next position
t.penup()
t.forward(-35)
t.right(40)
t.forward(40)
t.right(90)
t.forward(30)
t.pendown()

#ে
t.forward(50)
t.right(130)
t.circle(130,90)
t.circle(10)

#next position
t.penup()
t.left(127)
t.forward(183)
t.right(87)
t.pendown()

#দ
t.forward(-25)
t.forward(160)
t.forward(-95)
t.right(90)
t.forward(100)
t.left(130)
t.forward(80)
t.right(90)
t.forward(30)
t.right(90)
t.circle(130,60)

#next position
t.penup()
t.right(8)
t.forward(-195)
t.left(87)
t.forward(50)
t.pendown()

#শ 1st
t.circle(-90,90)
t.circle(-20,180)
t.circle(-40,65)
#position
t.penup()
t.forward(80)
t.right(25)
t.forward(40)
t.left(90)
t.forward(20)
t.left(90)
t.pendown()

#2nd
t.circle(90,90)
t.circle(20,180)
t.circle(40,100)

#next position
t.penup()
t.forward(-120)
t.right(98)
t.forward(25)
t.right(182)
t.pendown()

#া
t.forward(190)
t.forward(-170)
t.right(140)
t.circle(60, 50)


#hide turtle
t.penup()
t.forward(300)
t.pendown()
t.hideturtle()

#end
turtle.done()