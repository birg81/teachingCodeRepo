# Traccia

### versione base
Definire una funzione che prende in ingresso una stringa e restituisce una stringa
codificata secondo il cifrario di Cesare.

### versione avanzata
Ripere l'esercizio usando stavolta il cifrario di di Vigenère e facendo sì che il messaggio in chiaro sia case sensitive; sviluppare inoltre anche una funzione di decodifica.

## PREREQUISITI TEORICI
- Definizione di una funzione
- Dizionari
- Funzioni built-in su stringhe
- Strutture decisionali
- richiesta di input
- Utilizzo di moduli

## Funzionamento **cifrario di Cesare**:

È trai più antichi cifrari ed è probabilmente anche il più semplice, eppure applicando tale cifrario agli antichi testi, sono venute alla luce diverse curiosità storiche.
In tale crifrario ogni lettera del messaggio viene traslata in avanti di 3 posizioni, ovvero ogni lettera è sostituita con la lettera corrispondente a tre posizioni in avanti.

## ESEMPIO
- INPUT: "CESARE"
- OUTPUT: "FHVDUH"

## Funzionamento **cifrario di Vigenère**:
Questo cifrario si può considerare una versiona avanzata di quello di Cesare.
Chiave non è più un numero che rappresenta il numero di lettere da traslare.
In questo cifrario ogni lettera della chiave rappresenta il numero di lettere che deve traslare il messaggio, di conseguenza ogni lettera del messaggio può effetture un numero di traslazioni differenti.
Se la chiave è più corta del messaggio, le lettere della chiave si replicano in modo tale da diventare lunga quanto il messaggio!

## Esempio
- INPUT:
	- "Cesare" (plain text)
	- "Roma" (key)
- OUTPUT:
	- "Utfbjt"