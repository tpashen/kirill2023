#створи гру "Лабіринт"!
# підключення бібліотеки
from pygame import *

# класи
# для всіх спрайтів
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
# клас головного персонажа
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 650:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed
# клас ворога 
class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= 600:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
# клас стіна
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height       
        self.image = Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))      
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y 
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
# створення вікна програми
window = display.set_mode((1280,720))
# заголовок вікна
display.set_caption("Лабіринт")
# змінна фону
background = transform.scale(image.load("fon.jpg"),(1280,720))

# змінна ігорового циклу
game = True
clock = time.Clock()
FPS = 60
finish = False
# текст написів 
font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

#музика
mixer.init()
#mixer.music.load('jungles.ogg')
#mixer.music.play()

#money = mixer.Sound('money.ogg')
#kick = mixer.Sound('kick.ogg')

# cтворення спрайтів
player = Player('hero.png',10,400,5)
monster = Enemy('cyborg.png',350,250,5)
final=GameSprite("treasure.png",1100,600,0)
#  створення стін
w1 = Wall(28,27,65, 0, 44 , 45, 625)
w2 = Wall(28,27,65, 0, 0, 1280, 45)
w3 = Wall(28,27,65, 1250, 0 , 45, 720)
w4 = Wall(28,27,65, 0, 680, 1280, 45)
w5 = Wall(28,27,65, 170, 150, 45, 540)
w6 = Wall(28,27,65, 200, 265, 175, 45)
w7 = Wall(28,27,65, 380, 150, 45, 380)
w8 = Wall(28,27,65, 530, 135, 80, 45)
w9 = Wall(28,27,65, 550, 475, 45, 215)
w10 = Wall(28,27,65, 680, 0, 45, 255)
w11 = Wall(28,27,65, 845, 280, 45, 225)
w12 = Wall(28,27,65, 1145, 280, 45, 225)
w13 = Wall(28,27,65, 845, 500, 175, 45)
w14 = Wall(28,27,65, 900, 175, 175, 45)
# ігорвий цикл
while game:
    # подія закриття вікна
    for e in event.get():
       if e.type == QUIT:
           game = False
    if finish!=True:
        # фон
        window.blit(background,(0, 0))
        player.reset()
        player.update()
        monster.reset()
        monster.update()
        final.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w11.draw_wall()
        w12.draw_wall()
        w13.draw_wall()
        w14.draw_wall()
        
        # зіткнення зі стінами
        if  (sprite.collide_rect(player, w1) 
            or sprite.collide_rect(player, w2) 
            or sprite.collide_rect(player, w2)
            or sprite.collide_rect(player, w3)
            or sprite.collide_rect(player, w4)
            or sprite.collide_rect(player, w5)
            or sprite.collide_rect(player, w6)
            or sprite.collide_rect(player, w7)
            or sprite.collide_rect(player, w8)
            or sprite.collide_rect(player, w9)
            or sprite.collide_rect(player, w10)
            or sprite.collide_rect(player, w11)
            or sprite.collide_rect(player, w12)
            or sprite.collide_rect(player, w13)
            or sprite.collide_rect(player, w14)):
                
                player.rect.x=50
                player.rect.y=400 

        #Ситуація "Програш"
        if sprite.collide_rect(player, monster):
            window.blit(lose, (200, 200))
            player.rect.x=50
            player.rect.y=400 
            
            finish = True 

        #Ситуація "Виграш"
        if sprite.collide_rect(player, final):      
            window.blit(win, (200, 200))
            
            player.rect.x=50
            player.rect.y=400 
            finish = True  
    display.update()
    clock.tick(FPS)



