import pygame
import random
 
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

alien_sprites = []

alien_sprites.append([
        [0,0,1,0,0,0,0,0,1,0,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,1,1,1,1,1,1,1,0,0],
        [0,1,1,0,1,1,1,0,1,1,0],
        [1,1,1,1,1,1,1,1,1,1,1],
        [1,0,1,1,1,1,1,1,1,0,1],
        [1,0,1,0,0,0,0,0,1,0,1],
        [0,0,0,1,1,0,1,1,0,0,0]
    ])

class Invader(pygame.sprite.Sprite):
    def __init__(self):
        super(Invader, self).__init__()
        width, height = len(alien_sprites[0][0]),len(alien_sprites[0])

        self.width=width
        self.height=height
        self.image = pygame.Surface([width, height])
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

        self.image.fill(WHITE)
        
        for y, line in enumerate(alien_sprites[0]):
            for x, pixel in enumerate(line):
                if pixel:
                    self.image.set_at((x,y), BLACK)
                print pixel,
            print "\n"

        # Position the sprite
        self.rect.x = 100
        self.rect.y = 100

        

pygame.init()

all_sprites = pygame.sprite.Group()
player = Invader()
all_sprites.add(player)


screen_width = 640
screen_height = 480
screen = pygame.display.set_mode([screen_width, screen_height])

running = True 
clock = pygame.time.Clock()
 
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x: 
                running=False
            if event.key==pygame.K_q: 
                running=False
            if event.key==pygame.K_ESCAPE: 
                running=False
            if event.key == pygame.K_SPACE:
                print("Game Paused")
                while True:
                    event = pygame.event.wait()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        print("Game Unpaused")
                        break
        elif event.type == pygame.KEYUP:
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")

    keys = pygame.key.get_pressed()
 
    screen.fill(WHITE)
 
    all_sprites.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
