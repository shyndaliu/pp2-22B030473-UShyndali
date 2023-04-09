import pygame as pg
import psycopg2 as pgsql
from sys import exit
import random
import time
from pygame.math import Vector2 as vt

connection=pgsql.connect(host="localhost", dbname="postgres", user="postgres",
                         password="12345", port=5432)
cur=connection.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS snakegame (
    username VARCHAR(255),
    user_score INT,
    user_level INT
);
""")

#CONSTANTS
cell_s=int(40)
speed=200
#------------

pg.init()
screen=pg.display.set_mode((cell_s*20,cell_s*20))
pg.display.set_caption("shashlyk snake")
clock=pg.time.Clock()
shashlyk=pg.image.load("shashlyk.png").convert_alpha()
qazy=pg.image.load("qazy.png").convert_alpha()
bg=pg.image.load("bg.png").convert_alpha()
bgdead=pg.image.load("bgdead.png").convert_alpha()
icon=pg.image.load("icon.png").convert_alpha()
pg.display.set_icon(icon)
game_font = pg.font.Font('Minecraft.ttf', 25)

qazymode=1
welcomescreen=True
timer=0
CNTSHASHLYK=0
CNTQAZY=0

listofx=list(range(0,19))
listofy=list(range(0,19))


#CLASSES
class FRUIT:
    def __init__(self):
        self.newpos()
    def draw_f(self):
        fruit_rect=pg.Rect(self.pos.x*cell_s, self.pos.y*cell_s, cell_s, cell_s)
        if qazymode==0:
            screen.blit(qazy,fruit_rect)
        else:
            screen.blit(shashlyk,fruit_rect)
    def newpos(self):
        global qazymode
        qazymode =random.randint(0,5)
        self.x=random.choice(listofx)
        self.y=random.choice(listofy)
        self.pos=vt(self.x, self.y)

class SNAKE:
    def __init__(self):
        self.body=[vt(7,10), vt(6,10), vt(5,10)]
        self.dirc=vt(1,0)
        self.add_block=False
        self.head_up = pg.image.load('head_up.png').convert_alpha()
        self.head_down = pg.image.load('head_down.png').convert_alpha()
        self.head_right = pg.image.load('head_right.png').convert_alpha()
        self.head_left = pg.image.load('head_left.png').convert_alpha()
		
        self.tail_up = pg.image.load('tail_up.png').convert_alpha()
        self.tail_down = pg.image.load('tail_down.png').convert_alpha()
        self.tail_right = pg.image.load('tail_right.png').convert_alpha()
        self.tail_left = pg.image.load('tail_left.png').convert_alpha()

        self.body_vertical = pg.image.load('body_vertical.png').convert_alpha()
        self.body_horizontal = pg.image.load('body_horizontal.png').convert_alpha()

        self.body_tr = pg.image.load('body_tr.png').convert_alpha()
        self.body_tl = pg.image.load('body_tl.png').convert_alpha()
        self.body_br = pg.image.load('body_br.png').convert_alpha()
        self.body_bl = pg.image.load('body_bl.png').convert_alpha()
        self.crunch_sound = pg.mixer.Sound('se_fruit.mp3')
    
    def draw_s(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index,block in enumerate(self.body):
            x_pos = int(block.x*cell_s)
            y_pos = int(block.y*cell_s)
            block_rect = pg.Rect(x_pos,y_pos,cell_s,cell_s)
            
            if index == 0:
                screen.blit(self.head,block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail,block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                     screen.blit(self.body_vertical,block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal,block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl,block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl,block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr,block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br,block_rect)
    
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == vt(1,0): self.head = self.head_left
        elif head_relation == vt(-1,0): self.head = self.head_right
        elif head_relation == vt(0,1): self.head = self.head_up
        elif head_relation == vt(0,-1): self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == vt(1,0): self.tail = self.tail_left
        elif tail_relation == vt(-1,0): self.tail = self.tail_right
        elif tail_relation == vt(0,1): self.tail = self.tail_up
        elif tail_relation == vt(0,-1): self.tail = self.tail_down
        
    def move_s(self):
        if self.add_block:
            body2=self.body[:]
            body2.insert(0, body2[0]+self.dirc)
            self.body=body2
            self.add_block=False
        else:
            body2=self.body[:-1]
            body2.insert(0, body2[0]+self.dirc)
            self.body=body2
        
    def newblock(self):
        self.add_block=True

    def play_crunch_sound(self):
        self.crunch_sound.play()
                
    def reset(self):
        self.body = [vt(5,10),vt(4,10),vt(3,10)]
        self.direction = vt(0,0)


class MAIN:
    def __init__(self):
        self.snake=SNAKE()
        self.fruit=FRUIT()
        self.dead=False
        self.dead_sound = pg.mixer.Sound('se_dead.mp3')

    def upd(self):
        self.snake.move_s()
        self.check()
        self.check_death()
        listofx=list(range(0,19))
        listofy=list(range(0,19))
        for i in self.snake.body:
            if i.x in listofx:
                listofx.remove(i.x)
            if i.y in listofy:
                listofy.remove(i.y)


    
    def play_dead_sound(self):
        self.dead_sound.play()

    def draw_all(self):
        if welcomescreen:
            screen.blit(bg,(0,0))
        elif not self.dead:
            screen.blit(bg,(0,0))
            self.fruit.draw_f()
            self.snake.draw_s()
            self.draw_score()
        else:
            screen.blit(bgdead,(0,0))
            text = "SCORE:"+str(CNTSHASHLYK+CNTQAZY*5)
            surface = game_font.render(text,True,(255,255,255))
            score_rect = surface.get_rect(center = (10*cell_s,15*cell_s))
            text2 = "LEVEL:"+str(1+(CNTSHASHLYK+CNTQAZY)//10)
            surface2 = game_font.render(text2,True,(255,255,255))
            score_rect2 = surface2.get_rect(center = (10*cell_s,16*cell_s))
            screen.blit(surface,score_rect)
            screen.blit(surface2,score_rect2)


    def check(self):
        if self.fruit.pos==self.snake.body[0]:
            if qazymode==0:
                global CNTQAZY
                CNTQAZY+=1
            else:
                global CNTSHASHLYK
                CNTSHASHLYK+=1
            self.fruit.newpos()
            self.snake.newblock()
            self.snake.play_crunch_sound()
    def check_death(self):
        if not 0<=self.snake.body[0].x<=19 or not 0<=self.snake.body[0].y<=19:
            self.endthegame()
        for block in self.snake.body[1:]:
            if block.x==self.snake.body[0].x and block.y==self.snake.body[0].y:
                self.endthegame() 

    def endthegame(self):
        self.play_dead_sound()
        self.dead=True
        update(user)
    		
    def draw_score(self):
        level_text="Your level is: "+str(1+(CNTSHASHLYK+CNTQAZY)//10)
        level_surface=game_font.render(level_text,True,(0,0,0))
        level_rect = level_surface.get_rect(center = (10*cell_s,20))

        score_text = str(CNTSHASHLYK+CNTQAZY*5)
        score_surface = game_font.render(score_text,True,(0,0,0))
        score_x = int(cell_s * 20 - 60)
        score_y = int(cell_s * 20 - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = shashlyk.get_rect(midright = (score_rect.left,score_rect.centery))
        bg_rect = pg.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 6,apple_rect.height)
        pg.draw.rect(screen,(255,255,255),bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(shashlyk,apple_rect)
        screen.blit(level_surface,level_rect)
        pg.draw.rect(screen,(0,0,0),bg_rect,2)



#-----------------------------------


def insert(newuser):
    cur.execute("""INSERT INTO snakegame VALUES ('{}',0,0)""".format(newuser))

def update(curuser):
    cur.execute("SELECT * FROM snakegame WHERE username='{}'".format(curuser))
    data=cur.fetchone()
    cur.execute("""UPDATE snakegame
    SET user_score={}, user_level={}
    WHERE username='{}'
    """.format(max(data[1],CNTSHASHLYK+CNTQAZY*5),max(data[2],1+(CNTSHASHLYK+CNTQAZY)//10),curuser))
    connection.commit()


print("Enter your username:")
user=input()
cur.execute("SELECT count(*) FROM snakegame WHERE username='{}'".format(user))
if cur.fetchone()[0]==0:
    insert(user)
    connection.commit()
else:
    cur.execute("SELECT * FROM snakegame WHERE username='{}'".format(user))
    data=cur.fetchone()
    print("User's max score:{}".format(data[1]))
    print("User's max level:{}".format(data[2]))
welcomescreen=False

print("game will start in:")

for i in range(1,4):
    print(i)
    time.sleep(1)
print("go!")


SCREEN_UPDATE=pg.USEREVENT
pg.time.set_timer(SCREEN_UPDATE, speed)


main=MAIN()

while(True):
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            connection.commit()
            cur.close()
            connection.close()
            exit()
        if event.type==SCREEN_UPDATE and main.dead==False and welcomescreen==False:
            main.upd()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_UP:
                if main.snake.dirc.y!=1:
                    main.snake.dirc=vt(0, -1)
            if event.key==pg.K_DOWN:
                if main.snake.dirc.y!=-1:
                    main.snake.dirc=vt(0, 1)
            if event.key==pg.K_LEFT:
                if main.snake.dirc.x!=1:
                    main.snake.dirc=vt(-1, 0)
            if event.key==pg.K_RIGHT:
                if main.snake.dirc.x!=-1:
                    main.snake.dirc=vt(1, 0)
            if event.key==pg.K_SPACE:
                update(user)

    if qazymode==0:
        timer+=1
    if qazymode==0 and timer>=500:
        qazymode=random.randint(1,5)
        timer=0
            
    speed=200-((len(main.snake.body) - 3)//10)*5
    screen.fill((25,24,56))
    main.draw_all()
    pg.display.update()
    clock.tick(60)
