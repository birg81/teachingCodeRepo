[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

<a name="TOP"></a>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

---


![🇬🇧](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png) <a name="EN"></A>

<!-- English -->
# 🐧 The Galactic Guide to the Linux Terminal 🚀

> Welcome, **explorer**! 🌌 If you're here, it means you've decided to ditch colorful icons and dive into the raw power of text. In this guide, we’ll learn how to master Linux from the ground up. 🛠️

## 1. 🔌 The Command Bridge: Connecting via SSH

Imagine driving a machine while chilling on your couch. 🛋️ **SSH (*Secure Shell*)** is the protocol that lets you do exactly that: send encrypted commands to another computer (Linux) from your Windows PC.

### How to do it on Windows 🪟

* Open the **Terminal** (or **PowerShell**). 💻
* Type: `ssh <username>@<ip_address>` (*e.g.* `ssh mario@192.168.1.50`).
* Accept the security key by typing `yes`. ✅
* Enter the `password` (***you won’t see any characters appear, that’s normal!*** 🤫)

---

## ⚠️ Educational Disclaimer & Practical Notes 🛡️

> 👨‍🏫 Before we begin, let’s clarify the environment we’re working in. 🔍

### 🌐 Our Setup: *Shared Connection* 🤝

For our lab activities, both I (your instructor) and you students are connected via **SSH protocol** to a physical device: a **Raspberry Pi 4 Model B** running Linux. 🍓💻

* **Why SSH?** 🔌 Because it allows multiple users to work **simultaneously** on the same machine. 👥
* **Goal:** Learn how to manage files, folders, and permissions collaboratively, just like in a real professional server environment. 🏗️📂

### 💻 No Linux on your PC? No problem! 🚀

If you don’t have Linux installed and want to practice on your own, here are two great options: 🛤️

1. **Virtual Machine (VM):** 📦 Install software like VirtualBox or VMware to create a “computer inside your computer” and run your favorite Linux distro. 💿

2. **WebVM (Quick Solution):** ☁️ Use [https://webvm.io](https://webvm.io). 🌐 It’s a Linux distribution that runs directly in your browser thanks to WebAssembly. ⚡

	* **Note:** In this case, **you don’t need SSH**; you’ll have a ready-to-use `bash shell` immediately! ⌨️🔥

> Now, back to the good stuff.

---

## 2. 👥 Who are you? ***User*** and the legendary ***Root***

In Linux, not all users are created equal. ⚖️

* ***User*** *Standard User*: That’s you. You can do almost anything in your “home,” but you can’t mess with system files. 🏠
* ***Root*** *Superuser*: The *god mode* of the system. ⚡ Can create, destroy, and modify anything.

*With great power comes great responsibility*: one wrong command as root can wipe an entire disk! 💀

## 3. 📂 The World Map: Main Directories

Unlike Windows (`C:\`), Linux uses a tree structure starting from the root **`/`**. 🌳

> Don’t confuse `/` (*root directory*) with the ***root*** user

| **Folders** | *Description* |
| ---: | --- |
| `/bin` | Basic commands (`ls`, `cp`, `mv`). ⚙️ |
| `/boot` | Everything needed to boot the system (*Kernel and bootloader*). 🔑 |
| `/dev` | **Devices**: hardware components appear here as files. 🖱️ |
| `/etc` | System configuration files live here. 🛠️ |
| `/lib` and `/lib64` | Shared libraries required by programs in `/bin`. 📚 |
| `/media` and `/mnt` | ***Mount points*** for external drives, USBs, temporary partitions. 🔌 |
| `/home` | Users’ personal directories. 🛌 |
| `/proc` | **Process info**: virtual filesystem providing kernel and process information. 🧠 |
| `/root` | Root’s private space. 🔒 |
| `/tmp` | *Temporary files* that disappear on reboot. 💨 |
| `/var` | **Variable data** like logs and databases. 📈 |

## 4. 🔐 The Secret of `rwx` (Permissions)

Every file and folder has a label with three letters: `rwx`

| `rwx` | *permission* | binary | octal | description |
| ---: | :---: | :---: | :---: | --- |
| `r` | ***r**ead* | `100` | `4` | You can read the file. 📖 |
| `w` | ***w**rite* | `010` | `2` | You can modify or delete it. ✍️ |
| `x` | *e**x**ecute* | `001` | `1` | You can run it as a program. 🏃 |

This pattern repeats three times: for the *owner*, *group*, and *others*.

## 5. 📋 Essential Commands Table

| Command | What does it do? 🤔 | Example / Parameters 💡 |
| ---: | --- | --- |
| `clear` | Clears the screen when things get messy. 🧼 | `clear` or press `CTRL + L` |
| `whoami` | Tells you who you are logged in as. 👤 | `whoami` |
| `pwd` | Where am I? (**Print Working Directory**). 📍 | `pwd` |
| `uname` | System info. 🐧 | `uname -a` |
| `echo` | Prints text to the screen. 🗣️ | `echo <message>` |
| `touch` | Creates an empty file. ✨ | `touch note.txt` |
| `cat` | Displays file content. 📄 | `cat file1.txt file2.txt` |
| `nano` | Simple text editor. ✍️ | `nano -c file.txt` (*shows line numbers*) |
| `mkdir` | Creates a folder. 📁 | `mkdir -p ./<folder>/<subfolder>` |

## 6. 🧭 Navigation and File Management

The `cd` command lets you move around. 🏃‍♂️

| `<command> <parameters>` | Description |
| ---: | --- |
| `cd` | Go back home (**Home directory**). 🏠 |
| `cd ~` | Same as `cd`, `~` represents your home |
| `cd .` | Stay where you are. 📍 |
| `cd ..` | Go up one level. 🔙 |

To see what’s inside a folder, use `ls`: 🕵️‍♂️

| `<command> <parameters>` | Description |
| ---: | --- |
| `ls -l` | Detailed list |
| `ls -a` | Show hidden files |
| `ls -1` | One file per line |
| `ls -r` | Reverse order |
| `ls -v` | Natural alphabetical order |
| `ls -h` | Human-readable sizes (KB, MB, GB…) |
| `ls --color=always` | Colored output |
| `ls --group-directories-first` | Folders first |

### 🛠️ File manipulation

| `<command> <parameters>` | Description | Example |
| ---: | --- | --- |
| `cp` | Copy 👯‍♂️ | `cp <source> <destination>` |
| `mv` | Move or rename 🚚 | `mv <file/folder> <path/new_name>` |
| `rm` | Remove (careful!) 🗑️ | `-r` remove folders 📂🧨 `-f` force delete 🔥 |

## 7. 🌊 Pipes and Streams (Input/Output)

In Linux, everything flows like data streams. 🌊

| **Standard** | value | Description |
| ---: | :---: | --- |
| **`STDIN`** | `0` | Input (keyboard). ⌨️ |
| **`STDOUT`** | `1` | Standard output (screen). 📺 |
| **`STDERR`** | `2` | Error output. ⚠️ |

### ✨ Pipes and Redirection

| Operator | Description | Example |
| ---: | --- | --- |
| `>` | Overwrites a file with output | `echo <text> > file.txt` |
| `>>` | Appends output to file ➕ | `echo <text> >> file.txt` |
| `\|` | **Pipe**: sends output of one command into another | `ls \| grep napoli` 🚿 |

## 8. 🛠️ Bonus: Real-Life Useful Commands

| **Command** | *Description*|
| ---: | --- |
| `history` | Shows previously used commands 📜 |
| `top` / `htop` | Displays CPU usage (text task manager) 📊 |
| `man <command>` | ***The manual*** 📚 |
| `grep <text>` | ***The search tool*** 🔍 |
| `less` | Scroll through content up/down 📄 |
| `more` | Scroll down only ⬇️ |
| `chown` | Change file owner 👤 |
| `chgrp` | Change group 👥 |
| `chmod` | Change permissions 🔐 |
| `sudo` | Run as administrator (*root*) 🔑 |

🍎💻 *One command a day keeps the bugs away!*

---

![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>

<!-- Italian -->
# 🐧 Guida Galattica al Terminale Linux 🚀

> Benvenuto, **esploratore**! 🌌 Se sei qui, è perché hai deciso di abbandonare le icone colorate per immergerti nel potere del testo. In questa guida impareremo a dominare Linux partendo da zero. 🛠️

## 1. 🔌 Il Ponte di Comando: Collegarsi via SSH

Immagina di voler guidare una macchina restando comodamente seduto sul divano. 🛋️ **SSH (*Secure Shell*)** è il protocollo che ti permette di fare proprio questo: inviare comandi crittografati a un altro computer (Linux) dal tuo PC Windows.

### Come si fa su Windows? 🪟

* Apri il **Terminale** (o **PowerShell**). 💻
* Digita: `ssh <nomeutente>@<indirizzo_ip>` (*es*. `ssh mario@192.168.1.50`).
* Accetta la chiave di sicurezza digitando `yes`. ✅
* Inserisci la `password` (***non vedrai i caratteri muoversi, è normale!*** 🤫).

---

## ⚠️ Disclaimer Didattico & Note Operative 🛡️

> 👨‍🏫 Prima di iniziare, è fondamentale chiarire lo scenario in cui ci stiamo muovendo. 🔍

### 🌐 Il nostro Setup: *Connessione Condivisa* 🤝
Per le nostre attività di laboratorio, io (il vostro docente) e voi studenti ci siamo connessi tramite **protocollo SSH** ad un dispositivo fisico: un **Raspberry Pi 4 Mod. B** con distribuzione Linux. 🍓💻
*	**Perché SSH?** 🔌 Abbiamo scelto questa strada per permettere a più persone di lavorare **contemporaneamente** sullo stesso dispositivo. 👥
*	**Obiettivo:** Imparare a gestire in maniera condivisa file, cartelle e permessi, simulando un vero ambiente server professionale. 🏗️📂

### 💻 Non hai Linux sul tuo PC? Nessun problema! 🚀
Se non disponi di un computer con Linux installato e vuoi esercitarti in autonomia, hai due strade fantastiche per non restare indietro: 🛤️

1.	**Virtual Machine (VM):** 📦 Puoi installare un software come VirtualBox o VMware per creare un "computer dentro il computer" ed eseguire la tua distro Linux preferita. 💿
2.	**WebVM (Soluzione Rapida):** ☁️ Se non vuoi installare nulla, usa [https://webvm.io](https://webvm.io). 🌐 Si tratta di una distribuzione Linux che gira direttamente nel tuo browser grazie alla tecnologia WebAssembly. ⚡
	*	**Nota bene:** In questo caso **non è necessario usare SSH**; avrai subito a disposizione una `bash shell` pronta all'uso per digitare i tuoi comandi! ⌨️🔥

> Ma adesso torniamo alle spiegazioni

---

## 2. 👥 Chi sei? ***User*** e il leggendario ***Root***

In Linux, non tutti gli utilizzatori sono uguali. ⚖️

* ***User*** *Utente Standard*: *Sei tu*. Puoi fare quasi tutto nella tua "*casa*", ma non puoi toccare i file di sistema. 🏠
* ***Root*** *Superuser*: È il *Dio* del sistema. ⚡ Può creare, distruggere e modificare qualsiasi cosa!

*Con grandi poteri derivano grandi responsabilità*: un comando sbagliato da root può cancellare l'intero disco! 💀

## 3. 📂 La Mappa del Mondo: Le Cartelle Principali

A differenza di Windows (`C:\`), Linux ha una struttura ad albero che parte dalla radice **root** `/`. 🌳

> Non confondere il percorso `/` (*root*) con il superuser ***root***

| **Cartelle** | *Descrizione* |
| ---: | --- |
| `/bin` | I comandi base (come `ls`, `cp`, `mv`). ⚙️ |
| `/boot` | Contiene tutto ciò che serve per l'avvio (*il Kernel e il bootloader*). 🔑 |
| `/dev` | **Device**: qui i componenti hardware (dischi, mouse) appaiono come file. 🖱️ |
| `/etc` | Dove vivono i file di configurazione del sistema. 🛠️ |
| `/lib` e `/lib64` | Le librerie condivise (i pezzi di codice) necessarie ai programmi in `/bin`. 📚 |
| `/media` e `/mnt` | Cartelle del ***mounting***, punti di aggancio per dischi esterni, USB o partizioni temporanee. 🔌|
| `/home` | Le stanze private degli *utenti*. 🛌 |
| `/proc` | **Process info**: filesystem virtuale che fornisce informazioni sul kernel e sui processi. 🧠 |
| `/root` | La stanza privata di Dio (**root**). 🔒 |
| `/tmp` | *File temporanei* che spariscono al riavvio. 💨 |
| `/var` | **Variable**: dati che cambiano spesso, come file di log e database. 📈|

## 4. 🔐 Il Segreto di `rwx` (Permessi)

Ogni file e cartella hanno un'etichetta con tre lettere: `rwx`

| `rwx` | *permesso* | base 2 | base 8 | descrizione |
| ---: | :---: | :---: | :---: | --- |
| `r` | ***r**ead* | `100` | `4` | Puoi leggere il file. 📖 |
| `w` | ***w**rite* | `010` | `2` | Puoi scriverci o cancellarlo. ✍️ |
| `x` | *e**x**ecute* | `001` | `1` | Puoi eseguirlo come un programma. 🏃 |

Questa etichetta si ripete tre volte ed indica cosa può fare il *proprietario*, cosa il *gruppo* e cosa tutti gli *altri*.

## 5. 📋 Tabella dei Comandi Fondamentali

| Comando | Cosa fa? 🤔 | Esempio / Parametri 💡|
| ---: | --- | --- |
| `clear` | ripulisce lo schermo quando c'è troppo caos. 🧼 | `clear` o in alternativa basta premere `**CRTL** + l` contemporaneamente |
| `whoami` | Ti dice chi sei loggato. 👤 | `whoami` |
| `pwd` | Dove sono? (**Print Working Directory**).📍 | `pwd` |
| `uname` | Info sul sistema operativo. 🐧 | `uname -a` *tutte le info* |
| `echo` | Stampa del testo a video. 🗣️ | `echo <messaggio da stampare>` |
| `touch` | Crea un file vuoto. ✨ | `touch note.txt` |
| `cat` | Legge il contenuto di un file. 📄 | `cat file1.txt file2.txt` |
| `nano` | Editor di testo semplice. ✍️ | `nano -c file.txt` **NB:** `-c` *mostra i numeri di riga* |
| `mkdir` | Crea una cartella. 📁 | `mkdir -p ./<cartella>/<sottocartella>` **NB:** `-p` *permette di creare anche sottocartelle dentro la cartella appena creata* |

## 6. 🧭 Navigazione e Gestione File

Il comando `cd` serve per muoversi. 🏃‍♂️

| `<comando> <parametri>` | Descrizione |
| ---: | --- |
| `cd <senza parametri>` | Torna subito a casa (**Home**). 🏠 |
| `cd ~` | fa lo stesso di `cd`, `~` rappresenta la cartella dell'*utente corrente* |
| `cd .` | Rimani dove sei (punto corrente). 📍 |
| `cd ..` | Torna indietro di una cartella. 🔙 |

Per vedere cosa c'è dentro una cartella, usiamo `ls`: 🕵️‍♂️

| `<comando> <parametri>` | Descrizione |
| ---: | --- |
| `ls -l` | lista dettagliata |
| `ls -a` | mostra anche file nascosti |
| `ls -1` | una riga per file |
| `ls -r` | visualizza il contenuto in ordine inverso (*reverse*) |
| `ls -v` | ordine alfabetico (*ordine naturale*) |
| `ls -h` | *human readble* mostra le dimensioni non più solo in *kB*, ma in base al file anche in *MB*, *GB*, *TB*, ecc… |
| `ls --color=always` | visualizzazione colorata |
| `ls --group-directories-first` | cartelle prima dei file |

Per manipolare i file: 🛠️

| `<comando> <parametri>` | Descrizione | Esempio / Parametri 💡|
| ---: | --- | --- |
| `cp` | Copia . 👯‍♂️ | `cp <sorgente> <destinazione>` |
| `mv` | Sposta o Rinomina. 🚚 | `mv <file/cartella> <percorso / nuovo nome>` |
| `rm` | Rimuove (attenzione!). 🗑️ | `-r` : Rimuove intere cartelle. 📂🧨 `-f` : Forza la rimozione senza chiedere. 🔥 |

## 7. 🌊 Pipe e Flussi (Input/Output)

In Linux, tutto è un flusso di dati. 🌊

| **Standard** | valore| Descrizione |
| ---: | :---: | --- |
| **`STDIN`** | `0` | L'input che dai (tastiera). ⌨️ |
| **`STDOUT`** | `1` | L'uscita normale (schermo). 📺 |
| **`STDERR`** | `2` | L'uscita relativa ai messaggi di errore. ⚠️ |

### Gli Operatori di Pipe e Ridirezione Flussi: ✨

| Operatore | Descrizione | esempio |
| ---: | --- | --- |
| `>` | Sovrascrive un file con l'output | `echo <testo> > file.txt` 📥 sovrascrive il contenuto di un file, se il file non esiste lo crea e ci scrive dentro |
| `>>` | Aggiunge l'output in fondo al file senza cancellare nulla. ➕ | `echo <altro testo> >> file.txt` agginge a fine del file la scritta di `<altro testo>` |
| `\|` | **Pipe**: Prende l'uscita di un comando e la *butta* dentro un altro | `ls \| grep napoli` 🚿 filtra solo le righe che contengono `napoli` |

## 8. 🛠️ Bonus: Comandi Utili per la Vita Vera

| **comando** | *descrizione* |
| ---: | --- |
| `history` | Ti mostra tutti i comandi che hai digitato in passato. 📜 |
| `top` o `htop` | Vedi cosa sta consumando la CPU (il task manager testuale). 📊 |
| `man <comando>` | ***Il manuale***! Se non sai cosa fa un comando, chiedi a lui. 📚 |
| `grep <testo>` | ***Il cercatore***! Filtra l'output per trovare solo le righe che contengono una specifica parola. 🔍 |
| `less` | Apre un file o un output permettendoti di scorrerlo su e giù (molto più potente di more). 📄 |
| `more` | Simile a `less`, ma ti permette solo di scorrere verso il basso, una pagina alla volta. ⬇️ |
| `chown` |	***ch**ange **own**er*: cambia il proprietario di un file o di una cartella. 👤 |
| `chgrp` | ***ch**ange **gr**ou**p***: cambia il gruppo associato a un file. 👥 |
| `chmod` | ***ch**ange **mod**e*: cambia i permessi di lettura, scrittura ed esecuzione. 🔐 |
| `sudo` | esegue un comando con i privilegi da amministratore (*root*). 🔑 |

*Un comando al giorno toglie il bug di torno*! 🍎💻

<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)
