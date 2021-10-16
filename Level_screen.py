import pygame
import sys

import draw_func


class Level:
    window_size = width, height = 360, 420

    def get_objects(self):
        raise NotImplementedError  #считывает данные из файлов

    def get_heights(self):
        raise NotImplementedError #считывает данные з файла в зависимости от уровня

    def __init__(self, background, objects, level, heights):
        self.level = level
        self.objects = self.get_objects() #get all objects from files, create a method
        self.background = background
        draw_func.draw(Level.screen, self.background)
        for i in self.objects:
            draw_func.draw(Level.screen, self.object)

    def get_screen(self):
        return Level.screen

    def check_height(self, pos_x, pos_y):
        raise NotImplementedError



    # def draw_background(self, display, size):
    #     pygame.init()
    #     """"
    #     size - width and height
    #
    #     #ground = (68, 148, 74)
    #     #sky = (66, 170, 255)
    #     """
    #     pygame.draw.rect(display, (Screen.sky), (0, 0, size[0], (size[1]) // 3))
    #     pygame.draw.rect(display, (Screen.ground), (0, (size[1] // 3), size[0], (size[1] - (size[1]) // 3)))
    #     #Код ниже отображает уровень в правом верхнем углу, пока что без скейлинга цифры
    #     #print((int(size[0]*size[1]*0.0001)))
    #     lfont = pygame.font.SysFont('comicsansms', (int(size[0]*size[1]*0.0001)))
    #     levelid = lfont.render(str(self.level), False, (255, 255, 255))
    #     #display.blit(levelid, (int(size[0]*(0.95-(len(str(self.level))*0.025)))))) - рабочий
    #     #display.blit(levelid, (int(size[0]*0.9), 0)) - ломался при значениях уровня >10000
    #     display.blit(levelid,(int(size[0]*(0.95-(len(str(self.level))*0.025))),0))
    #     #self.level+=1


    # def get_height(self):
    #     # возвращает высоту через поиск объектов на уровне через json и словарь/список объектов (использует поле ОБЪЕКТОВ )
    #     for i in self.background[self.level]:
    #          return self.objects[i].height
    #         #return (self.listofobj[i][height]-i["position"][1])
    #
    #
    #
    # def draw_obj(self,screen):
    #     #pygame.init()
    #     #self.json
    #     # рисует объекты на уровне через их же метод ,ну и использует json для поиска объектов в словаре/списке
    #     for i in self.background[self.level]:
    #         if(i["type"]=="static"):
    #             self.objects[i].draw(screen, i["position"], i["color"])
    #         else:
    #             self.objects[i].draw(screen, i["position"], i["state"], i["color"])


       #for i in self.listofobj[level]:
            #i.draw
    """
    def screen_change(self,level):
        self.level=level/or
        self.level+=1
        self.draw_back(self,self.level/or/level)
    """

        




# ground = (68, 148, 74)
# sky = (66, 170, 255)

# def main():
#     pygame.init()
#     level = 1
#     screen = pygame.display.set_mode(size)
#     gameover = False
#     Scren = Screen({}, {})
#     while not gameover:
#         for event in pygame.event.get():
#             if event.type == pygame.quit:
#                 gameover = True
#         screen.fill((255, 255, 255))
#         Scren.draw_back(screen, size)
#         """"
#         pygame.draw.rect(screen, (sky), (0, 0, width, (height)//3))
#         pygame.draw.rect(screen, (ground), (0,(height//3)-1, width, (height-(height)//3)))
#         lfont = pygame.font.SysFont('comicsansms',10)
#         levelid = lfont.render(str(level), False, (255, 255, 255))
#         screen.blit(levelid, (width-(width//10), 0))
#         level+=1
#         """
#         pygame.display.flip()
#         pygame.time.wait(10)
#     sys.exit
#
#
# if __name__ == "__main__":
#     main()


