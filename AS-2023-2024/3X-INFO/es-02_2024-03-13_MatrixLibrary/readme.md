[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

<a name="TOP"></a>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇬🇧](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png) <a name="EN"></a>
# Matrix Library 🧮

Welcome to the matrix library!
This [library](./matrixlib.c) provides functions for working with matrices in C.
With just a few lines of code, you can manipulate matrices and perform various operations.
Discover what this library has to offer.

## Introduction 📝

Matrices are fundamental mathematical objects used to represent data in various fields, including computer graphics, physics, and engineering.
This library aims to simplify working with matrices by providing functions to load, generate, print, and manipulate them efficiently.

### Theoretical Overview

Before continuing, it's important to understand: **why was the code divided into multiple files?**

The division of files into libraries in C and other programming languages is useful because:

* **Code Reusability**: 🔄 Libraries allow you to write once and reuse functionalities multiple times.

* **Code Organization**: 📁 It helps organize the code into logical and structured units, facilitating understanding and maintenance.

* **Functionality Isolation**: 🛡️ Libraries hide the implementation and provide only a public interface, promoting encapsulation.

* **Separate Compilation**: 🛠️ It allows separate compilation of parts of the program, speeding up compilation times and simplifying development.

In C, the division is done through [header files](./matrixlib.h) (`.h`) and [implementation files](./matrixlib.c) (`.c`), promoting modularity and separation of concerns in the code.

### Preprocessor Directives 🛠️

To achieve code division, it's important to use preprocessor directives, i.e., commands used before compilation that are recognizable by the `#` symbol.

**But what are they for?**
They are used to avoid multiple inclusion of headers in source files.

* `#ifndef` 🛠️: This construct, abbreviated as **if not defined**, checks if a symbol (or macro) has not been defined previously.
If the symbol hasn't been defined, the code block between `#ifndef … #endif` will be included in the compiled program.
If the symbol has already been defined, the code block will be ignored.

* `#define` 🛠️: This construct is used to define a symbol or a macro if it hasn't already been defined.
In practice, if the symbol hasn't been defined before, `#define` defines it.
If the symbol has already been defined, `#define` does nothing.
Usually, this is used to avoid conflicts of multiple header inclusions.

* `#endif` 🛠️: This construct indicates the end of the conditional code block started by `#ifndef`.
All preprocessor directives following `#endif` are non-conditional and will be included in the compiled program.

### Curiosity ℹ️

Usually in [header files](./matrixlib.h), the combination of `#ifndef` and `#define` is used, defining a symbol that usually corresponds to the name of the header file written in uppercase, replacing the dot with `_`.

All the code is included between these two directives and `#endif`, which represents the final line of the header file.

📢 The [header file](./matrixlib.h) thus contains the prototypes of the various functions, while the [implementation file](./matrixlib.c) after calling `#include "library.h"` must implement the function prototypes.

🚨 It's **important to note** that while standard C libraries are enclosed in angle brackets (`#include <librery.h>`), user-defined libraries are enclosed in double quotes (`#include "library.h"`).

### General Functionalities 🛠️

* `loadMatrix()`: This function prompts the user to input values for each element of a given matrix.

* `randMatrix()`: This function fills the elements of a matrix with random values.
It's useful for testing and generating random data.

* `printMatrix()`: This function displays the elements of a matrix on the screen.

* `zeroNegative()`: This function replaces any negative elements of a matrix with zero.

### Operations Specific to Square Matrices 🔄

The following functions specifically operate on square matrices, meaning functions that have the same number of rows and columns:

* `zeroBelowMainDiagonal()`: This function sets all elements below the main diagonal of a square matrix to zero.
The main diagonal consists of elements where the row index is equal to the column index.

* `zeroAboveMainDiagonal()`: This function sets all elements above the main diagonal of a square matrix to zero.

* `zeroBelowInverseDiagonal()`: This function sets all elements below the inverse diagonal of a square matrix to zero.
The inverse diagonal consists of elements where the sum of the row and column indices is greater than the size of the matrix minus one.

* `zeroAboveInverseDiagonal()`: This function sets all elements above the inverse diagonal of a square matrix to zero.

## Getting Started 🚀

To start using this library, include the header file `matrixlib.h` in your C program.
Then, you can call any of the functions provided by the library to work with matrices easily.

Explore and use the functions according to your needs!

If you have questions or suggestions, feel free to contact us.

*Happy coding*! 🚀


<hr/>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a> 🤍 <a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>
# Matrix Library 🧮

Benvenuto nella libreria per le matrici!
Questa [libreria](./matrixlib.c) fornisce funzioni per lavorare con le matrici in C.
Con poche righe di codice, puoi manipolare le matrici ed eseguire varie operazioni.
Scopri cosa offre questa libreria.

## Introduzione 📝

Le matrici sono oggetti matematici fondamentali utilizzati per rappresentare dati in vari campi, tra cui grafica computerizzata, fisica e ingegneria.
Questa libreria mira a semplificare il lavoro con le matrici fornendo funzioni per caricarle, generarle, stamparle e manipolarle in modo efficiente.

### Cenni teorici

Prima di continuare è importante capire: **perché il codice è stato suddiviso in più file?**

La suddivisione dei file in librerie in C e in altri linguaggi di programmazione è utile perché:

* **Riutilizzo del codice**: 🔄 Le librerie consentono di scrivere una volta e riutilizzare più volte le funzionalità definite all'interno.

* **Organizzazione del codice**: 📁 Aiuta a organizzare il codice in unità logiche e strutturate, facilitando la comprensione e il mantenimento.

* **Isolamento delle funzionalità**: 🛡️ Le librerie nascondono l'implementazione e forniscono solo un'interfaccia pubblica, promuovendo l'incapsulamento.

* **Compilazione separata**: 🛠️ Consentono la compilazione separata delle parti del programma, accelerando i tempi di compilazione e semplificando lo sviluppo.

In C, la suddivisione avviene tramite [file header](./matrixlib.h) (`.h`) e [file di implementazione](./matrixlib.c) (`.c`), promuovendo la modularità e la separazione delle responsabilità nel codice.

### Direttive pre-processore 🛠️

Per ottenere la suddivisione del codice è importante adoperare le direttive di pre-processore, ovvero dei comandi che vengono adoperati prima che avvenga la compilazione e si riconoscono per la presenza del `#`.

**Ma a cosa servono?**
Vengono utilizzate per evitare l'inclusione multipla degli header nei file sorgente.

* `#ifndef` 🛠️: Questo costrutto, abbreviazione di **if not defined**, verifica se un simbolo (o macro) non è stato definito in precedenza.
Se il simbolo non è stato definito, il blocco di codice compreso tra `#ifndef … #endif` verrà incluso nel programma compilato.
Se il simbolo è già stato definito, il blocco di codice verrà ignorato.

* `#define` 🛠️: Questo costrutto viene utilizzato per definire un simbolo o una macro se non è già stato definito.
In pratica, se il simbolo non è stato definito prima, `#define` lo definisce.
Se il simbolo è già stato definito, #define non fa nulla.
 solito, questo viene utilizzato per evitare conflitti di inclusione multipla degli header.

* `#endif` 🛠️:  Questo costrutto indica la fine del blocco di codice condizionale iniziato da `#ifndef`.
Tutte le direttive di pre-processore successive a `#endif` non sono condizionali e verranno incluse nel programma compilato.

### Curiosity ℹ️

Solitamente nei [file header](./matrixlib.h) si combina l'uso di `#ifndef` e `#define`, viene definito un simbolo che solitamente corrisponde al nome del file header scritto in maiuscolo, sostituendo il punto con `_`.

Tutto il codice viene è compreso in tra queste due direttive ed `#endif`, che rappresenta la riga finale del file header.

📢 Il [file header](./matrixlib.h) contiene quindi i prototipi delle diverse funzioni, mentre il [file di implementazione](./matrixlib.c) dopo aver richiamato `#include "library.h"` dovrà implementazione i prototipi delle funzioni.

🚨 È **importante notare** che mentre le librerie di C sono racchiuse tra le parentesi angolari (`#include <librery.h>`), le librerie definite dall'utente sono invece racchiuse trai doppi apici (`#include "library.h"`).

### Funzionalità Generali 🛠️

* `loadMatrix()` questa funzione chiede all'utente di inserire i valori di ogni elemento di una matrice data.

* `randMatrix()` questa funzione riempie gli elementi di una matrice con valori casuali.
È utile per testare e generare dati casuali.

* `printMatrix()` questa funzione visualizza gli elementi di una matrice a schermo.

* `zeroNegative()` questa funzione sostituisce eventuali elementi negativi di una matrice con zero.

### Operazioni specifiche per Matrici Quadrate 🔄

Le seguenti funzioni operano specificamente su matrici quadrate, ovvero funzioni che hanno lo stesso numero di righe e di colonne:

* `zeroBelowMainDiagonal()` questa funzione imposta tutti gli elementi sotto la diagonale principale di una matrice quadrata a zero.
La diagonale principale consiste di elementi in cui l'indice di riga è uguale all'indice di colonna.

* `zeroAboveMainDiagonal()` questa funzione imposta tutti gli elementi sopra la diagonale principale di una matrice quadrata a zero.

* `zeroBelowInverseDiagonal()` questa funzione imposta tutti gli elementi sotto la diagonale inversa di una matrice quadrata a zero.
La diagonale inversa consiste di elementi in cui la somma dell'indice di riga e di colonna è maggiore della dimensione della matrice meno uno.

* `zeroAboveInverseDiagonal()` questa funzione imposta tutti gli elementi sopra la diagonale inversa di una matrice quadrata a zero.

## Per Iniziare 🚀

Per iniziare a utilizzare questa libreria, includi il file header `matrixlib.h` nel tuo programma C.
Poi, puoi chiamare qualsiasi delle funzioni fornite dalla libreria per lavorare con le matrici in modo semplice.


Esplora e utilizza liberamente le funzioni secondo le tue esigenze!

Se hai domande o suggerimenti, non esitare a contattarci.

*Buon coding*! 🚀

<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)