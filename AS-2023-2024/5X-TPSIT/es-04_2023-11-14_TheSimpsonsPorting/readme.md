work in progress

In riferimento all'esempio presente a [questo link](../../5X-INFO/es-05_2023-11-07_TheSimpsonsDB), questo esempo è il porting in Python / FastAPI, rappresentando però una versione leggermente più limitata in quanto non dispone dell'accesso ai DBMS, in quanto non era ancora oggetto di studio.

Nello specifico il ruolo del DB è svolto da un file [`model.py`](./model.py) che contiene una lista di dizionari.

Il file [`main.py`](./main.py) assolve egregiamente il ruolo che le servlet avevano nel precedente progetto.

Le pagine web sono state edulcorate da qualche link, in quanto non c'è più il concetto di Dispatcher

Per il resto il porting ha richiesto modifiche decisamente marginali.

* Interessante resta la pagina [`characters.v1.jsp`](../../5X-INFO/es-05_2023-11-07_TheSimpsonsDB/src/main/webapp/characters.v1.jsp) che in questa sede viene ad essere rinominata [`characters.v1.html`](./templates/characters.v1.html) e viene edulcorata da molto codice java pedante.
* Interessante è inoltre il ruolo svolto dalle rotte statiche introdotte nel main file ed assolte mediante la funzione `url_for(...)`