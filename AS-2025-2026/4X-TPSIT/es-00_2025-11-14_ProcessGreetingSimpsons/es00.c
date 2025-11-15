/*
This code generates a parent process and a child process. Depending on the execution mode, the PID is printed.
*/

#include <stdio.h>
#include <unistd.h>

int main() {
	int pid = fork();
	if(pid == 0) {
		printf("child process [%d] >> main process [%d]\n", getpid(), getppid());
	} else {
		printf("main process [%d] >> child process [%d]\n", getpid(), pid);
	}
	return 0;
}