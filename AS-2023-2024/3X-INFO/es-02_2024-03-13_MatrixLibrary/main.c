#include "matrixlib.h"

int main() {
	int matrix[ROWS][COLS];

	randMatrix(matrix, ROWS, COLS);
	printMatrix(matrix, ROWS, COLS);
	printf("\n\n");
	zeroAboveInverseDiagonal(matrix, ROWS);
	printMatrix(matrix, ROWS, COLS);

	return 0;
}