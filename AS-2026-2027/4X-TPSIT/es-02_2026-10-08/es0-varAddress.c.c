#include <stdio.h>
#include <unistd.h>

int main(int argc, char* argv[]) {
	int a = 10;
	printf("[%x] a = %d\n", &a, a);
	return 0;
}
