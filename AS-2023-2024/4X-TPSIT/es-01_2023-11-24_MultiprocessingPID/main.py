import os
import time
import multiprocessing as mp

'''
Funzione saluto
Stampa un messaggio di saluto e il valore del processo corrette e del processo padre (parent pid).
Dopo la stampa addormenta il sistema per un secondo
'''
def greating(name):
	while True:
		print(f">> Hi {name}! pid: {os.getpid()}, ppid: {os.getppid()} ")
		time.sleep(1)


if __name__ == '__main__':
	print(">>>> START <<<<") # OPZIONALE: indica l'inizio del codice

	# OPZIONALE: stampa delle informazioni del sistema, numero di processori e pid/ppid
	print(f"Your system have {mp.cpu_count()} cpu(s) :: - pid: {os.getpid()}, ppid: {os.getppid()}")

	# crea un processo richiamando la funzione greating() e gli passa l'argomento 'Admin0'
	t1 = mp.Process(target=greating, args=('Admin0',))
	# avvia il processo creato
	t1.start()

	t2 = mp.Process(target=greating, args=('Cesare',))
	t2.start()

	t3 = mp.Process(target=greating, args=('Biagio',))
	t3.start()

	print(">>>> END <<<<") # OPZIONALE: indica la fine del codice del main