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

# 🔮 Beginner's Guide to Pointers in C: The Power of the Voodoo Doll 🎎

In C, a **regular variable** 📦 is like a container (a drawer 🗄️ or a box in memory 🧠) that directly holds a piece of data: an integer 🔢, a character 🔤, a floating-point number 🌊.

A **pointer** 👉, on the other hand, holds no actual data 🚫📦. A pointer is a voodoo doll 🎎.

The *"value"* 💎 inside this doll is not an ordinary number 🔢❌: it is the memory address 📍 of the variable it is bound to 🔗. Through this bond, the pointer can manipulate ✋, read 👀 and modify ✏️ the linked variable from a distance 🔭, without ever touching it directly 🚫🤚.

## 📜 1. The Tools of the Ritual 🕯️: `&` and `*`

To master 🧙 the magic of pointers ✨, you need two fundamental operators 🛠️:

- 🔗 **The Binding Operator** (`&` - *Address-of*): extracts 📤 the memory address 📍 of a regular variable 📦. It is used to "bind the voodoo doll" 🎎 to a specific target 🎯.
	* `p = &a;	// → 🔗 Binds the doll p to the variable a.`
- 🪡 **The Voodoo Operator** (`*` - **Dereferencing**): acts from a distance 🔭 through the doll 🎎 to strike 💥 or read 👀 the bound variable 📦.
	* `*p = 19;	// → 🪡 Stab the doll p to change the value of a to 19`
	* `(*p)++;	// → ⬆️ Use the doll p to increment the value of the bound variable (b)`.

## 🧪 2. [Exercise 01](./main-es01_PointerBasics.c): *The Ritual of Initialization and Control* 🕯️🔍

Let's walk 🚶 through the code of Exercise 01 step by step 👣 to understand how variables 📦 and pointers 🎎 behave in memory 🧠.

### ⚠️ What happens in the Initial Situation (Output 1)? 🎬

In C, variables are not automatically initialized to zero 0️⃣🚫. When you declare a variable or a pointer (`int* p;`) 📝, the system assigns ✋ an area of memory 🧠 that contains garbage 🗑️ (**garbage value**), i.e. whatever sequence of bits 💾 was left behind by previous executions 🕰️.

In the first output 🖨️:
- 📦 `a` contains `13` and has its own memory address 📍 (e.g. `61ff1c`).
- 📦 `b` contains `72` and has its own memory address 📍 (e.g. `61ff18`).
- 🎎 `p` is an **unbound** 🔓 ***voodoo doll***. Its value `p` is a random address 🎲📍 (*garbage* 🗑️). Trying to use `*p` before it is bound to anything 🔗❌ means *"stabbing a voodoo doll 🪡 aimed at nothing 🕳️"*: the program might show a random value 🎲 or crash right away 💥 (**Segmentation Fault** ☠️).

#### 🖨️ Possible Output of Print 1:

```
[61ff1c] a = 13
[61ff18] b = 72
[61ff14] p = (77c34b10) 32767 <-- 🗑️ p points to random/garbage memory!
```

#### 🚨 Best Practice ✅

It is a good idea 💡 to set the pointer to `NULL` ⭕ so as to avoid unwanted situations 🙅:

```c
int* p = NULL;
```

### 🩸 The First Bond and the Action from a Distance (Output 2) 🔗🔭

Let's perform the binding 🔗:

```c
p = &a; // 🔗 Assign to 'p' the address of 'a'
*p = 19; // 🪡 Modify 'a' through the voodoo doll 'p'
```

Now the doll 🎎 `p` points exactly 🎯 to the memory cell 🧱 of `a`. Writing `*p = 19` ✏️ directly changes the value held in `a` 📦.

#### 🖨️ Output of Print 2:

```
[61ff1c] a = 19
[61ff18] b = 72
[61ff14] p = (61ff1c) 19 <-- 🎯 The value of 'p' is now the address of 'a'!
```

### 🔄 Changing the Voodoo Target (Output 3) 🎯➡️🎯

Pointers are dynamic 🌀: the doll 🎎 can change its target at any time ⏱️.

```c
p = &b; // 🔄 Now the doll 'p' is bound to 'b'
(*p)++; // ⬆️ We remotely increment the value of 'b' (from 72 to 73)
```

#### 🖨️ Output of Print 3:

```
[61ff1c] a = 19
[61ff18] b = 73
[61ff14] p = (61ff18) 73 <-- 🎯 'p' now holds the address of 'b' and reads 73
```

## 🔀 3. [Exercise 02](./main-es02_SwapByReference.c): Sending the Doll on a Mission 🎎🚀

By default ⚙️, in C all functions receive their parameters **by value** 📋 (*they receive a copy*). If you pass `a` and `b` to a function to swap them 🔁, the function will only swap its local copies 📋📋, leaving the originals untouched 🧊.

To modify the local variables 📦 of `main` 🏠 inside another function 🧩, we must send their memory addresses 📍 (the voodoo dolls 🎎):


### In main: 🏠

```C
int a = 13;
int b = 37;

// 📍 We pass the addresses (&a and &b) to the voodoo-doll parameters of swap
swap(&a, &b);
```

### 🖨️ Output of Exercise 02:

```
*** Before swapping ***
[61ff1c] a = 13
[61ff18] b = 37
*** After swapping ***
[61ff1c] a = 37
[61ff18] b = 13
```

📍 The addresses of the variables `a` and `b` never changed, but the values 💎 held inside them were swapped 🔁 from a distance 🔭 by the `swap()` function.

## 🧱 4. [Exercise 03](./main-es03_ArrayPointerSorting.c): Multiple Voodoo Control over Arrays 🎎🎎🎎


In C, the very name of an array 🧱 (e.g. `array`) is equivalent to the address 📍 of its first element (`&array[0]`) 1️⃣. An array is a contiguous sequence 🚂 of memory cells 🧱🧱🧱.

When we pass an array to the sorting function `sort(array, 5)` 📊, the function does not receive a copy 📋❌ of all 5 elements, but a pointer 👉 to the first element 1️⃣.

In the loop 🔁 of the `sort()` algorithm:

- 🔍 The addresses of two specific cells of the array (`&a[i]` and `&a[j]`) are identified 📍📍.
- 📤 These addresses are passed to `swap()`.
- 🎎🎎 `swap()` receives the two voodoo dolls and swaps the values 🔁 directly inside the original array structure 🧱.

### 🖨️ Output of Exercise 03:

```
Before Sorting: 2, 37, 5, 13, 7.
After Sorting: 2, 5, 7, 13, 37.
```

## 📌 Summary of Key Points 🗝️

| Concept 💡 | Voodoo Representation 🎎 | C Syntax 💻 |
| ---: | --- | --- |
| 📦 Regular Variable | The target 🎯 (physically holds a value 💎). | `int a = 10;` |
| 👉 Pointer | The voodoo doll 🎎 (holds the address 📍 of the target). | `int* p;` |
| 🗑️ Missing Initialization | An unbound doll 🔓🎎: it points to garbage 🗑️ in memory 🧠. | `int* p;` (without `= &a`) |
| 🔗 `&` Operator | Creating the voodoo bond 🔗 with the variable 📦. | `p = &a;` |
| 🪡 `*` Operator | The act of stabbing the doll 🎎 to act on the target 🎯 from a distance 🔭. | `*p = 20;` |


---

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

---

![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>

<!-- Italiano -->

# 🔮 Guida Introduttiva ai Puntatori in C: Il Potere della Bambola Voodoo 🎎

In C, una **variabile normale** 📦 è come un contenitore (un cassetto 🗄️ o una scatola in memoria 🧠) che conserva direttamente un dato: un numero intero 🔢, un carattere 🔤, un numero in virgola mobile 🌊.

Un **puntatore** 👉, invece, non contiene alcun dato concreto 🚫📦. Un puntatore è una bambola voodoo 🎎.

Il *"valore"* 💎 contenuto dentro questa bambola non è un numero normale 🔢❌, ma l'indirizzo di memoria 📍 della variabile a cui viene legata 🔗. Attraverso questo legame, il puntatore può manipolare ✋, leggere 👀 e modificare ✏️ a distanza 🔭 la variabile associata, senza toccarla direttamente 🚫🤚.

## 📜 1. Gli Strumenti del Rito 🕯️: `&` e `*`

Per padroneggiare 🧙 la magia dei puntatori ✨ servono due operatori fondamentali 🛠️:

- 🔗 **L'operatore di Legame** (`&` - *Indirizzo*): estrae 📤 l'indirizzo di memoria 📍 di una variabile normale 📦. Serve per "associare la bambola voodoo" 🎎 a un bersaglio preciso 🎯.
	* `p = &a;	// → 🔗 Lega la bambola p alla variabile a.`
- 🪡 **L'operatore Voodoo** (`*` - **Dereferenziazione**): agisce a distanza 🔭 attraverso la bambola 🎎 per colpire 💥 o leggere 👀 la variabile legata 📦.
	* `*p = 19;	// → 🪡 Infilza la bambola p per cambiare il valore di a in 19`
	* `(*p)++;	// → ⬆️ Usa la bambola p per incrementare il valore della variabile legata (b)`.

## 🧪 2. [Esercizio 01](./main-es01_PointerBasics.c): *Il Rituale di Inizializzazione e Controllo* 🕯️🔍

Esaminiamo 🚶 il codice dell'Esercizio 01 passo dopo passo 👣 per capire come agiscono le variabili 📦 e i puntatori 🎎 in memoria 🧠.

### ⚠️ Cosa succede nella Situazione Iniziale (Stampa 1)? 🎬

In linguaggio C, le variabili non sono inizializzate automaticamente a zero 0️⃣🚫. Quando dichiari una variabile o un puntatore (`int* p;`) 📝, il sistema assegna ✋ un'area di memoria 🧠 che contiene spazzatura 🗑️ (**garbage value**), ossia qualsiasi sequenza di bit 💾 rimasta lì da precedenti esecuzioni 🕰️.

Nella prima stampa 🖨️:

- 📦 `a` contiene `13` e ha un suo indirizzo di memoria 📍 (es. `61ff1c`).
- 📦 `b` contiene `72` e ha un suo indirizzo di memoria 📍 (es. `61ff18`).
- 🎎 `p` è una ***bambola voodoo*** *"non vincolata"* 🔓. Il suo valore `p` è un indirizzo casuale 🎲📍 (*spazzatura* 🗑️). Tentare di usare `*p` prima che sia legato a qualcosa 🔗❌ significa *"infilzare una bambola voodoo 🪡 puntata verso il nulla 🕳️"*: il programma potrebbe mostrare un valore casuale 🎲 oppure andare in crash immediato 💥 (**Segmentation Fault** ☠️).

#### 🖨️ Possibile Output della Stampa 1:

```
[61ff1c] a = 13
[61ff18] b = 72
[61ff14] p = (77c34b10) 32767 <-- 🗑️ p punta a memoria casuale/spazzatura!
```

#### 🚨 Best Practice ✅

Potrebbe essere buona idea 💡 inizializzare il puntatore a `NULL` ⭕ in modo da evitare situazioni indesiderate 🙅:

```c
int* p = NULL;
```

### 🩸 Il Primo Legame e l'Azione a Distanza (Stampa 2) 🔗🔭

Eseguiamo l'associazione 🔗:

```c
p = &a; // 🔗 Assegniamo a 'p' l'indirizzo di 'a'
*p = 19; // 🪡 Modifichiamo 'a' attraverso la bambola voodoo 'p'
```

Ora la bambola 🎎 `p` punta esattamente 🎯 alla cella di memoria 🧱 di `a`. Scrivere `*p = 19` ✏️ cambia direttamente il valore contenuto in `a` 📦.

#### 🖨️ Output della Stampa 2:

```
[61ff1c] a = 19
[61ff18] b = 72
[61ff14] p = (61ff1c) 19 <-- 🎯 Il valore di 'p' ora è l'indirizzo di 'a'!
```

### 🔄 Cambiamento del Bersaglio Voodoo (Stampa 3) 🎯➡️🎯

I puntatori sono dinamici 🌀: la bambola 🎎 può cambiare bersaglio in qualsiasi momento ⏱️.

```c
p = &b; // 🔄 Ora la bambola 'p' viene legata a 'b'
(*p)++; // ⬆️ Incrementiamo a distanza il valore di 'b' (da 72 a 73)
```

#### 🖨️ Output della Stampa 3:

```
[61ff1c] a = 19
[61ff18] b = 73
[61ff14] p = (61ff18) 73 <-- 🎯 'p' ora ha dentro l'indirizzo di 'b' e legge 73
```

## 🔀 3. [Esercizio 02](./main-es02_SwapByReference.c): Mandare la Bambola in Missione 🎎🚀

Di base ⚙️, in C tutte le funzioni ricevono i parametri per **valore** 📋 (*ricevono una copia*). Se passi `a` e `b` a una funzione per scambiarle 🔁, la funzione scambierà solo le sue copie locali 📋📋, lasciando intatti gli originali 🧊.

Per modificare le variabili locali 📦 del `main` 🏠 dentro un'altra funzione 🧩, dobbiamo inviare i loro indirizzi di memoria 📍 (le bambole voodoo 🎎):

### Nel main: 🏠

```C
int a = 13;
int b = 37;

// 📍 Passiamo gli indirizzi (&a e &b) ai parametri-bambola voodoo di swap
swap(&a, &b);
```

### 🖨️ Output di Esercizio 02:

```
*** Before swapping ***
[61ff1c] a = 13
[61ff18] b = 37
*** After swapping ***
[61ff1c] a = 37
[61ff18] b = 13
```

📍 Gli indirizzi delle variabili `a` e `b` non sono mai cambiati, ma i valori 💎 contenuti al loro interno sono stati invertiti 🔁 a distanza 🔭 dalla funzione `swap()`.

## 🧱 4. [Esercizio 03](./main-es03_ArrayPointerSorting.c): Controllo Voodoo Multiplo sugli Array 🎎🎎🎎

In C, il nome stesso di un array 🧱 (es. `array`) equivale all'indirizzo 📍 del suo primo elemento (`&array[0]`) 1️⃣. Un array è una sequenza contigua 🚂 di celle di memoria 🧱🧱🧱.

Quando passiamo un array alla funzione di ordinamento `sort(array, 5)` 📊, la funzione non riceve una copia 📋❌ di tutti i 5 elementi, ma un puntatore 👉 al primo elemento 1️⃣.

Nel ciclo 🔁 dell'algoritmo della funzione `sort()`:

- 🔍 Vengono individuati gli indirizzi di due celle specifiche dell'array (`&a[i]` e `&a[j]`) 📍📍.
- 📤 Questi indirizzi vengono passati a `swap()`.
- 🎎🎎 `swap()` riceve le due bambole voodoo e scambia i valori 🔁 direttamente dentro la struttura dell'array originale 🧱.

### 🖨️ Output di Esercizio 03:

```
Before Sorting: 2, 37, 5, 13, 7.
After Sorting: 2, 5, 7, 13, 37.
```

## 📌 Riepilogo dei Punti Chiave 🗝️

| Concetto 💡 | Rappresentazione Voodoo 🎎 | Sintassi C 💻 |
| ---: | --- | --- |
| 📦 Variabile Normale | Il bersaglio 🎯 (contiene un valore 💎 fisicamente). | `int a = 10;` |
| 👉 Puntatore | La bambola Voodoo 🎎 (contiene l'indirizzo 📍 del bersaglio). | `int* p;` |
| 🗑️ Inizializzazione Mancante | Bambola voodoo non associata 🔓🎎: punta alla spazzatura 🗑️ in memoria 🧠. | `int* p;` (senza `= &a`) |
| 🔗 Operatore `&` | Creazione del legame voodoo 🔗 con la variabile 📦. | `p = &a;` |
| 🪡 Operatore `*` | L'atto di infilzare la bambola 🎎 per agire sul bersaglio 🎯 a distanza 🔭. | `*p = 20;` |

<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)
[![gmail](https://img.shields.io/badge/gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:birg81@gmail.com)