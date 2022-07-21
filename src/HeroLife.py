''' 

Коуч-игра "Жизнь героя". 
Количество игроков от 3 до 7.
Поля с именами игроков редактируемые, остальные заполняются при нажатии на соответствующие кнопки.
Перед началом игры необходимо заполнить базу данных, нажав на соответствующую кнопку.
Затем необходимо выбрать количество игроков в выпадающем списке и нажать кноку "ОК".
Герои, задачи и таланты из базы данных распределяются между игроками случайным образом, не повторяясь.
При распределении ролей в поле активного игрока всегда всталяется значение "Главный", 
между остальными игроками роли распределяются случайным образом.

 
'''

from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QMessageBox
import sqlite3

from HeroLifeUI import Ui_HeroLife

import sys
import random
import subprocess


connection = sqlite3.connect('db.sqlite3')

# start Qt widget
app = QtWidgets.QApplication(sys.argv)
HeroLife = QtWidgets.QMainWindow()
ui = Ui_HeroLife()
ui.setupUi(HeroLife)
HeroLife.show()

def db():
    # open database window.
    subprocess.Popen('Database.exe')        

def number_of_players():    
    # hide or show elements depending on the number of players. By default is 7 players.    
    if ui.num_of_players_box.currentIndex() == 4: # 3 players
        ui.player4_lineedit.hide()
        ui.player5_lineedit.hide()
        ui.player6_lineedit.hide()
        ui.player7_lineedit.hide()
        ui.hero4_label.hide()
        ui.hero5_label.hide()
        ui.hero6_label.hide()
        ui.hero7_label.hide()
        ui.task4_label.hide()
        ui.task5_label.hide()
        ui.task6_label.hide()
        ui.task7_label.hide()
        ui.talent4_label.hide()
        ui.talent5_label.hide()
        ui.talent6_label.hide()
        ui.talent7_label.hide()
        ui.role4_label.hide()
        ui.role5_label.hide()
        ui.role6_label.hide()
        ui.role7_label.hide()
        ui.assign_role4_button.hide()
        ui.assign_role5_button.hide()
        ui.assign_role6_button.hide()
        ui.assign_role7_button.hide()
    elif ui.num_of_players_box.currentIndex() == 3:  # 4 players
        ui.player4_lineedit.show()
        ui.player5_lineedit.hide()
        ui.player6_lineedit.hide()
        ui.player7_lineedit.hide()
        ui.hero4_label.show()
        ui.hero5_label.hide()
        ui.hero6_label.hide()
        ui.hero7_label.hide()
        ui.task4_label.show()
        ui.task5_label.hide()
        ui.task6_label.hide()
        ui.task7_label.hide()
        ui.talent4_label.show()
        ui.talent5_label.hide()
        ui.talent6_label.hide()
        ui.talent7_label.hide()
        ui.role4_label.show()
        ui.role5_label.hide()
        ui.role6_label.hide()
        ui.role7_label.hide()
        ui.assign_role4_button.show()
        ui.assign_role5_button.hide()
        ui.assign_role6_button.hide()
        ui.assign_role7_button.hide()
    elif ui.num_of_players_box.currentIndex() == 2: # 5 players
        ui.player4_lineedit.show()
        ui.player5_lineedit.show()
        ui.player6_lineedit.hide()
        ui.player7_lineedit.hide()
        ui.hero4_label.show()
        ui.hero5_label.show()
        ui.hero6_label.hide()
        ui.hero7_label.hide()
        ui.task4_label.show()
        ui.task5_label.show()
        ui.task6_label.hide()
        ui.task7_label.hide()
        ui.talent4_label.show()
        ui.talent5_label.show()
        ui.talent6_label.hide()
        ui.talent7_label.hide()
        ui.role4_label.show()
        ui.role5_label.show()
        ui.role6_label.hide()
        ui.role7_label.hide()
        ui.assign_role4_button.show()
        ui.assign_role5_button.show()
        ui.assign_role6_button.hide()
        ui.assign_role7_button.hide()
    elif ui.num_of_players_box.currentIndex() == 1: # 6 players
        ui.player4_lineedit.show()
        ui.player5_lineedit.show()
        ui.player6_lineedit.show()
        ui.player7_lineedit.hide()
        ui.hero4_label.show()
        ui.hero5_label.show()
        ui.hero6_label.show()
        ui.hero7_label.hide()
        ui.task4_label.show()
        ui.task5_label.show()
        ui.task6_label.show()
        ui.task7_label.hide()
        ui.talent4_label.show()
        ui.talent5_label.show()
        ui.talent6_label.show()
        ui.talent7_label.hide()
        ui.role4_label.show()
        ui.role5_label.show()
        ui.role6_label.show()
        ui.role7_label.hide()
        ui.assign_role4_button.show()
        ui.assign_role5_button.show()
        ui.assign_role6_button.show()
        ui.assign_role7_button.hide()
    elif ui.num_of_players_box.currentIndex() == 0: # 7 players
        ui.player4_lineedit.show()
        ui.player5_lineedit.show()
        ui.player6_lineedit.show()
        ui.player7_lineedit.show()
        ui.hero4_label.show()
        ui.hero5_label.show()
        ui.hero6_label.show()
        ui.hero7_label.show()
        ui.task4_label.show()
        ui.task5_label.show()
        ui.task6_label.show()
        ui.task7_label.show()
        ui.talent4_label.show()
        ui.talent5_label.show()
        ui.talent6_label.show()
        ui.talent7_label.show()
        ui.role4_label.show()
        ui.role5_label.show()
        ui.role6_label.show()
        ui.role7_label.show()
        ui.assign_role4_button.show()
        ui.assign_role5_button.show()
        ui.assign_role6_button.show()
        ui.assign_role7_button.show()


def choose_heroes():
    # choose hero for every player.
    
    # create list of heroes from database.    
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM `hero`")
    heroes_tuple_list = cursor.fetchall()  # create list of tuples. 
    heroes_list = []
    for i in heroes_tuple_list:
        hero = ''.join(i)  
        if hero != '':
            heroes_list.append(hero)  # add a hero to the list if the hero's name contains at least 1 character.
    
    def get_heroes():
    # select a random hero from the heroes_list. The selected hero is removed from the list.  
         
        hero = random.choice(heroes_list)
        heroes_list.remove(hero)
        return hero

    # filling in fields with random non-repeating heroes from the heroes_list, if the fields are not filled in. If database have less then 7 heroes, it displays a message about it (according to the technical task). 
    if len(heroes_list) < 7:
        error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть не меньше 7 героев.")        
    elif ui.hero1_label.text() == '':
        ui.hero1_label.setText(f'{get_heroes()}')
        ui.hero2_label.setText(f'{get_heroes()}')
        ui.hero3_label.setText(f'{get_heroes()}')
        ui.hero4_label.setText(f'{get_heroes()}')
        ui.hero5_label.setText(f'{get_heroes()}')
        ui.hero6_label.setText(f'{get_heroes()}')
        ui.hero7_label.setText(f'{get_heroes()}')            
        
def choose_tasks():
    # choose task for every player.
    
    # create list of tasks from database. 
    
    cursor = connection.cursor()
    cursor.execute("SELECT task FROM `task`")
    task_tuple_list = cursor.fetchall()  # create list of tuples. 
    tasks_list = []
    for i in task_tuple_list:
        task = ''.join(i)  
        if task != '':
            tasks_list.append(task)   # add a task to the list if the task's name contains at least 1 character.
    
    def get_tasks():
        # select a random task from the tasks_list. The selected task is removed from the list.  
        
        task = random.choice(tasks_list)
        tasks_list.remove(task)
        return task
    
    # filling in fields with random non-repeating tasks from the tasks_list, if the fields are not filled in. If database have less then 7 tasks, it displays a message about it (according to the technical task).
    if len(tasks_list) < 7:
        error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть не меньше 7 задач.")    
    elif ui.task1_label.text() == '':
        ui.task1_label.setText(f'{get_tasks()}')
        ui.task2_label.setText(f'{get_tasks()}')
        ui.task3_label.setText(f'{get_tasks()}')
        ui.task4_label.setText(f'{get_tasks()}')
        ui.task5_label.setText(f'{get_tasks()}')
        ui.task6_label.setText(f'{get_tasks()}')
        ui.task7_label.setText(f'{get_tasks()}')
        
def choose_talents():
    # choose talent for every player.
    
    # create list of talents from database. 
    
    cursor = connection.cursor()
    cursor.execute("SELECT talent FROM `talent`")
    talents_tuple_list = cursor.fetchall()  # create list of tuples. 
    talents_list = []
    for i in talents_tuple_list:
        talent = ''.join(i)
        if talent != '':
            talents_list.append(talent)  # add a talent to the list if the talents's name contains at least 1 character.
                
    def get_talents():
        # select a random talent from the talents_list. The selected talent is removed from the list.  
        talent = random.choice(talents_list)
        talents_list.remove(talent)
        return talent   
    
    # filling in fields with random non-repeating talents from the talents_list, if the fields are not filled in. If database have less then 7 talents, it displays a message about it (according to the technical task).
    if len(talents_list) < 7:
        error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть не меньше 7 талантов.")   
    elif ui.talent1_label.text() == '':
        ui.talent1_label.setText(f'{get_talents()}')
        ui.talent2_label.setText(f'{get_talents()}')
        ui.talent3_label.setText(f'{get_talents()}')
        ui.talent4_label.setText(f'{get_talents()}')
        ui.talent5_label.setText(f'{get_talents()}')
        ui.talent6_label.setText(f'{get_talents()}')
        ui.talent7_label.setText(f'{get_talents()}') 
 

roles_list = []

def populate_roles_list():
    # populate the list with values from the database
    global roles_list
    roles_list = []    
    cursor = connection.cursor()
    cursor.execute("SELECT role FROM `role`")
    roles_tuple_list = cursor.fetchall()    
    for i in roles_tuple_list:
        role = ''.join(i)
        if role != '':
            roles_list.append(role)         
               
def get_roles():    
    # select a random role from the talents_list. The selected role is removed from the list.  
    role = random.choice(roles_list)
    roles_list.remove(role)
    return role  
     
def assign_roles_1():   
    # filling in fields with random non-repeating talents from the roles_list. Into the field of the player 1 inserted the inscription "Главный". 
    # If in the database are not enough roles, it displays a message about this.
    
    global roles_list 
    if ui.num_of_players_box.currentIndex() == 4: # 3 players            
        if len(roles_list) != 4:
            error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 4 роли.") 
        elif ui.role1_label.text() != 'Главный':
            ui.role2_label.setText(f'Главный')
            ui.role3_label.setText(f'{get_roles()}')
            ui.role4_label.setText(f'{get_roles()}')
            roles_list = []
            
    elif ui.num_of_players_box.currentIndex() == 3: # 4 players            
        if len(roles_list) != 5:
            error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 5 ролей.") 
        elif ui.role1_label.text() != 'Главный':
            ui.role1_label.setText(f'Главный')
            ui.role2_label.setText(f'{get_roles()}')
            ui.role3_label.setText(f'{get_roles()}')
            ui.role4_label.setText(f'{get_roles()}')
            roles_list = []
                
    elif ui.num_of_players_box.currentIndex() == 2: # 5 players
        if len(roles_list) != 6:
            error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 6 ролей.") 
        elif ui.role1_label.text() != 'Главный':
            ui.role1_label.setText(f'Главный')
            ui.role2_label.setText(f'{get_roles()}')
            ui.role3_label.setText(f'{get_roles()}')
            ui.role4_label.setText(f'{get_roles()}')                 
            ui.role5_label.setText(f'{get_roles()}')
            roles_list = []
            
    elif ui.num_of_players_box.currentIndex() == 1: # 6 players
        if len(roles_list) != 7:
            error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 7 ролей.") 
        elif ui.role1_label.text() != 'Главный':
            ui.role1_label.setText(f'Главный')
            ui.role2_label.setText(f'{get_roles()}')
            ui.role3_label.setText(f'{get_roles()}')
            ui.role4_label.setText(f'{get_roles()}')                 
            ui.role5_label.setText(f'{get_roles()}')
            ui.role6_label.setText(f'{get_roles()}')
            roles_list = []
            
    elif ui.num_of_players_box.currentIndex() == 0: # 7 players
        if len(roles_list) != 8:
            error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 8 ролей.") 
        elif ui.role1_label.text() != 'Главный':
            ui.role1_label.setText(f'Главный')
            ui.role2_label.setText(f'{get_roles()}')
            ui.role3_label.setText(f'{get_roles()}')
            ui.role4_label.setText(f'{get_roles()}')                 
            ui.role5_label.setText(f'{get_roles()}')
            ui.role6_label.setText(f'{get_roles()}')
            ui.role7_label.setText(f'{get_roles()}')
            roles_list = []
    
def assign_roles_2():   
    # filling in fields with random non-repeating talents from the roles_list. Into the field of the player 2 inserted the inscription "Главный". 
    # If in the database are not enough roles, it displays a message about this.
    
    global roles_list       
    if ui.num_of_players_box.currentIndex() == 4: # 3 players            
        if len(roles_list) != 4:
            error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 4 роли.") 
        elif ui.role2_label.text() != 'Главный':
            ui.role1_label.setText(f'{get_roles()}')
            ui.role2_label.setText(f'Главный')
            ui.role3_label.setText(f'{get_roles()}')
            
    elif ui.num_of_players_box.currentIndex() == 3: # 4 players            
        if len(roles_list) != 5:
            error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 5 ролей.") 
        elif ui.role2_label.text() != 'Главный':
            ui.role1_label.setText(f'{get_roles()}')
            ui.role2_label.setText(f'Главный')
            ui.role3_label.setText(f'{get_roles()}')
            ui.role4_label.setText(f'{get_roles()}')
                
    elif ui.num_of_players_box.currentIndex() == 2: # 5 players
        if len(roles_list) != 6:
            error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 6 ролей.") 
        elif ui.role2_label.text() != 'Главный':
            ui.role1_label.setText(f'{get_roles()}')
            ui.role2_label.setText(f'Главный')
            ui.role3_label.setText(f'{get_roles()}')
            ui.role4_label.setText(f'{get_roles()}')                 
            ui.role5_label.setText(f'{get_roles()}')
            roles_list = []
            
    elif ui.num_of_players_box.currentIndex() == 1: # 6 players
        if len(roles_list) != 7:
            error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 7 ролей.") 
        elif ui.role2_label.text() != 'Главный':
            ui.role1_label.setText(f'{get_roles()}')
            ui.role2_label.setText(f'Главный')
            ui.role3_label.setText(f'{get_roles()}')
            ui.role4_label.setText(f'{get_roles()}')                 
            ui.role5_label.setText(f'{get_roles()}')           
            ui.role6_label.setText(f'{get_roles()}')
    
    elif ui.num_of_players_box.currentIndex() == 0: # 7 players
        if len(roles_list) != 8:
            error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 8 ролей.") 
        elif ui.role2_label.text() != 'Главный':
            ui.role1_label.setText(f'{get_roles()}')
            ui.role2_label.setText(f'Главный')
            ui.role3_label.setText(f'{get_roles()}')
            ui.role4_label.setText(f'{get_roles()}')                 
            ui.role5_label.setText(f'{get_roles()}')           
            ui.role6_label.setText(f'{get_roles()}')
            ui.role7_label.setText(f'{get_roles()}')
    
def assign_roles_3():
    # filling in fields with random non-repeating talents from the roles_list. Into the field of the player 3 inserted the inscription "Главный". 
    # If in the database are not enough roles, it displays a message about this.
    
    global roles_list 
    if ui.num_of_players_box.currentIndex() == 4: # 3 players            
        if len(roles_list) != 4:
            error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 4 роли.") 
        elif ui.role3_label.text() != 'Главный':
            ui.role1_label.setText(f'{get_roles()}')
            ui.role2_label.setText(f'{get_roles()}')
            ui.role3_label.setText(f'Главный')
            
    elif ui.num_of_players_box.currentIndex() == 3: # 4 players            
        if len(roles_list) != 5:
            error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 5 ролей.") 
        elif ui.role3_label.text() != 'Главный':
            ui.role1_label.setText(f'{get_roles()}')
            ui.role2_label.setText(f'{get_roles()}')
            ui.role3_label.setText(f'Главный')
            ui.role4_label.setText(f'{get_roles()}')
                
    elif ui.num_of_players_box.currentIndex() == 2: # 5 players
        if len(roles_list) != 6:
            error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 6 ролей.") 
        elif ui.role3_label.text() != 'Главный':
            ui.role1_label.setText(f'{get_roles()}')
            ui.role2_label.setText(f'{get_roles()}')
            ui.role3_label.setText(f'Главный')
            ui.role4_label.setText(f'{get_roles()}')                 
            ui.role5_label.setText(f'{get_roles()}')
            roles_list = []
            
    elif ui.num_of_players_box.currentIndex() == 1: # 6 players
        if len(roles_list) != 7:
            error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 7 ролей.") 
        elif ui.role3_label.text() != 'Главный':
            ui.role1_label.setText(f'{get_roles()}')
            ui.role2_label.setText(f'{get_roles()}')
            ui.role3_label.setText(f'Главный')
            ui.role4_label.setText(f'{get_roles()}')                 
            ui.role5_label.setText(f'{get_roles()}')           
            ui.role6_label.setText(f'{get_roles()}')
            
    elif ui.num_of_players_box.currentIndex() == 0: # 7 players
        if len(roles_list) != 8:
            error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 8 ролей.") 
        elif ui.role3_label.text() != 'Главный':
            ui.role1_label.setText(f'{get_roles()}')
            ui.role2_label.setText(f'{get_roles()}')
            ui.role3_label.setText(f'Главный')
            ui.role4_label.setText(f'{get_roles()}')                 
            ui.role5_label.setText(f'{get_roles()}')           
            ui.role6_label.setText(f'{get_roles()}')
            ui.role7_label.setText(f'{get_roles()}')
    
def assign_roles_4():   
    # filling in fields with random non-repeating talents from the roles_list. Into the field of the player 4 inserted the inscription "Главный". 
    # If in the database are not enough roles, it displays a message about this.
    
    global roles_list
    if ui.num_of_players_box.currentIndex() == 3: # 4 players            
        if len(roles_list) !=5:
            error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 5 ролей.") 
        elif ui.role4_label.text() != 'Главный':
            ui.role1_label.setText(f'{get_roles()}')
            ui.role2_label.setText(f'{get_roles()}')
            ui.role3_label.setText(f'{get_roles()}')
            ui.role4_label.setText(f'Главный')
                
    elif ui.num_of_players_box.currentIndex() == 2: # 5 players
        if len(roles_list) != 6:
            error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 6 ролей.") 
        elif ui.role4_label.text() != 'Главный':
            ui.role1_label.setText(f'{get_roles()}')
            ui.role2_label.setText(f'{get_roles()}')
            ui.role3_label.setText(f'{get_roles()}')
            ui.role4_label.setText(f'Главный')                 
            ui.role5_label.setText(f'{get_roles()}')
            roles_list = []
            
    elif ui.num_of_players_box.currentIndex() == 1: # 6 players
        if len(roles_list) != 7:
            error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 7 ролей.") 
        elif ui.role4_label.text() != 'Главный':
            ui.role1_label.setText(f'{get_roles()}')
            ui.role2_label.setText(f'{get_roles()}')
            ui.role3_label.setText(f'{get_roles()}')
            ui.role4_label.setText(f'Главный')                 
            ui.role5_label.setText(f'{get_roles()}')           
            ui.role6_label.setText(f'{get_roles()}')
            
    elif ui.num_of_players_box.currentIndex() == 0: # 7 players
        if len(roles_list) != 8:
            error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 8 ролей.") 
        elif ui.role4_label.text() != 'Главный':
            ui.role1_label.setText(f'{get_roles()}')
            ui.role2_label.setText(f'{get_roles()}')
            ui.role3_label.setText(f'{get_roles()}')
            ui.role4_label.setText(f'Главный')                 
            ui.role5_label.setText(f'{get_roles()}')           
            ui.role6_label.setText(f'{get_roles()}')
            ui.role7_label.setText(f'{get_roles()}')
    
def assign_roles_5():
    # filling in fields with random non-repeating talents from the roles_list. Into the field of the player 5 inserted the inscription "Главный". 
    # If in the database are not enough roles, it displays a message about this.
    
    global roles_list
    if ui.num_of_players_box.currentIndex() == 2: # 5 players
        if len(roles_list) != 6:
            error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 6 ролей.") 
        elif ui.role5_label.text() != 'Главный':
            ui.role1_label.setText(f'{get_roles()}')
            ui.role2_label.setText(f'{get_roles()}')
            ui.role3_label.setText(f'{get_roles()}')
            ui.role4_label.setText(f'{get_roles()}')                 
            ui.role5_label.setText(f'Главный')
            roles_list = []
            
    elif ui.num_of_players_box.currentIndex() == 1: # 6 players
        if len(roles_list) != 7:
            error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 7 ролей.") 
        elif ui.role3_label.text() != 'Главный':
            ui.role1_label.setText(f'{get_roles()}')
            ui.role2_label.setText(f'{get_roles()}')
            ui.role3_label.setText(f'{get_roles()}')
            ui.role4_label.setText(f'{get_roles()}')                 
            ui.role5_label.setText(f'Главный')           
            ui.role6_label.setText(f'{get_roles()}')
            
    elif ui.num_of_players_box.currentIndex() == 0: # 7 players
        if len(roles_list) != 8:
            error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 8 ролей.") 
        elif ui.role3_label.text() != 'Главный':
            ui.role1_label.setText(f'{get_roles()}')
            ui.role2_label.setText(f'{get_roles()}')
            ui.role3_label.setText(f'{get_roles()}')
            ui.role4_label.setText(f'{get_roles()}')                 
            ui.role5_label.setText(f'Главный')           
            ui.role6_label.setText(f'{get_roles()}')
            ui.role7_label.setText(f'{get_roles()}')
        
def assign_roles_6():    
    # filling in fields with random non-repeating talents from the roles_list. Into the field of the player 6 inserted the inscription "Главный". 
    # If in the database are not enough roles, it displays a message about this.
    
    global roles_list
    if ui.num_of_players_box.currentIndex() == 1: # 6 players
        if len(roles_list) != 7:
            error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 7 ролей.") 
        elif ui.role3_label.text() != 'Главный':
            ui.role1_label.setText(f'{get_roles()}')
            ui.role2_label.setText(f'{get_roles()}')
            ui.role3_label.setText(f'{get_roles()}')
            ui.role4_label.setText(f'{get_roles()}')                 
            ui.role5_label.setText(f'{get_roles()}')           
            ui.role6_label.setText(f'Главный')
            
    elif ui.num_of_players_box.currentIndex() == 0: # 7 players
        if len(roles_list) != 8:
            error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 8 ролей.") 
        elif ui.role3_label.text() != 'Главный':
            ui.role1_label.setText(f'{get_roles()}')
            ui.role2_label.setText(f'{get_roles()}')
            ui.role3_label.setText(f'{get_roles()}')
            ui.role4_label.setText(f'{get_roles()}')                 
            ui.role5_label.setText(f'{get_roles()}')           
            ui.role6_label.setText(f'Главный')
            ui.role7_label.setText(f'{get_roles()}')
    
def assign_roles_7():    
   # filling in fields with random non-repeating talents from the roles_list. Into the field of the player 7 inserted the inscription "Главный". 
    # If in the database are not enough roles, it displays a message about this.
    
    global roles_list
    if ui.num_of_players_box.currentIndex() == 0: # 7 players
        if len(roles_list) != 8:
            error_message("Сейчас это действие выполнить невозможно. В базе данных должно быть 8 ролей.") 
        elif ui.role3_label.text() != 'Главный':
            ui.role1_label.setText(f'{get_roles()}')
            ui.role2_label.setText(f'{get_roles()}')
            ui.role3_label.setText(f'{get_roles()}')
            ui.role4_label.setText(f'{get_roles()}')                 
            ui.role5_label.setText(f'{get_roles()}')           
            ui.role6_label.setText(f'{get_roles()}')
            ui.role7_label.setText(f'Главный')

            
def restart_1():      
    subprocess.Popen('HeroLife.exe')    
    
def restart_2():    
    exit()
    
def error_message(text):
    error = QMessageBox()
    error.setWindowTitle("Ошибка")
    error.setText(text)
    error.setIcon(QMessageBox.Warning)
    error.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
    
    error.exec_()
    
ui.choose_hero_button.clicked.connect(choose_heroes)
ui.choose_task_button.clicked.connect(choose_tasks)
ui.choose_talent_button.clicked.connect(choose_talents)
ui.assign_role1_button.clicked.connect(populate_roles_list)
ui.assign_role1_button.clicked.connect(assign_roles_1)
ui.assign_role2_button.clicked.connect(populate_roles_list)
ui.assign_role2_button.clicked.connect(assign_roles_2)
ui.assign_role3_button.clicked.connect(populate_roles_list)
ui.assign_role3_button.clicked.connect(assign_roles_3)
ui.assign_role4_button.clicked.connect(populate_roles_list)
ui.assign_role4_button.clicked.connect(assign_roles_4)
ui.assign_role5_button.clicked.connect(populate_roles_list)
ui.assign_role5_button.clicked.connect(assign_roles_5)
ui.assign_role6_button.clicked.connect(populate_roles_list)
ui.assign_role6_button.clicked.connect(assign_roles_6)
ui.assign_role7_button.clicked.connect(populate_roles_list)
ui.assign_role7_button.clicked.connect(assign_roles_7)
ui.OK_button.clicked.connect(number_of_players)
ui.restart_button.clicked.connect(restart_1)
ui.restart_button.clicked.connect(restart_2)
ui.database_button.clicked.connect(db)
    
sys.exit(app.exec_())    