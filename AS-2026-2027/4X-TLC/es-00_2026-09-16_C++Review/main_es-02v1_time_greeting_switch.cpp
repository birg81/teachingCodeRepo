/*
Questo esercizio richiede all'utente di inserire un ora da 0-23 e restituisce in base a quel valore il giusto saluto, ovvero:
(versione con switch)
-  8:00 - 12:00 -> buongiorno
- 13:00 - 17:00 -> buon pomeriggio
- 18:00 - 21:00 -> buonasera
- 21:00 - 03:00 -> buonanotte
- 04:00 - 07:00 -> che ci fai ancora in piedi
*/

#include <iostream>
using namespace std;

int main() {
	int orario;

	cout << "Inserisci orario [0-23]: ";
	cin >> orario;

	orario %= 24;	// evita che vengano inseriti valori non consoni

	switch (orario) {
		case 8:
		case 9:
		case 10:
		case 11:
		case 12:
			cout << "buongiorno\n";
		break;

		case 13:
		case 14:
		case 15:
		case 16:
		case 17:
			cout << "buon pomeriggio\n";
		break;

		case 18:
		case 19:
		case 20:
		case 21:
			cout << "buonasera\n";
		break;

		case 22:
		case 23:
		case 0:
		case 1:
		case 2:
		case 3:
			cout<< "buonanotte\n";
 		break;

		default:
			cout << "che ci fai ancora in piedi?!\n";
		break;
	}
	return 0;
}