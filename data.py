import pandas as pd
import numpy as np
from pathlib import *

salary = pd.read_csv(Path.cwd() / 'assets' / 'salary.csv')
plan_learn = pd.read_csv(Path.cwd() / 'assets' / 'plan_learning.csv')
rent = pd.read_csv(Path.cwd() / 'assets' / 'rent.csv')
other_costs = pd.read_csv(Path.cwd() / 'assets' / 'other_costs.csv')

# функция вычисляет затраты, необходимые как для онлайн, так и офлайн обучения 
def university_costs():
    sum = 0
    #зарплата и ежеквартальные бонусы преподавателям 
    for i in range(8):
        sum += plan_learn['coach_count'][i] * (int(salary['salary'][salary.worker == 'coach']) * 6 + 2 * int(salary['bonus'][salary.worker == 'coach']))
    sum += sum * 0.3 
    #зарплата бухгалтера, методистов, системного администратора + бонусы
    sum += 12 * 4 * (int(salary['salary'][salary.worker == 'accountant']) + 2 * int(salary['salary'][salary.worker == 'methodist']) + int(salary['salary'][salary.worker == 'admin']))
    bonus = 0
    bonus += int(salary['bonus'][salary.worker == 'accountant'])
    bonus += int(salary['bonus'][salary.worker == 'methodist'])
    bonus += int(salary['bonus'][salary.worker == 'admin'])
    sum += 4 * 4 * 3 * bonus
    #оборудование
    sum += other_costs['equipment'][0]
    return sum
#функция вычисляет доп. затраты на офлайн обучение     
def offline_costs():
    sum = 0
    #аренда всех момещений
    sum += 4 * 12 * rent['rent_price'][0] * rent['square'][0]
    #зарплата охраннику и гардеробщице + ежеквартальные бонусы
    sum += 4 * 12 * (int(salary['salary'][salary.worker == 'security']) + int(salary['salary'][salary.worker == 'checkroom'])) 
    bonus = 0
    bonus += int(salary['bonus'][salary.worker == 'checkroom'])
    bonus += int(salary['bonus'][salary.worker == 'security'])
    sum += 4 * 3 * 2 * bonus
    return sum
#функция вычисляет доп. затраты на онлай обучение 
def online_costs():
    sum = 0
    sum += 4 * 12 * (other_costs['internet_price'][0] + other_costs['zoom'][0])
    return sum 

r = offline_costs()
print(r)