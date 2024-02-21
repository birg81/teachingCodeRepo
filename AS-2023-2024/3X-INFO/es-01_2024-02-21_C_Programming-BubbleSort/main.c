#include <stdio.h>

void loadArray(int[], const int);
void printArray(const int[], const int);
void bubbleSort(int[], const int);
int max(const int[], const int);
int min(const int[], const int);
int sum(const int[], const int);
double avg(const int[], const int);
int searchKey(const int[], const int, const int);
void reverse(int[], const int);
int isPalindrome(const int[], const int);
void rshift(int[], const int, int);

int main() {
	int size = 0;
	do {
		printf("\nInsert array size: ");
		scanf("%d", &size);
	} while(size <= 0);

	int list[size];

	int choice;
	do {
		printf("\n************************ MENU ****************************\n");
		printf("1. load array's values\n");
		printf("2. print array\n");
		printf("3. sort array\n");
		printf("4. show (max, min, sum, avarange)\n");
		printf("5. search key in array\n");
		printf("6. reverse array\n");
		printf("7. is palindrome?\n");
		printf("8. circular shift\n\n");
		printf("0. exit\n");
		printf("**********************************************************\n");
		printf("\nCHOICE:>_ ");
		scanf("%d", &choice);

		switch(choice) {
			case 1:
				printf("\n>>>>>>>>> LOAD ARRAY <<<<<<<<<<\n");
				loadArray(list, size);
				break;
			case 2:
				printf("\n>>>>>>>>> PRINT ARRAY <<<<<<<<\n");
				printArray(list, size);
				break;
			case 3:
				printf("\n>>>>>>>>>> SORTING <<<<<<<<<<<\n");
				printf("(normal)\t");
				printArray(list, size);
				printf("\n(sorting)\t");
				bubbleSort(list, size);
				printArray(list, size);
				break;
			case 4:
				printf("\n>>>>>>>>>> STATISTIC <<<<<<<<<\n");
				printf("values: %d\n", size);
				printf("sum: %d\n", sum(list, size));
				printf("min: %d\n", max(list, size));
				printf("min: %.3f\n", avg(list, size));
				printf("min: %d\n", min(list, size));
				break;
			case 5:
				printf("\n>>>>> SEARCH KEY <<<<<<<<<<<<<\n");
				int key = 0;
				printf("(insert key) >:_ ");
				scanf("%d", &key);
				int p = searchKey(list, size, key);
				if(p >= 0) {
					printf("find key %d! have index: %d", key, p);
				} else {
					printf("sorry! not found %d in list..", key);
				}
				break;
			case 6:
				printf("\n>>>>>>>> REVERSE LIST <<<<<<<<\n");
				printf("(normal)\t");
				printArray(list, size);
				printf("\n(reverse)\t\t");
				reverse(list, size);
				printArray(list, size);
				break;
			case 7:
				printf("\n>>>> PALINDROME CHECKING <<<<\n");
				if(isPalindrome(list, size) >= 0){
					printf("You are Lucky! IS PALINDROME");
				} else {
					printf("Sorry, but IS NOT PALINDROME");
				}
				break;
			case 8:
				printf("\n>>>>>>>> RSHIFT <<<<<<<<<<<<\n");
				int n = 0;
				printf("(insert times)>:_ ");
				scanf("%d", &n);
				printf("(normal)\t");
				printArray(list, size);
				printf("\n(shift)\t");
				rshift(list, size, n);
				printArray(list, size);
				break;
			case 0:
				printf("Thank you for using our software");
				break;
			default:
				printf("\n>>>>>> INVALID CHOICE <<<<<<\n");
				break;
		}
	} while(choice != 0);
	return 0;
}

void loadArray(int a[], const int n) {
	for (int i = 0; i < n; i++) {
		printf("(insert [%d/%d] value) >:_ ", i + 1, n);
		scanf("%d", &a[i]);
	}
}
void printArray(const int a[], const int n) {
	for (int i = 0; i < n; i++) {
		printf("%d", a[i]);
		if(i < n -1)
			printf(",\t");
	}
}
void bubbleSort(int a[], const int n) {
	for(int i = 0; i < n - 1; i++) {
		for (int j = i + 1; j < n; j++) {
			if(a[j] < a[i]) {
				int t = a[i];
				a[i] = a[j];
				a[j] = t;
			}
		}
	}
}
int max(const int a[], const int n) {
	int max = a[0];
	for (int i = 1; i < n; i++) {
		if(a[i] > max)
			max = a[i];
	}
	return max;
}
int min(const int a[], const int n) {
	int min = a[0];
	for (int i = 1; i < n; i++) {
		if(a[i] < min)
			min = a[i];
	}
	return min;
}
int sum(const int a[], const int n) {
	int sum = 0;
	for (int i = 0; i < n; i++) {
		sum += a[i];
	}
	return sum;
}
double avg(const int a[], const int n) {
	return ((double) sum(a, n))/n;
}
int searchKey(const int a[], const int n, const int key) {
	for (int i = 0; i < n; i++) {
		if(a[i] == key)
			return i;
	}
	return -1;
}
void reverse(int a[], const int n) {
	for (int i = 0; i < n/2; i++) {
		int t = a[i];
		a[i] = a[n -1 - i];
		a[n -1 - i] = t;
	}
}
int isPalindrome(const int a[], const int n) {
	for (int i = 0; i < n/2; i++) {
		if(a[i] != a[n -1 - i])
			return -1;
	}
	return 1;
}
void rshift(int a[], const int n, int ntimes) {
	ntimes = ntimes % n;
	for(int j = 0; j < ntimes; j++) {
		const int t = a[0];
		for (int i = 0; i < n - 1; i++) {
			a[i] = a[i + 1];
		}
		a[n - 1] = t;
	}
}