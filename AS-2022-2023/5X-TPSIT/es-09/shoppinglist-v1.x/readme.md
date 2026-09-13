# Shopping List 🛒

## approccio semplice v. 1.x

### Introduzione

In questo esempio per restare semplici si crea un **CRUD** completo attraverso la creazione e l’uso di 4 rotte, le quali corrispondono alle 4 operazioni CRUD fondamentali, (lettura della lista, aggiunta di una voce, eliminazione e modifica) solo che queste anziché essere svolte attraverso 4 metodi differenti verranno svolte attraverso il metodo GET, inoltre verranno analizzati le variabili nella URL; in generale i parametri che verranno valutati saranno l’ ```id``` della voce, il valore (la stringa) che rappresenta la voce ```item```, fornendo una risposta puramente html. Non verrà quindi fatto uso di una approccio SPA (single page application) ma a 4 rotte differenti che avranno come ultimo scopo, dopo eventuali operazioni, quello di visualizzare la pagina html con la lista di voci.

### Design delle rotte

Di seguito vengono mostrate le rotte adoperate e loro funzionamento:

* ```./``` **READ** mostra la lista completa delle voci presenti
* ```./create?item=<tua voce>``` **CREATE** crea ed aggiunge una nuova voce alla lista di voci, a patto che la voce non sia già presente nella lista.
* ```./delete?id=<id voce>``` **DELETE** elimina una nuova voce dalla lista di voci, a patto che l’indice sia un valore valido.
* ```./update?id=<id voce>&item=<tua voce>``` **UPDATE** modifica, aggiorna una nuova voce dalla lista di voci a patto che l’indice sia valido e il nuovo valore della voce non sia già presente nella lista.

### Dettagli implementativi

L’elemento principale di questo esempio è la variabile ```itemsList = []``` ovvero una lista di stringhe che contiene l’elenco delle diverse voci.

Visto che le 4 rotte hanno come scopo ultimo quello di mostrare la medesima pagina ([```root.html```](./templates/root.html)) nella quale richiamare la lista delle voci; onde ripetere lo stesso spezzone di codice 4 volte nelle differenti rotte; è stata definita una funziona ad hoc:
```python
def home(req: Request):
	# do someting
	pass
```
questa viene richiamata di volta in volta dalle quattro rotte rendendo quindi il codice più snello, modulare, leggibile e più facilmente debuggubile.

Sebbene nel file [```shopapp.py```](./shopapp.py) si faccia riferimento a risorse statiche, tale utilizzo è davvero marginale, infatti serve prevalentemente per fare riferimento alla favicon e al file javascript.
In sostanza è stato introdotto solo per rendere l’esempio più completo e significativo.

### Integrazione di JavaScript

Tra i diversi file presenti nell’esempio, si faccia attenzione al file [```script.js```](./static/src/js/script.js). Questo file viene richiamato dalla pagina html ed adoperato per la modifica delle diverse voci. Allo scopo di non dover creare una nuova pagina con un form per la modifica della voce, è stata fatta la scelta di adoperare una funzione in JavaScript ```modifyItem(id, item)```, (funzione scritta nella forma di arrow function) che mostra una finestra di inserimento per chiedere il nuovo valore della voce. Se il nuovo valore è una stringa valida diversa dal valore precedente, richiama la rotta per la modifica, inviando ad essa il valore nuovo della voce e l’indice della voce suddetta.

### Dettagli e Curiosità della GUI

Questo esempio è disponibile in due subversion, che potremmo rispettivamente chiamare 

* **ver. 1.0**: nella quale viene mostrata una pagina html basilare (viene eseguita la pagine [```root.html```](./templates/root.html) ), 
* **ver 1.1**: nella quale viene mostrata in luogo alla pagina html base una pagina che ingloba al suo interno anche il framework per lo stile **bootstrap**, ciò oltre a migliorare l’usabilità dalla webapp, la rende anche più responsive; a tale scopo viene sostituita la root.html con [```root.advance.html```](./templates/root.advance.html)

Passare da una versione all’altra è semplice basta indicare nel file [```shopapp.py```](./shopapp.py) da lanciare è ```root.advance.html``` in luogo a ```root.html```, ovvero basta togliere il commentare e decommentare l’altra nella funzione ```home()``` sopracitata.

La necessità di queste due versioni è presto detto: anche l’occhio vuole la sua parte, ma ciò non deve per forza di cose rappresentare un sovraccarico di informazioni che possano creare eccessiva confusione con queste righe di codice.

### Automatismi

L’esempio dispone di un [```file batch```](./start.bat), il quale se avviato sui sistemi DOS/Windows, avvia la tua applicazione automaticamente e lancia il tuo Browser sul tuo IP in modo da verificare il rendering del tuo progetto.
Attraverso tale script, oltre ad avviare l’applicazione vi è una sezione che permetterà di controllare ed eventualmente scaricare e installare i moduli python attraverso pip in maniera completamente automatica.
Dopo il primo avvio, si consiglia di modificare il file batch in modo da evitare tali controlli e rendere l’avvio più veloce, per far ciò si consiglia di controllare il file batch e decommentare opportunamente delle righe.
All’interno di tale file Batch sono state settate alcune impostazioni in linea con la scelta del mio browser preferito; nello specifico io adopero Vivaldi, se tu adoperi un browser diverso potresti pensare di evitare quella sezione o modificare la variabile alla riga 40 in modo da settarla con quella del tuo browser preferito.
Attraverso l’uso delle impostazioni di tale file batch sarà possibile, all’interno della propria rete privata, aprire dal browser del proprio dispositivo mobile la webapp e condividere la stessa esperienza anche col proprio telefonino.
Nel caso si faccia uso del file bath (magari perché si sta avviando l’esempio da un sistema unix like), si può ottenere il medesimo effetto lanciando al terminale delle istruzioni precise, ovvero:
```bash
python -m uvicorn shopapp:webapp --host 0.0.0.0 --http httptools --reload
```
Adesso basterà avviare l’app browser del proprio dispositivo mobile e, dopo aver trovato l’indirizzo **IP** del dispositivo dove gira la webapp (quello sul quale è installato python), ```http://<tuo ip>:<tua porta>/``` e godere così di un’esperienza più immersiva.
