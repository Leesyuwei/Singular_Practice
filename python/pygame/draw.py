import pygame
pygame.init()
screen = pygame.display.set_mode((640, 320))  # set screen size
pygame.display.set_caption('screen')  # set screen name


background = pygame.Surface(screen.get_size())
screenWidth, screenHeight = screen.get_size()
background = background.convert()
background.fill((65, 65, 210))
rectx = 250
recty = 50
pygame.draw.rect(background, (255, 255, 255), [
                 screenWidth//2-rectx//2, screenHeight//2-recty//2, rectx, recty], 0)

pygame.draw.circle(background, (0, 0, 0), (
    screenWidth//2, screenHeight//2), 100, 3)

ovalx = 100
ovaly = 300
pygame.draw.ellipse(background, (0, 255, 0), [
    screenWidth//2-ovalx//2, screenHeight//2-ovaly//2, ovalx, ovaly], 0)

arcx = 500
arcy = 200
pygame.draw.arc(background, (255, 0, 0), [
    screenWidth//2-arcx//2, screenHeight//2-arcy//2, arcx, arcy], 0, 3.14, 3)

lineStart = [100, 400]
lineEnd = [300, 100]
pygame.draw.rect(background, (255, 255, 0),
                 (lineStart[0], lineStart[1]), (lineEnd[0], lineEnd[1]), 3)


screen.blit(background, (0, 0))
pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # quit screen
