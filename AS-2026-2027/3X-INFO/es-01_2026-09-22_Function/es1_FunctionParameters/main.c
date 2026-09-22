#include <stdio.h>

int twoTimes(int);
void printHurryNapl(int);

int main() {
	int n = 0;
	printf("Insert n, please? ");
	scanf("%d", &n);
	n = twoTimes(n);
	printHurryNapl(n);
	return 0;
}

void printHurryNapl(int howTimes) {
	if(howTimes > 0) {
		for(int i = 0; i < howTimes; i++) {
			printf("Forza Napoli!\n");
		}
	}
}

int twoTimes(int num) {
	num *= 2;
	return num;
}