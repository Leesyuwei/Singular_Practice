import pygame
pygame.init()
screen = pygame.display.set_mode((640, 320))  # set screen size
pygame.display.set_caption('screen')  # set screen name


background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((65, 65, 210))

clock = pygame.time.Clock()
FPS = 60

while 1:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # quit screen

    screen.blit(background, (0, 0))
    pygame.display.update()
