# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.
'''
import os
import sys
import shutil

file_mane = os.path.realrath(input("Укажите название файла "))


def cp(file_name):
	pass


def rm(file_name):
	q = input('Вы действительно хотите удалить указанный объект?  Д/Н ')
	if q == 'Д':	
		try:
        	os.remove(file_name)
        		print('файл {} удален'.format(file_name))
    		except FileNotFoundError:
        		print('Не удается найти файл')
	elif: q == 'Н':
		break
	else:
		print('Неверная команда')


def cd(file_path):	
	try:
        os.chdir(file_path)
        	print('директория изменена {} '.format(file_path))
    	except FileNotFoundError:
        	print('Не удается найти путь')
 

def ls():
	print(os.getcwd())

'''
