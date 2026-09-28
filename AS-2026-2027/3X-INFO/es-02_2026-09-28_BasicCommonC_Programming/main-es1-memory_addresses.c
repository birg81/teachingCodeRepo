#include <stdio.h>

int main(int argc, char* argv[]) {
	// variable declarations
	double
		x = 017,		// base 8	-> base 10:	15
		y = 0xaf,		// base 16	-> base 10:	175
		z = 0b1101;		// base 2	-> base 10:	13

	// output
	printf("x =  %f (%x)\ny =  %f (%x)\nz =  %f (%x)\n",
		x, &x,
		y, &y,
		z, &z
	);

	return 0;
}