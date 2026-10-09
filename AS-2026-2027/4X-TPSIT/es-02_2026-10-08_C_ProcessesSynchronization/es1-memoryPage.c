#include <stdio.h>
#include <unistd.h>

int main(int argc, char* argv[]) {
	int pid = fork();
	int v = 37;
	if (pid < 0)
		perror(">>> ERROR <<< Failed to create the child process!!!...\n");
	else if (pid == 0) {
		v += 5;
		printf("[-] CHILD [pid: %d]\t> fork() [pid: %d]\t@ Parent [pid: %d] > [%x] v = %d\n", getpid(), pid, getppid(), &v, v);
	} else {
		v -= 5;
		sleep(3);
		printf("[+] PARENT [pid: %d]\t> child [pid: %d]\t@ Parent [pid: %d] > [%x] v = %d\n", getpid(), pid, getppid(), &v, v);
	}
	return 0;
}
