'''
Questa funzione prende in ingresso una stringa e restituisce una stringa codificata secondo il cifrario di cesare
'''
def cifrario_cesare(myString, index = 3):	# definizione di una funzione che prende in ingresso la stringa da codificare e l'indice per shiftare le lettere (3)

	# definisco una lista alphabet che contiene l'alfabeto e una lista vuota coded_string che conterrà i caratteri shiftati di una quantità index
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	coded_string = []


	for i in range(0, len(myString)):	# L'indice i varia da 0 fino alla lunghezza della mia stringa. myString[i] ogni ciclo conterrà una lettera diversa della mia parola di ingresso.

		for j in range(0, len(alphabet)):	# Ciclo per cercare mySstring[i] nella lista alphabet. Ogni iterazione, alphabet[j] contiene una lettera diversa dell'alfabeto

			if myString[i].lower() == alphabet [j]:	# Quando ho trovato la mia lettera myString[i] nell'alfabeto, tengo a mente che l'indice j contiene

				coded_index = j + index	# calcolo l'indice del carattere codificato.


				# caso in cui la lettera codificata ha un indice <= della lunghezza della lista alphabet
				if coded_index <= len(alphabet):
					coded_string.append(alphabet[coded_index])	# aggiungo nella lista coded_string la lettera codificata.

				# caso in cui la lettera codificata ha un indice > della lunghezza della lista alphabet.
				else:
					diff = coded_index - len(alphabet)	# mi calcolo il nuovo indice che parte da 0
					coded_string.append(alphabet[diff])	# aggiungo nella lista coded_string la lettera codificata.

				break	# ho codificato la lettera, non sono necessarie ulteriori iterazioni ed esco dal ciclo

	coded_word = ''.join(coded_string)	# coded_word è una lista. Es. ['c','i','a','o']. Il metodo join serve per unire la lista usando il carattere nullo tra un elemento e l'altro.
	print(
		f'\nCodifica effettuata con successo.\nLa parola codificata è: {coded_word}'
	)	# stampa della parola codificata in maiuscolo

	return coded_word	# ritorno la stringa codificata


print('\n- - CIFRARIO DI CESARE - -\n')
a = input('Inserisci la parola da codificare: ')	# chiedo in input la parola da codificare
cifrario_cesare(a)	# chiamo la funzione cifrario_cesare passandogli la stringa fornita dall'utente
