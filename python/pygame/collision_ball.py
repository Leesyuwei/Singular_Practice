import pygame
import random
pygame.init()
screen = pygame.display.set_mode((640, 320))  # set screen size
pygame.display.set_caption('screen')  # set screen name

clock = pygame.time.Clock()
FPS = 60

class Block(pygame.sprite.Sprite):
    def __init__(self,color,width,hieght):
        super().__init__()
        
        self.image = pygame.Surface([width,hieght])
        self.image.fill(color)
        self.image.set_colorkey(color)

        self.rect = self.image.get_rect()

block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

score = 0

pygame.mouse.set_visible(False)

for i in range(1000):
    block = Block((255,255,255),15,15)
    pygame.draw.circle(block.image,(0,0,0),(7.5,7.5),7.5,0)

    block.rect.center = (random.randrange(0,screen.get_width(),16),random.randrange(0,screen.get_height(),16))

    block_list.add(block)
    all_sprites_list.add(block)

player = Block((255,255,255),15,15)
pygame.draw.circle(player.image,(255,0,0),(7.5,7.5),7.5,0)
all_sprites_list.add(player)

while 1:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 

    screen.fill((255,255,255))
    player.rect.center = (pygame.mouse.get_pos())


    blocks_hit_list = pygame.sprite.spritecollide(player,block_list,True)

    for block in blocks_hit_list:
        score += 1
        print(score)
    
    all_sprites_list.draw(screen)
        
    pygame.display.update()