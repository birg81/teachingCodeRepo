# This code generates a parent process and a child process.
# Depending on the execution mode, the PID is printed.

#!/usr/bin/python3
from os import fork, getpid, getppid

if __name__ == '__main__':
	pid = fork()
	if pid == 0:
		print(f"child process [{getpid()}] >> main process [{getppid()}]")
	else:
		print(f"main process [{getpid()}] >> child process [{pid}]")