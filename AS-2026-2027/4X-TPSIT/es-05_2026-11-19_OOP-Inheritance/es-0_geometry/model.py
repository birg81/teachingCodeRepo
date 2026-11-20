class Point:
	def __init__(self, x: float = 0.0, y: float = 0.0):
		self.__x:float = x
		self.__y:float = y

	def dist(self, p: 'Point' = None) -> float:
		if p is None:
			p = Point(0, 0)
		return ((self.__x - p.__x)**2 + (self.__y - p.__y)**2)**.5

	def __str__(self) -> str:
		return f'P({self.__x:g}, {self.__y:g})'

	def x(self) -> float:
		return self.__x

	def y(self) -> float:
		return self.__y

class Line:
	def __init__(self, m: float = 0.0, q: float = 0.0):
		self.__m = float(m)
		self.__q = float(q)

	def is_parallel(self, r: 'Line') -> bool:
		return self.__m == r.__m

	def is_orthogonal(self, r: 'Line') -> bool:
		return self.__m * r.__m == -1

	def dist(self, p: 'Point' = None) -> float:
		if p is None:
			p = Point(0, 0)
		return abs(self.__m * p.x() + self.__q - p.y()) / ((1 + self.__m**2)**.5)

	def __str__(self) -> str:
		return f"y = {self.__m:g}x {'+' if self.__q >= 0 else '-'} {abs(self.__q):g}"
