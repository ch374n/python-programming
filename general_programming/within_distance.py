# program to find whether given point is within certain distance
import math

class Point:
	def __init__(self, x, y):
		self.__x = x
		self.__y = y

	@property
	def x(self):
		return self.__x

	@property
	def y(self):
		return self.__y

	def get_distance(self, point, distance):
		return math.sqrt(pow(point.x - self.x, 2) + pow(point.y - self.y, 2))			

	def is_within_distance(self, point, distance):
		if point.x - self.x > distance or point.y - self.y > distance:
			return False
		else:			
			return self.get_distance(point, distance) >= distance



point_1 = Point(10, 10)
point_2 = Point(5, 5)

print(point_1.is_within_distance(point_2, 6.0))


