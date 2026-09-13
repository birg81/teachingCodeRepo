'''
Creare una funzione che data una stringa fornisce un dizionario con le occorenze delle  diverse lettere
'''

# funzione che effettua il conteggio
def lettersCounter(word = ''):
# dizionario che contiene le lettere e le loro occorrenze
	counting = {}
# - .lower() -> trasforma la stringa in caratteri miniscoli
# - .replace() -> sostituisce i caratteri
# Il ciclo scorre la stringa tutta minuscola
# (conteggio case-insensitive)
# ripulita dagli spazi;
# scorrendola lettera per lettera e
# memorizzando la specifica lettera nella variabile l
# l rappresenta l'indice del dizionario.
# Qualora l'indice l del dizionario fosse già presente,
# il valore viene incrementato,
# altrimenti il valore viene posto ad 1
	for l in word.lower().replace(" ", ""):
		if l in counting:
			counting[l] += 1
		else:
			counting[l] = 1
	return counting

print(lettersCounter('Forza Napoli'))

# OUTPUT:
# {'f': 1, 'o': 2, 'r': 1, 'z': 1, 'a': 2, 'n': 1, 'p': 1, 'l': 1, 'i': 1}
