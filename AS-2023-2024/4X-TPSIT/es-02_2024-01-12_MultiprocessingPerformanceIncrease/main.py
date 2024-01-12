import time as t
import multiprocessing as proc

# funzione per un calcolo molto complesso
def myTask(n: int = 1):
	l = []
	for i in range(5_000_000):
		l.append(i ** 3)

if __name__ == '__main__':
	numeri = [2, 3, 5, 7, 11]

	# esecuzione dei task in maniera sequenziale
	start0 = t.time() # istante in cui partono le operazioni
	for n in numeri:
		myTask(n)
	stop0 = t.time() # instante in cui queste operazioni finiscono

	# NB: (stop - start) è il tempo trascorso per fare le operazioni

	# creazione dei diversi processi
	pList = []
	for n in numeri:
		pList.append(proc.Process(target = myTask, args = (n,)))

	# esecuzione dei processi in parallelo
	start1 = t.time()
	for p in pList:
		p.start()
	stop1 = t.time()

	# stampa delle dei tempi e delle performance
	print(f'''
******** ISTRUZIONI SEQUENZIALI *******
time: {(stop0 - start0):.5f} s
******** PROCESSO DI ISTRUZIONI *******
time: {(stop1 - start1):.5} s
************** INCREASE ***************
increase: {((stop0 - start0) / (stop1 - start1)):.1f} times
	''')