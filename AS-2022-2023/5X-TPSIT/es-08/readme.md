<table>
<tr>
<td>
<img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" height="120px" />
</td>
<td>
<img src="https://raw.githubusercontent.com/tomchristie/uvicorn/master/docs/uvicorn.png" height="75px" />
</td>
<td>
<img src="https://jinja.palletsprojects.com/en/3.1.x/_images/jinja-logo.png" width="150px" />
</td>
</tr>
</table>


# FastAPI

## Introduzione sugli esempi proposti

Questa cartella propone due esempi, uno [```/generico```](./generic) il quale contiene tutto il codice generalista, ed uno molto più [```/specifico```](./fullsimple).
All'interno di ognuno dei due esempi vi è un file batch che ha lo scopo di avviare velocemente la webapp creata senza dover ricordare la lista completa di comandi da fornire nella CLI.
A tale scopo il file batch al suo avvio, avvia anche il browser.
Adoperando come browser predefinito Vivaldi, ho personalizzato il batch file, ma tale riga può tranquillamente essere estromessa o modificata in favore del proprio browser preferito.
Gli esempi sono realizzati in modo che, una volta avviata la webapp sia possibile col proprio telefonino condividere la stessa visualizzazione, semplicemente avviando il browser del proprio telefono e scrivendo sulla barra dell'indirizzo l'indirizzo IP e la porta del pc sul quale è avviato FastAPI.

## Primo [```esempio```](./generic)

È una webapp che cerca di essere di esempio ed ha un po' tante cose mischiate, vuole essere una summa di cose (tra le quali anche una cartella della tombola).
Su http://localhost/ verrà mostrato banalmente una pagina HTML, i link in essa contenuti riportano ai diversi esempi

## Secondo [```esempio```](./fullsimple)

È una webapp che propone una scacchiera, ha molte meno cose caotiche ma è più completo in quanto propone anche contenuti statici

## Cosa installare e istruzioni per l'uso

Sebbene i file batch cercano di operare diversi automatismi, trai quali anche il controllo e l'eventuale installazione di moduli richiesti, è bene conoscere i comandi da dare nella CLI.

Dopo aver modificato il file batch, prima di avviarlo è importante installare i diversi componenti richiesti; quindi cmd da amministratore, installare quanto segue:
```bash
pip install fastapi
pip install "uvicorn[standard]"
pip install Jinja2
pip install typing-extensions (opzionale)
pip install httptools
```
od equivalentemente scrivendo:
```bash
python -m pip install httptools uvicorn fastapi Jinja2
```
* **uvicorn** è un semplice server in python
* **fastapi** è il nostro framework stateless che ritorna valori in formato json e costruzione di rotte
* **Jinja2** è un motore di rendering, ovvero un package che permette di integrare codice python all'interno delle pagine html in magniera completamente trasparente al visitatore della pagina
* **typing-extensions** serve a fare il controllo statico del tipo. Sebbene python non sia fortemente tipizzato, questo pacchetto è in grado di forzare i tipi dei diversi parametri
* **httptools** permette ad uvicorn di accettare le connessioni provenienti da altri devices nello specifico si potrà visualizzare lo stesso sito anche dal telefonino!
* **sqlite3** sebbene non è previsto nell'installazione, questi permette il binding con un DBMS locale sqlite

Inoltre è possibile consultare i pacchetti installati attraverso il seguente comando
```bash
python -m pip list
```

Per controllare se un pacchetto è installato basterà scrivere:
```bash
pip show <nomePacchetto>
```

Invece per aggioranre i pacchetti sarà possibile lanciare:
```bash
pip install --upgrade <nomePacchetto>
```

Per se vi sono pacchetti da installare è possibile adoperare invece
```bash
pip list --outdated
```

Infine per disinstallare un pacchetto basta scrivere
```bash
pip uninstall <nomePacchetto>
```

Installate le diverse dipendenze, come si può vedere nei file batch creati a seguito, il miglior modo per avviare la webapp è il seguente
```bash
python -m uvicorn <NomeFileSenzaEstensione>:<NomeOggetto> --reload
```

Di seguito sono indicate le opzioni più significative da dare al comando visto sopra
* ```--reload``` questa opzione permette ad ogni modifica del file .py di poter ricaricare automaticamente il server
* ```--no-use-colors``` questa opzione può essere molto utile se si lancia la webapp dal prompt di windows in quanto questo non è in grado di interpretare i colori e di conseguenza visualizza solo delle scritte senza significato; diversametne powershell è in grado di interpretare correttamente il codice a colori tipico dei terminali UNIX-Like
* ```--port``` per indicare la porta sulla quale girare, può essere in tal caso interessante indicare la porta 80 che viene usata di default per il protocollo HTTP
* ```--host``` per indicare l'host sul quale gira la web app; tale opzione si rileva particolarmente interessante in quanto indicando l'indirizzo IP del proprio dispositivo sarà possibile raggiungere la webapp da tutta la rete locale
* ```--http httptools``` di default è settato su auto od h11, avendo installato il modulo httptools è possibile permettere di accetare connessioni provenienti anche da altri device all'interno della propria rete e così permettere di visualizzare la webapp anche dal browser del proprio telefonino!
