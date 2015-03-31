# -*- coding: utf-8 -*-
import random
arquivo = open("entrada.txt", encoding="utf-8")
palavras = arquivo.readlines()
for i in range(len(palavras)-1):
    palavras[i] = palavras[i].strip().upper()
    if palavras[i] == '':
        del palavras[i]
    palavras[i] = palavras[i].strip().upper()
pa = random.choice(palavras)


import turtle          # Usa a biblioteca de turtle graphics
window = turtle.Screen()    # cria uma janela
window.bgcolor("lightblue")
window.title("Jogo Da Forca")

tartaruga   = turtle.Turtle()  # Cria um objeto "desenhador"
tartaruga.speed(10)  # define a velocidade
tartaruga.penup()       # Remova e veja o que acontece
tartaruga.setpos(-250,-200)
tartaruga.pendown()
tartaruga.color("blue")

dist = 120

#funções
def cabeça():
    tartaruga.penup()   # cabeça
    tartaruga.setpos(-80,90)
    tartaruga.pendown()
    tartaruga.circle(40)
    tartaruga.penup()
    tartaruga.setpos(-40,50)
    tartaruga.penup()
    
    
def corpo():    
    tartaruga.penup()
    tartaruga.setpos(-40,50)
    tartaruga.pendown()   # corpo
    tartaruga.forward(150)
    tartaruga.penup()
    
def braço1():    
    tartaruga.penup()
    tartaruga.setpos(-40,-100)
    tartaruga.pendown()
    tartaruga.backward(125)   # braço 1
    tartaruga.left(60)
    tartaruga.forward(70)
    tartaruga.backward(70)
    tartaruga.penup()
    
def braço2():    
    tartaruga.penup()
    tartaruga.setpos(-40,25)
    tartaruga.pendown()
    tartaruga.right(125)    # braço2
    tartaruga.forward(70)
    tartaruga.backward(70) 
    tartaruga.penup()
    
def perna1():
    tartaruga.left(65)    # perna1
    tartaruga.forward(125)
    tartaruga.left(35)
    tartaruga.penup()
    tartaruga.setpos(-40,-100)
    tartaruga.pendown()
    tartaruga.forward(100)
    tartaruga.backward(100)
    tartaruga.penup()
    
def perna2():   
    tartaruga.penup()
    tartaruga.setpos(-40,-100)
    tartaruga.pendown()
    tartaruga.right(75)   # perna2
    tartaruga.forward(100)



tartaruga.forward(120) 
tartaruga.backward(60)
tartaruga.left(90)
tartaruga.forward(400)
tartaruga.left(270)
tartaruga.forward(150)
tartaruga.right(90)
tartaruga.forward(70)
tartaruga.penup()

espaço = len(pa)
i=0
acertos = 0

while i<= espaço-1:
    
    
    if pa[i] == (" "):
        acertos+=1
    else:
        tartaruga.setpos(35*i-5*espaço,-200)
        tartaruga.write("_ ",font=("arial",25))
        
    i+=1


erros=0
espaço = len(pa)
lista = []
