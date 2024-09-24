#include <stdio.h>
#include <unistd.h>

int main() {
	int var = 10;			// shared memory -> ONLY FOR TEST
	int p = fork();			// fork return PID Child process value

	// CASE fork return ZERO ==>			I'm CHILD process
	if(p == 0) {
		var--;
		printf("Parent PID: %05d\tPID: %05d\tfork PID: %05d\tvar: %02d (%08x)\t\t<< CHILD process!\n", getppid(), getpid(), p, var, &var);
	// CASE fork return POSITIVE VALUE ==>	I'm PARENT process
	} else if(p > 0) {
		var++;
		printf("Parent PID: %05d\tPID: %05d\tfork PID: %05d\tvar: %02d (%08x)\t\t<< PARENT process!\n", getppid(), getpid(), p, var, &var);
	// CASE fork return NEGATIVE VALUE ==>	FORK FAIL
	} else {
		perror("Fork FAIL!!!\n");
	}
	return 0;
}