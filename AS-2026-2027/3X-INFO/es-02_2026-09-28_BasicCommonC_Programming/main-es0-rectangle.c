#include <stdio.h>

// function prototypes
double rectanglePerimeter(double, double);
double rectangleArea(double, double);

int main(int argc, char* argv[]) {
	// variable declarations
	double base = 0., height = 0., area = 0., perimeter;

	// input validation
	do{
		printf("insert base, please? ");
		scanf("%lf", &base);
	} while (base <= 0.);

	do {
		printf("inserisci height, please? ");
		scanf("%lf", &height);
	} while (height <= 0.);

	// calculate perimeter and area
	perimeter = rectanglePerimeter(base, height);
	area = rectangleArea(base, height);

	// output
	printf(
		"rectangle base x height: %.2f x %.2f -> perimeter: %.2f, area: %.2f",
		base, height,
		perimeter, area
	);

	return 0;
}

// function definitions
double rectanglePerimeter(double b, double h) {
	return 2 * (b + h);
}

double rectangleArea(double b, double h) {
	return b * h;
}