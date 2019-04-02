# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

fib_arr = [0]

def fibonacci(n, m):
	i = 0
	fib_arr.append(n)
	while int(fib_arr[-1]) < m:
		x = int(fib_arr[i]) + int(fib_arr[i+1])
		fib_arr.append(x)
		i += 1
		
		
fibonacci(1, 344)
print(fib_arr[:-1])	
# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


a = [2, 10, -12, 2.5 , 20, -11, 4, 4, 0]
N = len(a)
print(N)
def sort_to_max(a):
	for i in range(N-1):
    		for j in range(N-i-1):
        		if a[j] > a[j+1]:
        		    a[j], a[j+1] = a[j+1], a[j]
	return a
print(sort_to_max(a))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
arr = [0, '', 0, '', 0, 1, 1, 0]
nr = []
def not_null(arr):
	for i in arr:
		if i == 1:
			return i
q = not_null(arr)
print(q)



def my_filter(df, arr):
	a = []	
	for i in arr:	
		if df([i]) == True:
			a.append(i)
	return a

x = my_filter(not_null, arr)
print(x)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма

A1 = input('введите x1, y1: ')
A2 = input('введите x2, y2: ')
A3 = input('введите x3, y3: ')
A4 = input('введите x4, y4: ')

if A1[1] == A2[1] and A3[1] == A4[1] and (int(A1[0]) - int(A4[0])) == (int(A2[0]) - int(A3[0])):
	print("Заданные координаты - вершины параллелограмма")
else: 
	print("Неизвестная фигура")

