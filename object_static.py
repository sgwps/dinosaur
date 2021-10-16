import pygame
import json


class Object:
    def read_json(self):
        file = "obj_" + str(self.level) + "_" + str(self.number) + ".json"
        reader = open(file)
        self.params = json.load(reader)
        reader.close()

    def __init__(self, level, number):
        self.level = level
        self.number = number
        self.params = None
        self.read_json()

    def draw(self, screen):
        print(tuple(self.params["0"]['color']))
        for i in self.params.keys():
            if self.params[i]["figure"] == "circle":
                pygame.draw.circle(screen, tuple(self.params[i]['color']), tuple(self.params[i]['centre']), self.params[i]['radius'], self.params[i].get('width', 0))
        return screen

