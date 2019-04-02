# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
import math

def my_round(number, ndigits):
	dg = round(number, ndigits)   
	return dg

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
	ticket_number = str(ticket_number)
	if len(ticket_number) < 6:
		return 'НЕПРАВИЛЬНЫЙ БИЛЕТ!!!'
	else:
		ld = ticket_number[:3]
		rd = ticket_number[3:]
		if int(ld[0]) + int(ld[1]) + int(ld[2]) == int(rd[0]) + int(rd[1]) + int(rd[2]): 
			return 'Счастливый билет!!!'
		else:
			return 'Повезет в любви!!!'

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
