import pygame
import random
import math
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

pygame.mouse.set_visible(False)

score=0
scoremsg = "Score:" + str(0)
fail=False

def gameover(message):
    text = gameoverfont.render(message , True, (255,0,0))
    screen.blit(text, (screen.get_width()/2 - 100, screen.get_height()/2 -20))
    pygame.display.update()

class Pad(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([38, 8])
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = (screen.get_width()-self.image.get_width())/2
        self.rect.y = screen.get_height()-30-self.image.get_height()

    def update(self):
        self.rect.x = pygame.mouse.get_pos()[0]
        if self.rect.x + self.image.get_width() > screen.get_width():
            self.rect.x = screen.get_width() - self.image.get_width()

class Ball(pygame.sprite.Sprite):
    def __init__(self, speed, r, color):
        super().__init__()

        self.image = pygame.Surface([r*2, r*2])
        self.image.fill((255, 255, 255))
        self.image.set_colorkey((255, 255, 255))
        pygame.draw.circle(
            self.image, color, (r, r), r, 0)
        self.rect = self.image.get_rect()
        (self.rect.x, self.rect.y) = (pad.rect.x+pad.rect.width/2-r, pad.rect.top-2*r)
        self.direction = random.randint(20, 70)
        self.speed = speed

    def update(self):
        self.radian = math.radians(self.direction)
        self.dx = self.speed * math.cos(self.radian)
        self.dy = -self.speed * math.sin(self.radian)
        self.rect.move_ip(self.dx, self.dy)
        global fail

        if self.rect.left <= 0 or self.rect.right >= (screen.get_width()- 8):
            self.side_edge()
        if self.rect.top <= 10:
            self.rect.top = 10
            self.top_edge()
        if self.rect.bottom >= screen.get_height() - 30:
            fail = True
        else:
            fail = False

    def top_edge(self):
        self.direction = 360 - self.direction

    def side_edge(self):
        self.direction = 360 - self.direction + 180
        

allsprite = pygame.sprite.Group()
bricks = pygame.sprite.Group()

pad = Pad()
allsprite.add(pad)

ball = Ball(5, 8, (255, 0, 0))
allsprite.add(ball)

pygame.init()
score = 0
scorefont = pygame.font.SysFont("Arial",20)
gameoverfont = pygame.font.SysFont("Arial",32)

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
    if not fail:
        pad.update()
        ball.update()

        if fail:
            gameover('GAME OVER')
            break

        hitpad = pygame.sprite.collide_rect(ball,pad)
        if hitpad:
            ball.top_edge()

        hitbrick = pygame.sprite.spritecollide(ball,bricks,True)
        if len(hitbrick):
            score += len(hitbrick)
            scoremsg = "Score:" + str(score)
            ball.rect.y += 8
            ball.top_edge()


    screen.blit(background, (0, 0))

    message = scorefont.render(scoremsg,True,(255,0,255))
    screen.blit(message,(screen.get_width()/2 -30,screen.get_height()-30))
    allsprite.draw(screen)
    pygame.display.update()
