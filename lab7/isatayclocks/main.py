import pygame as pg
from sys import exit
import datetime
import sys

pg.init()
screen = pg.display.set_mode((500, 500))
pg.display.set_caption("ЧАСЫ ЧАСТЬ 5 ОНЛАЙН ВЗЛОМКА БЕСПЛАТНО ИГРАТЬ...")
clock=pg.time.Clock()

icon=pg.image.load("iconn.png")
pg.display.set_icon(icon)

bg=pg.image.load('base1.png')
sexyboy=pg.image.load('body2.png')

minhand=pg.image.load('minhand3.png')
minrec=minhand.get_rect()
minrec.center=(255,250)
mincnt=-5

sechand=pg.image.load('sechand4.png')
secrec=sechand.get_rect()
secrec.center=(270,250)
seccnt=-5

currt=datetime.datetime.now()

seccnt=currt.second
mincnt=currt.minute


while True:
        for event in pg.event.get():
                if event.type == pg.QUIT:
                        pg.quit()
                        exit()
        screen.blit(bg,(0,0))

        minhand1=pg.transform.rotate(minhand, -1*((6*mincnt)%360))
        minrec1=minhand1.get_rect()
        minrec1.center=minrec.center
        screen.blit(minhand1, minrec1)

        screen.blit(sexyboy,(0,0))

        sechand1=pg.transform.rotate(sechand, -1*((6*seccnt+180)%360))
        secrec1=sechand1.get_rect()
        secrec1.center=secrec.center
        screen.blit(sechand1, secrec1)

        currt=datetime.datetime.now()
        seccnt=currt.second
        mincnt=currt.minute


        pg.display.update()
        clock.tick(60)
        