[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

<a name="TOP"></a>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇬🇧](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png) <a name="EN"></a>
# 🚦 Concurrency Control with Binary Semaphores

Welcome to the repository for managing concurrency with binary semaphores in Python!
This repository contains a file [`main.py`](./main.py), which demonstrates the use of binary semaphores for controlling access to shared resources in a multithreaded environment.

## What are Binary Semaphores? 🤔

Binary semaphores are synchronization primitives used in concurrent programming to control access to a shared resource.
They are essentially a variable with two possible states: locked or unlocked. 🛑🔓

In Python, binary semaphores are provided by the `threading` module.
They are particularly useful for scenarios where only one thread should access a critical section of the code at a time.

## Understanding the File 📝

The file showcases a simple implementation of binary semaphores in Python.
Let's see how it works:

1. **Semaphore Initialization**:
- We initialize a binary semaphore with an initial value of 1 using the constructor `threading.Semaphore(1)`.

2. **Shared Variable**:
- We define a shared variable named `variabile_condivisa` that will be accessed and modified by multiple threads.

3. **Thread Function**:
- The file defines a function `funzione_thread(id_thread)` representing the task performed by each thread.
- Each thread acquires the semaphore before entering the critical section, ensuring mutual exclusion.
- Inside the critical section, the shared variable is incremented.
- Finally, the semaphore is released to allow other threads to access the critical section.

4. **Thread Creation and Execution**:
- Two threads are created, each calling the function `funzione_thread` with a unique thread ID.

5. **Output**:
- The file prints the current state of the semaphore before and after acquisition, as well as the value of the shared variable after each increment.

### Contributions and Feedback 🙌

Feel free to contribute to this repository by suggesting improvements, reporting issues, or adding other features related to concurrency control.
Your feedback and contributions are highly appreciated! 🚀

*Happy coding*! 😊✨


<hr/>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a> 🤍 <a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>
# 🚦 Concurrency Control with Binary Semaphores

Benvenuto nel repository per gestire la concorrenza con semafori binari in Python!
Questo repository contiene un file [`main.py`](./main.py), che dimostra l'uso dei semafori binari per controllare l'accesso a risorse condivise in un ambiente multithread.

## Che cosa sono i Semafori Binari? 🤔

I semafori binari sono primitive di sincronizzazione usate nella programmazione concorrente per controllare l'accesso a una risorsa condivisa.
Sono essenzialmente una variabile con due possibili stati: bloccato o sbloccato. 🛑🔓

In Python, i semafori binari sono forniti dal modulo `threading`.
Sono particolarmente utili per scenari in cui solo un thread dovrebbe accedere a una sezione critica del codice alla volta.

## Comprensione del File 📝

Il file mostra un'implementazione semplice di semafori binari in Python.
Vediamo come funziona:

1. **Inizializzazione del Semaforo**:
- Inizializziamo un semaforo binario con un valore iniziale di 1 usando il costruttore `threading.Semaphore(1)`.

2. **Variabile Condivisa**:
- Definiamo una variabile condivisa chiamata `variabile_condivisa` che sarà accessibile e modificata da più thread.

3. **Funzione del Thread**:
- Il file definisce una funzione `funzione_thread(id_thread)` che rappresenta il compito svolto da ciascun thread.
- Ogni thread acquisisce il semaforo prima di entrare nella sezione critica, garantendo l'esclusione reciproca.
- All'interno della sezione critica, la variabile condivisa viene incrementata.
- Infine, il semaforo viene rilasciato per consentire ad altri thread di accedere alla sezione critica.

4. **Creazione ed Esecuzione dei Thread**:
- Vengono creati due thread, ognuno dei quali chiama la funzione `funzione_thread` con un ID univoco per il thread.

5. **Output**:
- Il file stampa lo stato corrente del semaforo prima e dopo l'acquisizione, oltre al valore della variabile condivisa dopo ciascun incremento.

### Contributi e Feedback 🙌

Sentiti libero di contribuire a questo repository suggerendo miglioramenti, segnalando problemi o aggiungendo altre funzionalità legate al controllo della concorrenza.
Il tuo feedback e i tuoi contributi sono molto apprezzati! 🚀

*Buon coding*! 😊✨


<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)