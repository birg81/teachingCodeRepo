# 🐾 PetsList from CLI answer and Data Persistence 🐕🐟

## Obiettivo:

Creare un sistema di gestione di animali domestici con classi in Java.
Utilizzare ereditarietà e un'`ArrayList` per memorizzare una lista dinamica di animali.
Implementare anche un meccanismo di persistenza dei dati tramite un file CSV.

## Classi da Implementare:

* `Animal`:

- Classe base rappresentante un animale.
- Ogni animale ha un nome (`name: String`), e una dimensione (`dimension: int`)
- La classe deve prevedere un *costruttore*, dei metodi *getters/setters* e un metodo `toString()`
- La classe deve inoltre prevedere un metodo `toCSVfile()` che restituisce una stringa che verrà usata per il salvataggio nel file **csv**.

* `LandPet`:

- Estende la classe `Animal`.
- Rappresenta un animale domestico terrestre (**es**: *cane* 🐕, *gatto* 🐈).
- Aggiungi come attributo specifico il verso (`animalSound: String` 🙊🔊).

* `WaterPet`:

- Estende la classe `Animal`.
- Rappresenta un animale domestico acquatico (**es**: *pesce rosso* 🐠 o *animali marini* 🦀 🦑 🦞).
- Aggiungi come attributo specifico un booleano per indicare se appartiene ad una specie di acqua dolce (*fresh water*) o salata (*sea water*) (`isSeaWater`).

## CSVManager:

- Nel main bisogna prevedere del codice per gestire la lettura e la scrittura del file CSV.
- All'avvio del programma, controlla se esiste un file CSV; in tal caso leggi gli animali dal file e aggiungili a `ArrayList<Animal> pets`.
- Utilizza un ciclo `while` per permettere all'utente di inserire animali fintanto che lo desidera.
- All'interno del ciclo, chiedi all'utente di specificare se vuole aggiungere un animale terrestre o acquatico.
- Chiedi il nome dell'animale e gli attributi specifici in base al tipo di animale.
- Aggiungi l'animale a `ArrayList<Animal> pets`.
- Alla chiusura del programma, scrivi la lista aggiornata di animali nel file CSV.