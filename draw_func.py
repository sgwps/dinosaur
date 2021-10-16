import pygame
pygame.init()
window_size = width, height = 900, 900
run = True
while run:
    screen = pygame.display.set_mode(window_size)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print(9)
    pygame.display.flip()
    pygame.time.delay(10)