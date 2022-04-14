import turtle as t
import math
edge, vertex, restart = 0, 0, "yes"

def oddstar(edge, vertex) :
    t.goto(0,edge/2)
    t.setheading(-90 - 90/vertex)
    t.showturtle()
    t.pendown()
    t.begin_fill()
    
    for i in range(0,vertex) : 
        t.forward(edge)
        t.left(180 - 180/vertex)
    t.end_fill()
    t.hideturtle()
    
def evenstar(edge, vertex) :
    t.setheading(90)
    t.forward(edge/(2*math.sin(math.radians(360/vertex))))
    t.left(90 + 360/vertex)
    t.showturtle()
    t.pendown()
    t.begin_fill()
        
    for i in range(0,int(vertex/2)) : 
        t.forward(edge)
        t.left(720/vertex)
    t.end_fill()
    t.penup()

    t.home()
    t.setheading(90 + 360/vertex)
    t.forward(edge/(2*math.sin(math.radians(360/vertex))))
    t.left(90 + 360/vertex)
    t.showturtle()
    t.pendown()
    t.begin_fill()
        
    for i in range(0,int(vertex/2)) : 
        t.forward(edge)
        t.left(720/vertex)
    t.end_fill()
    t.penup()

    t.hideturtle()



while restart == "yes" :
    t.reset()
    t.pensize(3)
    t.penup()
    t.hideturtle()
    t.shape("classic")
    t.color("orange")
    
    edge = input("별을 그려봅시다. 한 변의 길이를 얼마로 할까요? : ")
    while edge.isnumeric() == False :
        edge = input("변의 길이는 자연수로 입력해 주세요. : ")
    edge = int(edge)

    vertex = input("별의 꼭짓점은 몇 개로 할까요? : ")
    while vertex.isnumeric() == False :
        edge = input("꼭짓점의 개수는 자연수로 입력해 주세요. : ")
    vertex = int(vertex)
    while vertex<5:
        vertex = int(input("꼭짓점은 5 이상의 자연수를 입력해 주세요. : "))

    if vertex%2 == 1 : 
        oddstar(edge, vertex)
    else :
        evenstar(edge, vertex)

    restart = input("별을 한 번 더 그리려면 [yes]를, 프로그램을 종료하려면 [no]를 입력해 주세요. : ")
    
