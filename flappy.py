
import pygame, sys
from pygame.locals import QUIT, K_SPACE

pygame.init()

FPS = 160
Frames = pygame.time.Clock() 

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

DARK = (87, 87, 81)
TEAL = (244, 250, 156)

pygame.display.set_caption('Flappy Bird!')

screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('twitter.png')
        self.rect = self.image.get_rect()
        self.rect.top = SCREEN_HEIGHT / 2 - self.rect.size[0] / 2
        self.rect.left = 20
        self.velocity = 1
        self.gravity = 0.2

    def update(self):
        self.rect.move_ip(0, self.velocity)
        self.velocity += self.gravity
        self.key_press()

        if (self.rect.bottom >= SCREEN_HEIGHT):
            self.rect.bottom = SCREEN_HEIGHT
        if (self.rect.top <= 0):
            self.rect.top = 0

    def key_press(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_SPACE]:
            self.velocity = -3

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Pipe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 30
        self.height = 80
        self.rect = pygame.Rect((
            SCREEN_WIDTH-self.width, 
            0, 
            self.width, 
            self.height))

    def draw(self, surface):
        pygame.draw.rect(surface, TEAL, self.rect)
    
    def update(self):
        self.rect.move_ip(-1, 0)
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH

player = Bird()
pipe = Pipe()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # update
    player.update()
    pipe.update()
    # render
    screen_surface.fill(DARK)
    player.draw(screen_surface)
    pipe.draw(screen_surface)
    pygame.display.update()
    Frames.tick(FPS)