# CRUD Java - Gestione Persone

Questo progetto Java implementa un'applicazione console che gestisce un elenco di persone tramite un menu interattivo. L'utente può eseguire le seguenti operazioni su un elenco di oggetti `Persona`:

- Visualizzare tutte le persone
- Aggiungere una nuova persona
- Modificare i dati di una persona esistente
- Eliminare una persona

## Descrizione

Il progetto si compone di una classe `Persona` con proprietà come nome, cognome, età e ID. L'applicazione offre un menu interattivo che consente all'utente di selezionare una delle operazioni sopra elencate. I dati vengono gestiti in memoria e il menu continua a essere visualizzato finché l'utente non decide di uscire.

## Funzionalità

Le principali funzionalità implementate sono:

1. **Visualizzare tutte le persone**:
   - Visualizza un elenco completo di tutte le persone presenti nel sistema.

2. **Aggiungere una nuova persona**:
   - Permette di inserire una nuova persona, specificando nome, cognome e età.

3. **Modificare una persona esistente**:
   - Permette di modificare i dettagli di una persona già presente nell'elenco, come nome, cognome e età.

4. **Eliminare una persona**:
   - Permette di rimuovere una persona dall'elenco.

## Struttura del progetto

Il progetto è composto da due classi principali:

- `Persona.java`: La classe che definisce l'oggetto persona con attributi come `id`, `nome`, `cognome`, `età`.
- `Main.java`: La classe che implementa il menu interattivo e la logica del CRUD.

## Come eseguire il progetto

1. **Clona il repository**:
   ```bash
   git clone https://github.com/tuo-username/crud-persona-java.git
   cd crud-persona-java