#include <stdio.h>

const float PI = 3.1415926;

float calculateCircleArea(float);
float calculateCirclePerimeter(float);
void printCircleInfo(float);

int main() {
	float radius = 0.f;
	do {
		printf("Insert radius, please? ");
		scanf("%f", &radius);
		printCircleInfo(radius);
		printf("\nagain (until r > 0)..\n");
	} while(radius > 0);
	printf("godbye..");
	return 0;
}

float calculateCircleArea(float r) {
	return PI * r * r;
}

float calculateCirclePerimeter(float r) {
	return 2 * PI * r;
}

void printCircleInfo(float r) {
	float area = calculateCircleArea(r);
	float perimeter = calculateCirclePerimeter(r);
	printf("Cerchio di raggio: %.2f, perimetro: %.2f cm, area: %.2f cm^2\n", r, perimeter, area);
}