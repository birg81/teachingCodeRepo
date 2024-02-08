import time as t
import threading as th
import multiprocessing as mp

num:int = 25_000

def calculatePrime(num: int):
	prime = []
	for i in range(2, num):
		isPrime = True
		for j in range(2, 1 + int(i ** 0.5)):
			if i % j == 0:
				isPrime = False
				break
		if isPrime:
			prime.append(i)
	return prime

def primeByThread():
	th1 = th.Thread(target = calculatePrime, args = (num,))
	th2 = th.Thread(target = calculatePrime, args = (num,))

	t0 = t.time()

	th1.start()
	th2.start()

	th1.join()
	th2.join()

	elapsedTime = t.time() - t0
	print(f'Thread: elapsedTime {elapsedTime:.3f} sec..')

def primeByProcess():
	p1 = mp.Process(target = calculatePrime, args = (num,))
	p2 = mp.Process(target = calculatePrime, args = (num,))

	t0 = t.time()

	p1.start()
	p2.start()

	p1.join()
	p2.join()

	elapsedTime = t.time() - t0
	print(f'Process: elapsedTime {elapsedTime:.3f} sec..')

if __name__ == '__main__':
	print('\n************** Process ***************')
	primeByProcess()

	print('\n*************** Thread ***************')
	primeByThread()