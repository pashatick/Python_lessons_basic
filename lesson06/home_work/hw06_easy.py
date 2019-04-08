import math
	
# Задача-1: 	
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


class Triangle:
	def __init__(self, ptA, ptB, ptC):
		self.ptA = ptA
		self.ptB = ptB
		self.ptC = ptC

	def line(self, point1, point2):
		return math.sqrt((point1[0] - point2[0])**2 
							+ (point1[1] - point2[1])**2)
	
	
	def areaTriangle(self): 
		semi_perimeter = self.line_sum() / 2
		return math.sqrt(semi_perimeter 
						* (semi_perimeter - self.line(self.ptA, self.ptB)) 
						* (semi_perimeter - self.line(self.ptB, self.ptC)) 
						* (semi_perimeter - self.line(self.ptC, self.ptA)))	
	
	def line_sum(self):
		return self.line(self.ptA, self.ptB) + self.line(self.ptB, self.ptC) + self.line(self.ptC, self.ptA)
	
	def tri_H(self):
		return self.areaTriangle() / (self.line(self.ptA, self.ptB) / 2)

tri1 = Triangle((4, 9), (16, 25), (36, 49))
print('Площадь треугольника', tri1.areaTriangle())
print('Периметр треугольника', tri1.line_sum())
print('Высота', tri1.tri_H())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapeze(Triangle):
	def __init__(self, ptA, ptB, ptC, ptD):
		super().__init__(ptA, ptB, ptC)		
		self.ptD = ptD
		self.lnAB = self.line(self.ptA, self.ptB)
		self.lnBC = self.line(self.ptB, self.ptC)
		self.lnCD = self.line(self.ptC, self.ptD)
		self.lnDA = self.line(self.ptD, self.ptA)	
	
	def areaTriangle2(self): 
		semi_perimeter = self.line_sum() / 2
		return math.sqrt(semi_perimeter 
						* (semi_perimeter - self.line(self.ptA, self.ptC)) 
						* (semi_perimeter - self.lnCD) 
						* (semi_perimeter - self.lnDA))

	def trap_area(self):
		return self.areaTriangle() + self.areaTriangle2()
	
	def line_sum_trap(self):
		 return self.lnAB + self.lnBC + self.lnCD + self.lnDA
	
	def uniside(self):
		if self.lnAB == self.lnCD and self.lnBC != self.lnDA:
			return 'Трапеция равнобочная'
		elif self.lnAB != self.lnCD and self.lnBC != self.lnDA:
			return 'Трапеция не равнобочная'
		else:
			return 'Другая фигура'  
		
	def side_long(self):
		return self.lnAB, self.lnBC, self.lnCD, self.lnDA

trap1 = Trapeze((4, 10), (16, 223), (36, 49), (56,72))

print()	

print('Периметр трапеции = ', trap1.line_sum_trap())
print('Площадь трапеции = ', trap1.trap_area())
print(trap1.uniside())	
print(trap1.side_long())
