/*
Questo esercizio richiede all'utente di inserire un ora da 0-23 e restituisce in base a quel valore il giusto saluto, ovvero:
(versione con if)
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

	if(orario >= 8 && orario <= 12)
		cout << "buongiorno\n";
	else if(orario >= 13 && orario <= 17)
		cout << "buon pomeriggio\n";
	else if(orario >= 18 && orario <= 21)
		cout << "buonasera\n";
	else if(orario >=22  && orario <= 3)
		cout << "buonanotte\n";
	else
		cout << "che ci fai ancora in piedi?!\n";

	return 0;
}