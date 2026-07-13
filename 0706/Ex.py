# print("안녕하세요?")
# print("programming에 입문하신 것을 축하드립니다.")
# print("생일축하!!"*10)


# import math
# math.cos(math.radians(30.0))
# (1/100)*1234

# print("내가 제일 좋아하는 음식은 피자!")
# print("피자"*10)
# print("얌얌"*10)

# print("수식의 결과값은", 10, "입니다")
# print("Hello")
# print()
# print("World")
# print("수식의 결과값은", 2*5, "입니다")
# print(3*1)
# print(3*2)
# print(3*3)

# print("*"*30)
# print("print()를 사용한 예제입니다.")
# print("내가 제일 좋아하는 숫자는 7입니다.")
# print("*"*30)

# print("3*1의 곱셈결과 = ", 3*1)

# turtle 모듈을 사용하여 거북이 그래픽을 그리는 예제입니다. 아래 코드를 실행하면 거북이가 화면에 나타나서 앞으로 이동하고 왼쪽으로 회전하는 모습을 볼 수 있습니다.
# import turtle

# t = turtle.Turtle()
# t.shape("turtle")

# t.forward(100)
# t.left(90)
# t.forward(50)

# turtle.mainloop()
# turtle.bye()

# 두번째 turtle 모듈 예제입니다. 이번에는 삼각형을 그리는 모습을 보여줍니다.
# import turtle
# t=turtle.Turtle()

# t.shape("turtle")
# t.forward(100)
# t.left(120)
# t.forward(100)
# t.left(120)
# t.forward(100)

# turtle.mainloop()
# turtle.bye()

# 세번째 turtle 모듈 예제입니다. 이번에는 반복문을 사용하여 여러 개의 삼각형을 그리는 모습을 보여줍니다.
import turtle

colors = ["red", "purple", "blue", "green", "yellow", "orange"]
t = turtle.Turtle()

turtle.bgcolor("black")
t.speed(0)
t.width(3)
length = 10

while length < 300:
    t.forward(length)
    t.pencolor(colors[length%6])
    t.right(86)
    length += 5
    
turtle.mainloop()
turtle.bye()    