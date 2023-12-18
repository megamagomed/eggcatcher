import pygame, sys
from pygame.locals import QUIT, K_SPACE, K_LEFT, K_RIGHT
import math
from random import randint
pygame.init()
FPS = 60
Frames = pygame.time.Clock()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
pygame.display.set_caption('Eggcatcher')
screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DARK = (87, 87, 81)
BLUE = (0, 0, 255)

font = pygame.font.SysFont(None, 50)
img = font.render('КОНЕЦ', True, BLUE)



class Thing():
    def __init__(self, x, y, direction, lives_and_score, stick_direction):
        self.lives_and_score = lives_and_score
        self.radius = 10
        self.color = (255, 0, 0)
        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y
        self.start_direction = direction
        self.direction = direction
        self.gipotenuza = 0
        self.stick_direction = stick_direction
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
    
    def reset(self):
        self.x = self.start_x
        self.y = self.start_y
        self.direction = change_gr(self.stick_direction)
        self.gipotenuza = 0
        if len(self.lives_and_score.lives_collection) == 0:

            screen_surface.blit(img, (300,200))

    def update(self):
        if (self.y>=390 and self.x < 300) or(self.y>=390 and self.x >300):
            if self.lives_and_score.lives_collection:
                self.lives_and_score.lives_collection.pop()
                
                self.reset()


        if self.gipotenuza <=200:
            self.gipotenuza = math.sqrt((self.x-self.start_x)**2 + (self.y-self.start_y)**2)
            self.x = self.x + math.sin(self.direction)
            self.y = self.y + math.cos(self.direction)
        else:
            self.x = self.x + math.sin(0)
            self.y = self.y + math.cos(0) + 0.6
            

class Stick():    
    def __init__(self, obj):
        self.x = obj.x
        self.y = obj.y
        self.obj = obj
        self.color = (255, 0, 0)
        self.radius = obj.radius
    def draw(self, surface):
        switch = 1
        x1 = self.x
        y1 = self.y + self.radius
        if x1 > 100:
            switch = -1
        x2 = math.sin(self.obj.direction)*200 + x1 - self.radius*switch##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        y2 = math.cos(self.obj.direction)*200 + y1
        pygame.draw.line(surface, self.color, (x1, y1), (x2,y2))

class Eggcatcher():
    def __init__(self, arg):
        self.eggs = arg
        self.image = pygame.image.load('avoska.png')
        self.rect = self.image.get_rect()
        self.rect.top = SCREEN_HEIGHT - self.rect.height
        self.rect.left = SCREEN_WIDTH/2
        self.friction = 0.2
        self.velocity = 0
    
    def update(self):
        self.rect.move_ip(self.velocity, 0)
        self.key_press()
        if self.velocity < 0:
            self.velocity += self.friction
        if self.velocity > 0:
            self.velocity -= self.friction
        if self.rect.left < 0 :
            self.velocity = 0
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.velocity = 0
            self.rect.right = SCREEN_WIDTH
        self.check_collision()

    def check_collision(self):
        distance = 0
        for egg in self.eggs:
            if egg.y + egg.radius*2 > self.rect.y:
                if egg.x + egg.radius*2 > self.rect.x and egg.x < self.rect.x + self.rect.width:
                    egg.reset() 
            


    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
    def key_press(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.velocity = -3
        if pressed_keys[K_RIGHT]:
            self.velocity = 3


class Lives_and_score():
    def __init__(self, lives):
        # self.eggs = arg
        self.image = pygame.image.load('cheaken_heart.png')
        self.rect = self.image.get_rect()
        self.rect.top = 10
        self.rect.left = 10
        self.lives = lives
        self.lives_collection = []
        for i in range(lives):
            data = {
                'image': pygame.image.load('cheaken_heart.png'),
                'rect': self.image.get_rect(),
                'top': 10,
                'left': 10 + self.rect.width*i+10

            }
            self.lives_collection.append(data)
    def draw(self, surface):
        for live in self.lives_collection:
            rect = live['rect']
            rect.top  = live['top']
            rect.left = live['left']
            surface.blit(live['image'], rect) 






def change_gr(arg):
    if arg == 'left':
        return randint(30,85) *(3.14/180)
    if arg == 'right':
        return randint(275,330) *(3.14/180)

def change_stick_start_y():
        return randint(50,150)

lives_and_score = Lives_and_score(3)
thing = Thing(50,change_stick_start_y(), change_gr("left"), lives_and_score, 'left')
thing2 = Thing(550,change_stick_start_y(),change_gr("right"), lives_and_score, 'right')
thing_collection = [thing]
stick = Stick(thing)
stick2 = Stick(thing2)
eggcatcher = Eggcatcher(thing_collection)





while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # update
   
    # render
    screen_surface.fill(DARK)
    thing.update()    
    thing.draw(screen_surface)

    thing2.update()    
    thing2.draw(screen_surface)
    
    stick.draw(screen_surface)
    stick2.draw(screen_surface)

    eggcatcher.update()
    eggcatcher.draw(screen_surface)

    lives_and_score.draw(screen_surface)
    
    

    pygame.display.update()
    Frames.tick(FPS)