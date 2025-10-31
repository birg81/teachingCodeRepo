/*
Convert a number to Roman numeral notation
*/
#include <stdio.h>

int main() {
	int number;

	// Choose your number
	printf("Insert a number in this range [1..3999] please? ");
	scanf("%d", &number);

	// Check if the number is within the valid range
	if(number <= 0 || number > 3999) {
		printf("*** ERROR: ****\n(invalid number [%d])\n", number);
	} else {
		// Extract units (u), tens (da), hundreds (c), and thousands (k) from number
		int
			u = number % 10,               // units place
			da = (number - u) % 100,       // tens place
			c = (number - da - u) % 1000,  // hundreds place
			k = number - c - da - u;        // thousands place
		switch(k) {             // switch..case for thousands
			case 1000:
				printf("M");
				break;
			case 2000:
				printf("MM");
				break;
			case 3000:
				printf("MMM");
				break;
			default:
				break;
		}
		switch(c) {             // switch..case for hundreds
			case 100:
				printf("C");
				break;
			case 200:
				printf("CC");
				break;
			case 300:
				printf("CCC");
				break;
			case 400:
				printf("CD");
				break;
			case 500:
				printf("D");
				break;
			case 600:
				printf("DC");
				break;
			case 700:
				printf("DCC");
				break;
			case 800:
				printf("DCCC");
				break;
			case 900:
				printf("CM");
				break;
			default:
				break;
		}
		switch(da) {             // switch..case for tens
			case 10:
				printf("X");
				break;
			case 20:
				printf("XX");
				break;
			case 30:
				printf("XXX");
				break;
			case 40:
				printf("XL");
				break;
			case 50:
				printf("L");
				break;
			case 60:
				printf("LX");
				break;
			case 70:
				printf("LXX");
				break;
			case 80:
				printf("LXXX");
				break;
			case 90:
				printf("XC");
				break;
			default:
				break;
		}
		switch(u) {             // switch..case for units
			case 1:
				printf("I");
				break;
			case 2:
				printf("II");
				break;
			case 3:
				printf("III");
				break;
			case 4:
				printf("IV");
				break;
			case 5:
				printf("V");
				break;
			case 6:
				printf("VI");
				break;
			case 7:
				printf("VII");
				break;
			case 8:
				printf("VIII");
				break;
			case 9:
				printf("IX");
				break;
			default:
				break;
		}
	}
	printf("\n\n");
	return 0;
}
