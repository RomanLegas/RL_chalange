import pygame
import sys
from menu import Menu
import datetime
pygame.init()

def run():
    screen = pygame.display.set_mode()
    pygame.display.set_caption('Челендж 0.0.2')
    bg_color = (0, 102, 51)
    ARIAL_100 = pygame.font.SysFont('arial', 100)
    menu_x = 100
    menu_y = 500
    menu = Menu()
    menu.append_options_menu0('Отжимания', menu.callback0, 0)
    menu.append_options_menu0('Настройки', menu.callback1, 1)
    menu.append_options_menu0('Выход', menu.stop, 2)
    menu.append_options_menu1('Увеличить число отжиманий', menu.callback4, 0)
    menu.append_options_menu1('Повторить в след раз', menu.callback5, 1)
    menu.append_options_menu1('Главное меню', menu.mainmenu, 2)
    menu.append_options_menu2('Начать сначала', menu.callback3, 0)
    menu.append_options_menu2('Изменить кол-во отжиманий    +     -   ', menu.callback2, 1)
    menu.append_options_menu2('Главное меню', menu.mainmenu, 2)
    k = 1


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu.stop()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    menu.switch(event.pos,  menu_x, menu_y)
                    menu.select(event.pos)




        screen.fill(bg_color)
        menu.draw(screen, menu_x , menu_y, 100,)


        pygame.display.flip()

run()