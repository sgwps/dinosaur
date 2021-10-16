import os

import pygame
import json
import Level_screen_2

class Dinosaur:
    pos_x = 0
    pos_y = 300
    c = 6
    RUNNING = [pygame.image.load(os.path.join("Images/Dino", "DinoRun2.png")),
               pygame.image.load(os.path.join("Images/Dino", "DinoJump.png"))]

    def __init__(self):


        self.x = self.pos_x #Дублёры.
        self.y = self.pos_y

        # self.view = self.get_view()


    def draw(self, screen):
        if self.c < 10:
            screen.blit(self.RUNNING[0], (self.x, self.y))
        else:
            screen.blit(self.RUNNING[1], (self.x, self.y))

        return screen



    def jump(self):
        self.c = 0

    def move(self, timer):
        if timer % 5 == 1:
            if self.c < 10:
                self.x = min (self.x + 3, 1080)
                self.y = min (max(self.y - 5, 0), 720)
                self.c += 1
            else:
                self.x = min(self.x + 2, 1080)
                self.y = min(self.y + 2, 720)

        return self.x, self.y


