/*
Calcolo IMC (bmi): Indice Massa Corporea (Body Mass Index)
*/

#include <iostream>
using namespace std;

int main() {
	float peso, altezza, bmi;

	cout << "inserisci peso (kg): ";
	cin >> peso;
	cout << "inserisci altezza (m): ";
	cin >> altezza;

	bmi = peso / (altezza * altezza);

	cout << "il tuo bmi vale " << bmi << "\n";

	if (bmi >= 25)
		cout << "sei in sovrappeso\n";
	else if (bmi < 18.5)
		cout << "sei in sottopeso\n";
	else
		cout << "sei normopeso\n";

	return 0;
}