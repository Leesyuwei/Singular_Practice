import pygame
pygame.init()
screen = pygame.display.set_mode((640, 320))  # set screen size
pygame.display.set_caption('screen')  # set screen name


background = pygame.Surface((32, 32))
background = background.convert()
background.fill((255, 255, 255))

item1 = pygame.Rect((0, 0), (32, 32))

clock = pygame.time.Clock()
FPS = 30

while 1:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # quit screen
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                item1.move_ip(0, -32)
            if event.key == pygame.K_a:
                item1.move_ip(-32, 0)
            if event.key == pygame.K_s:
                item1.move_ip(0, 32)
            if event.key == pygame.K_d:
                item1.move_ip(32, 0)

        if item1.left < 0:
            item1.move_ip(32, 0)
        if item1.right >= screen.get_width():
            item1.move_ip(-32, 0)
        if item1.top < 0:
            item1.move_ip(0, 32)
        if item1.bottom >= screen.get_height():
            item1.move_ip(0, -32)

    screen.fill((0, 0, 0))

    screen.blit(background, item1)
    pygame.display.update()
