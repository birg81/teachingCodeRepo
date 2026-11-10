#include <stdio.h>
#include "array_tools.h"

#define N 20

int main(int argc, char* argv[]) {
	int a0[N];
	int a1[N];
	loadRandArray(a0, N);
	duplicateArray(a0, a1, N);

	printf("\n>>> PRINT -> ARRAY a0 <<<\n");
	printArray(a0, N);
	b_sort(a0, N);
	printf("\n>>> BUBBLE SORT <<<\n");
	printArray(a0, N);

	printf("\n>>> PRINT ARRAY a1 <<<\n");
	printArray(a1, N);
	s_sort(a1, N);
	printf("\n>>> SELECTION SORT <<<\n");
	printArray(a1, N);

	int k;
	printf("\nInsert key to find: ");
	scanf("%d", &k);

	printf("\nLinear search path: ");
	int lin_idx = linSearch(a0, N, k);
	if (lin_idx >= 0)
		printf("\nLinear Search: Found value %d at index %d\n", k, lin_idx);
	else
		printf("\nLinear Search: Value %d not found\a\n", k);

	printf("\nBinary search path: ");
	int bin_idx = binSearch(a1, N, k);
	if (bin_idx >= 0)
		printf("\nBinary Search: Found value %d at index %d\n", k, bin_idx);
	else
		printf("\nBinary Search: Value %d not found\a\n", k);

	return 0;
}
