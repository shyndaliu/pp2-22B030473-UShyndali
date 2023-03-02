from pygame import mixer as mix
import pygame as pg
import os
from sys import exit
from tkinter import *
from tkinter import filedialog

Playlist=[]

allsongs = os.listdir(r"U:\всё\учеба\2022-2023\pp2\pp2-22B030473-UShyndali\lab7\musicplayer")
for song in allsongs:
       if song.endswith(".mp3"):
           Playlist.append(song)

pg.init()
mix.init()
clock=pg.time.Clock()

screen=pg.display.set_mode((500, 250))
pg.display.set_caption("music player")

icon=pg.image.load("iconn.png")
pg.display.set_icon(icon)

bg=pg.Surface((500,500))
pg.Surface.fill(bg,(241,203,255))
f1=pg.font.SysFont('calibri', 20, True)
f2=pg.font.SysFont('calibri', 15)



btnplay=pg.image.load("playbutton.png")
btnpause=pg.image.load("pausebutton.png")


btnnext=pg.image.load("nextbutton1.png")
btnnext2=pg.image.load("nextbutton2.png")


btnprev=pg.image.load("prevbutton.png")
btnprev2=pg.image.load("prevbutton2.png")


currid=0
currsong=pg.mixer.music.load(Playlist[currid])
pg.mixer.music.play()
pg.mixer.music.pause()
ch=False
ch1=False
ch2=False
tm=0
tm2=0

while True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()
        elif event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE:
                if(ch):
                    pg.mixer.music.pause()
                    ch=0
                else:
                    pg.mixer.music.unpause()
                    ch=1
            if event.key==pg.K_RIGHT:
                currid=(currid+1)%3
                pg.mixer.music.stop()
                pg.mixer.music.load(Playlist[currid])
                pg.mixer.music.play()
                ch1=True
                if not ch :
                    pg.mixer.music.pause()
            if event.key==pg.K_LEFT:
                currid=(currid-1+3)%3
                pg.mixer.music.stop()
                pg.mixer.music.load(Playlist[currid])
                pg.mixer.music.play()
                ch2=True
                if not ch :
                    pg.mixer.music.pause()
                   


                  
    text1=f1.render("Currently playing:", True, (138,25,151))
    text2=f2.render(Playlist[currid], True, (99,20,108))        
    screen.blit(bg, (0,0))
    screen.blit(text1,(25,25))
    screen.blit(text2,(100,50))
    if ch:
        screen.blit(btnpause, (195,90))
    else:
        screen.blit(btnplay, (195,90))

    if ch1:
        screen.blit(btnnext2, (295,90))
        tm+=1
    else:
        screen.blit(btnnext, (295,90))

    if ch2:
        screen.blit(btnprev2, (95,90))
        tm2+=1
    else:
        screen.blit(btnprev, (95,90))

    if tm>=8:
        ch1=False
        tm=0
    if tm2>=8:
        ch2=False
        tm2=0
    pg.display.update()
    clock.tick(60)
