import pygame as pg
from pygame import mixer as mix
from sys import exit
import random, time

pg.init()
mix.init()
clock=pg.time.Clock()

#CONSTANTS
SCR_W=400
SCR_H=600
ENEMYSPEED=3
CAPYSPEED=5
SCORECOINS=0
SCORE=0
CAPYMODE=False

f1 = pg.font.Font('Minecraft.ttf', 20)
f2 = pg.font.Font('Minecraft.ttf', 36)

screen=pg.display.set_mode((SCR_W, SCR_H))
pg.display.set_caption("capybara racer")

icon=pg.image.load("iconn.png")

pg.display.set_icon(icon)
mix.music.load("themesong.mp3")
mix.music.set_volume(0.2)
mix.music.play(-1)

bg=pg.image.load("background.png")
bg1=pg.image.load("backgrounddead.png")


deadscreen=False


class Enemy(pg.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pg.image.load("enemy1.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCR_W-40),0) 
 
      def move(self):
        self.rect.move_ip(0,ENEMYSPEED)
        if (self.rect.bottom > 650):
            global SCORE
            SCORE+=5
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
      def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pg.image.load("capidef.png")
        self.imagecool=pg.image.load("capihapi.png")
        self.imagefail=pg.image.load("capidead.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    def move(self):
        pressed_keys = pg.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[pg.K_LEFT]:
                  self.rect.move_ip(-1*(CAPYSPEED+SCORECOINS//10), 0)
        if self.rect.right < SCR_W:        
              if pressed_keys[pg.K_RIGHT]:
                  self.rect.move_ip(CAPYSPEED+SCORECOINS//10, 0)
    def draw(self, surface):
        if CAPYMODE:
            surface.blit(self.imagecool, self.rect)
        else:
            surface.blit(self.image, self.rect)  

CAPY=Player()

class Coins(pg.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pg.image.load("orange.png")
        self.rect = self.image.get_rect()
        mylist1=[*range(20, max(CAPY.rect.center[0]-50,20))]
        mylist2=[*range(min(CAPY.rect.center[0]+50, SCR_W-20), SCR_W-20)]
        mylist1.extend(mylist2)
        self.rect.center=(int(random.choice(mylist1)),525) 
    def update(self):
        mylist1=[*range(20, max(CAPY.rect.center[0]-50,20))]
        mylist2=[*range(min(CAPY.rect.center[0]+50, SCR_W-20), SCR_W-20)]
        mylist1.extend(mylist2)
        self.rect.center=(int(random.choice(mylist1)),525)
    def draw(self, surface):
        surface.blit(self.image, self.rect)  
 


E1=Enemy()
ORANGE=Coins()

enemies = pg.sprite.Group()
enemies.add(E1)

regards=pg.sprite.Group()
regards.add(ORANGE)

all_sprites = pg.sprite.Group()
all_sprites.add(CAPY)
all_sprites.add(E1)

#Adding a new User event 
INC_SPEED = pg.USEREVENT + 1
pg.time.set_timer(INC_SPEED, 10000)

while True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()
        if event.type==INC_SPEED:
            ENEMYSPEED+=1
    text1 = f1.render("x{}".format(str(SCORE)),False,(255, 255, 255))
    text2 = f1.render("x{}".format(str(SCORECOINS)),False,(255, 255, 255))
    if deadscreen:
        screen.blit(bg1,(0,0))
        tex1=f2.render("TOTAL SCORE:{}".format(str(SCORE)),True,(255, 255, 255))
        rect=tex1.get_rect()
        rect.center=(200,480)
        tex2=f2.render("ORANGE:{}".format(str(SCORECOINS)),True,(255, 255, 255))
        rect2=tex2.get_rect()
        rect2.center=(200,530)
        screen.blit(tex1, rect)
        screen.blit(tex2,rect2)
    else:
        screen.blit(bg, (0,0))
        screen.blit(ORANGE.image, ORANGE.rect)
        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)
            entity.move()
        screen.blit(text1, (7,35))
        screen.blit(icon, (3,3))
        screen.blit(text2, (38,7))

    if pg.sprite.spritecollideany(CAPY, regards):
          ORANGE.update()
          SCORECOINS+=1
          CAPYMODE=1
 
    #To be run if collision occurs between Player and Enemy
    if pg.sprite.spritecollideany(CAPY, enemies):
          pg.display.update()
          mix.music.stop()
          mix.music.load("deadfile.mp3")
          mix.music.set_volume(0.3)
          mix.music.play(-1)
          for entity in all_sprites:
                entity.kill() 
          deadscreen=True

    
    pg.display.update()
    clock.tick(60)