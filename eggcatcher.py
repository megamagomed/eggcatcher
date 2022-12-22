import pygame, sys
from pygame.locals import QUIT
import math
pygame.init()
FPS = 60
Frames = pygame.time.Clock()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
pygame.display.set_caption('Eggcatcher')
screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DARK = (87, 87, 81)

class Thing():
    def __init__(self, x, y, direction):
        self.radius = 10
        self.color = (255, 0, 0)
        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y
        self.start_direction = direction
        self.direction = direction
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def update(self):
        if (self.y>=390 and self.x < 300) or(self.y>=390 and self.x >300):
            self.x = self.start_x
            self.y = self.start_y
            self.direction = self.start_direction

        if self.x < 200 or self.x>400 :
            self.x = self.x + math.sin(self.direction)
            self.y = self.y + math.cos(self.direction)
        else:
            self.x = self.x + math.sin(0)
            self.y = self.y + math.cos(0)

class Stick():    
    def __init__(self, obj):
        self.x = obj.x
        self.y = obj.y
        self.angle = obj.direction
        self.color = (255, 0, 0)
        self.radius = obj.radius
    def draw(self, surface):

        pygame.draw.line(surface, self.color, (self.x, self.y+self.radius), (190, ((140)/math.sin(self.angle))+self.y-10))


def change_gr(arg):
    return arg*(3.14/180)


thing = Thing(50,100, 3.14/3)
thing2 = Thing(550,50,5*3.14/3)
stick = Stick(thing)
# stick2 = Stick(thing2)




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
    # stick2.draw(screen_surface)
    pygame.display.update()
    Frames.tick(FPS)