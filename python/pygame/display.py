import pygame
pygame.init()
screen = pygame.display.set_mode((640, 320))  # set screen size
pygame.display.set_caption('screen')  # set screen name


background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((65, 65, 210))
screen.blit(background, (0, 0))
pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # quit screen
