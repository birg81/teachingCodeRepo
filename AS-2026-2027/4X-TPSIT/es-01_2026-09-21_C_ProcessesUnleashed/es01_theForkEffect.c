#include <stdio.h>
#include <unistd.h>

int main() {
	fork();
	fork();
	fork();
	printf("[*] Current [pid: %d]\t@ Parent [pid: %d]\n", getpid(), getppid());
	return 0;
}