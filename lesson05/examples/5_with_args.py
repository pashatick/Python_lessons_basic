# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")



def cp():
	pass


def rm():
	file_mane = os.path.realrath(input("Укажите название файла "))	
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


def cd():	
	file_mane = os.path.realrath(input("Укажите название файла "))
	try:
        os.chdir(file_path)
        	print('директория изменена {} '.format(file_path))
    	except FileNotFoundError:
        	print('Не удается найти путь')
 

def ls():
	print(os.getcwd())


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp, 
    "rm": rm, 
    "ls": ls, 
    "cd": cd 
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
