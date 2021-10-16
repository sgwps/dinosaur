import pygame
import json

import Level_screen
import Level_screen_2
import dinosaur
from object_static import Object
from draw_func_2 import draw


if __name__ == "__main__":
    pygame.init()
    window_size = width, height = 1080, 720
    d = dinosaur.Dinosaur()
    run = True
    timer = 0
    lev = 0
    L = Level_screen_2.Level()
    font = pygame.font.SysFont('Comic Sans MS', 30)
    pygame.display.set_caption('dinosaur')

    while run:
        print(d.x, d.y)
        screen = pygame.display.set_mode(window_size)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and lev in (1, 2):
                if event.key == pygame.K_UP:
                    d.jump()
            if event.type == pygame.KEYDOWN and lev == 0:
                lev += 1
        if lev == 0:
            text = font.render('Press any button to start the game', True, (255, 255, 255), (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (540, 360)
            screen.blit(text, textRect)
        if lev == -1:
            text = font.render('You lost', True, (255, 255, 255), (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (540, 360)
            screen.blit(text, textRect)
        if lev in (1, 2):

            if lev == 1:
                screen = L.draw_1(screen)
            elif lev == 2:
                screen = L.draw_2(screen)
            d.move(timer)

            if d.y > 250 and (d.y > 700 or not L.check_back_colors(screen, (d.x, d.y)) or not L.check_back_colors(screen, (min(d.x + 10, 1079), d.y)) or not L.check_back_colors(screen, (d.x, max(d.y - 10, 0)))):
                lev = -1
            if d.x >= 1070:
                lev += 1
                d.x = 0
                d.y = 300
            timer += 1
            screen = d.draw(screen)
        if lev == 3:
            with open("final_screen.json") as f:
                screen = draw(json.load(f), screen)
        pygame.display .flip()
        pygame.time.delay(10)