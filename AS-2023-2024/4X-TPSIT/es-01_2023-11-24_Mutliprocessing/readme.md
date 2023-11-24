[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

<a name="TOP"></a>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇬🇧](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png) <a name="EN"></a>
# Multiprocess in Python 🚀

## Introduction to Processes in Python 👋
Welcome to the world of processes in Python! This is the place where the mysteries of parallelization are unveiled, and your code will run simultaneously in multiple dimensions.

## **Definition**: What is a Process? 🔄

A process is like a star 🌟 in the sky of your operating system.
Each star shines independently, carrying out its task without disturbing the others. In more technical terms, it's an isolated snapshot of a running program.

## Python 🐍 and Processes: ✨ the **module** (`Library`) `multiprocessing` 🎩

Python has an ace up its sleeve called `multiprocessing`.
This module turns your code into a magic act, allowing you to perform operations in parallel and fully harness the power of your computer.

## Analysis of Different Phases 🚀

Starting from the code in the [`main.py`](./main.py) file, let's analyze the Code 🕵️‍♂️

### List of Phases 🔍

* **Module Importation**: `import multiprocessing as mp` - like other languages, Python allows importing external modules and libraries; in our case, the `multiprocessing` module has been imported, and to avoid typing `multiprocessing` every time, an alias `mp` is created, allowing for shorter code.
* **Processor Counting**: `mp.cpu_count()` - this imported module provides many useful pieces of information; in this case, thanks to the `.cpu_count()` method, we get to know the number of processors in your system (CPU).
* **Creation of Processes**: `mp.Process(target=callableFunction, args=('functionArgument',))` - through the `.Process(…)` method, we can create a process by indicating what the process should do with two parameters:
	- `target`: which calls the function to be executed
	- `args`: passing parameters to the function
In our case, the `hello()` function was called, along with the string representing the invoked parameter.
* **Start of the Created Process**: `.start()` - now that the process has been created, the only thing left is to start it by launching it through the `.start()` method.

## Conclusions 🌈

Now that you have discovered the world of processes in Python, you are ready to use the superpowers of parallelization in your code.
Boost your code's performance by running multiple tasks simultaneously and let your code express itself in ways you never imagined! 🚀✨

Thank you for entering the magical world of Python processes! 🌟✨


<hr/>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a> 🤍 <a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>
# Multiprocess in Python 🚀

## Introduzione ai Processi in Python 👋
Benvenuto nel mondo dei processi in Python!
Questo è il posto dove verranno svelati i misteri della parallelizzazione si svela, e il tuo codice verrà eseguito simultaneamente in più dimensioni.

## **Definizione**: Cos'è un Processo? 🔄

Un processo è come una stella 🌟 nel cielo del tuo sistema operativo.
Ogni stella brilla indipendentemente, eseguendo il proprio compito senza disturbare le altre.
In termini più tecnici, è una fotografia isolata di un programma in esecuzione.

## Python 🐍 e i Processi: ✨ il **modulo** (*Libreria*) `multiprocessing` 🎩

Python ha un asso nella manica chiamato `multiprocessing`.
Questo modulo trasforma il tuo codice in un atto di prestigio, consentendoti di eseguire operazioni in parallelo e di sfruttare appieno la potenza del tuo computer.

## Analisi delle diverse fasi 🚀

Partendo dal codice del file [`main.py`](./main.py), analiziamo il Codice 🕵️‍♂️

### Elenco delle fasi 🔍

* **Importazione del modulo**: `import multiprocessing as mp` - come altri linguaggi, anche python permette di importare moduli e librerie esterne; nel nostro caso è stato importato il modulo `multiprocessing` e per non scrivere ogni volta `multiprocessing`, viene creato un alias `mp` che mi permette di scrivere nel codice un testo più corto.
* **Conteggio dei processori**: `mp.cpu_count()` - questo modulo importato permette di avere molte informazioni utili, in questo caso, grazie al metodo `.cpu_count()` conoscere il numero di processori nel tuo sistema (CPU).
* **Creazione di processi**: `mp.Process(target=funzioneRichiamata, args=('argomentoFunzione',))` - attraverso il metodo `.Process(…)`, possiamo creare un processo indicando cosa il processo deve fare attraverso due parametri
	- `target`: che richiama la funzione da eseguire
	- `args`: che passa alla funzione i parametri
Nel nostro caso è stata richiamata la funzione `hello()` e la stringa che rappresenta il parametro richiamato
* **Avvio del processo creato**: `.start()` - adesso che il processo è stato creato non rimane che fallo partire avviandolo attraverso il metodo `.start()`.

## Conclusioni 🌈

Ora che hai scoperto il mondo dei processi in Python, sei pronto per utilizzare i superpoteri della parallelizzazione nel tuo codice.
Rendi più performante il tuo codice avviando in maniera parallela più task contemporaneamente e lascia che il tuo codice si esprima in modi che mai avresti immaginato!🚀✨

Grazie per essere entrato nel mondo magico dei processi Python! 🌟✨


<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)