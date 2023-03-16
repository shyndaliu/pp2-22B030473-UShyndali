import pygame as pg
from sys import exit

#CONSTANTS
WIDTH, HEIGHT = 800, 600
        

pg.init()
screen=pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("paint 2.0")
clock=pg.time.Clock()

class BUTTONF:
    def __init__(self, iconname, posx, posy):
        self.iconname=iconname
        self.icon=pg.image.load(iconname)
        self.posx=posx
        self.posy=posy
        self.rect = self.icon.get_rect(center=(self.posx, self.posy))
    def draw(self):
        screen.blit(self.icon, self.rect)
    def clicked(self, pos):
        x,y=pos
        if not (x>=0 and x<=100):
            return False
        if not (y>= self.rect.centery-50 and y<=self.rect.centery+50):
            return False
        return True
    
class BUTTONC:
    def __init__(self, iconname, posx, posy):
        self.iconname=iconname
        self.icon=pg.image.load(iconname)
        self.posx=posx
        self.posy=posy
        self.rect = self.icon.get_rect(center=(self.posx, self.posy))
    def draw(self):
        screen.blit(self.icon, self.rect)
    def clicked(self, pos):
        x,y=pos
        if not (x>=700 and x<=800):
            return False
        if not (y>=self.rect.centery-50 and y<=self.rect.centery+50):
            return False
        return True


buttonsf=[]
for i in range(0,6):
    name="icon"+str(i)+".png"
    j=50
    k=50+100*i
    buttonsf.append(BUTTONF(name,j,k ))

buttonsc=[]
for i in range(0,6):
    name="color"+str(i)+".png"
    j=750
    k=50+100*i
    buttonsc.append(BUTTONC(name,j,k ))

mode=False
figure="icon1"
curcolor="color5"
size=50

brush=pg.image.load(figure+curcolor+".png")

screen.fill((255,255,255))
for button in buttonsf:
    button.draw()
for button in buttonsc:
    button.draw()
pg.display.update()


while True:
    x,y=pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_DOWN:
                if size>=20:
                    size-=10
            if event.key==pg.K_UP:
                if size<=90:
                    size+=10
        if event.type==pg.MOUSEBUTTONDOWN:
            mode=True
        if event.type==pg.MOUSEBUTTONUP:
            mode=False

    if mode:
        for button in buttonsf:
            if not button.clicked((x,y)):
                continue
            figure=button.iconname[:-4]
            break
        for button in buttonsc:
            if not button.clicked((x,y)):
                continue
            curcolor=button.iconname[:-4]
            break
        brush=pg.image.load(figure+curcolor+".png")
        if (x-size//2>=100 and x+size//2<=700):
            brush=pg.transform.scale(brush, (size,size))
            screen.blit(brush, (x-size//2, y-size//2))
            pg.display.update()

    clock.tick(60)


