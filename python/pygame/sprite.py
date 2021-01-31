import pygame
import random
pygame.init()
screen = pygame.display.set_mode((500, 480))  # set screen size
pygame.display.set_caption('sprite')  # set screen name

background = pygame.image.load('./game/bg.jpg')
clock = pygame.time.Clock()
FPS = 60

wave = 50

walkRight = [pygame.image.load('./game/R1.png'),
             pygame.image.load('./game/R2.png'),
             pygame.image.load('./game/R3.png'),
             pygame.image.load('./game/R4.png'),
             pygame.image.load('./game/R5.png'),
             pygame.image.load('./game/R6.png'),
             pygame.image.load('./game/R7.png'),
             pygame.image.load('./game/R8.png'),
             pygame.image.load('./game/R9.png')]
walkLeft = [pygame.image.load('./game/L1.png'),
            pygame.image.load('./game/L2.png'),
            pygame.image.load('./game/L3.png'),
            pygame.image.load('./game/L4.png'),
            pygame.image.load('./game/L5.png'),
            pygame.image.load('./game/L6.png'),
            pygame.image.load('./game/L7.png'),
            pygame.image.load('./game/L8.png'),
            pygame.image.load('./game/L9.png')]


class player(pygame.sprite.Sprite):
    def __init__(self, x, dx, y):
        super().__init__()
        self.walkCount = 0
        self.image = walkRight[self.walkCount//3]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.dx = dx
        self.y = y

    def draw(self):
        if self.walkCount+1 >= 27:
            self.walkCount = 0

        if self.x > screen.get_width() - wave or self.x < wave:
            self.dx *= -1

        if self.dx > 0:
            self.image = walkRight[self.walkCount//3]

        if self.dx < 0:
            self.image = walkLeft[self.walkCount//3]

        self.rect.center = (self.x, self.y)
        self.x += self.dx
        self.walkCount += 1

men=[player(random.randint(50,300),1,random.randint(200,400)),
    player(random.randint(50,300),-2,random.randint(200,400)),
    player(random.randint(50,300),1,random.randint(200,400))]

allMen = pygame.sprite.Group()

for man in men:
    allMen.add(man)

while 1:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # quit screen

    screen.blit(background, (0, 0))

    for man in men:
        man.draw()
        
    allMen.draw(screen)
    pygame.display.update()
