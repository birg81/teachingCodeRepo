# importo la libreria random
import random

# definisco una lista di numeri interi nella quale pescherò due numeri casuali
number = range(1, 10)
# inizializzo la variabile punteggio
punteggio = 0

# stampo messaggio iniziale
print('''
MATH QUIZ!
''')

'''
appena commetterò un errore, la varibile diverrà False
ciò interromperà il ciclo e terminerà il programma
'''
esatto = True

while esatto:
	'''
	la funzione choice della libreria random serve per
	prendere un elemento random dalla lista per entrambi gli operandi
	'''
	first_number = random.choice(number)
	second_number = random.choice(number)

	# calcolo il risultato atteso
	result = first_number * second_number
	'''
	accetto in ingresso il valore dell'utente.
	ATTENZIONE:
	il valore in input è una stringa!!
	per questo usando la funzione int() verrà convertita in un intero
	'''
	user_input = int(input(f'Quanto fa {first_number} x {second_number}? '))

	'''
	Confronto il risultato corretto con quello inserito dall'utente.
	Se è corretto aumento il punteggio.
	'''
	if result == user_input:
		punteggio +=1

	# se il risultato è sbagliato, stampo il risultato a schermo ed esco dal ciclo con il break
	else:
		esatto = False

print(f'''
ERRATO:
Hai però totalizzato ben {punteggio} punti
''')