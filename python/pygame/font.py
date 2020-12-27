import pygame
pygame.init()
screen = pygame.display.set_mode((640, 320))  # set screen size
pygame.display.set_caption('screen')  # set screen name
screenWidth, screenHeight = screen.get_size()


image = pygame.image.load('./image/grapefruit-slice-332-332.jpg')
image = image.convert()
image = pygame.transform.smoothscale(image, (screenWidth, screenHeight))

font = pygame.font.SysFont("comicssansms", 72)
text = font.render('Hello world', True, (0, 0, 255), (0, 255, 0))

screen.blit(image, (0, 0))
screen.blit(text, (170, 270))
pygame.display.update()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # quit screen
