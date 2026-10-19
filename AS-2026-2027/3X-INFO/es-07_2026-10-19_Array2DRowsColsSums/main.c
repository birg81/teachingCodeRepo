#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ROWS 5
#define COLS 5

void loadMatrix(int[][COLS], const int, const int);
void loadRandomMatrix(int[][COLS], const int, const int);
void printMatrix(const int[][COLS], const int, const int);
void computeSums(int[][COLS], const int, const int);

int main(int argc, char* argv[]) {
	int matrix[ROWS][COLS];
	loadRandomMatrix(matrix, ROWS - 1, COLS - 1);
	printMatrix(matrix, ROWS - 1, COLS - 1);

	printf("\n>>>>> SOMMATORIA <<<<<\n");
	computeSums(matrix, ROWS, COLS);
	printMatrix(matrix, ROWS, COLS);

	return 0;
}
void loadMatrix(int m[][COLS], const int rows, const int cols) {
	for(int i = 0; i < rows; i++)
		for(int j = 0; j < cols; j++) {
			printf("Insert value [%d][%d]: ", i, j);
			scanf("%d", &m[i][j]);
		}
}
void loadRandomMatrix(int m[][COLS], const int rows, const int cols) {
	srand(time(NULL));
	for (int i = 0; i < rows; i++)
		for (int j = 0; j < cols; j++)
			m[i][j] = -10 + rand() % 21;
}
void printMatrix(const int m[][COLS], const int rows, const int cols) {
	for(int i = 0; i < rows; i++)
		for(int j = 0; j < cols; j++)
			printf("%d%s", m[i][j], j < cols -1 ? ", " : "\n");
}
void computeSums(int m[][COLS], const int rows, const int cols) {
	m[rows - 1][cols - 1] = 0;
	for(int i = 0; i < rows - 1; i++)
		for(int j = 0; j < cols - 1; j++) {
			m[i][cols - 1] = m[i][j] + (j != 0 ? m[i][cols - 1] : 0);
			m[rows - 1][j] = m[i][j] + (i != 0 ? m[rows - 1][j] : 0);
			m[rows - 1][cols - 1] += m[i][j];
		}
}