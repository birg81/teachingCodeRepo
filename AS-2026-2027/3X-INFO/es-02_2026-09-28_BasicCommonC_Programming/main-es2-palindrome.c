#include <stdio.h>

// function prototypes
int reverseNumber(int);
int isPalindrome(int);

int main(int argc, char* argv[]) {
	int num = 0;

	do {
		printf("Insert your number, please? ");
		scanf("%d", &num);
	} while (num <= 0);

	// palindrome checking
	if(isPalindrome(num)) {
		printf("%d is a palindrome number!\n", num);
	} else {
		printf(
			"Sorry, but %d is NOT a palindrome!\nIts reverse is %d!\n",
			num, reverseNumber(num)
		);
	}

	return 0;
}

// function definitions
int reverseNumber(int n) {
	int r = 0;
	while(n != 0) {
		r *= 10;
		r += n % 10;
		n /= 10;
	}
	return r;
}

int isPalindrome(int n) {
	return n == reverseNumber(n);
}