#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

void count_down(const int seconds) {
	for(int i = 0; i < seconds; i++) {
		printf(" >");
		fflush(stdout);
		sleep(1);
	}
	printf(" wake up before %d seconds!\n", seconds);
}
int main(int argc, char* argv[]) {
	int pid = fork();
	if(pid < 0) {
		perror("fork() failed!");
		return -1;
	} else if (pid == 0) {
		printf("[ CHILD (PID: %d, PPID: %d)]: I'm working...\n", getpid(), getppid());
		count_down(5);
		// execlp("sh", "sh", "-c", "hostname -I | awk '{print $1}'", NULL);
		printf("[ CHILD (PID: %d, PPID: %d)]: finished!\n", getpid(), getppid());
		return 53;
	} else {
		printf("[PARENT (PID %d, child: %d, PPID: %d)]: waiting for the child...\n", getpid(), pid, getppid());
		/*
		sleep(2);
		printf("\n[PARENT (PID %d)]: Sending SIGKILL to child %d...\n", getpid(), pid);
		if(kill(pid, 9) < 0) {
			perror("kill() failed!");
			return -1;
		}
		*/
		int status;
		int child = wait(NULL/*&status*/);      // waitpid(-1, &status, 0);
		if (child < 0) {
			perror("wait() failed!");
			return -1;
		}
		printf("[PARENT (PID %d, child: %d, PPID: %d)]: child %d finished!\n", getpid(), pid, getppid(), child);
		/*
		if (WIFEXITED(status))
			printf("[PARENT (PID %d)]: child's (%d) return value = %d\n", getpid(), child, WEXITSTATUS(status));
		else if (WIFSIGNALED(status))
			printf("[PARENT (PID %d)]: child (%d) killed by signal %d\n", getpid(), child, WTERMSIG(status));
		*/
	}
	return 0;
}
