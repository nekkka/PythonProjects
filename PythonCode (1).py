import nntplib
from fnmatch import fnmatch
from lib2to3.pgen2.pgen import NFAState
from math import radians
from tkinter import *
from turtle import width, window_width
 
HEIGHT = 500
WIDTH = 800
window = Tk()
window.title('Bubble Blast')
canvas= Canvas(window,height=HEIGHT,width=WIDTH,bg = 'darkblue')
canvas.pack()
 
ship_id = canvas.create_polygon(5,5,5,25,30,15,fill='red')
ship_id2 = canvas.create_oval(0,0,30,30,outline='red')
SHIP_R = 15
 
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2
canvas.move(ship_id,MID_X,MID_Y)
canvas.move(ship_id2,MID_X,MID_Y)
SHIP_SPEED = 20
def move_ship(event):
    if event.keysym == "Up":
        canvas.move(ship_id,0,-SHIP_SPEED)
        canvas.move(ship_id2,0,-SHIP_SPEED)
    elif event.keysym == "Down":
        canvas.move(ship_id,0,SHIP_SPEED)
        canvas.move(ship_id2,0,SHIP_SPEED)
    elif event.keysym == "Left":
        canvas.move(ship_id,-SHIP_SPEED,0)
        canvas.move(ship_id2,-SHIP_SPEED,0)
    elif event.keysym == "Right":
        canvas.move(ship_id,SHIP_SPEED,0)
        canvas.move(ship_id2,SHIP_SPEED,0)
canvas.bind_all('<Key>',move_ship)
 
from random import *
 
bubble_id = list()
bubble_r = list()
bubble_SPEED = list()
Min_bubble_R = 10
Max_bubble_R = 30
Max_bubble_speed = 10
 
GAP = 100
 
def create_bubbles():
    x = WIDTH + GAP
    y = randint(0,HEIGHT)
    r = randint(Min_bubble_R,Max_bubble_R)
    id1 = canvas.create_oval(x-r,y-r,x+r,y+r,outline='white')
    bubble_id.append(id1)
    bubble_r.append(r)
    bubble_SPEED.append(randint(1,Max_bubble_speed))
 
def move_bubble():
    for i in range(len(bubble_id)):
        canvas.move(bubble_id[i],-bubble_SPEED[i],0)
 
from time import sleep, time
 
Bubble_chance = 10
def get_coords(id_num):
    pos = canvas.coords(id_num)
    x  = (pos[0] + pos[2]) / 2
    y  = (pos[1] + pos[3]) / 2
    return x,y
 
def delete_bubbles(i):
    del bubble_r[i]
    del bubble_SPEED[i]
    canvas.delete(bubble_id[i])
    del bubble_id[i]
def cleanup_bubbles():
    for i in range(len(bubble_id)-1,-1,-1):
        x,y = get_coords(bubble_id[i])
        if x<GAP:
            delete_bubbles(i)
 
from math import sqrt
 
 
def distance(id1,id2):
    x1,y1 = get_coords(id1)
    x2,y2 = get_coords(id2)
    return sqrt((x2-x1)**2 +(y2-y1)**2)
 
canvas.create_text(50,30,text="TIME",fill='WHITE')
canvas.create_text(150,30,text="SCORE",fill='WHITE')
time_text = canvas.create_text(50,50,fill='WHITE')
score_text = canvas.create_text(30,50,fill='WHITE')
 
def show_score(score):
    canvas.itemconfig(score_text,text= str(score))
 
def show_time(time):
    canvas.itemconfig(score_text,text= str(time))
 
def collision():
    points = 0
    for bubble in range(len(bubble_id)-1,-1,-1):
        if distance(ship_id2,bubble_id[bubble]) < (SHIP_R + bubble_r[bubble]):
            points += (bubble_r[bubble] + bubble_SPEED[bubble])
            delete_bubbles(bubble)
    return points
 
from time import sleep, time
 
Bubble_chance = 10
Time_limit  = 30
bonus_score = 1000
score = 0
bonus = 0
end = time() + Time_limit
while time () < end:
    if randint(1,Bubble_chance) == 1:
        create_bubbles()
    move_bubble()
    cleanup_bubbles()
    score += collision()
    if (int(score / bonus_score)) > bonus:
        bonus += 1
        end +=Time_limit
    show_score(int(score))
    show_time(int(end - time()))
    window.update()#
    sleep(0.01)
 
canvas.create_text(MID_X,MID_Y,
                text= "score" + str(score), fill= 'WHITE')
canvas.create_text(MID_X,MID_Y +45,
                text='Bonus time: ' + str(bonus+Time_limit),fill='WHITE')