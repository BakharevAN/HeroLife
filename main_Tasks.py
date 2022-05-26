''' Игра "Жизнь героя". 
Количество игроков от 3 до 6 '''

from PyQt5 import QtCore, QtGui, QtWidgets

import subprocess
import copy
import sys
from ui_Tasks import Ui_HeroLife
import random
import subprocess

app = QtWidgets.QApplication(sys.argv)
                             

HeroLife = QtWidgets.QMainWindow()
ui = Ui_HeroLife()
ui.setupUi(HeroLife)
HeroLife.show()

''' Создаем копии списков для корректной работы рандомайзера. После того, как каждое поле будет заполнено значениями из списка, он может стать пустым, что приведет к ошибке при повторном нажатии кнопки.
Для того, чтобы этого избежать, каждый раз создается копия списка'''

heroes_list = [
    'Картон Кэт', 
    'Капитан Флинт', 
    'Флаундер', 
    'Ирина Хакамада', 
    'Дмитрий Нагиев', 
    'Сергей Шнуров', 
    'Волк из "Ну, погоди!"', 
    'Аладдин', 
    'Никола Тесла'
    'Доктор Ватсон',
    'Астрид  Линдгрен',
    'Чарли Чаплин'
]
tasks_list = [
    'Получить 5 за сочинение', 
    'Избавится от мух', 
    'Избавится от чувства вины', 
    'Избавиться от ипотеки', 
    'Рядом постоянный партнёр\nдля жизни и души', 
    'Завершить коррекцию челюсти\n(импланты, косметика)', 
    'Жениться/выйти замуж', 
    'Найти лекарство от всех болезней', 
    'Прыгнуть с парашютом',
    'Кайфовать от дела',
    'Приносить пользу мир',
    'приносить пользу природе\n(экологии)'
]  
talents_list = [
    'Магия', 
    'Левитация', 
    'Все, к чему прикоснется,\nпревращается в золото', 
    'Чтение людей на ментальном уровне', 
    'Телепортация', 
    'Вера в себя', 
    'Cпособность изменять свой размер',
    'Умение высоко прыгать',
    'Умение читать мысли',
    'Видеть правду',
    'не тревожиться',
    'Никогда не болеть'
]

roles_list = [
    'Обычный герой', 
    'Обычный герой', 
    'Обычный герой', 
    'Критик', 
    'Позитивчик',
    ]

rl = copy.copy(roles_list)

def players_quantity():
    # скрывает элементы в зависимости от выбранного количества игроков. по умолчанию 6 игроков
    if ui.comboBox.currentIndex() == 0: # 3 игрока
        ui.label_10.hide()
        ui.label_11.hide()
        ui.label_12.hide()
        ui.label_16.hide()
        ui.label_17.hide()
        ui.label_18.hide()
        ui.label_22.hide()
        ui.label_23.hide()
        ui.label_24.hide()
        ui.label_28.hide()
        ui.label_29.hide()
        ui.label_30.hide()
        ui.lineEdit_32.hide()
        ui.lineEdit_33.hide()
        ui.lineEdit_34.hide()
        ui.pushButton_7.hide()
        ui.pushButton_8.hide()
        ui.pushButton_9.hide()
    elif ui.comboBox.currentIndex() == 1:  # 4 игрока      
        ui.label_11.hide()
        ui.label_12.hide()
        ui.label_17.hide()
        ui.label_18.hide()
        ui.label_23.hide()
        ui.label_24.hide()
        ui.label_29.hide()
        ui.label_30.hide()
        ui.lineEdit_33.hide()
        ui.lineEdit_34.hide()
        ui.pushButton_8.hide()
        ui.pushButton_9.hide()
    elif ui.comboBox.currentIndex() == 2: # 5 игроков
        ui.label_12.hide()
        ui.label_18.hide()
        ui.label_24.hide()
        ui.label_30.hide()
        ui.lineEdit_34.hide()
        ui.pushButton_9.hide()       

def get_heroes():
    # выбирается случайный герой из списка heroes_list. Из списка удаляется выбранный герой.    
    hero = random.choice(heroes_list)
    heroes_list.remove(hero)
    return hero

def get_tasks():
    # выбирается случайная мечта из списка dreams_list. Из списка удаляется выбранная мечта.
    task = random.choice(tasks_list)
    tasks_list.remove(task)
    return task

def get_talents():
    # выбирается случайное препятствие из списка obstacles_list. Из списка удаляется выбранное препятствие.
    talent = random.choice(talents_list)
    talents_list.remove(talent)
    return talent

def get_roles():
    # выбирается случайная роль из списка roles_list. Из списка удаляется выбранная роль.  
    global rl  
    role = random.choice(rl)
    rl.remove(role)
    return role        

def choose_heroes():
    # заполнение полей случайными неповторяющимися героями из списка heroes_list, если поля пустые.
    if ui.label_7.text() == '':
        ui.label_7.setText(f'{get_heroes()}')
        ui.label_8.setText(f'{get_heroes()}')
        ui.label_9.setText(f'{get_heroes()}')
        ui.label_10.setText(f'{get_heroes()}')
        ui.label_11.setText(f'{get_heroes()}')
        ui.label_12.setText(f'{get_heroes()}')
        

def choose_tasks():
    # заполнение полей случайными неповторяющимися задачами из списка tasks_list, если поля пустые.
    if ui.label_13.text() == '':
        ui.label_13.setText(f'{get_tasks()}')
        ui.label_14.setText(f'{get_tasks()}')
        ui.label_15.setText(f'{get_tasks()}')
        ui.label_16.setText(f'{get_tasks()}')
        ui.label_17.setText(f'{get_tasks()}')
        ui.label_18.setText(f'{get_tasks()}')

def choose_talents():
    # заполнение полей случайными неповторяющимися препятствиями из списка talents_list, если поля пустые.
    if ui.label_19.text() == '':
        ui.label_19.setText(f'{get_talents()}')
        ui.label_20.setText(f'{get_talents()}')
        ui.label_21.setText(f'{get_talents()}')
        ui.label_22.setText(f'{get_talents()}')
        ui.label_23.setText(f'{get_talents()}')
        ui.label_24.setText(f'{get_talents()}')
    
def choose_roles_1():
    # заполнение полей случайными неповторяющимися ролями из списка roles_list. В поле активного игрока вставляется надпись "Главный"
    global rl
    if ui.label_25.text() != 'Главный':
        ui.label_25.setText(f'Главный')
        ui.label_26.setText(f'{get_roles()}')
        ui.label_27.setText(f'{get_roles()}')
        ui.label_28.setText(f'{get_roles()}')
        ui.label_29.setText(f'{get_roles()}')
        ui.label_30.setText(f'{get_roles()}')
        rl = copy.copy(roles_list)

    
def choose_roles_2():
    # заполнение полей случайными неповторяющимися ролями из списка roles_list. В поле активного игрока вставляется надпись "Главный"
    global rl
    if ui.label_26.text() != 'Главный':
        ui.label_25.setText(f'{get_roles()}')
        ui.label_26.setText(f'Главный')
        ui.label_27.setText(f'{get_roles()}')
        ui.label_28.setText(f'{get_roles()}')
        ui.label_29.setText(f'{get_roles()}')
        ui.label_30.setText(f'{get_roles()}')
        rl = copy.copy(roles_list)

def choose_roles_3():
    # заполнение полей случайными неповторяющимися ролями из списка roles_list. В поле активного игрока вставляется надпись "Главный"
    global rl
    if ui.label_27.text() != 'Главный':
        ui.label_25.setText(f'{get_roles()}')
        ui.label_26.setText(f'{get_roles()}')
        ui.label_27.setText(f'Главный')
        ui.label_28.setText(f'{get_roles()}')
        ui.label_29.setText(f'{get_roles()}')
        ui.label_30.setText(f'{get_roles()}')
        rl = copy.copy(roles_list)
    
def choose_roles_4():
    # заполнение полей случайными неповторяющимися ролями из списка roles_list. В поле активного игрока вставляется надпись "Главный"
    global rl
    if ui.label_28.text() != 'Главный':
        ui.label_25.setText(f'{get_roles()}')
        ui.label_26.setText(f'{get_roles()}')
        ui.label_27.setText(f'{get_roles()}')
        ui.label_28.setText(f'Главный')
        ui.label_29.setText(f'{get_roles()}')
        ui.label_30.setText(f'{get_roles()}')
        rl = copy.copy(roles_list)
    
def choose_roles_5():
    # заполнение полей случайными неповторяющимися ролями из списка roles_list. В поле активного игрока вставляется надпись "Главный"
    global rl
    if ui.label_29.text() != 'Главный':
        ui.label_25.setText(f'{get_roles()}')
        ui.label_26.setText(f'{get_roles()}')
        ui.label_27.setText(f'{get_roles()}')
        ui.label_28.setText(f'{get_roles()}')
        ui.label_29.setText(f'Главный')
        ui.label_30.setText(f'{get_roles()}')
        rl = copy.copy(roles_list)

def choose_roles_6():
    # заполнение полей случайными неповторяющимися ролями из списка roles_list. В поле активного игрока вставляется надпись "Главный"
    global rl
    if ui.label_30.text() != 'Главный':
        ui.label_25.setText(f'{get_roles()}')
        ui.label_26.setText(f'{get_roles()}')
        ui.label_27.setText(f'{get_roles()}')
        ui.label_28.setText(f'{get_roles()}')
        ui.label_29.setText(f'{get_roles()}')
        ui.label_30.setText(f'Главный')
        rl = copy.copy(roles_list)

def restart_1():      
    subprocess.Popen('c:\Python_p\Hero Life Tasks\Hero Life\Hero Life.exe')
    
    
def restart_2():    
    exit()

ui.pushButton.clicked.connect(choose_heroes)
ui.pushButton_2.clicked.connect(choose_tasks)
ui.pushButton_3.clicked.connect(choose_talents)
ui.pushButton_4.clicked.connect(choose_roles_1)
ui.pushButton_5.clicked.connect(choose_roles_2)
ui.pushButton_6.clicked.connect(choose_roles_3)
ui.pushButton_7.clicked.connect(choose_roles_4)
ui.pushButton_8.clicked.connect(choose_roles_5)
ui.pushButton_9.clicked.connect(choose_roles_6)
ui.pushButton_10.clicked.connect(players_quantity)
ui.pushButton_11.clicked.connect(restart_1)
ui.pushButton_11.clicked.connect(restart_2)

sys.exit(app.exec_())