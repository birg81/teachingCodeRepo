#include <stdio.h>

#define ROWS 4
#define COLS 4

void loadMatrix(int[][COLS], const int, const int);
void printMatrix(const int[][COLS], const int, const int);
void transposeSquareMatrix(int[][COLS], const int);

int main(int argc, char* argv[]) {
	int matrix[ROWS][COLS];
	/* = {
		{1, 2, 3, 5},
		{7, 11, 13, 17},
		{23, 31, 37, 41},
		{53, 57, 59, 61}
	};*/
	printf("\n *** CARICAMENTO VALORI MATRICE ***\n");
	loadMatrix(matrix, ROWS, COLS);
	printf("\n *** STAMPA VALORI MATRICE ***\n");
	printMatrix(matrix, ROWS, COLS);
	printf("\n *** MATRICE TRASPOSTA ***\n");
	transposeSquareMatrix(matrix, ROWS, COLS);
	printMatrix(matrix, ROWS, COLS);

	return 0;
}

void loadMatrix(int m[][COLS], const int rows, const int cols) {
	for(int i = 0; i < rows; i++) {
		for(int j = 0; j < cols; j++) {
			printf("Insert value [%d][%d]: ", i, j);
			scanf("%d", &m[i][j]);
		}
	}
}
void printMatrix(const int m[][COLS], const int rows, const int cols) {
	for(int i = 0; i < rows; i++) {
		for(int j = 0; j < cols; j++)
			printf("%d%s", m[i][j], j < cols -1 ? ", " : "");
		printf("\n");
	}
}
void transposeSquareMatrix(int m[][COLS], const int size) {
	for (int i = 0; i < size; i++)
		for (int j = i + 1; j < size; j++) {
			int t = m[i][j];
			m[i][j] = m[j][i];
			m[j][i] = t;
		}
}
