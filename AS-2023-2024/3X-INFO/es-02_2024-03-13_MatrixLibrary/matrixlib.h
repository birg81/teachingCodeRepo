#ifndef MATRIXLIB_H
#define MATRIXLIB_H

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ROWS 7
#define COLS 7

// generic matrix functions
void loadMatrix(int[][COLS], const int, const int);
void randMatrix(int[][COLS], const int, const int);
void printMatrix(const int[][COLS], const int, const int);
void zeroNegative(int[][COLS], const int, const int);

// only for square matrix
void zeroBelowMainDiagonal(int matrix[][COLS], const int);
void zeroAboveMainDiagonal(int matrix[][COLS], const int);
void zeroBelowInverseDiagonal(int matrix[][COLS], const int);
void zeroAboveInverseDiagonal(int matrix[][COLS], const int);

#endif