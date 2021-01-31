import pygame
import math
import random
pygame.init()
screen = pygame.display.set_mode((640, 320))  # set screen size
pygame.display.set_caption('screen')  # set screen name


background = pygame.Surface((32, 32))
background = background.convert()
background.fill((255, 255, 255))
image = pygame.image.load('image/logo-brand-dvd-symbol-dvdvideo .png')
image = image.convert_alpha()
image = pygame.transform.smoothscale(image, (64, 64))

item1 = pygame.Rect((0, 0), (32, 32))

clock = pygame.time.Clock()
FPS = 30

direction = random.randint(20, 70)
radian = math.radians(direction)
dx = 5 * math.cos(radian)
dy = -5 * math.sin(radian)

while 1:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()  # quit screen

    if item1.left < 0 or item1.right >= screen.get_width():
        dx *= -1
        background.fill((random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255)))
    if item1.top < 0 or item1.bottom >= screen.get_height():
        dy *= -1
        background.fill((random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255)))

    item1.move_ip(dx, dy)
    screen.fill((0, 0, 0))

    screen.blit(background, item1)
    pygame.display.update()
