#include <stdio.h>

int main(int argc, char* argv[]) {
	int a = 13;
	int b = 72;
	int* p;

	printf("[%x] a = %d\n", &a, a);
	printf("[%x] b = %d\n", &b, b);
	printf("[%x] p = (%x) %d\n", &p, p, *p);

	p = &a;
	*p = 19;
	printf("[%x] a = %d\n", &a, a);
	printf("[%x] b = %d\n", &b, b);
	printf("[%x] p = (%x) %d\n", &p, p, *p);

	p = &b;
	(*p)++;
	printf("[%x] a = %d\n", &a, a);
	printf("[%x] b = %d\n", &b, b);
	printf("[%x] p = (%x) %d\n", &p, p, *p);

	return 0;
}