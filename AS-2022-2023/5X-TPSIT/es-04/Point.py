#!/usr/local/bin/python

# REM __ for private method
# REM _ for protected method
# REM nothing for public method

class Point2D:
	'this is a 2D Point'
	def __init__(self, x = 0, y = 0):
		self._x = x		# _x, _y is a protected method
		self._y = y

	def __str__(self):
		return f'''({self.__x}, {self.__y})'''

class Point3D(Point2D):
	'this is a 3D Point'
	__countOBJ = 0	# static private method
	def __init__(self, x = 0, y = 0, z = 0):		# constructor
		super().__init__(x,y)
		self.__z = z
		Point3D.__countOBJ += 1
	
	def __str__(self):		# toString method
		return f'''({self._x}, {self._y}, {self.__z}) you've {Point3D.__countOBJ} objects'''

	def __del__(self):		# distructor
		Point3D.__countOBJ -= 1

	def __add__(self, o):
		return Point3D(self._x+o._x, self._y+o._y, self.__z+o.__z)

'''
this line allows our code to understand if it is being executed as a script in its own right, or if it has been called as a module by some program
'''
if __name__ == '__main__':
	p = Point3D(1, 1e1, 1e-3)
	p2 = Point3D(1,2,3)
	p += p2
	del p2
	print(p, p.__doc__)

	input('\n(press a key to continue)...')