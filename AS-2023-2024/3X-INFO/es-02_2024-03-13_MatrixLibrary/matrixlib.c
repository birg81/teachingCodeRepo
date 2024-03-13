#include "matrixlib.h"

// Chiede all'utente di inserire i diversi valori della matrice
void loadMatrix(int mat[][COLS], const int n, const int m) {
	for(int i = 0; i < n; i++) {
		printf("\n");
		for(int j = 0; j < m; j++) {
			printf("(insert value) [%d][%d] >_: ", i, j);
			scanf("%d", &mat[i][j]);
		}
	}
}
// Carica gli elementi della matrice con valori casuali
void randMatrix(int mat[][COLS], const int n, const int m) {
	srand(time(NULL));
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < m; j++) {
			mat[i][j] = -100 + rand() % 200;
		}
	}
}
// Stampa gli elementi della matrice
void printMatrix(const int mat[][COLS], const int n, const int m) {
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < m; j++) {
			printf("%d\t", mat[i][j]);
		}
		printf("\n");
	}
}
// elimina gli elementi negativi
void zeroNegative(int mat[][COLS], const int n, const int m) {
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < m; j++) {
			if(mat[i][j] < 0)
				mat[i][j] = 0;
		}
	}
}


/*** per le matrici quadrate ***/

// elimina gli elementi sotto la diagonale principale
void zeroBelowMainDiagonal(int mat[][COLS], const int n) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if(i > j) {
				mat[i][j] = 0;
			}
		}
	}
}
// elimina gli elementi sotto la diagonale principale
void zeroAboveMainDiagonal(int mat[][COLS], const int n) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if(i < j) {
				mat[i][j] = 0;
			}
		}
	}
}
// elimina gli elementi sotto la diagonale principale
void zeroBelowInverseDiagonal(int mat[][COLS], const int n) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if(i + j > n + 1) {
				mat[i][j] = 0;
			}
		}
	}
}
// elimina gli elementi sotto la diagonale principale
void zeroAboveInverseDiagonal(int mat[][COLS], const int n) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if(i + j < n -1) {
				mat[i][j] = 0;
			}
		}
	}
}