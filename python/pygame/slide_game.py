import pygame
from pygame.sprite import groupcollide


class Brick(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()

        self.image = pygame.Surface([38, 13])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('screen')

allsprite = pygame.sprite.Group()
bricks = pygame.sprite.Group()

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))

for row in range(0, 6):
    for column in range(0, 15):
        if row == 1 or row == 0:
            brick = Brick((153, 205, 255), column*40+1,  row*15 + 1)
        if row == 2 or row == 3:
            brick = Brick((94, 175, 255), column*40+1, row*15 + 1)
        if row == 4 or row == 5:
            brick = Brick((52, 153, 207), column*40+1,  row*15 + 1)
        bricks.add(brick)
        allsprite.add(brick)

clock = pygame.time.Clock()
FPS = 60
while 1:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(background,(0,0))

    allsprite.draw(screen)
    pygame.display.update()
