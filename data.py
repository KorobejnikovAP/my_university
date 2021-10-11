import pandas as pd
import numpy as np
from pathlib import *

university = pd.read_csv(Path.cwd() / 'assets' / 'university.csv')
plan_learn = pd.read_csv(Path.cwd() / 'assets' / 'plan_learning.csv')
ofline_un = pd.read_csv(Path.cwd() / 'assets' / 'ofline_un.csv')
online_un = pd.read_csv(Path.cwd() / 'assets' / 'online_un.csv')

# функция вычисляет затраты, необходимые как для онлайн, так и офлайн обучения 
def university_costs():
    sum = 0
    #зарплата и ежеквартальные бонусы преподавателям 
    for i in range(8):
        sum += plan_learn['coach_count'][i] * (university['salary_coach'][0] * 6 + 2 * university['bonus'][0])
    sum += sum * 0.3 
    #зарплата бухгалтера, методистов, системного администратора + бонусы
    sum += 12 * 4 * (university['salary_accountant'][0] + 2 * university['salary_met'][0] + university['salary_admin'][0])
    sum += 4 * 4 * 3 * university['bonus'][0]
    #оборудование
    sum += university['equipment'][0]
    return sum
#функция вычисляет доп. затраты на офлайн обучение     
def ofline_costs():
    sum = 0
    #аренда всех момещений
    sum += 4 * 12 * ofline_un['rent'][0] * ofline_un['square'][0]
    #зарплата охраннику и гардеробщице + ежеквартальные бонусы
    sum += 4 * 12 * (ofline_un['salary_secur'][0] + ofline_un['salary_checkroom'][0]) + 4 * 3 * 2 * ofline_un['bonus'][0]
    return sum
#функция вычисляет доп. затраты на онлай обучение 
def online_coast():
    sum = 0
    sum += 4 * 12 * (online_un['internet_price'][0] + online_un['zoom'][0])
    return sum
