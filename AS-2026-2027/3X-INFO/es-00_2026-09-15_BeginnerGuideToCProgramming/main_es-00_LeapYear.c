#include <stdio.h>

int main() {
	int anno, annoBisestile, resto;

	printf("Che anno si vuole controllare? ");
	scanf("%d", &anno);
	resto = anno % 4;
	if (resto == 0) {
		printf("L'anno è bisestile!\n");
	} else {
		annoBisestile = anno - resto;
		printf("L'anno %d non è bisestile, ma lo era %d\n", anno, annoBisestile);
	}
	return 0;
}
