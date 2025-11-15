#!/usr/bin/python3

from multiprocessing import Process, current_process
from time import sleep
from random import randint

# task executed by the process
def greeting(name:str = 'John Doe', t:int = 5):
	print(f"[pid: {current_process().pid}] I'm {name}. I will be terminated in {t} seconds..")
	sleep(t)
	print(f"process {name} [pid: {current_process().pid}] has been terminated")

# list of strings: characters from The Simpsons
simpsons_characters = [
	"Homer Jay Simpson",
	"Marjorie Jacqueline Simpson",
	"Bartholomew JoJo Simpson",
	"Lisa Marie Simpson",
	"Margaret Evelyn Simpson"
]

# process's list
p = [Process(target = greeting, args = (simpson, randint(3, 10))) for simpson in simpsons_characters]

# main
if __name__ == '__main__':
	print(f"main process [pid {current_process().pid}]")
	print("*** START PROCESS ***")

	# start your process
	for i in range(len(simpsons_characters)):
		p[i].start()
		print(f"process [pid: {p[i].pid}] has started..")

	# join() method is same than wait function in C-lang
	for i in range(len(simpsons_characters)):
		p[i].join()
	print("*** END PROCESS ***")