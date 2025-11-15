[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

<a name="TOP"></a>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />

![🇬🇧](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png) <a name="EN"></A>

<!-- English -->
# 🔥 Mastering Process Creation: A Cross-Platform Power Approach 🚀🧠

## 🌌 **Processes**: *what they are and why they matter 🧬⚙️*

A **process** is a living entity inside the operating system 🧿:

* a program *in execution*
* equipped with its own memory space
* identified by a **PID (Process ID)** 🔢
* scheduled by the kernel according to specific policies 🎛️

Thanks to processes, the system can run multiple programs at the same time—browsers, editors, system services, and much more.
They are a fundamental pillar of modern operating system architecture 💻🔥.

## 🧨 Creating processes in C *on Unix-like systems* 🍏🐧

**C** uses the powerful syscall **fork()** ⚔️, available *exclusively* on **Unix-like** systems (`Linux`, `macOS`, BSD, ...).
On Windows ❌ this call does *not* exist and cannot be replicated in the same way.

### 🧪 How *fork()* works

When a process calls `fork()`:

* an almost perfect **clone** of the parent process is created
* the execution flow splits in two 🪞
* `fork()` returns:

  * **0** inside the *child* process
  * the child’s **pid** (pid > 0) inside the *parent* process
  * **-1** if an error occurs

#### 📦 C Example [`es00.c`](./es00.c)

In [this example](./es00.c) you can see how to invoke `fork()` and use `getpid()` and `getppid()` to display the current process ID and the parent process ID.

#### 🔮 Compilation and execution

```bash
gcc es00.c -o viewProcess

./viewProcess
```

#### 🔮 Possible output

```
main process [500] >> child process [501]
child process [501] >> main process [500]
```

## 🐍 Processes in Python: *two approaches, two worlds* 🌍

*Python* can create processes in two different ways:

### 🟥 **Approach 1** – Based on `os.fork()` (Unix-like only) 🧫🐧

Python exposes a wrapper for the C syscall `fork()` via the `os` module.
**Huge limitation:** it does NOT work on Windows ❌ because Windows does not implement `fork()`.

### 📦 Python example using fork [`es00.py`](./es00.py)

This example is a direct translation of the [C code](./es00.c) into Python 🐍.

#### 🔮 Running the script

```bash
python3 ./es00.py
```

You can also execute it simply with:

```bash
./es00.py
```

As long as:

* you're running on a Unix-like system 🔮
* the first line contains the interpreter path: `#!/usr/bin/python3`
* the file is made executable using:

  ```bash
  chmod +x ./es00.py
  ```

#### 🔮 Possible output

```
main process [702] >> child process [703]
child process [703] >> main process [702]
```

### 🧨 *The problem*

On Windows → **an error is raised**.

Example:

```
AttributeError: module 'os' has no attribute 'fork'
```

### 🟩 **Approach 2** – Based on `multiprocessing` (portable!) 🌐🦾

This approach is:

* **cross-platform**
* **well-structured**
* supports communication, synchronization, queues, pipes
* mimics the “Unix-style process model” even on Windows

It is the recommended, universally compatible solution 🌍🤝.

## ✨ In-depth explanation of the multiprocessing example [`main.py`](./main.py) 💡🧠

### 💭 *General idea*

We create a separate process for each Simpson family member.
Each process:

* prints its PID
* sleeps for a random number of seconds
* prints a termination message

This demonstrates **true parallel execution** in a clear, practical way 💥.

#### 🔮 Possible output

```
main process [pid 880]
*** START PROCESS ***
process [pid: 881] has started..
process [pid: 882] has started..
process [pid: 883] has started..
process [pid: 884] has started..
process [pid: 885] has started..
[pid: 881] I'm Homer Jay Simpson. I will be terminated in 8 seconds..
[pid: 882] I'm Marjorie Jacqueline Simpson. I will be terminated in 3 seconds..
...
*** END PROCESS ***
```

## 🌐 Working with Linux without installing it: [webvm.io](https://www.webvm.io) <img src="https://webvm.io/tower.ico" style="max-width:24px; max-height:24px;"> 🚀🖥️

If you're working on Windows but want to run programs using `fork()` or test Unix-like C/Python code, use: 👉 [https://www.webvm.io](https://www.webvm.io)

![webvm.io](https://webvm.io/assets/social_2024.png)

It’s a fully functional Linux environment **inside your browser**, completely sandboxed, free, and instantaneous.
You can:

* write files
* compile them
* run programs
* use terminal editors

### 🧭 Essential Linux terminal commands 🧱🐧

* 📁 Create folders → `mkdir foldername`
* Move into a folder → `cd foldername`
* Go back → `cd ..`
* Show current directory → `pwd`
* Edit files with nano → `nano -T 4 -l filename`
* Show file contents → `cat filename`

### 📤 Copying code from webvm

Even though it's a full Linux environment, file export isn’t available.
But since everything runs in your browser, you can:

* select the text → **CTRL+C**
* paste it into your editor → **CTRL+SHIFT+V**

## 🎯 Final Thoughts ✨

* ✔️ **C** and **Python** using `fork()` share a powerful but **Unix-only** model
* ✔️ **Windows** does not support `fork()` → *cannot be used*
* ✔️ The **multiprocessing** module is the ultimate solution: robust, portable, modern
* ✔️ [webvm.io](https://www.webvm.io) lets you experiment with Linux in seconds, *no installation required*
* ✔️ You now have clear, detailed, and highly professional knowledge about process creation 🚀

## 💥📢 Remember:

Understanding how processes are created and managed, both in **C** and **Python**, gives you a true developer superpower 🔥.

Experiment, make mistakes, fix them… and above all, *never stop exploring* 🚀.


<hr/>

![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>

<!-- Italian -->
# 🔥 Mastering Process Creation: A Cross-Platform Power Approach 🚀🧠

## 🌌 **Processi**: *cosa sono e perché esistono? 🧬⚙️*

Un **processo** è un’entità viva del sistema operativo 🧿:
* un programma *in esecuzione*
* dotato di spazio di memoria proprio
* identificato da un **PID (Process ID)** 🔢
* schedulato dal kernel secondo precise politiche 🎛️

Grazie ai processi, il sistema può eseguire simultaneamente più programmi: browser, editor, servizi di sistema, ecc.
Sono fondamentali per l’architettura moderna dei sistemi operativi 💻🔥.

## 🧨 Creazione di processi in C *su sistemi Unix-like* 🍏🐧

Il **C** usa la potentissima syscall **fork()** ⚔️, disponibile *solo* su sistemi **Unix-like** (`Linux`, `macOS`, BSD, ...).
Su Windows ❌ questa chiamata *non esiste* e non è implementabile allo stesso modo.

### 🧪 Meccanismo della *fork()*

Quando un processo chiama `fork()`:

* viene creato un **clone** quasi perfetto del processo padre
* il flusso si sdoppia 🪞
* `fork()` ritorna:
	* **0** nel processo *figlio*
	* **pid** (pid > 0) del *figlio* nel processo *padre*
	* **-1** in caso di errore

#### 📦 Esempio C [`es00.c`](./es00.c)

In [questo esempio](./es00.c) viene mostrato come invocare la `fork()` e come mostrare attravero `getpid()` e `getppid()` il pid del processo corrente e quello del processo padre.

#### 🔮 Compilazione ed esecuzione del codice

```bash
gcc es00.c -o viewProcess

./viewProcess
```

#### 🔮 Possibile output

```
main process [500] >> child process [501]
child process [501] >> main process [500]
```


## 🐍 Processi in Python: *due approcci, due mondi* 🌍

*Python* può creare processi tramite due modalità:


### 🟥 **Approccio 1** – Basato su `os.fork()` (solo Unix-like) 🧫🐧

Python espone un wrapper sulla syscall C `fork()` tramite il modulo `os`.
**Limite gigantesco:** NON funziona su Windows ❌, perché Windows non implementa `fork()`.

### 📦 Esempio Python che usa fork [`es00.py`](./es00.py)

Questo esempio è l'esatta traduzione del [codice C](./es00.c) in Python 🐍

#### 🔮 Esecuzione del codice

```bash
python3 ./es00.py
```

Inoltre è possibile avviare i file anche scrivendo semplicemente:

```bash
./es00.py
```

A patto però:
* di trovarci in dei sistemi Unix Like 🔮
* la riga del codice deve contenga l'indirizzo dell'interprete, ovvero `#!/usr/bin/python3`
* che il file sia reso eseguibile
	(ciò è possibile col comando):

		```bash
		chmod +x ./es00.py
		```

#### 🔮 Possibile output

```
main process [702] >> child process [703]
child process [703] >> main process [702]
```

### 🧨 *Problema*

Su Windows → **solleva un errore**.

Esempio:

```
AttributeError: module 'os' has no attribute 'fork'
```

### 🟩 **Approccio 2** – Basato su `multiprocessing` (portabile!) 🌐🦾

Questo approccio è:

* **cross-platform**
* **altamente strutturato**
* supporta comunicazione, sincronizzazione, code, pipes
* imita il modello “processi stile Unix” anche su Windows

È il metodo consigliato e universalmente compatibile 🌍🤝.

## ✨ Spiegazione approfondita dell’esempio multiprocessing [`main.py`](./main.py) 💡🧠

### 💭 *Idea generale*

Creiamo un processo separato per ogni membro dei Simpson.
Ogni processo:

* stampa il proprio PID
* dorme un numero casuale di secondi
* stampa quando termina

Questo dimostra in modo limpido la **parallelizzazione reale** 💥.

#### 🔮 Possibile output

```
main process [pid 880]
*** START PROCESS ***
process [pid: 881] has started..
process [pid: 882] has started..
process [pid: 883] has started..
process [pid: 884] has started..
process [pid: 885] has started..
[pid: 881] I'm Homer Jay Simpson. I will be terminated in 8 seconds..
[pid: 882] I'm Marjorie Jacqueline Simpson. I will be terminated in 3 seconds..
...
*** END PROCESS ***
```

## 🌐 Lavorare su Linux anche senza installarlo: [webvm.io](https://www.webvm.io) <img src="https://webvm.io/tower.ico" style="max-width:24px; max-height:24px;"> 🚀🖥️
Se stai lavorando da Windows ma vuoi eseguire programmi che usano `fork()` o vuoi testare codice C/Python Unix-like, allora usa: 👉 [https://www.webvm.io](https://www.webvm.io)

![webvm.io](https://webvm.io/assets/social_2024.png)

È un ambiente Linux completo **nel browser**, totalmente sandboxed, gratuito e immediato.
Puoi:

* scrivere file
* compilarli
* eseguire programmi
* usare editor da terminale

### 🧭 Comandi fondamentali da terminale Linux 🧱🐧

* 📁 Creare cartelle `mkdir nomecartella`
* `cd nomecartella` 🚶‍♂️ Spostarsi tra cartelle
* `cd ..` tornare indietro
* `pwd` mostrare la cartella corrente
* `nano -T 4 -l nomefile` 📝 Editare file con `nano` (con tab 4 spazi e numeri di linea)
* `cat nomefile` mostrare a schermo il contenuto di un file

### 📤 Copiare il codice da webvm

Sebbene sia un ambiente Linux completo non è possibile esportare i file, ma essendo eseguito tutto in un browser è possibile:

* selezionare il testo → **CTRL+C**
* incollarlo dentro nel tuo editor di fiducia → **CTRL+SHIFT+V**

## 🎯 Conclusioni ✨

* ✔️ **C** e **Python** basato su `fork()` condividono un modello potente ma **Unix-only**
* ✔️ **Windows** non supporta `fork()` → *impossibile usarlo*
* ✔️ Il modulo **multiprocessing** è la soluzione definitiva: robusto, portabile, moderno
* ✔️ [webvm.io](https://www.webvm.io) ti permette di sperimentare Linux in pochi secondi, *senza installazioni*
* ✔️ Ora possiedi conoscenze chiare, dettagliate e altamente professionali sui processi 🚀

## 💥📢 Ricordate:

Comprendere come nascono e lavorano i processi, sia in **C** che in **Python**, vi dà un superpotere da veri sviluppatori 🔥.

Sperimentate, sbagliate, correggete… e soprattutto *non smettete mai di esplorare* 🚀.

<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)