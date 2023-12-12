[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

<a name="TOP"></a>

# 🌵 ***Bienvenido Caballero, Explorar ed día de los Query*** 💀 🌵

<img align="right" src="https://t3.ftcdn.net/jpg/05/06/86/60/240_F_506866064_lNmNXAjVqAHLIggNBVij9dcm6TJ8TQor.jpg" height="150px" />

Nelle polverose terre delle Basi di dati, ti do il benvenuto a te Caballero.
Ogni query sarà una sfida, che potrà portarti alla pazia o peggio ancora alla morte. 💀
Solo uno scaltro cantastorie sagace sarà in grado di condurre questo cammino ricco di insidie 🤠
Ogni 10 query, avanzerai di livello ma attenzione a non perdere la tua anima.

Alcune query saranno
* come il sole messicano: calde e roventi ☀️
* altre pericolose come il morso di una serpe 🐍
* altre ancora spinose come cactus 🌵

Riuscirai a discernere tra una domanda facile e una da maestro?
La maestria si svela negli alias ben collocati, nell'indentazione elegante e nell'arte di combinare joins e subquery.

*Che inizi la tua avventura! 🌟*

## 📜 Lista Query

### 🌵 Q1
Elencare tutte le persone nella lista ordinandole per cognome, nome, data di nascita (ordinando prima le persone più giovani e poi quelle più anziane)

### 🌵 Q2
Elencare le generalità di tutte le donne nate prima del 2000

### 🌵 Q3
Elencare le generalità dei primi 10 uomini più alti della lista

### 🌵 Q4
Elencare le generalità delle 5 donne più magre della lista

### 🌵 Q5
Elencare le generalità (anche altezza, peso e IMC) delle persone dalla più magra alla più grassa

*si calcoli l’indice di massa corporea* $$IMC = 10^4 \cdot {weight \over height^2}$$

### 🌵 Q6
Ripetere la query precedente escludendo le persone sovrappeso o quelle sottopeso, ovvero selezionare solo quelle normopeso, quindi con IMC > 18.5 e IMC <= 25.0

### 🌵 Q7
Elencare le generalità delle persone il cui numero di cellulare non contiene il 2 o il numero 4

### 🌵 Q8
Elencare gli uomini la cui altezza è compresa tra 165 e 171 (estremi compresi, adoperare `BETWEEN`)

### 🌵 Q9
Elencare le donne che hanno nel codice fiscale una `I` nell’ultima lettera

### 🌵 Q10
Elencare le generalità degli uomini che nel loro nome non hanno la lettera `O`.

<img align="right" src="https://t4.ftcdn.net/jpg/01/96/75/59/240_F_196755933_6T0jRKuPz4zdKMNtn6WCzaA1TbmpJuRG.jpg" height="75px" />

#### 🕺 ***Caballero***
*Se sei arrivato fino a qui o se hai svolto almeno **10 query** puoi auto riconoscerti il grado di* **Caballero**

### 🌵 Q11
Elencare le generalità (Nome, Cognome, Sesso, Codice Fiscale, Città provincia) delle donne della provincia di Salerno, facendo appello non al sesso (gender) ma alle sole indicazioni del codice fiscale (campo code di person), ordinandole per cognome, nome città.

### 🌵 Q12
Selezionare le seguenti date
* oggi
* ieri
* domani
* della settimana scorsa
* del mese scorso
* domenica scorsa.

### 🌵 Q13
Conta i giorni che mancano al prossimo *Natale* 🎄

### 🌵 Q14
Selezionare il segno zodiacale corrente di questo mese

### 🌵 Q15
Verificare se oggi è il compleanno di qualcuno, in tal caso selezionare le generalità: Nome, Cognome, Data di nascita, sesso

### 🌵 Q16
Selezionare il segno zodiacale di tutte le donne che NON sono nate nella provincia di NA, elencando per queste: nome, cognome, data di nascita, sesso, segno zodiacale, città, provincia; ordinandoli per segno zodiacale, provincia, città, cognome

### 🌵 Q17
Selezionare per la provincia di Napoli, gli uomini con un segno zodiacale di fuoco e volendo mantenere la privacy: selzionare il nome, l'iniziale del cognome, la data di nasciata, il segno zodiacale, la tipologia del segno zodiacale e la provincia

### 🌵 Q18
Verificare se ci sono minorenni nella lista e per questi selezionare: Nome, Cognome, sesso, data di nascita

### 🌵 Q19
Selezionare le persone con sangue di fattore Rh+, visualizzando: Cognome, Nome, sesso, Data di nascita, città, provincia, gruppo sanguineo, fattore rh; ordinandoli per provincia, gruppo sanguineo, cognome

### 🌵 Q20
Selezionare per ogni città, le informazioni catastali, inoltre anche il numero di lettere contenute nel nome della città e per un motivo di privacy visualizzare solo le prime 3 lettere del nome della città; ordinare dunque questa lista per provincia, prime tre lettere del nome della città, numero di lettere totali, provincia e informazioni catastali


### 🕺 ***Caballero Bailante***

<img align="right" src="https://t3.ftcdn.net/jpg/01/36/15/92/360_F_136159254_4B59C8Lm85A8uIMqyAXaeb5Rwrr0LTmF.webp" height="75px" />

Sembra che ti stia divertendo!
Hai superato 20 sfide? Sei un ***Caballero Bailante***!

⚠️ **Attenzione!** *Le sfide si fanno più difficili.*
Narrano leggende di coloro che impazzirono e morirono cercando di risolverle senza un DBMS.

*Continua, ma a tuo rischio.*

*¡Señor, salva las almas de estos pobres malditos Caballeros!*


### 🌵 Q21
Elencare le città della prov di Napoli che non contengono la O nel loro nome; visualizzando dunque: città, provincia, CAP, codice, ordinandole per CAP

### 🌵 Q22
Elencare le generalità delle persone, dove queste sono nate, dove vivono e dove lavorano.

### 🌵 Q23
dalla query **Q22** elencare solo le persone che hanno a che fare con Castellammare (ovvero sono nate in questo posto o vi hanno vissuto o vi hanno lavorato)

***wip***

#### 🕺 ***Caballero Loco***

<img align="right" src="https://us.123rf.com/450wm/yupiramos/yupiramos1904/yupiramos190438645/122872876-mexican-hat-with-mustache-design-vector-illustration.jpg?ver=6" height="100px" />



<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)