#include <stdio.h>
void loadArrayWhileAZero(int[], const int, int*);
void printArray(const int[], const int);

int main(int argc, char* argv[]) {
	int n = 0;

	do {
		printf("Enter max array size, please? ");
		scanf("%d", &n);
		printf(n <= 0 ? "Invalid size!\n" : "");
	} while(n <= 0);

	int array[n];
	loadArrayWhileAZero(array, n, &n);
	printf("The actual size of the array is %d!...\n");
	printArray(array, n);

	return 0;
}

void printArray(const int a[], const int size) {
	for (int i = 0; i < size; i++)
		printf("%d%s", a[i], i < size - 1 ? ", " : ".\n");
}
void loadArrayWhileAZero(int a[], const int max_size, int* size) {
	for(*size = 0; *size < max_size && a[*size] != 0; *size += 1) {
		printf("Insert a value, please? ");
		scanf("%d", &a[*size]);
	}
}
