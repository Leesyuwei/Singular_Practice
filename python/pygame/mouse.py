import pygame
pygame.init()
screen = pygame.display.set_mode((640, 320))  # set screen size
pygame.display.set_caption('screen')  # set screen name

pygame.mouse.set_visible(False)

clock = pygame.time.Clock()
FPS = 60

while 1:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 

    screen.fill((255,255,255))

    pygame.draw.circle(screen,(0,0,0),pygame.mouse.get_pos(),10,0)
    pygame.display.update()