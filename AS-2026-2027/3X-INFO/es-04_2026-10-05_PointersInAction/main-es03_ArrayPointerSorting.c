#include <stdio.h>

void printArray(const int[], const int);
void sort(int[], const int);
void swap(int*, int*);

int main(int argc, char* argv[]) {
	int array[] = {
		2, 37, 5, 13, 7
	};

	printf("\nBefore Sorting:\t");
	printArray(array, 5);

	sort(array, 5);
	printf("\nAfter Sorting:\t");
	printArray(array, 5);

	return 0;
}

void swap(int* v1, int* v2){
	int t = *v1;
	*v1 = *v2;
	*v2 = t;
}
void printArray(const int a[], const int size) {
	for (int i = 0; i < size; i++)
		printf("%d%s", a[i], i < size -1 ? ",\t" : ".\n");
}
void sort(int a[], const int size) {
	for (int i = 0; i < size -1; i++)
		for (int j = i + 1; j < size; j++)
			if(a[i] > a[j])
				swap(&a[i], &a[j]);
}