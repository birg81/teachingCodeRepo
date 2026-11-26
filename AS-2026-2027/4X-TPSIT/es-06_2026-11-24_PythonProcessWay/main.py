from multiprocessing import Process
from time import sleep

def task(name: str = 'fruit'):
	for i in range(20):
		print(f"{name}: {i}")
		sleep(1)

	print(f'{name} has finished!')


if __name__ == '__main__':
	p1 = Process(target= task, args= ('ananas',))
	p2 = Process(target= task, args= ('banana',))
	p3 = Process(target= task, args= ('cherry',))

	p1.start()
	p2.start()
	p3.start()

	print(f'P1: {p1.pid}\tP2: {p2.pid}\tP3: {p3.pid}')

	# Wait for all processes to finish
	#p1.join()
	#p2.join()
	#p3.join()
