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
# 🧙‍♂️ Memory Voodoo: Pointers and Pass-by-Reference in C 🪆💾

## 📖 The Story in a Nutshell 🎬

The program asks for a number `n` 🔢, the **max capacity** 📦 of an array, and keeps asking 🔁 until it's a positive number ✅.
Then it builds the array 🧱, hands off ⚙️ the job of filling it up ✍️ to a function (which can stop early ⏹️ if the user wants 🙋), and finally prints 🖨️ only the part that was actually filled 🎯.

Here's the key thing 🔑: **the loading function has to give back two things** 2️⃣🎁 – the values in the array 📚 and *how many it really loaded* 🧮.
In C, a function can only `return` one value ☝️😬.
And that's where the doll comes in 🪆✨.

## 🏠 Variables, Addresses and Dolls 🪆📍

Every variable 📦 lives in a memory cell 🧠 with its own **address** 📬, just like a person 🧍 living at a certain house number 🏘️.
A regular variable holds the *data* 🧍 (the person), while a **pointer** 👉 holds an *address* 📍 (the voodoo doll 🪆).

The doll isn't the person 🙅, but it's connected to them 🔗: stick a pin 📌 in the doll 🪆 and the person feels it 😖.
In C 💻:

- 🪆 `&n` means "make me a doll of `n`": you get the address 📍 of the variable.
- 🏷️ `int* size` declares a doll-variable 🪆 that can stand for an `int`.
- 📌 `*size` is the pin: "go do something to the person 🧍 this doll is linked to 🔗".

So `*size = 0` doesn't touch the doll 🪆🚫 – it resets ⭕ the real variable 🧍 it points to 👉.

## 🔀 By Value or By Reference? 🤔

When you pass a variable **by value** 📄, the function gets a *photocopy* 🖨️.
It can scribble all over it ✏️ if it likes 🤪, and the original stays safe 🛡️.
That's what happens with `const int max_size` in `loadArrayWhileAZero`: it gets a copy 📄 of `n`, and the `const` 🔒 adds a promise 🤞: "I won't touch this one either".

When you pass **by reference** 🪆 (in C, that means passing a pointer 👉), you hand over the doll 🎁.
Now the function can mess with the original 🧍💥.
In `main` 🏁:

```c
loadArrayWhileAZero(array, n, &n);
```

where:
* `array` stands for 📍 the address of the first element, aka `&array[0]`
* `n` 📄 is a copy of `n` (max capacity)
* `&n` 🪆 is the doll of `n`

Notice 👀 that `n` travels **twice** ✌️, wearing two different hats 🎭:
as a **copy** 📄 (`max_size`, the limit 🚧 that must not change while the function is working 🛠️) and as a **doll** 🪆 (`size`, the counter 🧮 the function has to update 🔄).
The old value stays safe 🔐 in the photocopy 📄 while the real variable gets rewritten ✍️.

*What about the array*? 🤨
Passing `array` already means passing an address 📍 (the array *decays* 📉 into a pointer to its first element 1️⃣).
So `int a[]` is basically another doll 🪆: filling `a[i]` inside the function fills the real array 📚 from `main`, no copy involved 🚫📄.

## 🎁 Why Passing by Reference Is Like Returning Multiple Values 🔙➕

`loadArrayWhileAZero` is declared `void` 🕳️: it returns nothing with `return` 🤷.
And yet, when it's done 🏁, the caller 📞 has gotten **two results** 2️⃣🎉:

1. 📚 the filled array, through the doll `a` 🪆;
2. 🧮 the number of loaded elements, through the doll `size` 🪆, which is really `n`.

Every pointer you pass in is like a **mailbox** 📮 the function can fill up 📥 and the caller can empty afterwards 📤. `return` gives you just one parcel 📦☝️, while pointers let you drop off as many parcels as you want 📦📦📦.
That's why we talk about *output parameters* 🚪➡️: information doesn't just go in ⬅️, it comes out too ➡️.
It's the same trick 🎩 as `scanf("%d", &n)`: `scanf` also "returns" the number it read 🔢 through the doll 🪆 of `n`.

## 📏 Why the Actual Size Is Smaller Than the Max Size 📉🚌

The array is declared as `int array[n]` where `n` is the **max capacity** 🏟️ chosen at the start 🏁: it's like renting a bus 🚌 with 50 seats 💺.
But the loading function lets you stop early ✋, so the people who actually get on the bus 🚍 might be just 7 🧍‍♂️🧍‍♀️.

The job of `size` is to count the real passengers 🙋‍♂️🔢.
The `for` loop 🔁 uses it as a counter 🧮, starts it at 0 0️⃣ and bumps it up ➕ every time a value is typed in ⌨️.
At the end, `*size` holds the number of taken seats 💺✅, which is **less than or equal to** ⚖️ the capacity.

Since `size` is the doll 🪆 of `n`, when we get back 🔙 to `main` the variable `n` has changed meaning 🎭: **it's no longer the capacity, it's the number of valid elements** ✅.
That's why `printArray(array, n)` prints 🖨️ only the useful part 🎯 and skips the empty seats 💺🕳️, which are full of junk 🗑️.

Physically 🧱, the array stays at its max size 📦: it's `n` that tells us how far to look 👀. A neat ✨ but tricky ⚠️ solution, since we "recycled" ♻️ the name `n` for two different ideas 🔀 (see below 👇).

## 🐛 Two Programmer's Notes (a.k.a. Bugs) 🔧👨‍💻

As it stands, the code has a couple of problems 😅 that need fixing 🛠️.

**1️⃣ The loop condition reads before it writes** 🔍✍️.
In the `for`, the check `a[*size] != 0` runs ⏱️ *before* the user types the value ⌨️.
But `a[*size]` still holds garbage 🗑️ (the array isn't initialized 🚫), so the loop might stop right away 🛑 or act in unpredictable ways 🎲.

## 🎯 Wrapping Up 📝

- 🪆 A **pointer** is a voodoo doll: it holds the address 📍, not the data 🧍.
- ⚙️ `&` makes the doll 🪆, `*` sticks the pin 📌.
- 📄 **Pass by value** hands over a photocopy 🖨️, while **pass by reference** 🪆 hands over the doll 🎁.
- 🎁 With several dolls going in 🪆🪆, a `void` function can "return" several results 🎉.
- 🚌 The **actual size** is smaller than the max 📉 because the array is a bus booked in full 💺💺💺, while `size` only counts the passengers who really got on 🙋‍♂️.


---

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

---

![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>

<!-- Italiano -->
# 🧙‍♂️ Il vudù della memoria: puntatori e passaggio per riferimento in C 🪆💾

## 📖 La storia in breve 🎬

Il programma chiede un numero `n` 🔢, la **capienza massima** 📦 di un array, e la ripete 🔁 finché non è positivo ✅.
Poi crea l'array 🧱, delega ⚙️ a una funzione il compito di riempirlo ✍️ (interrompendosi in anticipo ⏹️ se l'utente lo desidera 🙋) e infine stampa 🖨️ solo la parte effettivamente riempita 🎯.

C'è un dettaglio chiave 🔑: **la funzione di caricamento deve restituire due cose** 2️⃣🎁, cioè i valori nell'array 📚 e *quanti ne ha caricati davvero* 🧮.
In C una funzione può fare `return` di un solo valore ☝️😬. Qui entra in scena la bambola 🪆✨.

## 🏠 Variabili, indirizzi e bambole 🪆📍

Ogni variabile 📦 vive in una cella di memoria 🧠 con un **indirizzo** 📬, come una persona 🧍 che abita a un certo civico 🏘️.
Una variabile normale contiene il *dato* 🧍 (la persona), mentre un **puntatore** 👉 contiene un *indirizzo* 📍 (la bambola vudù 🪆).

La bambola non è la persona 🙅, ma è legata a lei 🔗: se infili uno spillo 📌 nella bambola 🪆, la persona lo sente 😖.
In C 💻:

- 🪆 `&n` significa "fammi una bambola di `n`": ottieni l'indirizzo 📍 della variabile.
- 🏷️ `int* size` dichiara una variabile-bambola 🪆 che può rappresentare un `int`.
- 📌 `*size` è lo spillo: "agisci sulla persona 🧍 a cui questa bambola è legata 🔗".

Così `*size = 0` non modifica la bambola 🪆🚫, ma azzera ⭕ la variabile reale 🧍 a cui punta 👉.

## 🔀 Per valore o per riferimento? 🤔

Quando passi una variabile **per valore** 📄, la funzione riceve una *fotocopia* 🖨️.
Può scarabocchiarla ✏️ quanto vuole 🤪, l'originale resta intatto 🛡️.
È il caso di `const int max_size` in `loadArrayWhileAZero`: riceve una copia 📄 di `n`, e il `const` 🔒 aggiunge la promessa 🤞 "non la modificherò nemmeno lei".

Quando passi **per riferimento** 🪆 (in C, passando un puntatore 👉), consegni la bambola 🎁.
La funzione può agire sull'originale 🧍💥.
Nel `main` 🏁:

```c
loadArrayWhileAZero(array, n, &n);
```

dove:
* `array` rappresenta 📍 l'indirizzo del primo elemento ovvero `&array[0]`
* `n` 📄 copia di `n` (capienza massima)
* `&n` 🪆 bambola di `n`

Nota 👀 che `n` viaggia **due volte** ✌️, con due ruoli diversi 🎭:
come **copia** 📄 (`max_size`, il limite 🚧 che non deve cambiare mentre la funzione lavora 🛠️) e come **bambola** 🪆 (`size`, il contatore 🧮 che la funzione deve aggiornare 🔄).
Il vecchio valore resta al sicuro 🔐 nella fotocopia 📄 mentre la variabile reale viene riscritta ✍️.

*E l'array*? 🤨
Passare `array` equivale già a passare un indirizzo 📍 (in gergo, l'array *decade* 📉 in puntatore al primo elemento 1️⃣).
Quindi `int a[]` è di fatto un'altra bambola 🪆: riempire `a[i]` dentro la funzione riempie l'array vero 📚 del `main`, senza alcuna copia 🚫📄.

## 🎁 Perché passare per riferimento è "come ritornare più valori" 🔙➕

`loadArrayWhileAZero` è dichiarata `void` 🕳️: con il `return` non restituisce nulla 🤷.
Eppure, quando termina 🏁, il chiamante 📞 ha ricevuto **due risultati** 2️⃣🎉:

1. 📚 l'array riempito, tramite la bambola `a` 🪆;
2. 🧮 il numero di elementi caricati, tramite la bambola `size` 🪆, che coincide con `n`.

Ogni puntatore passato è una **cassetta della posta** 📮 che la funzione può riempire 📥 e il chiamante poi svuotare 📤. Il `return` ti dà un solo pacco 📦☝️, i puntatori ti permettono di lasciare tutti i pacchi che vuoi 📦📦📦.
Per questo si parla di *parametri di output* 🚪➡️: non entrano solo informazioni ⬅️, ne escono pure ➡️.
È lo stesso trucco 🎩 di `scanf("%d", &n)`: anche `scanf` "restituisce" il numero letto 🔢 passando per la bambola 🪆 di `n`.

## 📏 Perché la dimensione effettiva è minore di quella massima 📉🚌

L'array è dichiarato con `int array[n]` quando `n` è la **capienza massima** 🏟️ scelta all'inizio 🏁: è come affittare un autobus 🚌 da 50 posti 💺.
Ma la funzione di caricamento permette di fermarsi prima ✋, e chi sale davvero sull'autobus 🚍 potrebbero essere solo 7 persone 🧍‍♂️🧍‍♀️.

Il compito di `size` è proprio contare i passeggeri veri 🙋‍♂️🔢.
Il ciclo `for` 🔁 la usa come contatore 🧮, la parte da 0 0️⃣ e la incrementa ➕ a ogni valore inserito ⌨️.
Alla fine `*size` contiene il numero di posti occupati 💺✅, che è **minore o uguale** ⚖️ alla capienza.

Poiché `size` è la bambola 🪆 di `n`, al ritorno 🔙 nel `main` la variabile `n` ha cambiato significato 🎭: **non è più la capienza, ma il numero di elementi validi** ✅.
Ecco perché `printArray(array, n)` stampa 🖨️ solo la parte utile 🎯 e non i posti vuoti 💺🕳️, che contengono spazzatura 🗑️.

L'array fisicamente 🧱 resta di dimensione massima 📦: è `n` a dirci fin dove guardare 👀. Una soluzione elegante ✨ ma delicata ⚠️, perché abbiamo "riciclato" ♻️ il nome `n` per due concetti diversi 🔀 (vedi sotto 👇).

## 🐛 Due note da programmatore (i bug) 🔧👨‍💻

Il codice, così com'è, ha un paio di problemi 😅 da sistemare 🛠️.

**1️⃣ La condizione del ciclo legge prima di scrivere** 🔍✍️.
Nel `for`, il test `a[*size] != 0` viene valutato ⏱️ *prima* che l'utente inserisca il valore ⌨️.
Ma `a[*size]` contiene ancora spazzatura 🗑️ (l'array non è inizializzato 🚫), quindi il ciclo potrebbe fermarsi subito 🛑 o comportarsi in modo imprevedibile 🎲.

## 🎯 In sintesi 📝

- 🪆 Un **puntatore** è una bambola vudù: contiene l'indirizzo 📍, non il dato 🧍.
- ⚙️ `&` crea la bambola 🪆, `*` infilza lo spillo 📌.
- 📄 Il **passaggio per valore** consegna una fotocopia 🖨️, quello **per riferimento** 🪆 consegna la bambola 🎁.
- 🎁 Con più bambole in ingresso 🪆🪆, una funzione `void` può "restituire" più risultati 🎉.
- 🚌 La **dimensione effettiva** è minore della massima 📉 perché l'array è un autobus prenotato per intero 💺💺💺, mentre `size` conta solo i passeggeri saliti davvero 🙋‍♂️.


<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)
[![gmail](https://img.shields.io/badge/gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:birg81@gmail.com)
