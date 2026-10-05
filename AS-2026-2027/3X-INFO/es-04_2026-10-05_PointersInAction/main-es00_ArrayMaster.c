#include <stdio.h>

void loadArray(int[], const int);
void printArray(const int[], const int);
void printEven(const int[], const int);
void reverseArray(int[], const int);
void sortArray(int[], const int);
int seek(const int[], const int, const int);
void rshiftArray(int[], const int);
void swap(int*, int*);

int main(int argc, char* argv[]) {
	int n = 0;

	do {
		printf("Enter array size, please? ");
		scanf("%d", &n);

		if (n <= 0)
			printf("Invalid size!\n");
	} while(n <= 0);

	int array[n];
	loadArray(array, n);

	int choice = -1;

	do {
		printf("\n\n1. Display array\n");
		printf("2. Print even elements\n");
		printf("3. Reverse array\n");
		printf("4. Sort array\n");
		printf("5. Search for a value\n");
		printf("6. Circular right shift\n\n");
		printf("0. Exit\n\n");
		printf("(enter choice)>_ ");
		scanf("%d", &choice);

		switch (choice) {
			case 1:
				printf("\nArray:\t");
				printArray(array, n);
				break;
			case 2:
				printf("\nEven elements:\t");
				printEven(array, n);
				break;
			case 3:
				reverseArray(array, n);
				printf("\nReversed array:\t");
				printArray(array, n);
				break;
			case 4:
				sortArray(array, n);
				printf("\nSorted array:\t");
				printArray(array, n);
				break;
			case 5:
				int target = 0;
				printf("Enter value to search, please? ");
				scanf("%d", &target);
				int pos = seek(array, n, target);
				if (pos != -1)
					printf("Element %d found at index: %d\n", target, pos);
				else
					printf("Element %d not found in array.\n"), target;
				break;
			case 6:
				rshiftArray(array, n);
				printf("\nShifted array:\t");
				printArray(array, n);
				break;
			case 0:
				printf("\nExiting program.\n");
				break;
			default:
				printf("Invalid choice.\n");
				break;
		}
	} while(choice != 0);

	return 0;
}

void swap(int* v1, int* v2) {
	int t = *v1;
	*v1 = *v2;
	*v2 = t;
}
void loadArray(int a[], const int size) {
	for (int i = 0; i < size; i++) {
		printf("Enter element [%d/%d]: ", i, size);
		scanf("%d", &a[i]);
	}
}
void printArray(const int a[], const int size) {
	for (int i = 0; i < size; i++)
		printf("%d%s", a[i], i < size - 1 ? ",\t" : ".\n");
}
void printEven(const int a[], const int size) {
	for (int i = 0; i < size; i++)
		if (a[i] % 2 == 0)
			printf("%d\t", a[i]);
	printf("\n");
}
void reverseArray(int a[], const int size) {
	for (int i = 0; i < size / 2; i++)
		swap(&a[i], &a[size - 1 - i]);
}
void sortArray(int a[], const int size) {
	for (int i = 0; i < size - 1; i++)
		for (int j = i + 1; j < size; j++)
			if (a[i] > a[j])
				swap(&a[i], &a[j]);
}
int seek(const int a[], const int size, const int target) {
	for (int i = 0; i < size; i++)
		if (a[i] == target)
			return i;
	return -1;
}
void rshiftArray(int a[], const int size) {
	if (size <= 1) return;
	int last = a[size - 1];
	for (int i = size - 1; i > 0; i--)
		a[i] = a[i - 1];
	a[0] = last;
}