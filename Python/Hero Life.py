''' 

Игра "Жизнь героя". 
Количество игроков от 3 до 6
 
'''

from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QMessageBox
import sqlite3

from ui_Tasks import Ui_HeroLife

import sys
import random
import subprocess

try:
    # подключение локальной базы данных
    connection = sqlite3.connect('db.sqlite3')        
    print('Successfully connected')
    print('#' * 20) 
    
    # создаем таблицы, если их еще нет
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS hero (
        hero_id INT AUTO_INCREMENT PRIMARY_KEY, 
        name VARCHAR(80));
    """)       

    cursor.execute("""CREATE TABLE IF NOT EXISTS task (
        task_id INT AUTO_INCREMENT PRIMARY_KEY, 
        task VARCHAR(80));
    """)       

    cursor.execute("""CREATE TABLE IF NOT EXISTS talent (
        talent_id INT AUTO_INCREMENT PRIMARY_KEY, 
        talent VARCHAR(80));
    """)       

    cursor.execute("""CREATE TABLE IF NOT EXISTS role (
        role_id INT AUTO_INCREMENT PRIMARY_KEY, 
        role VARCHAR(80));   
    """)      
    connection.commit()          

    # запуск виджета Qt
    app = QtWidgets.QApplication(sys.argv)
    HeroLife = QtWidgets.QMainWindow()
    ui = Ui_HeroLife()
    ui.setupUi(HeroLife)
    HeroLife.show()       
    
    def db():
        # открывает окно для занесения данных в базу данных
        subprocess.Popen('db_tasks.exe')        

    def number_of_players():
        # скрывает или отображает элементы в зависимости от выбранного количества игроков. по умолчанию 6 игроков
        if ui.comboBox.currentIndex() == 4: # 3 игрока
            ui.label_39.hide()
            ui.label_40.hide()
            ui.label_41.hide()
            ui.label_42.hide()
            ui.label_10.hide()
            ui.label_11.hide()
            ui.label_12.hide()
            ui.label_31.hide()
            ui.label_16.hide()
            ui.label_17.hide()
            ui.label_18.hide()
            ui.label_32.hide()
            ui.label_22.hide()
            ui.label_23.hide()
            ui.label_24.hide()
            ui.label_33.hide()
            ui.label_28.hide()
            ui.label_29.hide()
            ui.label_30.hide()
            ui.label_34.hide()
            ui.pushButton_7.hide()
            ui.pushButton_8.hide()
            ui.pushButton_9.hide()
            ui.pushButton_13.hide()
        elif ui.comboBox.currentIndex() == 3:  # 4 игрока
            ui.label_39.show()
            ui.label_40.hide()
            ui.label_41.hide()
            ui.label_42.hide()
            ui.label_10.show()
            ui.label_11.hide()
            ui.label_12.hide()
            ui.label_31.hide()
            ui.label_16.show()
            ui.label_17.hide()
            ui.label_18.hide()
            ui.label_32.hide()
            ui.label_22.show()
            ui.label_23.hide()
            ui.label_24.hide()
            ui.label_33.hide()
            ui.label_28.show()
            ui.label_29.hide()
            ui.label_30.hide()
            ui.label_34.hide()
            ui.pushButton_7.show()
            ui.pushButton_8.hide()
            ui.pushButton_9.hide()
            ui.pushButton_13.hide()
        elif ui.comboBox.currentIndex() == 2: # 5 игроков
            ui.label_39.show()
            ui.label_40.show()
            ui.label_41.hide()
            ui.label_42.hide()
            ui.label_10.show()
            ui.label_11.show()
            ui.label_12.hide()
            ui.label_31.hide()
            ui.label_16.show()
            ui.label_17.show()
            ui.label_18.hide()
            ui.label_32.hide()
            ui.label_22.show()
            ui.label_23.show()
            ui.label_24.hide()
            ui.label_33.hide()
            ui.label_28.show()
            ui.label_29.show()
            ui.label_30.hide()
            ui.label_34.hide()
            ui.pushButton_7.show()
            ui.pushButton_8.show()
            ui.pushButton_9.hide()
            ui.pushButton_13.hide()
        elif ui.comboBox.currentIndex() == 1: # 6 игроков
            ui.label_39.show()
            ui.label_40.show()
            ui.label_41.show()
            ui.label_42.hide()
            ui.label_10.show()
            ui.label_11.show()
            ui.label_12.show()
            ui.label_31.hide()
            ui.label_16.show()
            ui.label_17.show()
            ui.label_18.show()
            ui.label_32.hide()
            ui.label_22.show()
            ui.label_23.show()
            ui.label_24.show()
            ui.label_33.hide()
            ui.label_28.show()
            ui.label_29.show()
            ui.label_30.show()
            ui.label_34.hide()
            ui.pushButton_7.show()
            ui.pushButton_8.show()
            ui.pushButton_9.show()
            ui.pushButton_13.hide()
        elif ui.comboBox.currentIndex() == 0: # 7 игроков
            ui.label_39.show()
            ui.label_40.show()
            ui.label_41.show()
            ui.label_42.show()
            ui.label_10.show()
            ui.label_11.show()
            ui.label_12.show()
            ui.label_31.show()
            ui.label_16.show()
            ui.label_17.show()
            ui.label_18.show()
            ui.label_32.show()
            ui.label_22.show()
            ui.label_23.show()
            ui.label_24.show()
            ui.label_33.show()
            ui.label_28.show()
            ui.label_29.show()
            ui.label_30.show()
            ui.label_34.show()
            ui.pushButton_7.show()
            ui.pushButton_8.show()
            ui.pushButton_9.show()
            ui.pushButton_13.show()

    def choose_heroes():
        # создаем список героев из БД
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM `hero`")
        heroes_tuple_list = cursor.fetchall()  # создается список из кортежей. В каждом кортеже - герой
        heroes_list = []
        for i in heroes_tuple_list:
            hero = ''.join(i)  # меняем tuple на str
            if hero != '':
                heroes_list.append(hero)  # добавляем героя в список, если имя героя не пустое
        
        def get_heroes():
        # Формируется список героев heroes_list из БД. Выбирается случайный герой из списка heroes_list, затем выбранный герой удаляется из списка.        
            hero = random.choice(heroes_list)
            heroes_list.remove(hero)
            return hero
    
        # заполнение полей случайными неповторяющимися героями из списка heroes_list, если поля пустые. Если в базе данных меньше 6 героев, выводит сообщение об этом.
        if len(heroes_list) < 7:
            error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть не меньше 7 героев!")        
        elif ui.label_7.text() == '':
            ui.label_7.setText(f'{get_heroes()}')
            ui.label_8.setText(f'{get_heroes()}')
            ui.label_9.setText(f'{get_heroes()}')
            ui.label_10.setText(f'{get_heroes()}')
            ui.label_11.setText(f'{get_heroes()}')
            ui.label_12.setText(f'{get_heroes()}')
            ui.label_31.setText(f'{get_heroes()}')            
            
    def choose_tasks():
        # создаем список задач из БД
        cursor = connection.cursor()
        cursor.execute("SELECT task FROM `task`")
        task_tuple_list = cursor.fetchall()
        tasks_list = []
        for i in task_tuple_list:
            task = ''.join(i)
            if task != '':
                tasks_list.append(task)   
        
        def get_tasks():
            # Формируется список задач tasks_list из БД. Выбирается случайная задача из списка tasks_list, затем выбранная задача удаляется из списка.
            task = random.choice(tasks_list)
            tasks_list.remove(task)
            return task
        
        # заполнение полей случайными неповторяющимися задачами из списка tasks_list, если поля пустые. Если в базе данных меньше 6 задач, выводит сообщение об этом.
        if len(tasks_list) < 7:
            error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть не меньше 7 задач!")    
        elif ui.label_13.text() == '':
            ui.label_13.setText(f'{get_tasks()}')
            ui.label_14.setText(f'{get_tasks()}')
            ui.label_15.setText(f'{get_tasks()}')
            ui.label_16.setText(f'{get_tasks()}')
            ui.label_17.setText(f'{get_tasks()}')
            ui.label_18.setText(f'{get_tasks()}')
            ui.label_32.setText(f'{get_tasks()}')
            
    def choose_talents():
        # создаем список талантов из БД
        cursor = connection.cursor()
        cursor.execute("SELECT talent FROM `talent`")
        talents_tuple_list = cursor.fetchall()
        talents_list = []
        for i in talents_tuple_list:
            talent = ''.join(i)
            if talent != '':
                talents_list.append(talent)
                   
        def get_talents():
            # Формируется список талантов talents_list из БД. Выбирается случайный талант из списка talents_list, затем выбранный талант удаляется из списка.
            talent = random.choice(talents_list)
            talents_list.remove(talent)
            return talent   
        
        # заполнение полей случайными неповторяющимися талантами из списка talents_list, если поля пустые. Если в базе данных меньше 6 талантов, выводит сообщение об этом.
        if len(talents_list) < 7:
            error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть не меньше 7 талантов!")   
        elif ui.label_19.text() == '':
            ui.label_19.setText(f'{get_talents()}')
            ui.label_20.setText(f'{get_talents()}')
            ui.label_21.setText(f'{get_talents()}')
            ui.label_22.setText(f'{get_talents()}')
            ui.label_23.setText(f'{get_talents()}')
            ui.label_24.setText(f'{get_talents()}')
            ui.label_33.setText(f'{get_talents()}')
        
    def choose_roles_1():
        # создаем список ролей из БД
        cursor = connection.cursor()
        cursor.execute("SELECT role FROM `role`")
        roles_tuple_list = cursor.fetchall()
        roles_list = []
        for i in roles_tuple_list:
            role = ''.join(i)
            if role != '':
                roles_list.append(role)
        
        def get_roles():
            # выбирается случайная роль из списка roles_list. Из списка удаляется выбранная роль.  
            role = random.choice(roles_list)
            roles_list.remove(role)
            return role  
    
        # заполнение полей случайными неповторяющимися ролями из списка roles_list. В поле первого игрока вставляется надпись "Главный". 
        # Если в базе данных ролей недостаточно, выводит сообщение об этом.
        if ui.comboBox.currentIndex() == 4: # 3 игрока            
            if len(roles_list) != 4:
                error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 4 роли!") 
            elif ui.label_25.text() != 'Главный':
                ui.label_25.setText(f'Главный')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'{get_roles()}')
                
        elif ui.comboBox.currentIndex() == 3: # 4 игрока            
            if len(roles_list) != 5:
                error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 5 ролей!") 
            elif ui.label_25.text() != 'Главный':
                ui.label_25.setText(f'Главный')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'{get_roles()}')
                   
        elif ui.comboBox.currentIndex() == 2: # 5 игроков
            if len(roles_list) != 6:
                error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 6 ролей!") 
            elif ui.label_25.text() != 'Главный':
                ui.label_25.setText(f'Главный')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'{get_roles()}')                 
                ui.label_29.setText(f'{get_roles()}')
                
        elif ui.comboBox.currentIndex() == 1: # 6 игроков
            if len(roles_list) != 7:
                error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 7 ролей!") 
            elif ui.label_25.text() != 'Главный':
                ui.label_25.setText(f'Главный')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'{get_roles()}')                 
                ui.label_29.setText(f'{get_roles()}')           
                ui.label_30.setText(f'{get_roles()}')
                
        elif ui.comboBox.currentIndex() == 0: # 7 игроков
            if len(roles_list) != 8:
                error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 8 ролей!") 
            elif ui.label_25.text() != 'Главный':
                ui.label_25.setText(f'Главный')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'{get_roles()}')                 
                ui.label_29.setText(f'{get_roles()}')           
                ui.label_30.setText(f'{get_roles()}')
                ui.label_34.setText(f'{get_roles()}')
        
    def choose_roles_2():
        # создаем список ролей из БД
        cursor = connection.cursor()
        cursor.execute("SELECT role FROM `role`")
        roles_tuple_list = cursor.fetchall()
        roles_list = []
        for i in roles_tuple_list:
            role = ''.join(i)
            if role != '':
                roles_list.append(role)
        
        def get_roles():
            # выбирается случайная роль из списка roles_list. Из списка удаляется выбранная роль.  
            role = random.choice(roles_list)
            roles_list.remove(role)
            return role  
    
        # заполнение полей случайными неповторяющимися ролями из списка roles_list. В поле второго игрока вставляется надпись "Главный". 
        # Если в базе данных ролей недостаточно, выводит сообщение об этом.        
        if ui.comboBox.currentIndex() == 4: # 3 игрока            
            if len(roles_list) != 4:
                error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 4 роли!") 
            elif ui.label_26.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'Главный')
                ui.label_27.setText(f'{get_roles()}')
                
        elif ui.comboBox.currentIndex() == 3: # 4 игрока            
            if len(roles_list) != 5:
                error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 5 ролей!") 
            elif ui.label_26.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'Главный')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'{get_roles()}')
                   
        elif ui.comboBox.currentIndex() == 2: # 5 игроков
            if len(roles_list) != 6:
                error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 6 ролей!") 
            elif ui.label_26.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'Главный')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'{get_roles()}')                 
                ui.label_29.setText(f'{get_roles()}')
                
        elif ui.comboBox.currentIndex() == 1: # 6 игроков
            if len(roles_list) != 7:
                error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 7 ролей!") 
            elif ui.label_26.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'Главный')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'{get_roles()}')                 
                ui.label_29.setText(f'{get_roles()}')           
                ui.label_30.setText(f'{get_roles()}')
        
        elif ui.comboBox.currentIndex() == 0: # 7 игроков
            if len(roles_list) != 8:
                error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 8 ролей!") 
            elif ui.label_26.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'Главный')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'{get_roles()}')                 
                ui.label_29.setText(f'{get_roles()}')           
                ui.label_30.setText(f'{get_roles()}')
                ui.label_34.setText(f'{get_roles()}')
        
    def choose_roles_3():
        # создаем список ролей из БД
        cursor = connection.cursor()
        cursor.execute("SELECT role FROM `role`")
        roles_tuple_list = cursor.fetchall()
        roles_list = []
        for i in roles_tuple_list:
            role = ''.join(i)
            if role != '':
                roles_list.append(role)
        
        def get_roles():
            # выбирается случайная роль из списка roles_list. Из списка удаляется выбранная роль.  
            role = random.choice(roles_list)
            roles_list.remove(role)
            return role  
    
        # заполнение полей случайными неповторяющимися ролями из списка roles_list. В поле третьего игрока вставляется надпись "Главный". 
        # Если в базе данных ролей недостаточно, выводит сообщение об этом.
        if ui.comboBox.currentIndex() == 4: # 3 игрока            
            if len(roles_list) != 4:
                error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 4 роли!") 
            elif ui.label_27.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'Главный')
                
        elif ui.comboBox.currentIndex() == 3: # 4 игрока            
            if len(roles_list) != 5:
                error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 5 ролей!") 
            elif ui.label_27.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'Главный')
                ui.label_28.setText(f'{get_roles()}')
                   
        elif ui.comboBox.currentIndex() == 2: # 5 игроков
            if len(roles_list) != 6:
                error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 6 ролей!") 
            elif ui.label_27.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'Главный')
                ui.label_28.setText(f'{get_roles()}')                 
                ui.label_29.setText(f'{get_roles()}')
                
        elif ui.comboBox.currentIndex() == 1: # 6 игроков
            if len(roles_list) != 7:
                error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 7 ролей!") 
            elif ui.label_27.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'Главный')
                ui.label_28.setText(f'{get_roles()}')                 
                ui.label_29.setText(f'{get_roles()}')           
                ui.label_30.setText(f'{get_roles()}')
                
        elif ui.comboBox.currentIndex() == 0: # 7 игроков
            if len(roles_list) != 8:
                error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 8 ролей!") 
            elif ui.label_27.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'Главный')
                ui.label_28.setText(f'{get_roles()}')                 
                ui.label_29.setText(f'{get_roles()}')           
                ui.label_30.setText(f'{get_roles()}')
                ui.label_34.setText(f'{get_roles()}')
        
    def choose_roles_4():
        # создаем список ролей из БД
        cursor = connection.cursor()
        cursor.execute("SELECT role FROM `role`")
        roles_tuple_list = cursor.fetchall()
        roles_list = []
        for i in roles_tuple_list:
            role = ''.join(i)
            if role != '':
                roles_list.append(role)
        
        def get_roles():
            # выбирается случайная роль из списка roles_list. Из списка удаляется выбранная роль.  
            role = random.choice(roles_list)
            roles_list.remove(role)
            return role  
    
        # заполнение полей случайными неповторяющимися ролями из списка roles_list. В поле четвертого игрока вставляется надпись "Главный". 
        # Если в базе данных ролей недостаточно, выводит сообщение об этом. 
        if ui.comboBox.currentIndex() == 3: # 4 игрока            
            if len(roles_list) !=5:
                error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 5 ролей!") 
            elif ui.label_28.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'Главный')
                   
        elif ui.comboBox.currentIndex() == 2: # 5 игроков
            if len(roles_list) != 6:
                error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 6 ролей!") 
            elif ui.label_28.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'Главный')                 
                ui.label_29.setText(f'{get_roles()}')
                
        elif ui.comboBox.currentIndex() == 1: # 6 игроков
            if len(roles_list) != 7:
                error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 7 ролей!") 
            elif ui.label_28.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'Главный')                 
                ui.label_29.setText(f'{get_roles()}')           
                ui.label_30.setText(f'{get_roles()}')
                
        elif ui.comboBox.currentIndex() == 0: # 7 игроков
            if len(roles_list) != 8:
                error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 8 ролей!") 
            elif ui.label_28.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'Главный')                 
                ui.label_29.setText(f'{get_roles()}')           
                ui.label_30.setText(f'{get_roles()}')
                ui.label_34.setText(f'{get_roles()}')
        
    def choose_roles_5():
        # создаем список ролей из БД
        cursor = connection.cursor()
        cursor.execute("SELECT role FROM `role`")
        roles_tuple_list = cursor.fetchall()
        roles_list = []
        for i in roles_tuple_list:
            role = ''.join(i)
            if role != '':
                roles_list.append(role)
        
        def get_roles():
            # выбирается случайная роль из списка roles_list. Из списка удаляется выбранная роль.  
            role = random.choice(roles_list)
            roles_list.remove(role)
            return role  
    
        # заполнение полей случайными неповторяющимися ролями из списка roles_list. В поле пятого игрока вставляется надпись "Главный". 
        # Если в базе данных ролей недостаточно, выводит сообщение об этом.
        if ui.comboBox.currentIndex() == 2: # 5 игроков
            if len(roles_list) != 6:
                error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 6 ролей!") 
            elif ui.label_29.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'{get_roles()}')                 
                ui.label_29.setText(f'Главный')
                
        elif ui.comboBox.currentIndex() == 1: # 6 игроков
            if len(roles_list) != 7:
                error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 7 ролей!") 
            elif ui.label_27.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'{get_roles()}')                 
                ui.label_29.setText(f'Главный')           
                ui.label_30.setText(f'{get_roles()}')
                
        elif ui.comboBox.currentIndex() == 0: # 7 игроков
            if len(roles_list) != 8:
                error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 8 ролей!") 
            elif ui.label_27.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'{get_roles()}')                 
                ui.label_29.setText(f'Главный')           
                ui.label_30.setText(f'{get_roles()}')
                ui.label_34.setText(f'{get_roles()}')
            
    def choose_roles_6():
        # создаем список ролей из БД
        cursor = connection.cursor()
        cursor.execute("SELECT role FROM `role`")
        roles_tuple_list = cursor.fetchall()
        roles_list = []
        for i in roles_tuple_list:
            role = ''.join(i)
            if role != '':
                roles_list.append(role)
        
        def get_roles():
            # выбирается случайная роль из списка roles_list. Из списка удаляется выбранная роль.  
            role = random.choice(roles_list)
            roles_list.remove(role)
            return role  
    
        # заполнение полей случайными неповторяющимися ролями из списка roles_list. В поле шестого игрока вставляется надпись "Главный". 
        # Если в базе данных ролей недостаточно, выводит сообщение об этом. 
        if ui.comboBox.currentIndex() == 1: # 6 игроков
            if len(roles_list) != 7:
                error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 7 ролей!") 
            elif ui.label_27.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'{get_roles()}')                 
                ui.label_29.setText(f'{get_roles()}')           
                ui.label_30.setText(f'Главный')
                
        elif ui.comboBox.currentIndex() == 0: # 7 игроков
            if len(roles_list) != 8:
                error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 8 ролей!") 
            elif ui.label_27.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'{get_roles()}')                 
                ui.label_29.setText(f'{get_roles()}')           
                ui.label_30.setText(f'Главный')
                ui.label_34.setText(f'{get_roles()}')
                
    def choose_roles_7():
        # создаем список ролей из БД
        cursor = connection.cursor()
        cursor.execute("SELECT role FROM `role`")
        roles_tuple_list = cursor.fetchall()
        roles_list = []
        for i in roles_tuple_list:
            role = ''.join(i)
            if role != '':
                roles_list.append(role)
        
        def get_roles():
            # выбирается случайная роль из списка roles_list. Из списка удаляется выбранная роль.  
            role = random.choice(roles_list)
            roles_list.remove(role)
            return role  
    
        # заполнение полей случайными неповторяющимися ролями из списка roles_list. В поле седьмого игрока вставляется надпись "Главный". 
        # Если в базе данных ролей недостаточно, выводит сообщение об этом. 
        if ui.comboBox.currentIndex() == 0: # 7 игроков
            if len(roles_list) != 8:
                error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 8 ролей!") 
            elif ui.label_27.text() != 'Главный':
                ui.label_25.setText(f'{get_roles()}')
                ui.label_26.setText(f'{get_roles()}')
                ui.label_27.setText(f'{get_roles()}')
                ui.label_28.setText(f'{get_roles()}')                 
                ui.label_29.setText(f'{get_roles()}')           
                ui.label_30.setText(f'{get_roles()}')
                ui.label_34.setText(f'Главный')
            
    def restart_1():      
        subprocess.Popen('Hero Life.exe')    
        
    def restart_2():    
        exit()
        
    def error_message(text):
        error = QMessageBox()
        error.setWindowTitle("Ошибка")
        error.setText(text)
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        
        error.exec_()
        
    ui.pushButton.clicked.connect(choose_heroes)
    ui.pushButton_2.clicked.connect(choose_tasks)
    ui.pushButton_3.clicked.connect(choose_talents)
    ui.pushButton_4.clicked.connect(choose_roles_1)
    ui.pushButton_5.clicked.connect(choose_roles_2)
    ui.pushButton_6.clicked.connect(choose_roles_3)
    ui.pushButton_7.clicked.connect(choose_roles_4)
    ui.pushButton_8.clicked.connect(choose_roles_5)
    ui.pushButton_9.clicked.connect(choose_roles_6)
    ui.pushButton_13.clicked.connect(choose_roles_7)
    ui.pushButton_10.clicked.connect(number_of_players)
    ui.pushButton_11.clicked.connect(restart_1)
    ui.pushButton_11.clicked.connect(restart_2)
    ui.pushButton_12.clicked.connect(db)
        
    sys.exit(app.exec_())
        
except Exception as ex:
    print('Connection refused')
    print(ex)