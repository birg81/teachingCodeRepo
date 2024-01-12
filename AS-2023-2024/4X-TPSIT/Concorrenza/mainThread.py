import threading
import os
from time import sleep

def mioTask(n: int = -1):
	for i in range(100):
		print(f'Task {n} named "{threading.current_thread().name}" have ID:{os.getpid()}')

if __name__ == "__main__":
	print(
		f'''
PID (process running in MAIN PROGRAM) is {os.getpid()}
Main thread name: {threading.current_thread().name}
	'''
	)

	t1 = threading.Thread(target=mioTask, name='t1', args=(1,))
	t2 = threading.Thread(target=mioTask, name='t2', args=(2,))
	t3 = threading.Thread(target=mioTask, name='t3', args=(3,))

	t1.start()
	t2.start()
	t3.start()

	t1.join()
	t2.join()
	t3.join()