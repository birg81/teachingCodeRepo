#include <stdio.h>
#include <unistd.h>

int main() {
	int pid = fork();
	if (pid < 0) {
		perror(">>> ERROR <<< Failed to create the child process!!!...\n");
	} else if (pid == 0) {
		printf("[-] CHILD [pid: %d]\t> fork() value [pid: %d]\t@ Parent [pid: %d]\n", getpid(), pid, getppid());
	} else {
		printf("[+] PARENT [pid: %d]\t> child [pid: %d]\t@ Parent [pid: %d]\n", getpid(), pid, getppid());
	}
	return 0;
}