[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

# Introduzione
<img align="right" src="https://t3.ftcdn.net/jpg/05/06/86/60/240_F_506866064_lNmNXAjVqAHLIggNBVij9dcm6TJ8TQor.jpg" height="150px" />
A seguire lo studente dovrà svolgere le seguenti interrogazioni.
Pertanto il docente propone una sfida con la quale ogni 10 query si scatta di livello.

Alcune query prevederanno un livello semplice ed uno avanzato e ciò solitamente indicando nelle specifiche; se non viene indicato nulla, una query si considera di livello avanzato quando viene scritta in maniera professionale, ovvero scritta con una corretta indentazione, facendo uso di alias sui nomi dei campi e delle tabelle, ordinando le istanze con il giusto criterio, adoperando join ove previsto ed adoperando con giudizio query annidate.

*Buon Lavoro*

## Dove Scaricare la Base di dati

Visto che a seguire verranno proposte una serie di query su un db predefinito chiamato *sakila*, vediamo dove è possibile scaricare questo DB di esempio.
Seguendo il link [http://dev.mysql.com/doc/index-other.html](https://dev.mysql.com/doc/index-other.html) sarà possibile scaricare dalla sezione Example Databases il file compresso che rappresenta il DB sakila.
In alternativa si può seguire il link diretto [https://downloads.mysql.com/docs/sakila-db.zip](https://downloads.mysql.com/docs/sakila-db.zip).

## Come installare manualmente il DB
Nell'ipotesi di voler installare la base di dati appena scaricata in nel R-DBMS MySQL di XAMPP, procedere con i seguenti passi:
* In primo luogo, dopo aver scaricato la base di dati, estrarre il file compresso e da questi eliminare il file ```sakila.mwb```.
* I due file con estensione ```.sql```, rappresentano rispettivamente le tabelle e le relative righe; dunque copiare questi due fil nella seguente cartella
```batch
C:\xampp\mysql\bin
```

<img align="right" src="https://static.javatpoint.com/tutorial/xampp/images/xampp-control-panel12.png" height="300px" />

* Di seguito avviare da XAMPP Control Panel il Servizio MySQL, come in figura

* Aprire il prompt dei comandi e digitare i seguenti comandi
```batch
cd c:\xampp\mysql\bin
mysql.exe -u root
SOURCE sakila-schema.sql;
SOURCE sakila-data.sql;
```

## Sakila Schema
Per le Query si faccia riferimento a questo schema per aiutarsi:

<img align="center" src="https://database.guide/wp-content/uploads/2016/06/sakila_full_database_schema_diagram.png" width="100%" />

## Lista Query

Avventurieri, sfidate le query con audacia, ma occhio alle trappole nascoste.
La saggezza è un tesoro, ma l'eccesso d'orgoglio può condurre alla follia e alla morte.
*¡Buena suerte!*

### Q0
Selezionare il risultato della seguente operazione ```6 + 5```

### Q1
Elencare Nome e Cognome degli Attori dalla Tabella Attori.

### Q2
Ripetere la Q1 mostrando solo i primi 30 risultati.

### Q3
Mostrare il numero totale di attori contenuti in quella tabella.

### Q4
Elencare Nome e Cognome degli Attori, Ordinando gli attori per cognome in modo Crescente (A-Z), e per gli attori con lo stesso cognome, ordinarli in ordine decrescente del nome (Z-A)

### Q5
Ripetere la Q3 usando un alias per la colonna Numero Attori

### Q6
Ripetere la Q4 usando come alias per le colonne le stringhe Nome e Cognome (scritte in italiano) usando poi questi alias anche per l’ordinamento

### Q7
Ripetere la Q6 filtrando gli attori il cui nome inizia con la lettera B

### Q8
Ripetere la Q6 filtrando gli attori il cui nome o il cognome sia esattamente di 5 caratteri

### Q9
Ripetere la Q6 filtrando gli attori che hanno un nome od il cognome che contiene la lettera A


<img align="left" src="https://ilpost-media-production.ilpost.it/wp-content/uploads/2016/05/blu.jpg" height="2px" width="97%" />


<img align="right" src="https://t4.ftcdn.net/jpg/01/96/75/59/240_F_196755933_6T0jRKuPz4zdKMNtn6WCzaA1TbmpJuRG.jpg" height="100px" />

### CABALLERO
Se sei arrivato fino a qui o se hai svolto almeno 10 query puoi auto riconoscerti il grado di **Caballero**


<img align="left" src="https://ilpost-media-production.ilpost.it/wp-content/uploads/2016/05/blu.jpg" height="2px" width="97%" />


### Q10
Ripetere la Q6 filtrando gli attori che hanno un nome od il cognome che NON contiene la lettera E

### Q11
Elencare i cognomi di tutti gli attori (usare un alias per la colonna) e ordinarli in modo decrescente limitando il risultato alle prime 20 corrispondenze

### Q12
Ripetere la Q11 senza apporre nessun limite nei risultati ma elencando solo i cognomi distinti

### Q13
Contare il numero di record presenti nella Q12


<img align="left" src="https://img.freepik.com/premium-photo/colorful-blend-green-orange-red-pattern-background_7954-21709.jpg" height="2px" width="97%" />


### Q14
Dalla Tabella dei film elencare il nome di tutti i film e la relativa durata, ordinando la lista in base alla durata (in ordine decrescente) e ai titoli ordinati in modo crescente (apporre alle colonne degli alias indicativi).

### Q15
Ripetere la query precedente filtrando i film di durata inferiore a 54min.

### Q16
Ripetere la Q15 visualizzando solo i film di durata compresa tra 50 e 110 min (fare uso della clausola AND)

### Q17
Ripetere la Q16 facendo uso della clausola BETWEEN … AND

### Q18
Visualizzare le seguenti statistiche: il numero totale dei film, la durata totale espressa in ore e minuti (fare uso della clausola ROUND), la durata minima, la durata media e la durata massima


<img align="left" src="https://img.freepik.com/premium-photo/colorful-blend-green-orange-red-pattern-background_7954-21709.jpg" height="2px" width="97%" />



### Q19
Dividendo gli attori in gruppi sulla base del cognome, visualizzare i gruppi e il numero dei relativi membri


<img align="left" src="https://ilpost-media-production.ilpost.it/wp-content/uploads/2016/05/blu.jpg" height="2px" width="97%" />


### CABALLERO BAILANTE

<img align="right" src="https://t3.ftcdn.net/jpg/01/36/15/92/360_F_136159254_4B59C8Lm85A8uIMqyAXaeb5Rwrr0LTmF.webp" height="100px" />

Sembrerebbe che ci stai prendendo gusto!

Se hai concluso almeno 20 query puoi appellarti il titolo di **Caballero Bailante!**

**attenzione!** queste query prendono la mano, tra poco iniziamo con le query serie e la leggenda narra che colui che le risolse tutte prima impazì e poi morì!

*morì perché senza un DBMS doveva selezionare queste cose e riscriverle a mano su un pezzo di carta; in Messico c'era la crisi della carta!*

<img align="left" src="https://em-content.zobj.net/thumbs/120/facebook/65/flag-for-mexico_1f1f2-1f1fd.png" height="30px" />

Quindi continua ma a tuo discapito

  *¡Señor, salva las almas de estos pobres malditos Caballeros!*


<img align="left" src="https://ilpost-media-production.ilpost.it/wp-content/uploads/2016/05/blu.jpg" height="2px" width="97%" />


### Q20
Ripetere la Q19 usando degli alias ed escludendo gli attori i cui cognomi hanno cardinalità 1, ordinando i risultati in modo crescente in base alla cardinalità e in modo decrescente in base al cognome.

### Q21
Ripetere la Q20 filtrando gli attori che hanno il cognome che contiene la A (agire sulla clausola WHERE)

### Q22
Ripetere la Q21 agendo sulla clausola HAVING

### Q23
Elencare Cognomi e Numero degli attori i cui cognomi si ripetono almeno 3 volte


<img align="left" src="https://img.freepik.com/premium-photo/colorful-blend-green-orange-red-pattern-background_7954-21709.jpg" height="2px" width="97%" />


### Q24
Elencare i film, la durata e il genere (fare a questo punto uso di più tabelle) ordinando i film per genere (A-Z), per titolo (A-Z) e per durata (Z-A).

### Q25
Ripetere la Q24 escludendo i film che appartengono al genere drama o commedia

### Q26
Ripetere la Q18, ottenendo le statistiche in base al genere dei film filtrandoli come nella Q25 (sulla clausola HAVING prima e WHERE dopo)


<img align="left" src="https://img.freepik.com/premium-photo/colorful-blend-green-orange-red-pattern-background_7954-21709.jpg" height="2px" width="97%" />


### Q27
Selezionare per ogni indirizzo contenuto nella tabella address, l’indirizzo, il CAP, il nome della città e il nome del paese (ordinandoli per paese, cap e città)

### Q28
In riferimento alla Q27 filtrare gli indirizzi senza CAP o senza numero di  telefonico

### Q29
In riferimento alla Q27 raggrupparli per paese e città contando il numero di indirizzi in essa contenuti



<img align="left" src="https://ilpost-media-production.ilpost.it/wp-content/uploads/2016/05/blu.jpg" height="2px" width="97%" />



<img align="right" src="https://us.123rf.com/450wm/yupiramos/yupiramos1904/yupiramos190438645/122872876-mexican-hat-with-mustache-design-vector-illustration.jpg?ver=6" height="130px" />

### CABALLERO LOCO

Hai risolto altre query, 30 oramai

<img align="left" src="https://em-content.zobj.net/thumbs/120/facebook/65/flag-for-mexico_1f1f2-1f1fd.png" height="50px" />

*Cabalgando por estas tierras desoladas y desérticas, la falta de agua y un sol abrasador volvieron loco a aquel caballero. Felicidades, ahora te has convertido en el **Caballero Loco**. Detente, no continúes, no pierdas tu alma por estas consultas. Que el Señor Dios te devuelva la razón*


<img align="left" src="https://ilpost-media-production.ilpost.it/wp-content/uploads/2016/05/blu.jpg" height="2px" width="97%" />



### Q30
In riferimento alla Q28 filtrare le città che hanno nel loro elenco almeno 3 indirizzi

### Q31
Visualizzare per ogni categoria di film, il numero di film di quella categoria e la durata media dei suddetti film, escludendo le categorie che hanno un solo film

### Q32
Determinare la categoria che ha meno numero di film e la categoria che ha la durata media di film più corta (fare uso di alias e di una UNION od eventualmente strutturare come due query distinte)

### Q33
Per ogni Lingua determinare il numero di film prodotti ordinandoli in numero decrescente e a parità di numero in ordine alfabetico della lingua

### Q34
Determinate la lingua nella quale sono prodotti il maggior numero di film

### Q35
Per ogni attore contare il numero di film nei quali ha partecipato

### Q36
Per ogni film determinare il numero di attori che hanno partecipato

### Q37
Per ogni film determinare il numero di attori con cognome diverso che hanno partecipato

### Q38
Determinare i primi migliori 5 attori che maggiormente hanno partecipato a film e gli ultimi 5 escludendo dalle loro produzioni documentari e film di lunghezza inferiore ad 1 ora e 16 minuti

### Q39
Determinare i titoli dei film che hanno una durata superiore alla media


<img align="left" src="https://ilpost-media-production.ilpost.it/wp-content/uploads/2016/05/blu.jpg" height="2px" width="97%" />



<img align="right" src="https://img.freepik.com/premium-vector/skull-wearing-sombrero-with-mexican-hat-it_625341-2008.jpg" height="175px" />

### CABALLERO DE LA MUERTE

Alla fine ce l'hai fatta! Hai concluso anche l'ultima query!

<img align="left" src="https://em-content.zobj.net/thumbs/120/facebook/65/flag-for-mexico_1f1f2-1f1fd.png" height="50px" />


*Era el día cinco de mayo, en el día de los muertos, cuando aquel pobre caballero pereció en el intento de resolver la última consulta. Señor Dios, guía su alma al paraíso e ilumina a aquellos locos que intentarán inútilmente resolver estas consultas.*

*Felicidades, te has convertido en el **Caballero de la Muerte**.*


## 🔗 Links
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)