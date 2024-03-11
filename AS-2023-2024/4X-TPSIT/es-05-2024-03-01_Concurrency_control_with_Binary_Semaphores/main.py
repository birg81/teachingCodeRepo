import threading

# Inizializzazione di un semaforo binario con valore iniziale 1
semaforo = threading.Semaphore(1)

# Variabile condivisa tra i thread
variabile_condivisa = 0

# Funzione del thread
def funzione_thread(id_thread):
	global variabile_condivisa

	# Acquisizione del semaforo per entrare nella sezione critica
	stato_semaforo = 'VERDE' if semaforo._value == 1 else 'ROSSO'
	print(f'Thread {id_thread}: Semaforo {stato_semaforo}')

	semaforo.acquire()
	# Stampa del valore del semaforo
	stato_semaforo = 'VERDE' if semaforo._value == 1 else 'ROSSO'
	print(f'Thread {id_thread}: Semaforo {stato_semaforo}')

	# Sezione critica
	variabile_condivisa += 1
	print(f'Thread {id_thread}: Variabile condivisa = {variabile_condivisa}')

	# Rilascio del semaforo per lasciare la sezione critica
	semaforo.release()
	print(f'Thread {id_thread}: Semaforo {stato_semaforo} ')

# Creazione di due thread
thread1 = threading.Thread(target = funzione_thread, args = (1,))
thread2 = threading.Thread(target = funzione_thread, args = (2,))

# Avvio dei thread
thread1.start()
thread2.start()

# Attendo la fine dei thread
thread1.join()
thread2.join()