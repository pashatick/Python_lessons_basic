import os
import sys
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


n = 9

def mk_dir(path):	
	os.mkdir(path)

def ch_dir(path):
	os.chdir(path)

def del_dir(path):	
	ch_dir(path)
	#shutil.rmtree(path) # для рекурсивного удаления		
	os.rmdir(path)


for i in range(n):
	dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(i+1))
	mk_dir(dir_path)


for i in range(n):
	path = '/home/pavel/Python_lessons_basic/lesson05/home_work/dir_{}'.format(i+1)	
	del_dir(path)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dir(path):
    for i in os.listdir(path):
        print(i)

path1 = os.getcwd()
list_dir(path1)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

file = sys.argv[0]

def cp_file(file):
	cp_file = 'cp_' + file
	shutil.copy(file, cp_file)

cp_file(file)

