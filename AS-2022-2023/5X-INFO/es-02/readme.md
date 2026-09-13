# Introduzione
<img align="right" src="https://t3.ftcdn.net/jpg/05/06/86/60/240_F_506866064_lNmNXAjVqAHLIggNBVij9dcm6TJ8TQor.jpg" height="150px" />
A seguire lo studente dovrà svolgere le seguenti interrogazioni. Pertanto il docente propone una sfida alla quale ogni 10 query si scatta di livello.

Alcune query prevederanno un livello semplice ed uno avanzato, solitamente indicando nelle specifiche, se non indicato si intende che la query avanzata si distingue perché scritta in versione pro ovvero scritta con una corretta indentazione, facendo uso di alias sui nomi dei campi e delle tabelle, ordinando le istanze con il giusto criterio, adoperando join ove previsto e query annidate

*Buon Lavoro*

## Lista Query
### Q1
Elencare tutte le persone nella lista ordinandole per cognome, nome, data di nascita (ordinando prima le persone più giovani e poi quelle più anziane)
### Q2
Elencare le generalità di tutte le donne nate prima del 2000
### Q3
Elencare le generalità dei primi 10 uomini più alti della lista
### Q4
Elencare le generalità delle 5 donne più magre della lista
### Q5
Elencare le generalità (anche altezza, peso e IMC) delle persone dalla più magra alla più grassa

*si calcoli l’indice di massa corporea* $$IMC = 10^4 \cdot {weight \over height^2}$$
### Q6
Ripetere la query precedente escludendo le persone sovrappeso o quelle sottopeso, ovvero selezionare solo quelle normopeso, quindi con IMC > 18.5 e IMC <= 25.0
### Q7
Elencare le generalità delle persone il cui numero di cellulare non contiene il 2 o il numero 4
### Q8
Elencare gli uomini la cui altezza è compresa tra 165 e 171 (estremi compresi, adoperare BETWEEN)
### Q9
Elencare le donne che hanno nel codice fiscale una I nell’ultima lettera
### Q10
Elencare le generalità degli uomini che nel loro nome non hanno la lettera O

<img align="right" src="https://t4.ftcdn.net/jpg/01/96/75/59/240_F_196755933_6T0jRKuPz4zdKMNtn6WCzaA1TbmpJuRG.jpg" height="75px" />

### CABALLERO:
Se sei arrivato fino a qui o se hai svolto almeno 10 query puoi auto riconoscerti il grado di **Caballero**
### Q11
Elencare le generalità (Nome, Cognome, Sesso, Codice Fiscale, Città provincia) delle donne della provincia di Salerno, facendo appello non al sesso (gender) ma alle sole indicazioni del codice fiscale (campo code di person), ordinandole per cognome, nome città
### Q12
Selezionare la data di sistema di oggi, di ieri, di una settimana fa e del mese scorso
### Q13
Selezionare il segno zodiacale corrente
### Q14
Verificare se oggi è il compleanno di qualcuno, in tal caso selezionare le generalità: Nome, Cognome, Data di nascita, sesso
### Q15
Selezionare il segno zodiacale di tutte le donne che NON sono nate nella provincia di NA, elencando per queste: nome, cognome, data di nascita, sesso, segno zodiacale, città, provincia; ordinandoli per segno zodiacale, provincia, città, cognome
### Q16
Selezionare per la provincia di Napoli, gli uomini con un segno zodiacale di fuoco e volendo mantenere la privacy: selzionare il nome, l'iniziale del cognome, la data di nasciata, il segno zodiacale, la tipologia del segno zodiacale e la provincia
### Q17
Verificare se ci sono minorenni nella lista e per questi selezionare: Nome, Cognome, sesso, data di nascita
### Q18
Selezionare le persone con sangue di fattore Rh+, visualizzando: Cognome, Nome, sesso, Data di nascita, città, provincia, gruppo sanguineo, fattore rh; ordinandoli per provincia, gruppo sanguineo, cognome
### Q19
Selezionare per ogni città, le informazioni catastali, inoltre anche il numero di lettere contenute nel nome della città e per un motivo di privacy visualizzare solo le prime 3 lettere del nome della città; ordinare dunque questa lista per provincia, prime tre lettere del nome della città, numero di lettere totali, provincia e informazioni catastali
### Q20
Elencare le città della prov di Napoli che non contengono la O nel loro nome; visualizzando dunque: città, provincia, CAP, codice, ordinandole per CAP
### CABALLERO BAILANTE
<img align="right" src="https://t3.ftcdn.net/jpg/01/36/15/92/360_F_136159254_4B59C8Lm85A8uIMqyAXaeb5Rwrr0LTmF.webp" height="75px" />
Sembrerebbe che ci stai prendendo gusto!

Se hai concluso almeno 20 query puoi appellarti il titolo di **Caballero Bailante!**

**attenzione!** queste query prendono la mano, tra poco iniziamo con le query serie e la leggenda narra che colui che le risolse tutte prima impazì e poi morì!

*morì perché senza un DBMS doveva selezionare queste cose e riscriverle a mano su un pezzo di carta; in Messico c'era la crisi della carta!*

Quindi continua ma a tuo discapito
	*¡Señor, salva las almas de estos pobres malditos Caballeros!*
### Q21
Elencare le generalità delle persone, dove queste sono nate, dove vivono e dove lavorano.
### Q22
dalla query **Q21** elencare solo le persone che hanno a che fare con Castellammare (ovvero sono nate in questo posto o vi hanno vissuto o vi hanno lavorato)
### CABALLERO LOCO
<img align="right" src="https://us.123rf.com/450wm/yupiramos/yupiramos1904/yupiramos190438645/122872876-mexican-hat-with-mustache-design-vector-illustration.jpg?ver=6" height="100px" />
