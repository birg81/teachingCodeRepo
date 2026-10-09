#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char* argv[]) {
	int pid = fork();

	if (pid == 0) {
		printf("CHILD (%d): I'm working...\n", getpid());
		sleep(3);
		printf("CHILD (%d): I'm finish!\n", getpid());
		return 42;
	}

	printf("PARENT (%d): looking for child (%d)...\n", getpid(), pid);

	int status;
	int child_pid = wait(&status);

	printf("PARENT (%d): child (%d) finished!\n", getpid(), child_pid);

	return 0;
}
