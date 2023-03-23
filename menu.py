import pygame
import datetime
import sys
import sqlite3
pygame.init()


ARIAL_50 = pygame.font.SysFont('arial', 50)
userdata = sqlite3.connect('userdata.db')
cursor_userdata = userdata.cursor()
cursor_userdata.execute(""" CREATE TABLE IF NOT EXISTS data(
    Data_number INT,
    Data_name TEXT,
    Data_value TEXT);
""")
userdata.commit()

class Menu():
    """главное меню"""

    def __init__(self):
        cursor_userdata.execute("SELECT Data_value FROM data ")
        self._option_list_menu0 = [] # список пунктов меню 0
        self._callbacks_menu0 = [] # список реакций кнопок меню 0
        self._option_index_menu0 = [] # индекс пункта меню 0
        self._option_list_menu1 = []  # список кнопок меню 1
        self._callbacks_menu1 = []  # список реакций кнопок меню 1
        self._option_index_menu1 = []  # индекс пункта меню 1
        self._option_list_menu2 = []  # список кнопок меню 2
        self._callbacks_menu2 = []  # список реакций кнопок меню 2
        self._option_index_menu2 = []  # индекс пункта меню 2
        self._current_option_index_menu0 = 0
        self._current_option_index_menu1 = 0
        self._current_option_index_menu2 = 0
        self._current_page_index = 0
        cursor_userdata.execute("SELECT Data_value FROM data ")
        self._current_exersize = int(cursor_userdata.fetchall()[0][0]) # кол-во текущих отжиманий
        cursor_userdata.execute("SELECT Data_value FROM data ")
        k = (cursor_userdata.fetchall()[1][0]).split('-')
        self._last_date_of_exersize = datetime.date(int(k[0]),int(k[1]),int(k[2]))


    def append_options_menu0(self, option, callback, index):
        self._option_list_menu0.append(ARIAL_50.render(option, True, (255, 255, 0)))
        self._callbacks_menu0.append(callback)
        self._option_index_menu0.append(index)

    def append_options_menu1(self, option, callback, index):
        self._option_list_menu1.append(ARIAL_50.render(option, True, (255, 255, 0)))
        self._callbacks_menu1.append(callback)
        self._option_index_menu1.append(index)

    def append_options_menu2(self, option, callback, index):
        self._option_list_menu2.append(ARIAL_50.render(option, True, (255, 255, 0)))
        self._callbacks_menu2.append(callback)
        self._option_index_menu2.append(index)

    def switch(self, pos, menu_x, menu_y):
        if self._current_page_index == 0 :
            self._current_option_index_menu0 = (pos[1] - menu_y) // 100
            if self._current_option_index_menu0 > len(self._option_list_menu0):
                self._current_option_index_menu0 = 99
        if self._current_page_index == 1:
            self._current_option_index_menu1 = (pos[1] - menu_y) // 100
            if self._current_option_index_menu1 > len(self._option_list_menu1):
                self._current_option_index_menu1 = 99
        if self._current_page_index == 2:
            self._current_option_index_menu2 = (pos[1] - menu_y) // 100
            if pos[0] >=685 and pos[0] <= 715 and pos[1] >= 620 and pos[1] <= 640:
                self._current_exersize +=1
            elif pos[0] >=765 and pos[0] <= 780 and pos[1] >= 620 and pos[1] <= 640:
                self._current_exersize -=1
            elif pos[0] < 500 and self._current_option_index_menu2 > len(self._option_list_menu2):
                self._current_option_index_menu2 = 99


    def select(self,pos):
        if self._current_page_index == 0 :
            if self._current_option_index_menu0 != 99:
                self._callbacks_menu0[self._current_option_index_menu0]()

        elif self._current_page_index == 1 :
            if self._current_option_index_menu1 != 99 and self._current_option_index_menu1 >= 0 :
                self._callbacks_menu1[self._current_option_index_menu1]()
            elif pos[0]>=90 and pos[0]<= 320 and pos[1]>= 350 and pos[1]<= 410:
                self._last_date_of_exersize = datetime.date.today()



        elif self._current_page_index == 2 :
            if self._current_option_index_menu2 != 99:
                self._callbacks_menu2[self._current_option_index_menu2]()



    def callback0(self):
        self._current_page_index = 1

    def callback1(self):
        self._current_page_index = 2

    def callback2(self): # установка кол-ва отжиманий
        pass
    def callback3(self): # Сброс кол-ва отжиманий
        self._current_exersize = 5
        self._last_date_of_exersize = datetime.date(2000,12,25)

    def callback4(self): # Увеличить число отжиманий
        self._current_exersize +=1
        self._current_page_index = 0
    def callback5(self): # Увеличить число отжиманий
        self._current_page_index = 0


    def mainmenu(self):
        self._current_page_index = 0

    def stop(self):
        cursor_userdata.execute(f"UPDATE data SET Data_value = '{self._current_exersize}' WHERE Data_name = 'self._current_exersize'")
        userdata.commit()
        cursor_userdata.execute(
            f"UPDATE data SET Data_value = '{self._last_date_of_exersize}' WHERE Data_name = 'self._last_date_of_exersize'")
        userdata.commit()
        sys.exit()





    def draw(self, screen, x, y, option_y_padding):
        if self._current_page_index == 0:
            # option_y_padding - значение отступа в меню
            for i, option in enumerate(self._option_list_menu0):
                option_rect = option.get_rect()
                option_rect.topleft = (x, y + (self._option_index_menu0[i]) * option_y_padding)
                screen.blit(option, option_rect)
        elif self._current_page_index == 1:
            text3 = ARIAL_50.render(f'Последняя тренировка: {self._last_date_of_exersize}', True, (255, 255, 0))
            screen.blit(text3, (100, 50))
            if self._last_date_of_exersize != datetime.date.today():
                text1 = ARIAL_50.render('Отжиманий сегодня сделать:', True, (255, 255, 0))
                screen.blit(text1, (100, 150))
                text2 = ARIAL_50.render(f' 3 X {self._current_exersize} ', True, (255, 255, 0))
                screen.blit(text2, (100, 250))
                text4 = ARIAL_50.render('!!Сделано!!', True, (255, 255, 0))
                screen.blit(text4, (100, 350))
            else:
                text5 = ARIAL_50.render('Поздравляем!', True, (255, 255, 0))
                screen.blit(text5, (100, 150))
                text6 = ARIAL_50.render('Программа на сегодня выполнена!', True,
                                        (255, 255, 0))
                screen.blit(text6, (100, 250))
                text7 = ARIAL_50.render('Ждем Вас завтра.', True,
                                        (255, 255, 0))
                screen.blit(text7, (100, 350))


            for i, option in enumerate(self._option_list_menu1):
                option_rect = option.get_rect()
                option_rect.topleft = (x, y + (self._option_index_menu1[i]) * option_y_padding)
                screen.blit(option, option_rect)

        elif self._current_page_index == 2:
            text1 = ARIAL_50.render(f'{self._current_exersize}', True, (255, 255, 0))
            screen.blit(text1, (1000, y + option_y_padding))
            for i, option in enumerate(self._option_list_menu2):
                option_rect = option.get_rect()
                option_rect.topleft = (x, y + (self._option_index_menu2[i]) * option_y_padding)
                screen.blit(option, option_rect)

