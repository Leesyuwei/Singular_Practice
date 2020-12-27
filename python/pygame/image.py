import pygame
pygame.init()
screen = pygame.display.set_mode((640, 320))  # set screen size
pygame.display.set_caption('screen')  # set screen name
screenWidth, screenHeight = screen.get_size()


image = pygame.image.load('./image/grapefruit-slice-332-332.jpg')
image = image.convert()
image = pygame.transform.smoothscale(image, (screenWidth, screenHeight))
screen.blit(image, (0, 0))
pygame.display.update()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # quit screen
