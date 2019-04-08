# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

import os

class Workers_name:
	def __init__(self, Name, Surname):
		self.Name = Name
		self.Surname = Surname
		self.fullname = self.Name + ' ' + self.Surname

class Works_hours(Workers_name):
	def __init__(self, Name, Surname, Hours):
		super().__init__(Name, Surname)		
		self.Hours = int(Hours)
		self.works_d = {self.fullname: self.Hours}

class Workers(Workers_name):
	def __init__(self, Name, Surname, Money, Special, Hours):
		super().__init__(Name, Surname)
		self.Money = int(Money)
		self.Hours = int(Hours)
		self.MPH = self.Money / self.Hours 
	
	
wanted_name = input("Введите фамилию сотрудника ")

money_list = []

with open(os.path.join('data', 'hours_of'), 'r', encoding='UTF-8') as hours:
	for line in hours:
		if wanted_name in line:		
			per = tuple(line.split())
			W_H = Works_hours(per[0], per[1],per[2])
			
				

with open(os.path.join('data', 'workers'), 'r', encoding='UTF-8') as workers:
	for line in workers:		
		if wanted_name in line:					
			per = (line.split())
			W_M = Workers(per[0], per[1], per[2], per[3], per[4])
			print('Зарплата сотрудника {}'.format(W_M.fullname))			
			if W_M.Hours == W_H.Hours:
				print(W_M.Money)
			elif W_M.Hours > W_H.Hours:
				print (W_M.Money - ((W_M.Hours - W_H.Hours) * W_M.MPH))
			elif W_M.Hours < W_H.Hours:
				print (W_M.Money + ((W_H.Hours - W_M.Hours) * 2 * W_M.MPH))

