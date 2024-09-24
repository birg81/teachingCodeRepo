[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

<a name="TOP"></a>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇬🇧](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png) <a name="EN"></A>
# Multiprogramming & Processes in C 🖥️✨

[**Multiprogramming**](https://www.geeksforgeeks.org/fork-system-call/) is a vital technique 🛠️ in modern operating systems 💻, where multiple processes run simultaneously ⏳. This boosts efficiency 🚀 and allows for better resource management 💡. In a multiprogrammed system, processes can execute tasks interactively 🎮, respond to events 📡, or run in the background 🖥️.

A **process** is an instance of a program running ⚙️. Each process has its own memory space 📂 and can execute instructions independently 🧩. A key concept is the **PID** (**Process ID**) 🆔, which is a unique identifier 🔑 assigned by the operating system to each process 📝.

Processes can be grouped into two main categories:
- **Parent process** 👨‍👦: the process that creates another process 🎯.
- **Child process** 👶: the process created by the parent 🛠️. The child inherits some resources ⚙️ but runs independently 🏃‍♂️.

## Functions Used 📜🛠️

This code uses some key functions 🔧 from the `unistd.h` and `stdio.h` libraries 📚, essential for programming in Unix-like systems 🐧.

### `fork()` 🔀
The `fork()` function is used to create a new process 🚼. The new process is the **child** 👶. If `fork()` returns:
- `0`: we are in the **child process** 👶.
- *Positive value*: we are in the **parent process** 👨‍👦, and the returned value is the child's PID 🆔.
- *Negative value*: an error occurred 🚫, and the process was not created ❌.

### `getpid()` and `getppid()` 🔍
- `getpid()` returns the **PID** of the current process 🆔.
- `getppid()` returns the **PID** of the parent of the current process 🆔👨‍👦.

## How it works? 📂🔧
Let's examine the following [code](./forkInCLang.c), where some functions play a key role. It's crucial to understand how they work, so pay close attention.

### 1. Creating a child process with `fork()` 👶🔀

The program begins by declaring a `var` variable 📝, used to demonstrate shared memory behavior between parent and child 💡. The `fork()` function creates a child process 🌱. The return value of `fork()` is stored in the `p` variable 📊.

### 2. Distinguishing between parent and child processes 👨‍👦👶

The `p` variable is analyzed 🔍:
- If `p == 0`, we are in the **child process** 👶. Here, the `var` variable is decremented ➖, and the program prints a message showing the parent PID (`getppid()`), the child PID (`getpid()`), the value of `var`, and its memory address 📍.
- If `p > 0`, we are in the **parent process** 👨‍👦. Here, `var` is incremented ➕, and a message clearly indicates we are in the parent process 🧑‍💼.

### 3. Error handling 🚨❗

If `fork()` returns a negative value 🔻, it means an error occurred 🚫 during the creation of the child process 🔄. In this case, the program uses `perror()` to print an error message 🛑. `perror()` works similarly to `printf()`, but instead of printing to **Standard Output** (`STD_OUT`), it prints to **Standard Error** (`STD_ERR`).

## Understanding shared memory 🧠🔗

A key part of the code is the management of the `var` variable 🔄. While the parent and child initially share the same memory space 🧩, each process will have its **own copy** of the variable 🔓. Changes made by one process won’t affect the other 🔒. This behavior is common when using `fork()` because the operating system copies the parent's memory to the child when the process is created 📂.

### Example Output 📊🔍

If the program runs successfully, you might see an output like this 📜:

```
Parent PID: 01234	PID: 01235	fork PID: 01236	var: 11 (0x7ffcddd4e04c)		<< PARENT process!
Parent PID: 01235	PID: 01236	fork PID: 00000	var: 09 (0x7ffcddd4e04c)		<< CHILD process!
```

This output shows how the **PID** and `var` values differ between the parent and child processes 🧑‍💻👶, demonstrating the concept of **process independence** 🎯.

## Conclusion 🚀🌟

This example introduces the fundamentals of process management in Unix systems 🐧, such as creating processes with `fork()` and using PIDs to manage them 🔍. Experimenting with these concepts can give you a deeper understanding of how modern operating systems work 🧠.

### 💡 Final Thought:
Every process is like a small universe 🌌, with its own rules, memory, and tasks.

The more you explore and understand these concepts, the more you'll uncover the hidden beauty of computer science 💻.

*Keep experimenting, learning, and exploring new horizons!*👨‍💻


<hr/>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a> 🤍 <a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>
# Multiprogrammazione & Processi in C 🖥️✨

La [**multiprogrammazione**](https://www.geeksforgeeks.org/fork-system-call/) è una tecnica essenziale 🛠️ nei sistemi operativi moderni 💻, in cui più processi vengono eseguiti simultaneamente ⏳.
Questo aumenta l'efficienza 🚀 e permette una migliore gestione delle risorse 💡.
In un sistema operativo multiprogrammato, i processi possono eseguire operazioni in modo interattivo 🎮, rispondendo agli eventi 📡 o lavorando in background 🖥️.

Un **processo** è un'istanza di un programma in esecuzione ⚙️.
Ogni processo ha un proprio spazio di memoria 📂 e può eseguire istruzioni in modo indipendente dagli altri 🧩.
Un concetto fondamentale è il **PID** (**Process ID**) 🆔, che è un identificatore unico 🔑 assegnato dal sistema operativo a ciascun processo 📝.

I processi possono essere classificati in due categorie principali:
- **Processo padre** 👨‍👦: il processo che genera un altro processo 🎯.
- **Processo figlio** 👶: il processo creato dal padre 🛠️.
Il figlio eredita alcune risorse ⚙️ ma esegue istruzioni in modo indipendente 🏃‍♂️.

## Funzioni utilizzate 📜🛠️

Questo codice utilizza alcune funzioni chiave 🔧 derivanti dalle librerie `unistd.h` e `stdio.h` 📚, essenziali per la programmazione di sistemi Unix-like 🐧.

### `fork()` 🔀
La funzione `fork()` viene utilizzata per creare un nuovo processo 🚼.
Il processo generato è il **figlio** 👶.
Se `fork()` ritorna:
- `0`: siamo nel processo **figlio** 👶.
- *Valore positivo*: siamo nel processo **padre** 👨‍👦 e il valore restituito è il PID del processo figlio 🆔.
- *Valore negativo*: si è verificato un errore 🚫 e il processo non è stato creato ❌.

### `getpid()` e `getppid()` 🔍
- `getpid()` restituisce il **PID** del processo corrente 🆔.
- `getppid()` restituisce il **PID** del processo padre del processo corrente 🆔👨‍👦.

## Come funziona? 📂🔧
Osserviamo con attenzione il seguente [codice](./forkInCLang.c), noteremo la presenza di alcune funzioni, che sarà importante comprenderne il funzionamento, quindi prestate molta attenzione

### 1. Creazione di un processo figlio con `fork()` 👶🔀

Il programma inizia dichiarando una variabile `var` 📝, utilizzata per dimostrare il comportamento della memoria condivisa tra padre e figlio 💡.
La funzione `fork()` crea un processo figlio 🌱.
Il ritorno di `fork()` viene memorizzato nella variabile `p` 📊.

### 2. Differenziazione tra processo padre e figlio 👨‍👦👶

La variabile `p` viene quindi analizzata 🔍:
- Se `p == 0`, siamo nel **processo figlio** 👶.
Qui la variabile `var` viene decrementata ➖ e il programma stampa un messaggio con il PID del processo padre (`getppid()`), il PID del processo figlio (`getpid()`), il valore di `var` e il suo indirizzo di memoria 📍.
- Se `p > 0`, siamo nel **processo padre** 👨‍👦.
Qui la variabile `var` viene incrementata ➕ e viene stampato un messaggio che indica chiaramente che siamo nel processo padre 🧑‍💼.

### 3. Gestione degli errori 🚨❗

Se `fork()` restituisce un valore negativo 🔻, significa che si è verificato un errore 🚫 durante la creazione del processo figlio 🔄.
In questo caso, il programma utilizza `perror()` per stampare un messaggio di errore 🛑; `perror()` funziona esattamente come `printf()`, solo che invece di stampare i messaggi sullo **Standard Output** (`STD_OUT`), lo stampa sullo **Standard Error** (`STD_ERR`)

## Considerazioni sulla memoria condivisa 🧠🔗

Una parte importante del codice è la gestione della variabile `var` 🔄.
Anche se padre e figlio condividono inizialmente lo stesso spazio di memoria 🧩, ciascun processo avrà una **copia separata** della variabile 🔓.
Le modifiche fatte da un processo non influenzano l'altro 🔒.
Questo comportamento è comune quando si utilizza `fork()` perché il sistema operativo copia la memoria del padre al figlio al momento della creazione del processo 📂.

### Esempio di output 📊🔍

Eseguendo correttamente il programma, potresti vedere un output simile a questo 📜:

```
Parent PID: 01234	PID: 01235	fork PID: 01236	var: 11 (0x7ffcddd4e04c)		<< PARENT process!
Parent PID: 01235	PID: 01236	fork PID: 00000	var: 09 (0x7ffcddd4e04c)		<< CHILD process!
```

Questo output mostra come i **PID** e il valore di `var` siano differenti per il processo padre e figlio 🧑‍💻👶, dimostrando il concetto di **indipendenza tra processi** 🎯.

## Conclusione 🚀🌟

Questo esempio introduce i concetti base della gestione dei processi nei sistemi Unix 🐧, come la creazione dei processi con `fork()` e l'uso dei PID per identificare e gestire i processi 🔍.
Sperimentare con questi concetti può aiutarti a comprendere meglio come funzionano i sistemi operativi moderni 🧠.

### 💡 Curiosità finale:
Ogni processo è come un piccolo universo 🌌, con le sue regole, il suo spazio di memoria e le sue operazioni.

Più esplori e comprendi questi concetti, più ti renderai conto della bellezza nascosta nel mondo dell'informatica 💻.

*Continua a sperimentare, ad apprendere e a scoprire nuovi orizzonti*!👨‍💻

<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)