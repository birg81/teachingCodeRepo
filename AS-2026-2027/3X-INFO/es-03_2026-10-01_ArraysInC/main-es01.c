#include <stdio.h>

void loadArray(int[], const int);
void printArray(const int[], const int);

int main() {
	int N = 5;
	printf("Insert size, please? ");
	scanf("%d", &N);
	int array[N];
	loadArray(array, N);
	printArray(array, N);
	return 0;
}

void loadArray(int a[], const int size) {
	for(int i = 0; i < size; i++) {
		printf("Insert value, please? [%d/%d] >_ ", i + 1, size);
		scanf("%d", &a[i]);
	}
}

void printArray(const int a[], const int size) {
	for(int i = 0; i < size; i++) {
		printf("%d", a[i]);
		if(i < size -1)
			printf("\t");
		else
			printf("\n");
	}
}