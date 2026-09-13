![img](https://em-content.zobj.net/thumbs/120/twitter/348/shopping-cart_1f6d2.png)

# Shopping List

In questa esercitazione viene mostrato un esempio applicativo di FastAPI.
Questo esempio ha come fine quello di realizzare una lista della spesa; in pratica una casella di testo ci permetterà di inserire delle voci all’interno di un elenco non numerato. Una voce verrà aggiunta alla lista solo se questa non è già presente e se è una stringa valida. Le voci così inserite potranno poi essere ad una ad una cancellate, o potranno essere modificate (a patto che non venga sostituito con una voce già presente o con una stringa invalida).

L’esempio è particolarmente significativo perché propone un **CRUD** completo sulla lista di voci

In questa cartella verranno mostrati differenti approcci:

* [```ver. 1.x```](./shoppinglist-v1.x) adopera rotte che restituiscono pagine html, analizza le variabili nel URL ed adopera per semplicità solo il metodo GET; non fa uso degli url per analizzare i parametri.
* [```ver. 2.x```](./shoppinglist-v2.x) crea un CRUD usando i protocolli appropriati, quindi non solo il GET, si relega FastAPI a svolgere il semplice ruolo di avvio della pagina principale e WebAPI, spostando il carico di lavoro verso il client-side, adoperando Vanilla javaScript per creare in effetti una **SPA** (single page application).
