''' Игра "Жизнь героя". 
Количество игроков от 3 до 6 '''

from PyQt5 import QtWidgets 
import sqlite3

from ui_Tasks import Ui_HeroLife

import copy
import sys
import random
import subprocess

try:
    # подключение локальной базы данных
    connection = sqlite3.connect('hl.db')        
    print('Successfully connected')
    print('#' * 20)      

    # запуск виджета Qt
    app = QtWidgets.QApplication(sys.argv)
    HeroLife = QtWidgets.QMainWindow()
    ui = Ui_HeroLife()
    ui.setupUi(HeroLife)
    HeroLife.show()
    
    # создание списков из БД
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM `hero`")
    heroes_tuple_list = cursor.fetchall()  # создается список из кортежей. В каждой кортеже - герой
    heroes_list = []
    for i in heroes_tuple_list:
        hero = ''.join(i)  # меняем tuple на str
        if hero != '':
            heroes_list.append(hero)  # добавляем героя в список, если имя героя не пустое
        
    cursor.execute("SELECT task FROM `task`")
    task_tuple_list = cursor.fetchall()
    tasks_list = []
    for i in task_tuple_list:
        task = ''.join(i)
        if task != '':
            tasks_list.append(task)   
        
    cursor.execute("SELECT talent FROM `talent`")
    talents_tuple_list = cursor.fetchall()
    talents_list = []
    for i in talents_tuple_list:
        talent = ''.join(i)
        if talent != '':
            talents_list.append(talent)   
        
    cursor.execute("SELECT role FROM `role`")
    roles_tuple_list = cursor.fetchall()
    roles_list = []
    for i in roles_tuple_list:
        role = ''.join(i)
        if role != '':
            roles_list.append(role)
        
    rl = copy.copy(roles_list) # создаем копию списка ролей, т.к. операция распределения ролей будет проводиться несколько раз за 1 игру, а roles_list должен оставаться неизменым  
    
    def db():
        # открывает окно для занесения данных в базу данных
        subprocess.Popen('db_tasks.exe')        

    def number_of_players():
        # скрывает или отображает элементы в зависимости от выбранного количества игроков. по умолчанию 6 игроков
        if ui.comboBox.currentIndex() == 3: # 3 игрока
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
        elif ui.comboBox.currentIndex() == 2:  # 4 игрока
            ui.label_10.show()      
            ui.label_11.hide()
            ui.label_12.hide()
            ui.label_16.show()
            ui.label_17.hide()
            ui.label_18.hide()
            ui.label_22.show()
            ui.label_23.hide()
            ui.label_24.hide()
            ui.label_28.show()
            ui.label_29.hide()
            ui.label_30.hide()
            ui.lineEdit_32.show()
            ui.lineEdit_33.hide()
            ui.lineEdit_34.hide()
            ui.pushButton_7.show()
            ui.pushButton_8.hide()
            ui.pushButton_9.hide()
        elif ui.comboBox.currentIndex() == 1: # 5 игроков
            ui.label_10.show()
            ui.label_11.show()
            ui.label_12.hide()
            ui.label_16.show()
            ui.label_17.show()
            ui.label_18.hide()
            ui.label_22.show()
            ui.label_23.show()
            ui.label_24.hide()
            ui.label_28.show()
            ui.label_29.show()
            ui.label_30.hide()
            ui.lineEdit_32.show()
            ui.lineEdit_33.show()
            ui.lineEdit_34.hide()
            ui.pushButton_7.show()
            ui.pushButton_8.show()
            ui.pushButton_9.hide()
        elif ui.comboBox.currentIndex() == 0: # 6 игроков
            ui.label_10.show()
            ui.label_11.show()
            ui.label_12.show()
            ui.label_16.show()
            ui.label_17.show()
            ui.label_18.show()
            ui.label_22.show()
            ui.label_23.show()
            ui.label_24.show()
            ui.label_28.show()
            ui.label_29.show()
            ui.label_30.show()
            ui.lineEdit_32.show()
            ui.lineEdit_33.show()
            ui.lineEdit_34.show()
            ui.pushButton_7.show()
            ui.pushButton_8.show()
            ui.pushButton_9.show() 
        rl = copy.copy(roles_list)         

    def get_heroes():
        # Формируется список героев heroes_list из базы данных. Выбирается случайный герой из списка heroes_list, затем выбранный герой удаляется из списка.        
        hero = random.choice(heroes_list)
        heroes_list.remove(hero)
        return hero
    
    def get_tasks():
        # Формируется список задач tasks_list из базы данных. Выбирается случайная задача из списка tasks_list, затем выбранная задача удаляется из списка.
        task = random.choice(tasks_list)
        tasks_list.remove(task)
        return task
    
    def get_talents():
        # Формируется список талантов talents_lis из базы данных. Выбирается случайный талант из списка talents_list, затем выбранный талант удаляется из списка.
        talent = random.choice(talents_list)
        talents_list.remove(talent)
        return talent
    
    def get_roles():
        # выбирается случайная роль из списка roles_list. Из списка удаляется выбранная роль.  
        role = random.choice(rl)
        rl.remove(role)
        return role  
          
    def choose_heroes():
        # заполнение полей случайными неповторяющимися героями из списка heroes_list, если поля пустые. Если в базе данных меньше 6 героев, выводит сообщение об этом.
        if len(heroes_list) < 6:
            Ui_HeroLife.error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть не меньше 6 героев!")        
        elif ui.label_7.text() == '':
            ui.label_7.setText(f'{get_heroes()}')
            ui.label_8.setText(f'{get_heroes()}')
            ui.label_9.setText(f'{get_heroes()}')
            ui.label_10.setText(f'{get_heroes()}')
            ui.label_11.setText(f'{get_heroes()}')
            ui.label_12.setText(f'{get_heroes()}')
            
    def choose_tasks():
        # заполнение полей случайными неповторяющимися задачами из списка tasks_list, если поля пустые. Если в базе данных меньше 6 задач, выводит сообщение об этом.
        if len(tasks_list) < 6:
            Ui_HeroLife.error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть не меньше 6 задач!")    
        elif ui.label_13.text() == '':
            ui.label_13.setText(f'{get_tasks()}')
            ui.label_14.setText(f'{get_tasks()}')
            ui.label_15.setText(f'{get_tasks()}')
            ui.label_16.setText(f'{get_tasks()}')
            ui.label_17.setText(f'{get_tasks()}')
            ui.label_18.setText(f'{get_tasks()}')
            
    def choose_talents():
        # заполнение полей случайными неповторяющимися талантами из списка talents_list, если поля пустые. Если в базе данных меньше 6 талантов, выводит сообщение об этом.
        if len(talents_list) < 6:
            Ui_HeroLife.error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть не меньше 6 талантов!")   
        elif ui.label_19.text() == '':
            ui.label_19.setText(f'{get_talents()}')
            ui.label_20.setText(f'{get_talents()}')
            ui.label_21.setText(f'{get_talents()}')
            ui.label_22.setText(f'{get_talents()}')
            ui.label_23.setText(f'{get_talents()}')
            ui.label_24.setText(f'{get_talents()}')
        
    def choose_roles_1():
        # заполнение полей случайными неповторяющимися ролями из списка roles_list. В поле первого игрока вставляется надпись "Главный". 
        # Если в базе данных ролей недостаточно, выводит сообщение об этом.
        global rl               
        if ui.comboBox.currentIndex() == 3: # 3 игрока            
            if len(rl) < 4:
                Ui_HeroLife.error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 4 роли!") 
            elif ui.label_25.text() != 'Главный':
                ui.label_25.setText(f'Главный')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'{get_roles()}')
                
        elif ui.comboBox.currentIndex() == 2: # 4 игрока            
            if len(rl) < 5:
                Ui_HeroLife.error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 5 ролей!") 
            elif ui.label_25.text() != 'Главный':
                ui.label_25.setText(f'Главный')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'{get_roles()}')
                   
        elif ui.comboBox.currentIndex() == 1: # 5 игроков
            if len(rl) < 6:
                Ui_HeroLife.error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 6 ролей!") 
            elif ui.label_25.text() != 'Главный':
                ui.label_25.setText(f'Главный')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'{get_roles()}')                 
                ui.label_29.setText(f'{get_roles()}')
                
        elif ui.comboBox.currentIndex() == 0: # 6 игроков
            if len(rl) < 7:
                Ui_HeroLife.error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 7 ролей!") 
            elif ui.label_25.text() != 'Главный':
                ui.label_25.setText(f'Главный')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'{get_roles()}')                 
                ui.label_29.setText(f'{get_roles()}')           
                ui.label_30.setText(f'{get_roles()}')
        rl = copy.copy(roles_list)
        
    def choose_roles_2():
        # заполнение полей случайными неповторяющимися ролями из списка roles_list. В поле второго игрока вставляется надпись "Главный". 
        # Если в базе данных ролей недостаточно, выводит сообщение об этом.
        global rl
        if ui.comboBox.currentIndex() == 3: # 3 игрока            
            if len(rl) < 4:
                Ui_HeroLife.error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 4 роли!") 
            elif ui.label_26.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'Главный')
                ui.label_27.setText(f'{get_roles()}')
                
        elif ui.comboBox.currentIndex() == 2: # 4 игрока            
            if len(rl) < 5:
                Ui_HeroLife.error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 5 ролей!") 
            elif ui.label_26.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'Главный')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'{get_roles()}')
                   
        elif ui.comboBox.currentIndex() == 1: # 5 игроков
            if len(rl) < 6:
                Ui_HeroLife.error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 6 ролей!") 
            elif ui.label_26.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'Главный')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'{get_roles()}')                 
                ui.label_29.setText(f'{get_roles()}')
                
        elif ui.comboBox.currentIndex() == 0: # 6 игроков
            if len(rl) < 7:
                Ui_HeroLife.error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 7 ролей!") 
            elif ui.label_26.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'Главный')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'{get_roles()}')                 
                ui.label_29.setText(f'{get_roles()}')           
                ui.label_30.setText(f'{get_roles()}')
        rl = copy.copy(roles_list)
        
    def choose_roles_3():
        global rl
        # заполнение полей случайными неповторяющимися ролями из списка roles_list. В поле третьего игрока вставляется надпись "Главный". 
        # Если в базе данных ролей недостаточно, выводит сообщение об этом.
        if ui.comboBox.currentIndex() == 3: # 3 игрока            
            if len(rl) < 4:
                Ui_HeroLife.error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 4 роли!") 
            elif ui.label_27.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'Главный')
                
        elif ui.comboBox.currentIndex() == 2: # 4 игрока            
            if len(rl) < 5:
                Ui_HeroLife.error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 5 ролей!") 
            elif ui.label_27.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'Главный')
                ui.label_28.setText(f'{get_roles()}')
                   
        elif ui.comboBox.currentIndex() == 1: # 5 игроков
            if len(rl) < 6:
                Ui_HeroLife.error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 6 ролей!") 
            elif ui.label_27.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'Главный')
                ui.label_28.setText(f'{get_roles()}')                 
                ui.label_29.setText(f'{get_roles()}')
                
        elif ui.comboBox.currentIndex() == 0: # 6 игроков
            if len(rl) < 7:
                Ui_HeroLife.error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 7 ролей!") 
            elif ui.label_27.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'Главный')
                ui.label_28.setText(f'{get_roles()}')                 
                ui.label_29.setText(f'{get_roles()}')           
                ui.label_30.setText(f'{get_roles()}')
        rl = copy.copy(roles_list)
        
    def choose_roles_4():
        # заполнение полей случайными неповторяющимися ролями из списка roles_list. В поле четвертого игрока вставляется надпись "Главный". 
        # Если в базе данных ролей недостаточно, выводит сообщение об этом. 
        global rl       
        if ui.comboBox.currentIndex() == 2: # 4 игрока            
            if len(rl) < 5:
                Ui_HeroLife.error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 5 ролей!") 
            elif ui.label_28.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'Главный')
                   
        elif ui.comboBox.currentIndex() == 1: # 5 игроков
            if len(rl) < 6:
                Ui_HeroLife.error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 6 ролей!") 
            elif ui.label_28.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'Главный')                 
                ui.label_29.setText(f'{get_roles()}')
                
        elif ui.comboBox.currentIndex() == 0: # 6 игроков
            if len(rl) < 7:
                Ui_HeroLife.error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 7 ролей!") 
            elif ui.label_28.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'Главный')                 
                ui.label_29.setText(f'{get_roles()}')           
                ui.label_30.setText(f'{get_roles()}')
        rl = copy.copy(roles_list)
        
    def choose_roles_5():
        # заполнение полей случайными неповторяющимися ролями из списка roles_list. В поле пятого игрока вставляется надпись "Главный". 
        # Если в базе данных ролей недостаточно, выводит сообщение об этом.
        global rl
        if ui.comboBox.currentIndex() == 1: # 5 игроков
            if len(rl) < 6:
                Ui_HeroLife.error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 6 ролей!") 
            elif ui.label_29.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'{get_roles()}')                 
                ui.label_29.setText(f'Главный')
                
        elif ui.comboBox.currentIndex() == 0: # 6 игроков
            if len(rl) < 7:
                Ui_HeroLife.error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 7 ролей!") 
            elif ui.label_27.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'{get_roles()}')                 
                ui.label_29.setText(f'Главный')           
                ui.label_30.setText(f'{get_roles()}')
        rl = copy.copy(roles_list)
            
    def choose_roles_6():
        # заполнение полей случайными неповторяющимися ролями из списка roles_list. В поле шестого игрока вставляется надпись "Главный". 
        # Если в базе данных ролей недостаточно, выводит сообщение об этом. 
        global rl       
        if ui.comboBox.currentIndex() == 0: # 6 игроков
            if len(rl) < 7:
                Ui_HeroLife.error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 7 ролей!") 
            elif ui.label_27.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'{get_roles()}')                 
                ui.label_29.setText(f'{get_roles()}')           
                ui.label_30.setText(f'Главный')
        rl = copy.copy(roles_list)
            
    def restart_1():      
        subprocess.Popen('Hero Life.exe')    
        
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
    ui.pushButton_10.clicked.connect(number_of_players)
    ui.pushButton_11.clicked.connect(restart_1)
    ui.pushButton_11.clicked.connect(restart_2)
    ui.pushButton_12.clicked.connect(db)
        
    sys.exit(app.exec_())
        
except Exception as ex:
    print('Connection refused')
    print(ex)