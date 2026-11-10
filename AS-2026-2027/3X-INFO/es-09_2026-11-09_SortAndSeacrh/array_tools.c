#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "array_tools.h"

void loadRandArray(int a[], const int size) {
	srand(time(NULL));
	for (int i = 0; i < size; i++)
		a[i] = rand() % 100;
}

void duplicateArray(const int a[], int copy[], const int size) {
	for(int i = 0; i < size; i++)
		copy[i] = a[i];
}

void printArray(const int a[], const int size) {
	for (int i = 0; i < size; i++)
		printf("%d%s", a[i], i < size - 1 ? ", " : "\n");
}

void swap(int* v1, int* v2, const char c) {
	int t = *v1;
	*v1 = *v2;
	*v2 = t;
	printf("%c", c);
}

void b_sort(int a[], const int size) {
	int swapped = 1;
	for (int i = 0; i < size - 1 && swapped; i++) {
		swapped = 0;
		for (int j = 0; j < size - 1 - i; j++)
		if (a[j] > a[j + 1]) {
			swap(&a[j], &a[j + 1], ':');
			swapped++;
		}
	}
}

void s_sort(int a[], const int size) {
	for (int i = 0; i < size - 1; i++) {
		int i_min = i;
		for (int j = i + 1; j < size; j++)
			if (a[j] < a[i_min])
				i_min = j;
		if (i_min != i)
			swap(&a[i_min], &a[i], '.');
	}
}

int linSearch(const int a[], const int size, const int key) {
	for (int i = 0; i < size; i++) {
		printf("+");
		if (a[i] == key)
			return i;
	}
	return -1;
}

int binSearch(const int a[], const int size, const int key) {
	for (int i_L = 0, i_R = size - 1; i_L <= i_R; ) {
		int i_M = i_L + (i_R - i_L) / 2;
		printf("-");
		if (key > a[i_M])
			i_L = i_M + 1;
		else if (key < a[i_M])
			i_R = i_M - 1;
		else
			return i_M;
	}
	return -1;
}
