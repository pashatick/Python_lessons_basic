# Задание-1:
# Матрицы в питоне реализуются в виде вложенных списков:
# Пример. Дано:
matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2]]

print("rotate_matrix = ", list(map(list, zip(*matrix)))) #было в методичке(
          
# Выполнить поворот (транспонирование) матрицы
# Пример. Результат:
# matrix_rotate = [[1, 3, 0],
#                  [0, 4, 4],
#                  [8, 1, 2]]

# Суть сложности hard: Решите задачу в одну строку

# Задание-2:
# Найдите наибольшее произведение пяти последовательных цифр в 1000-значном числе.
# Выведите произведение и индекс смещения первого числа последовательных 5-ти цифр.
# Пример 1000-значного числа:
number = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""



def prod_5(s):
	prod = int(s[1])*int(s[2])*int(s[3])*int(s[4])*int(s[4])		
	return prod
#print(prod_5(s))

n = 0	
while n < 10:
	s = number[n:n+5]
	mx = 0		
	if mx < prod_5(s):
		mx = prod_5(s)
		index = number[n]
		print(s, prod_5(s), number[n], mx)
	else:
		mx = mx
	n += 1
print("Максимальное произведение", mx,'идекс', index)



# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
import random
fz_mt = matrix = [[random.randint(0, 0) for _ in range(9)] for _ in range(9)]
fz_mt[0] = [i for i in range(0, 9)]
n = 0
for i in fz_mt:
	i[0] = n
	n +=1
	 
for i in fz_mt: 	
	print(i)
poss = []
i = 0
while i < 8:
	i += 1
	print('Введите позицию фигуры (парой чисел: 11 или 23 или 54...)', i)
	poss.append(list(input()))

print(poss)

def line_mat(poss):
	mat = poss[0][0]	
	for i in poss:
		if i[0] == mat:
			return('YES')
		else:
			mat = i[0]
	return('NO')

def column_mat(poss):
	mat = poss[0][1]	
	for i in poss:
		if i[1] == mat:
			return('YES')
		else:
			mat = i[1]
	return('NO')


def diag_mat(poss):
	pass


if diag_mat(poss) == 'NO' and line_mat(poss) == 'NO' and column_mat(poss) == 'NO':
	print('Фигуры расставлены верно')
else:
	print('Ферзи бьют друг друга')
				  

 








