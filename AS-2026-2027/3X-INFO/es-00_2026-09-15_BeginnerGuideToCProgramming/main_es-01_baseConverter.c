#include <stdio.h>

int main() {
	for (int i = 0; i < 32; i++) {
		printf("%d \t %05b \t %o \t %x \t %c \n", i, i, i, i, i + 64);
	}
	return 0;
}
