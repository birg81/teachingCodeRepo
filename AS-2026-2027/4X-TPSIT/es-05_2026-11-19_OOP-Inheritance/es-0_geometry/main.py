from model import (
	Point, Line
)

if __name__ == '__main__':
	p1 = Point(4, 3)
	p2 = Point(8, 7)
	print(
f'''
P1: {p1}
P2: {p2}
distance P1 - (0.0, 0.0): {p1.dist()}
distance P1 - P2: {p1.dist(p2)}
'''
	)

	r1 = Line(5, 4)
	r2 = Line(5, 1)
	r3 = Line(-0.2, 0)
	print(
f'''
r1: {r1}
r2: {r2}
r3: {r3}
r1 // r2 ?? {r1.is_parallel(r2)}
r1 ⊥ r3 ?? {r1.is_orthogonal(r3)}
dist r1 - P1: {r1.dist(p1)}
dist r1 - (0, 0): {r1.dist()}
'''
	)
