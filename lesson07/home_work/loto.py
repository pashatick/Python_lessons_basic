#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import random
import sys


class GameCard:
	def __init__(self, Name):
		self.players_name = Name
		self.cards_numbers = random.sample(range(90), 15)
		self.matrix = [['-']*9 for i in range(3)]	 
	
	def card_gen(self):
		arr = self.matrix		
		a = 0
		card = []			
		for lst in arr:
			c = 0
			i = 0		
			k = random.sample(range(9), 5)						
			while c < 5:							
				lst[k[i]] = self.cards_numbers[a] 
				c += 1
				i += 1
				a += 1		
		for i in arr:
			card.append(i)
		return card

babulya = GameCard(input('Введите сове имя: '))
computer = GameCard('Компухтер')

babulya_card = babulya.card_gen()
computer_card = computer.card_gen()


def print_card(name, arr):
	print('{:-^40}'.format(name.players_name))	
	for i in arr:
		print(i)

print_card(babulya, babulya_card)
print_card(computer, computer_card)

keg_list = random.sample(range(90), 90)

def find_empty(player, arr, line):
	if arr == [['-']*9 for i in range(3)]:
		print('{} WIN!!!'.format(player.players_name))
		sys.exit()	
	if line == ['-']*9:
		print('У игрока {} Квартира!!!'.format(player.players_name))
		
def Game(keg, name_player1, name_player2, player1_card, player2_card):
	c = 89		
	for digit in keg:				
		print('Бочёнок № {}'.format(digit))
		print('Осталось ходов {}'.format(c))		
		answer = input('Хотите убрать цифру? Y/N')
		print('#'*50)
		print('#'*50)		
		if answer == 'Y':
			t = 0			
			for line in player1_card:				
				if digit in line:
					line[line.index(digit)] = '-'
				else:
					t += 1 
				if t == 3:
					print('Такого номера нет в вашей карте! \n Вы проиграли!!! ;(')
					sys.exit()
				find_empty(name_player1, player1_card, line)		
		
		elif answer == 'N':
			for line in player1_card:
				if digit in line:
					print('Вы пропустили бочёнок! \n Вы проиграли!!! ;(')
					sys.exit()
		
		else:
			print('Вы пропустили бочёнок! \n Вы проиграли!!! ;(')
			sys.exit()
		for line in player2_card:
			if digit in line:
				line[line.index(digit)] = '-'
			find_empty(name_player2, player2_card, line)

		print_card(name_player1, player1_card) 
		print()		
		print_card(name_player2, player2_card)
		c -= 1

Game(keg_list, babulya, computer, babulya_card, computer_card)			




























  










