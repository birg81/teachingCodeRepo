from os import fork, getpid, getppid

if __name__ == '__main__':
	pid = fork()
	if pid < 0:
		print(">>> ERROR <<< Failed to create the child process!!!...\n")
	elif pid == 0:
		print(f"[-] CHILD [pid: {getpid()}]\t> fork() value [pid: {pid}]\t@ Parent [pid: {getppid()}]\n")
	else:
		print(f"[+] PARENT [pid: {getpid()}]\t> child [pid: {pid}]\t@ Parent [pid: {getppid()}]\n")
