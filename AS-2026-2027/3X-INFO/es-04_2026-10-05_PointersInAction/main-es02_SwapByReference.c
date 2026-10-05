#include <stdio.h>

void swap(int*, int*);

int main(int argc, char* argv[]) {
	int a = 13;
	int b = 37;

	printf("\n*** Before swapping ***\n");
	printf("[%x] a = %d\n", &a, a);
	printf("[%x] b = %d\n", &b, b);

	swap(&a, &b);
	printf("\n*** After swapping ***\n");
	printf("[%x] a = %d\n", &a, a);
	printf("[%x] b = %d\n", &b, b);

	return 0;
}

void swap(int* v1, int* v2){
	int t = *v1;
	*v1 = *v2;
	*v2 = t;
}