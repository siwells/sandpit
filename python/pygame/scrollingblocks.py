import pygame
import random
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
 
class Block(pygame.sprite.Sprite):
    """
    This class represents the ball
    It derives from the "Sprite" class in Pygame
    """
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        super(Block, self).__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()
 
    def reset_pos(self):
        """ Reset position to the top of the screen, at a random x location.
        Called by update() or the main program loop if there is a collision.
        """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, screen_width)
 
    def update(self):
        """ Called each frame. """
 
        self.rect.y += 1
 
        if self.rect.y > 410:
            self.reset_pos()
 
 
class Player(Block):
    """ The player class derives from Block, but overrides the 'update'
    functionality with new a movement function that will move the block
    with the mouse. """
    def update(self):
        pos = pygame.mouse.get_pos()
 
        self.rect.x = pos[0]
        self.rect.y = pos[1]
 
pygame.init()
 
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
 
block_list = pygame.sprite.Group()
 
all_sprites_list = pygame.sprite.Group()
 
for i in range(50):
    block = Block(BLACK, 20, 15)
 
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
 
    block_list.add(block)
    all_sprites_list.add(block)
 
player = Player(RED, 20, 15)
all_sprites_list.add(player)
 
done = False
 
clock = pygame.time.Clock()
 
score = 0
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    screen.fill(WHITE)
 
    all_sprites_list.update()
 
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
 
    for block in blocks_hit_list:
        score += 1
        print(score)
 
        block.reset_pos()
 
    all_sprites_list.draw(screen)
 
    clock.tick(20)
 
    pygame.display.flip()
 
pygame.quit()
