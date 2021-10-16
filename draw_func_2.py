import pygame


def draw(objects, screen):
    for i in objects.keys():
        if objects[i]["figure"] == "circle":
            pygame.draw.circle(screen, tuple(objects[i]['color']), tuple(objects[i]['centre']),
                               objects[i]['radius'], objects[i].get('width', 0))
        elif objects[i]["figure"] == "rectangle":
            pygame.draw.rect(screen, tuple(objects[i]['color']), tuple(objects[i]['position']),
                             objects[i].get('width', 0))
        elif objects[i]["figure"] == "line":  # обычная линия
            pygame.draw.line(screen, tuple(objects[i]['color']), tuple(objects[i]['position'][0]),
                             tuple(objects[i]['position'][1]), objects[i].get('width', 0))
        elif objects[i]["figure"] == "aaline":  # сглаженная линия(нельзя указать толщину)
            pygame.draw.aaline(screen, tuple(objects[i]['color']), tuple(objects[i]['start']),
                               tuple(objects[i]['end']))
        elif objects[i]["figure"] == "lines":
            pygame.draw.lines(screen, tuple(objects[i]['color']), objects[i]['bool'], # параметр указывающий на замкнутость ломанной
                              tuple(objects[i]['position']),  objects[i].get('width', 0))
        elif objects[i]["figure"] == "aalines":  # аналогично сглаженная линия, только ломанная
            pygame.draw.aalines(screen, tuple(objects[i]['color']), objects[i]['bool'],
                                tuple(objects[i]['position']))
        elif objects[i]["figure"] == "polygon":
            pygame.draw.polygon(screen, tuple(objects[i]['color']), tuple(objects[i]['position']), objects[i].get('width', 0))
            pygame.draw.aalines(screen, tuple(objects[i]['color']), True,   # чисто косметическое, ибо если отрисовать вокруг полигона сглаженную ломанную, то он будет красивее выглядеть, если не нужно делитни
                                tuple(objects[i]['position']))
        elif objects[i]["figure"] == "ellipse":
            pygame.draw.ellipse(screen, tuple(objects[i]['color']), tuple(objects[i]['color']),
                                tuple(objects[i]['position']))
        elif objects[i]["figure"] == "arc":
            pygame.draw.arc(screen, tuple(objects[i]['color']), tuple(objects[i]['color']),
                            tuple(objects[i]['position']), objects[i]['start'], objects[i]['end'],
                            objects[i].get('width', 0))
        else:
            raise NotImplementedError
    return screen
