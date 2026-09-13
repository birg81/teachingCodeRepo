'''
Questo programma mostra una funzione somma che somma solo i numeri positivi.
Nel caso di numeri negativi li pone a 0
'''

# funzione che effettua la somma
def sumPositive(add1 = 0, add2 = 0):
	if add1 < 0:
		add1 = 0
	if add2 < 0:
		add2 = 0
	return add1 + add2

a = 13
b = -5
# stampa risultato
print(f'{a} + {b} = {sumPositive(a,b)}')