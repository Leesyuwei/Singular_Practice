import pygame
pygame.init()
screen = pygame.display.set_mode((640, 320))  # set screen size
pygame.display.set_caption('screen')  # set screen name

clock = pygame.time.Clock()
FPS = 60

moving = False

screen.fill((255,255,255))

pygame.draw.circle(screen,(0,0,0),((screen.get_width()/2),(screen.get_height()/2)),10,0)

while 1:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 

    pressed = pygame.mouse.get_pressed()
    if pressed[0]:
        moving = True
    elif pressed[2]:
        moving = False

    if moving == True:
        screen.fill((255,255,255))

        pygame.draw.circle(screen,(0,0,0),pygame.mouse.get_pos(),10,0)


    pygame.display.update()