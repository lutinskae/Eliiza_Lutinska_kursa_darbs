# from tkinter import Y
import turtle
import math
# li = ["Kursa darbs!", "Tēma", "--"]
# for x in range(0, len(li)):
#     print(li[x])
screen = turtle.Screen()
# background color
screen.bgcolor("lightblue")
# turtle object

def SaulesZiimeejums(): #funkcija, lai izveidotu sauli
    y.penup()
    y.goto(95, 120)
    y.fillcolor("yellow")
    y.pendown()
    y.begin_fill()
    y.circle(45)
    y.end_fill()
    # zimee saules starinus
    y.penup()
    y.goto(95, 179)
    y.pendown()
    drawFourRays(y, 95, 64)
    y.right(45)
    drawFourRays(y, 95, 64)
    y.left(45)
    k = turtle.Turtle()
    #color and speed
    # of turtle

def MaajasZiimeejums(): #funkcija, lai izveidotu māju
    k = turtle.Turtle()
    k.color("black")
    k.shape("turtle")
    k.speed(1)
    # veido majas pirmo stavu
    k.fillcolor('cyan')
    k.begin_fill()
    k.right(90)
    k.forward(250)
    k.left(90)
    k.forward(400)
    k.left(90)
    k.forward(250)
    k.left(90)
    k.forward(400)
    k.right(90)
    k.end_fill()
    # veido majas jumtu
    k.fillcolor('brown')
    k.begin_fill()
    k.right(45)
    k.forward(200)
    k.right(90)
    k.forward(200)
    k.left(180)
    k.forward(200)
    k.right(135)
    k.forward(259)
    k.right(90)
    k.forward(142)
    k.end_fill()
    # for door and
    # windows
    y.right(90)
    y.forward(400)
    y.left(90)
    y.forward(50)
    y.left(90)
    y.forward(150)
    y.right(90)
    y.forward(200)
    y.right(180)
    y.forward(200)
    y.right(90)
    y.forward(200)
    y.right(90)
    y.forward(150)
    y.right(90)
    y.forward(200)
    y.right(90)
    y.forward(150)
    y.right(90)
    y.forward(100)
    y.right(90)
    y.forward(150)
    y.right(90)
    y.forward(100)
    y.right(90)
    y.forward(75)
    y.right(90)
    y.forward(200)
    y.right(180)
    y.forward(200)
    y.right(90)
    y.forward(75)
    y.left(90)
    y.forward(15)
    y.left(90)
    y.forward(200)
    y.right(90)
    y.forward(15)
    y.right(90)
    y.forward(75)

y = turtle.Turtle()

izveeleetie = []

while True:
    try:
        opcija = int(input("Izvēlieties opcijas\n1 Saule\n2 Māja\n3 Koks\n"))
        if opcija == 1:
            izveeleetie.append("Sauli")
        if opcija == 2:
            izveeleetie.append("Māju")
        if opcija == 3:
            izveeleetie.append("Koku")  

    except: print("Ievadiet skaitli!")


    # definee funkciju lai zimeetu sauliti
    def drawFourRays(t, length, radius):
        for i in range(4):
            t.penup()
            t.forward(radius)
            t.pendown()
            t.forward(length)
            t.penup()
            t.backward(length + radius)
            t.left(90)
    # uzzimee apli, prieks saules
    if opcija == 1: #Zīmēt sauli
        SaulesZiimeejums()
    
    if opcija == 2:
        MaajasZiimeejums()
    
    #peec sis rindinas saksies koka zimesanas dala
    # lai uzzimetu celmu
    def drawRectangle(t, width, height, color):
        t.fillcolor(color)
        t.begin_fill()
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
        t.end_fill()
    # lai uzzimetu trijsturi
    def drawTriangle(t, length, color):
        t.fillcolor(color)
        t.begin_fill()
        t.forward(length)
        t.left(135)
        t.forward(length / math.sqrt(2))
        t.left(90)
        t.forward(length / math.sqrt(2))
        t.left(135)
        t.end_fill()
        # izveido turtle
    if opcija == 3:
        tip = turtle.Turtle()
        tip.color ("black")
        tip.shape ("turtle")
        tip.speed (2)
        # Tree base
        tip.penup()
        tip.goto(-100, -130)
        tip.pendown()
        drawRectangle(tip, 20, 40, "brown")
        # Tree top
        tip.penup()
        tip.goto(-135, -90)
        tip.pendown()
        drawTriangle(tip, 90, "lightgreen")
        tip.penup()
        tip.goto(-130, -45)
        tip.pendown()
        drawTriangle(tip, 80, "lightgreen")
        tip.penup()
        tip.goto(-125, -5)
        tip.pendown()
        drawTriangle(tip, 70, "lightgreen")
        tip.penup()
    
    
    izvele = str(input("Vai turpināt zīmēšanu?\nY Jā \nN Nē"))
    if izvele == "N" or izvele == "n": break
    

fails = open("Rezultati.txt", "w")
fails.write("Lietotajs izvelejas: ")

for x in range(len(izveeleetie)):
    fails.write(f"{izveeleetie[x]}, ")

fails.close()
