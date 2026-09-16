# 💻☕ **Tutto quello che avreste voluto sapere sulla programmazione ma che non avete mai osato chiedere**

### *Guida semiseria all'arte di spiegare a una macchina esattamente cosa deve fare* 🧠⚙️💾

## 🚪 0. Prima di cominciare: una piccola confessione... 😏

Avete studiato **C++**. Avete visto variabili, condizioni, cicli, probabilmente array e magari siete arrivati persino agli **array bidimensionali**.

E adesso arriva il professore e dice:

> 🧑‍🏫 «Bene ragazzi, quest'anno facciamo C.»

E voi:

> 😐 «C++?»

> 🧑‍🏫 «No. C.»

> 😑 «Ma... non è una specie di C++ senza alcune cose?»

> 🧑‍🏫 «Esattamente.»

> 😭

Tranquilli. Non è davvero un **downgrade**. O, almeno, non soltanto. 😎

Il C è più piccolo, più essenziale e molto meno indulgente. Toglie parecchie comodità che avete imparato a dare per scontate e vi costringe a guardare un po' più da vicino **come ragiona il computer**.

E questa è una buona notizia. 💡

Perché programmare non significa conoscere a memoria cinquanta comandi.

Significa soprattutto saper rispondere a una domanda:

> 🧠 **«Come faccio a trasformare un problema in una sequenza precisa di operazioni che una macchina possa eseguire?»**

Da questa domanda parte tutto.

Algoritmi.
Diagrammi di flusso.
Variabili.
Condizioni.
Cicli.
Numeri.
Memoria.
Codice.

E, alla fine, anche quella misteriosa creatura chiamata **programmatore**. 👨‍💻👩‍💻

---

# 🧠 1. Che cos'è un algoritmo?

Cominciamo dalla parola che probabilmente avete già sentito mille volte.

### 📌 Un algoritmo è una sequenza finita e ordinata di istruzioni che permette di risolvere un problema o ottenere un determinato risultato.

Detta così sembra una cosa molto informatica.

In realtà gli algoritmi ci circondano.

📱 Per sbloccare lo smartphone:

1. accendi lo schermo;
2. riconosci il volto oppure inserisci il PIN;
3. il sistema verifica il dato;
4. se è corretto, sblocca il dispositivo;
5. altrimenti nega l'accesso.

🍝 Per preparare la pasta:

1. riempi la pentola;
2. aggiungi l'acqua;
3. accendi il fornello;
4. aspetta l'ebollizione;
5. aggiungi il sale;
6. metti la pasta;
7. aspetta il tempo necessario;
8. scola.

E qui arriva il primo grande concetto:

> 💡 **Un algoritmo non è necessariamente un programma.**

Un programma è un algoritmo **espresso attraverso un linguaggio che il computer può interpretare/eseguire**, insieme alle strutture necessarie per realizzarlo.

---

# ☕ 2. L'algoritmo definitivo: fare il caffè con la moka

Immaginiamo di voler insegnare a un robot a preparare il caffè.

Il robot è molto intelligente.

Ma non sa assolutamente nulla.

Gli diciamo:

> «Preparami un caffè.»

E lui probabilmente ci guarderà con l'equivalente digitale di uno sguardo perso nel vuoto. 🤖

Dobbiamo quindi essere più precisi.

### ☕ Algoritmo per preparare un caffè con la moka

**Input:** acqua, caffè macinato, moka, fornello.

**Procedimento:**

1. 🔧 Smontare la moka.
2. 💧 Riempire la caldaia con acqua.
3. 🥄 Inserire il filtro.
4. ☕ Riempire il filtro con il caffè.
5. 🔩 Avvitare la parte superiore.
6. 🔥 Posizionare la moka sul fornello.
7. ⏳ Attendere che il caffè salga.
8. 🔥 Spegnere il fornello.
9. ☕ Versare il caffè nella tazzina.
10. 😌 Bere.

Sembra banale.

Ma abbiamo appena scritto un **algoritmo**.

E soprattutto abbiamo scoperto una cosa fondamentale:

> 🧠 **Un algoritmo deve essere sufficientemente preciso da eliminare l'ambiguità.**

«Metti un po' d'acqua» non è una grande istruzione.

«Riempi la caldaia fino a poco sotto la valvola» è decisamente più utile.

Il computer, infatti, ha una caratteristica molto particolare:

> 🤖 **Non comprende le nostre intenzioni.**

E questa è una delle prime grandi differenze fra programmare un computer e parlare con una persona.

Se dite a un essere umano:

> «Portami il libro.»

potrebbe capire quale libro intendete dal contesto.

Se lo dite a un computer:

> `portami_libro();`

prima dovete avergli spiegato **che cosa significa** `portami_libro()`.

Il computer non è stupido.

È semplicemente **terribilmente letterale**. 😈

---

# 🧮 3. Problema → algoritmo → programma

Possiamo quindi costruire una catena molto importante:

```text
       PROBLEMA
          ↓
       SOLUZIONE
          ↓
       ALGORITMO
          ↓
    RAPPRESENTAZIONE
          ↓
      PROGRAMMA
          ↓
      ESECUZIONE
          ↓
       RISULTATO
```

Oppure, in versione ancora più compatta:

> 🧠 **Pensare → progettare → descrivere → programmare → eseguire**

Il linguaggio C non è quindi il punto di partenza.

È **l'ultimo tratto del viaggio**.

---

# 🧠 4. E qui arriva Church-Turing...

Adesso possiamo permetterci una piccola incursione nella teoria dell'informatica. 🎩

Una formulazione divulgativa che possiamo usare è:

> 💡 **Se una funzione è effettivamente calcolabile, allora esiste un procedimento algoritmico capace di calcolarla.**

Attenzione però.

Non significa:

> ❌ «Se un problema esiste, allora sicuramente esiste un algoritmo che lo risolve.»

Magari!

Esistono problemi per i quali **non esiste alcun algoritmo generale risolutivo**.

La cosiddetta **tesi di Church-Turing**, sviluppata indipendentemente da Alonzo Church e Alan Turing negli anni '30, riguarda proprio il concetto di **calcolabilità effettiva**: in termini divulgativi, ciò che può essere calcolato mediante un procedimento effettivo può essere rappresentato da una macchina di Turing. ([Enciclopedia di Filosofia di Stanford][1])

Quindi la nostra frase iniziale va leggermente aggiustata:

> 🧠 **Se un problema è effettivamente calcolabile, possiamo descriverne la soluzione attraverso un algoritmo.**

Ed è già una frase abbastanza potente da far venire voglia di aprire una parentesi filosofica.

Ma non lo faremo.

Per ora. 😏

---

# 🔀 5. Il diagramma di flusso: disegnare il pensiero

Un algoritmo può essere scritto in linguaggio naturale.

Può essere espresso attraverso pseudocodice.

Oppure possiamo **disegnarlo**.

Ed eccoci al **flowchart**, cioè il **diagramma di flusso**. 🔀

Un diagramma di flusso rappresenta graficamente:

* 🔢 le operazioni da eseguire;
* 🔀 le decisioni;
* ⌨️ l'input;
* 🖥️ l'output;
* 🔄 il flusso di esecuzione;
* 🔚 l'inizio e la fine dell'algoritmo.

L'idea è meravigliosamente semplice:

> 👁️ **Prima ancora di scrivere il codice, possiamo guardare l'algoritmo.**

Ed è molto utile perché un errore nel diagramma è generalmente più facile da individuare di un errore nascosto in cinquanta righe di codice.

---

# 🧩 6. Anatomia di un flowchart

Nel diagramma che avete davanti, quello dell'**anno bisestile**, possiamo riconoscere diversi simboli. 🔍

![Image](https://images.openai.com/static-rsc-4/kSwofiXrCCcsDZMWIQgSMzYqhp3infWsrYUY49dxUHlTNGtizU8hNcacuOzUzJTL6KSvkdE6aGHEqGQdnhFbEYftD2GHwCy72WEP4Rlli5UsFKosJDMqCmqgQCbGmcn38P02Wr_ACM0RSmj8zrn0BRIYu0jdcVXs5gjIlRG-TfaauMmTJM3ROueWpEthqbiP?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/h5kA9kmDxwfJuB44XswA1K4zGMrUdqH8YbevceMxTdVtS1DVuh1KKhIZEcl06cSTT41yn5UoQu9ha9E-_9-WQL8HYkZUG3MVeQMjMre6QJbSBK3EEiME80lRuT90EE43nwyOLsbLo4zNCjk7vZRHT9H1EYSnXlEJ0C_iWs94l04vxy-ZFnlsdICooPqWM9cS?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/H6DvafL0wG9SJy9G9-_5yLZFV7DaknEq49XCzPEhbuLQS3-_7JQMhmGCVBNo-VcP9KgV3C7OiCfV5tyH2T-gLX49lq2_KEHPUmr5zDqm76ptB6Ho4rX36BxLXgLSI7i9zU69IU7CblBURsQQGqhPuqzsJQROdflPPTVXI4GCTqyHTqFRQUQMSRhlPZynFguq?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/Y_1qTBHzhjw35LWbBgQs1ZooJQcO63_LyLJfwHYMcgHwhsNBFQIe_fb0dFPGwDW2Q57UMesK0gSaoqfEpSxNFFQhvRgLcGiskQ3c9dIorV-ihsNhH3uJre3SFAgcD0OzOu39c-cpKvs63hF-BaijkPLk8C05-aZO7xKnWeFaEZwaxLLk4_MLxogEy_1rcdjg?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/VMbAu7ISk2tTU12xmTyWNaTqJi2ZeAlK0ya3jst5zPluLr_PghQJq_5PdhLV7UGZt9XR-kXBrMIUAoEMPGUogqkmQY0hS7TuOZnZwyO0AsBvRilMaLOQsapWaZOu0P5zxtEj74Z2ReBQ8jw6eIkWLtv6VHR8okp9jUDHUCbUfgx1lIdZZC482KxFE8xu0H9x?purpose=fullsize)

### 🟢 Il terminatore

Ha normalmente forma ovale.

```text
   ╭──────────╮
   │  INIZIO  │
   ╰──────────╯
```

Indica:

* ▶️ l'inizio dell'algoritmo;
* 🛑 la fine dell'algoritmo.

Nel nostro diagramma troviamo:

**Inizio** → **Fine**

---

### ▭ Il processo

È normalmente un rettangolo.

```text
┌────────────────────┐
│ resto = anno % 4   │
└────────────────────┘
```

Rappresenta un'operazione.

Per esempio:

```c
resto = anno % 4;
```

Quindi:

> 🧠 **Rettangolo = fai qualcosa.**

---

### 🔶 La decisione

È il famoso rombo.

```text
       ◇
    condizione?
```

Serve per porre una domanda.

Nel nostro caso:

```text
resto == 0 ?
```

Da qui partono due strade:

```text
             resto == 0 ?
              /        \
           VERO        FALSO
```

> 🔀 **Rombo = scegli quale strada prendere.**

Ed è esattamente ciò che nel C faremo con:

```c
if (condizione) {
    ...
} else {
    ...
}
```

---

### ▱ Input / Output

Il parallelogramma rappresenta generalmente un'operazione di ingresso o uscita.

Nel nostro esempio:

```text
Scrivi "Che anno si vuole controllare?"
```

e:

```text
Leggi anno
```

corrispondono rispettivamente a output e input.

In C:

```c
printf(...);
```

serve principalmente per l'output.

```c
scanf(...);
```

serve per acquisire dati dall'input standard.

---

### ⚪ Il connettore

Il piccolo cerchio che vediamo in fondo al diagramma serve a **ricongiungere due percorsi**.

Abbiamo:

```text
             decisione
             /       \
          vero       falso
            \         /
             \       /
             ○
             |
            Fine
```

Non è un'operazione.

È semplicemente un modo per rendere il diagramma più leggibile.

---

### ➡️ Le frecce

Le frecce sono il **flusso di esecuzione**.

Ci dicono:

> «Dopo questa operazione, vai lì.»

In pratica sono la strada che attraversa il nostro algoritmo.

---

# 📅 7. Il nostro primo algoritmo: l'anno bisestile

Nel diagramma fornito abbiamo questa idea:

```text
leggi anno
   ↓
calcola resto = anno % 4
   ↓
resto == 0 ?
  ↙       ↘
SI         NO
↓           ↓
bisestile   calcola anno precedente
            divisibile per 4
```

È interessante perché in poche figure abbiamo già incontrato:

* variabili;
* input;
* output;
* operazioni aritmetiche;
* operatore `%`;
* confronto;
* selezione;
* due percorsi alternativi.

Praticamente metà della cassetta degli attrezzi di un programmatore. 🧰

---

# ➗ 8. L'operatore `%`: il resto che nessuno considera mai abbastanza

Questo è uno dei piccoli operatori più importanti della programmazione.

```c
%
```

Si chiama **operatore modulo** o, più semplicemente, operatore **resto della divisione intera**.

Esempio:

```text
17 / 5 = 3
resto = 2
```

quindi:

```c
17 % 5
```

restituisce:

```text
2
```

### 🚨 Attenzione

Stiamo parlando di **divisione intera**.

L'operatore `%` in C si applica agli **operandi di tipo intero**.

Quindi:

```c
17 % 5
```

ha perfettamente senso.

Ma non dobbiamo pensare a `%` come a "una percentuale".

Non è:

```text
17% di 5
```

È:

> 🧮 **il resto della divisione intera.**

---

## 🔥 Una proprietà importantissima

Se:

```text
m % n
```

con `m` e `n` interi e `n > 0`, il risultato può assumere soltanto valori compresi tra:

```text
0 e n - 1
```

cioè:

$$
0 \leq m \% n < n
$$

Per esempio:

```text
x % 2 → 0 oppure 1
x % 3 → 0, 1 oppure 2
x % 10 → 0 ... 9
x % 100 → 0 ... 99
```

Ed ecco perché `%` è una specie di coltellino svizzero della programmazione. 🔪

Lo possiamo usare per:

* verificare se un numero è pari;
* verificare se un numero è divisibile;
* estrarre le cifre di un numero;
* lavorare con cicli periodici;
* gestire ore, minuti e secondi;
* lavorare con sistemi numerici;
* determinare posizioni cicliche.

Per esempio:

```c
if (numero % 2 == 0) {
    printf("Numero pari\n");
}
```

Traduzione:

> «Se il resto della divisione per 2 è zero, allora il numero è pari.»

Elegantissimo.

E soprattutto: **niente magia**. Solo matematica. 🧙‍♂️➗

---

# 🇨 9. Dal diagramma al C

Una volta costruito l'algoritmo, possiamo tradurlo in un linguaggio di programmazione.

Nel nostro caso:

```c
#include <stdio.h>

int main() {
    int anno, annoBisestile, resto;

    printf("Che anno si vuole controllare? ");
    scanf("%d", &anno);

    resto = anno % 4;

    if (resto == 0) {
        printf("L'anno è bisestile!\n");
    } else {
        annoBisestile = anno - resto;
        printf("L'anno %d non è bisestile, ma lo era %d\n",
               anno, annoBisestile);
    }

    return 0;
}
```

Non ci interessa imparare questo programma a memoria.

Ci interessa riconoscere la corrispondenza:

| Algoritmo            | C                          |
| -------------------- | -------------------------- |
| Leggi un valore      | `scanf()`                  |
| Scrivi qualcosa      | `printf()`                 |
| Memorizza un dato    | variabile                  |
| Calcola              | espressione                |
| Prendi una decisione | `if / else`                |
| Ripeti               | `for`, `while`, `do while` |
| Fine del programma   | `return 0`                 |

Il linguaggio cambia.

La **logica** no.

Ed è proprio questa la cosa importante che dovete portarvi dietro dal C++.

---

# 🧰 10. Perché `#include <stdio.h>`?

Questa riga:

```c
#include <stdio.h>
```

potrebbe sembrare un rito voodoo richiesto dal compilatore.

Non lo è. 🧙‍♂️

`stdio.h` significa:

> **Standard Input/Output**

È un **header**, cioè un file che contiene dichiarazioni necessarie per utilizzare determinate funzionalità della libreria standard.

Dentro questo mondo troviamo, tra le altre:

```c
printf()
scanf()
```

Il preprocessore, incontrando:

```c
#include <stdio.h>
```

inserisce logicamente le dichiarazioni contenute nell'header nel punto indicato, prima della compilazione vera e propria.

### 🆚 E nel C++?

Nel C++ potreste aver utilizzato:

```cpp
#include <iostream>
```

e poi:

```cpp
std::cout
std::cin
```

C e C++ condividono una parte della storia e molte librerie derivano dalla tradizione del C, ma **non sono lo stesso linguaggio**.

Nel C tradizionale l'input/output testuale di base ruota intorno alle funzioni della famiglia `stdio`.

Nel C++ troviamo invece anche il sistema a stream:

```cpp
std::cout
std::cin
```

Quindi:

```text
C       → stdio.h → printf / scanf
C++     → iostream → cout / cin
```

Non significa che il C++ "non abbia `printf`".

Può usarlo.

Significa semplicemente che **C++ offre un altro modello di I/O, quello degli stream**, mentre qui stiamo lavorando nel territorio del C.

---

# 📦 11. Variabili e tipi: il computer vuole sapere cosa stai conservando

Quando scriviamo:

```c
int anno;
```

stiamo dicendo:

> 🧠 «Riserva una variabile chiamata `anno` destinata a contenere un intero.»

Il tipo dice **che genere di dato** vogliamo rappresentare.

I principali tipi fondamentali del C sono:

| Tipo          | Significato                | Esempio                      |
| ------------- | -------------------------- | ---------------------------- |
| `char`        | carattere / piccolo intero | `'A'`                        |
| `_Bool`       | valore booleano            | `0`, `1`                     |
| `short`       | intero corto               | `1200`                       |
| `int`         | intero                     | `2026`                       |
| `long`        | intero lungo               | `1000000L`                   |
| `long long`   | intero molto lungo         | `9000000000LL`               |
| `float`       | reale a precisione singola | `3.14f`                      |
| `double`      | reale a precisione doppia  | `3.141592`                   |
| `long double` | reale a precisione estesa  | dipende dall'implementazione |
| `void`        | assenza di tipo/valore     | `void funzione()`            |

Esistono poi tipi derivati e compositi, puntatori, array, strutture, union, enumerazioni e, nelle versioni moderne del linguaggio, altri strumenti.

Ma per ora teniamo la cassetta degli attrezzi chiusa. 🧰

---

# 🔢 12. Ma quanti numeri può contenere un `int`?

Qui arriva una delle cose che spesso si imparano male.

Non bisogna dire:

> ❌ «Un `int` è sempre 32 bit.»

Il C **non lo garantisce**.

Lo standard stabilisce requisiti minimi e lascia diverse caratteristiche dipendenti dalla piattaforma. Per esempio `int` deve avere almeno 16 bit, mentre sulle macchine moderne è molto comune trovarlo a 32 bit. ([Cppreference][2])

### 📊 Minimi garantiti dal C e valori tipici

| Tipo                 | Ampiezza minima |                          Range signed tipico |
| -------------------- | --------------: | -------------------------------------------: |
| `char`               |           8 bit |            dipende da `signed/unsigned char` |
| `signed char`        |           8 bit |                                 −128 ... 127 |
| `unsigned char`      |           8 bit |                                    0 ... 255 |
| `short`              |          16 bit |                           −32.768 ... 32.767 |
| `unsigned short`     |          16 bit |                                 0 ... 65.535 |
| `int`                |          16 bit | tipicamente −2.147.483.648 ... 2.147.483.647 |
| `unsigned int`       |          16 bit |              tipicamente 0 ... 4.294.967.295 |
| `long`               |          32 bit |                    dipende dalla piattaforma |
| `unsigned long`      |          32 bit |                    dipende dalla piattaforma |
| `long long`          |          64 bit |          circa −9,22 × 10¹⁸ ... +9,22 × 10¹⁸ |
| `unsigned long long` |          64 bit |                      0 ... circa 1,84 × 10¹⁹ |

⚠️ **Attenzione:** la tabella distingue tra **minimi garantiti dallo standard** e **dimensioni comunemente utilizzate**. Per sapere i valori reali sulla macchina sulla quale state compilando, esistono le macro di `<limits.h>` come:

```c
INT_MIN
INT_MAX
UINT_MAX
LONG_MIN
LONG_MAX
```

Il C mette quindi a disposizione gli strumenti per **chiedere al sistema stesso quali siano i suoi limiti**. ([Cppreference][3])

---

# 🔢 13. E adesso: perché esistono tante basi numeriche?

Qui arriviamo al punto dolente. 😈

Noi esseri umani siamo affezionati alla base 10.

Probabilmente perché abbiamo dieci dita.

Il computer, invece, è cresciuto in un ambiente nel quale:

```text
ON / OFF
1 / 0
vero / falso
```

sono concetti estremamente comodi.

Ed ecco la **base 2**.

### 🧮 Base 10

Usa:

```text
0 1 2 3 4 5 6 7 8 9
```

### 💻 Base 2

Usa soltanto:

```text
0 1
```

### 🐙 Base 8

Usa:

```text
0 1 2 3 4 5 6 7
```

### 👻 Base 16

Usa:

```text
0 1 2 3 4 5 6 7 8 9 A B C D E F
```

Quindi:

```text
A = 10
B = 11
C = 12
D = 13
E = 14
F = 15
```

---

# 💡 14. La stessa informazione può avere facce diverse

Prendiamo:

```text
42
```

In base 10:

```text
42
```

In binario:

```text
101010
```

In ottale:

```text
52
```

In esadecimale:

```text
2A
```

Sono **quattro rappresentazioni dello stesso valore**.

Non sono quattro numeri diversi.

È come scrivere:

> quarantadue
> 42
> XLII

Il valore è lo stesso.

Cambia il sistema utilizzato per rappresentarlo.

---

# 🧠 15. Un trucco fondamentale: le potenze della base

In base 10:

```text
583
```

significa:

```text
5 × 10²
+ 8 × 10¹
+ 3 × 10⁰
```

cioè:

```text
500 + 80 + 3
```

In binario:

```text
101010
```

significa:

```text
1×2⁵ + 0×2⁴ + 1×2³ + 0×2² + 1×2¹ + 0×2⁰
```

quindi:

```text
32 + 8 + 2 = 42
```

🎯 **La base cambia, la matematica sottostante no.**

---

# 🔬 16. Il secondo programma: quattro modi per guardare lo stesso numero

Adesso possiamo capire questo:

```c
#include <stdio.h>

int main() {
    for (int i = 0; i < 32; i++) {
        printf("%d \t %05b \t %o \t %x \t %c \n",
               i, i, i, i, i + 64);
    }

    return 0;
}
```

Il ciclo:

```c
for (int i = 0; i < 32; i++)
```

fa assumere a `i` i valori:

```text
0, 1, 2, 3, ... 31
```

Poi `printf` visualizza quel valore in diverse forme.

| Formato | Rappresentazione                        |
| ------- | --------------------------------------- |
| `%d`    | decimale                                |
| `%05b`  | binario con larghezza 5 e zeri iniziali |
| `%o`    | ottale                                  |
| `%x`    | esadecimale minuscolo                   |
| `%c`    | carattere                               |

Quindi potremmo ottenere qualcosa del genere:

```text
decimale   binario   ottale   hex   carattere
------------------------------------------------
0          00000     0        0     @
1          00001     1        1     A
2          00010     2        2     B
3          00011     3        3     C
...
25         11001     31       19    Y
26         11010     32       1a    Z
```

Ed ecco il punto interessante.

---

# 🔤 17. Perché `i + 64`?

Per capire questo pezzo:

```c
%c
```

dobbiamo parlare di **ASCII**.

ASCII associa valori numerici a caratteri.

Per esempio:

```text
65 → A
66 → B
67 → C
...
90 → Z
```

Quindi:

```c
i + 64
```

produce:

```text
i = 1 → 65 → A
i = 2 → 66 → B
...
i = 26 → 90 → Z
```

Ma il programma parte da:

```text
i = 0
```

quindi:

```text
0 + 64 = 64 = @
```

E continua fino a:

```text
31 + 64 = 95 = _
```

Il programma attraversa quindi:

```text
@ A B C D ... Z [ \ ] ^ _
```

🎯 È un modo simpatico per vedere che **un carattere, a basso livello, può essere associato a un valore numerico**.

---

# 🔔 18. ASCII, caratteri di controllo e quella strana `\a`

La tabella ASCII originale comprende 128 codici.

I codici:

```text
0 ... 31
```

sono riservati ai **caratteri di controllo** e non rappresentano normalmente simboli stampabili. Unicode conserva questi codici nella propria area dei controlli C0. ([Unicode][4])

Alcuni sono diventati famosissimi:

| Escape C | Codice ASCII | Significato     |
| -------- | -----------: | --------------- |
| `\0`     |            0 | NUL             |
| `\a`     |            7 | Bell            |
| `\b`     |            8 | Backspace       |
| `\t`     |            9 | Tab             |
| `\n`     |           10 | Line Feed       |
| `\v`     |           11 | Vertical Tab    |
| `\f`     |           12 | Form Feed       |
| `\r`     |           13 | Carriage Return |

---

## ↔️ `\r` e `\n`

Questi due meritano attenzione.

### `\n`

```c
printf("Ciao\n");
```

indica un **nuovo avanzamento di riga**.

### `\r`

```text
Carriage Return
```

Storicamente significa riportare il cursore all'inizio della riga.

Ed è uno dei motivi per cui sistemi diversi hanno avuto storicamente differenti rappresentazioni della fine riga.

Su molti sistemi moderni:

```text
Linux / Unix → \n
Windows      → \r\n
```

Il runtime e le modalità di apertura dei file possono però gestire queste differenze.

---

## ↹ `\t`

Il tab:

```c
printf("Nome\tEtà\n");
```

produce una tabulazione.

È utilissimo per creare piccole tabelle testuali.

---

## 🔔 Bonus Track: `\a`

Questa è divertente.

Provate:

```c
printf("\a");
```

`\a` significa **bell**.

Su alcuni terminali produrrà effettivamente un suono.

Su altri potrebbe non accadere assolutamente nulla.

Quindi:

> 🔊 **Provate. Non fidatevi del professore. Fidatevi delle vostre casse.**

Se sentite un *bip*, congratulazioni: avete appena programmato il computer per infastidire qualcuno. 😈🔔

---

# 🌍 19. Ma allora UTF-8 cos'è?

A questo punto qualcuno potrebbe chiedere:

> «Prof, ma allora ASCII basta per scrivere `è`, `€`, `你`, `😀`?»

No.

ASCII è molto limitato.

Ed entra in scena **Unicode**.

Unicode assegna un **code point** ai caratteri del sistema universale di codifica.

UTF-8 è una delle modalità utilizzate per rappresentare questi code point come sequenze di byte.

La cosa bella è che UTF-8 mantiene una compatibilità fondamentale con ASCII:

> 💡 I caratteri ASCII da `U+0000` a `U+007F` hanno in UTF-8 la stessa rappresentazione a un byte.

Per i caratteri oltre ASCII possono servire più byte.

Quindi:

```text
A
```

occupa:

```text
1 byte
```

mentre un carattere non ASCII può richiederne diversi.

Ed è proprio qui che nasce una delle differenze concettuali più importanti:

> ⚠️ **un carattere non è necessariamente un byte.**

Il C moderno possiede anche strumenti specifici per caratteri e stringhe in codifiche diverse, ma per ora ci basta aver aperto la porta. Unicode definisce esplicitamente il blocco ASCII e i controlli C0 nell'intervallo `U+0000`...`U+001F`. ([Unicode][4])

---

# 🖨️ 20. `printf`: parlare al monitor

La funzione:

```c
printf()
```

serve principalmente a produrre output formattato sullo **standard output**.

Per esempio:

```c
printf("Ciao!");
```

oppure:

```c
int eta = 17;

printf("Ho %d anni", eta);
```

Il simbolo:

```text
%d
```

non viene stampato.

Dice a `printf`:

> «Qui devi inserire un intero decimale.»

---

# ⌨️ 21. `scanf`: parlare al contrario

Con:

```c
scanf()
```

facciamo il percorso inverso.

```c
int anno;

scanf("%d", &anno);
```

Significa, semplificando:

> «Leggi un intero e memorizzalo nella variabile `anno`.»

E qui compare:

```c
&anno
```

Quella `&` non è decorativa.

Indica l'**indirizzo** della variabile.

`scanf` deve infatti sapere **dove depositare il dato letto**.

---

# 🚨 Occhio al tranello: `scanf` vuole un indirizzo!

Questo:

```c
int x;

scanf("%d", &x);
```

è corretto.

Questo:

```c
scanf("%d", x);
```

non lo è per una normale variabile `int`.

Per ora ricordate:

> 🧠 `printf` riceve normalmente **il valore**.

> 🧠 `scanf` riceve normalmente **l'indirizzo della variabile** in cui deve scrivere.

Ed eccoci già con un piede nel mondo dei **puntatori**. 👀

---

# 📋 22. La grande tabella dei format specifier di `printf`

Eccoci alla parte che può salvare parecchi pomeriggi. 😎

La sintassi generale di una conversione di `printf` può essere molto più ricca del semplice:

```text
%d
```

Per esempio:

```text
%04X
```

può essere letto concettualmente come:

```text
%   0   4   X
│   │   │   └── esadecimale maiuscolo
│   │   └────── larghezza minima 4
│   └────────── riempi con zeri
└────────────── inizia conversione
```

### 🧾 Conversioni principali

| Specificatore | Significato                          |
| ------------- | ------------------------------------ |
| `%d`          | intero signed decimale               |
| `%i`          | intero signed decimale               |
| `%u`          | intero unsigned                      |
| `%o`          | intero unsigned ottale               |
| `%x`          | esadecimale minuscolo                |
| `%X`          | esadecimale maiuscolo                |
| `%f`          | numero floating point                |
| `%e`          | notazione scientifica                |
| `%E`          | notazione scientifica con `E`        |
| `%g`          | formato compatto tra `f` ed `e`      |
| `%G`          | come `%g`, con `E`                   |
| `%a`          | floating point in esadecimale        |
| `%A`          | floating point esadecimale maiuscolo |
| `%c`          | carattere                            |
| `%s`          | stringa                              |
| `%p`          | indirizzo/puntatore                  |
| `%%`          | carattere `%`                        |

`printf` dispone inoltre di modificatori di lunghezza e di formattazione. ([Cppreference][5])

---

# 🧬 23. I modificatori: quando `%d` comincia a prendere steroidi

Possiamo aggiungere informazioni prima del carattere finale.

Per esempio:

```c
printf("%04X", 42);
```

produce:

```text
002A
```

Perché:

* `X` → esadecimale maiuscolo;
* `4` → larghezza minima 4;
* `0` → riempi con zeri.

---

## 🧰 I modificatori più utili

| Forma   | Significato                                   |
| ------- | --------------------------------------------- |
| `%5d`   | larghezza minima 5                            |
| `%-5d`  | allinea a sinistra                            |
| `%05d`  | riempi con zeri                               |
| `%+d`   | mostra il segno anche per valori positivi     |
| `% d`   | spazio davanti ai positivi                    |
| `%#x`   | prefisso esadecimale                          |
| `%#o`   | prefisso ottale                               |
| `%.2f`  | 2 cifre dopo il punto                         |
| `%8.2f` | larghezza 8, precisione 2                     |
| `%08X`  | larghezza 8, zeri, esadecimale maiuscolo      |
| `%-10s` | stringa larga almeno 10, allineata a sinistra |

Per esempio:

```c
printf("%08X\n", 42);
```

produce:

```text
0000002A
```

Mentre:

```c
printf("%-10s\n", "C");
```

riserva almeno 10 posizioni e allinea il testo a sinistra.

La larghezza è normalmente una **larghezza minima**, non un limite massimo: se il valore richiede più spazio, viene comunque stampato. ([Cppreference][6])

---

# 🧙 24. La forma esoterica: `%*.*f`

Qui iniziamo a vedere perché `printf` può sembrare una formula magica.

```c
printf("%*.*f", larghezza, precisione, valore);
```

Per esempio:

```c
printf("%*.*f", 10, 3, 3.1415926);
```

può produrre:

```text
     3.142
```

La larghezza e la precisione vengono fornite come argomenti.

Quindi:

```text
%*.*f
 │ │ └── floating point
 │ └──── precisione dinamica
 └────── larghezza dinamica
```

La documentazione di `printf` prevede esplicitamente l'uso di `*` per specificare dinamicamente larghezza e precisione. ([Cppreference][6])

---

# 📥 25. `scanf`: qui le cose diventano ancora più interessanti

La famiglia `scanf` usa conversioni simili, ma **non identiche**.

La ragione è importante:

`printf` deve **trasformare un valore in testo**.

`scanf` deve **leggere testo e trasformarlo in un valore**, depositandolo nella memoria indicata.

### 📋 Tabella essenziale di `scanf`

| Specificatore | Destinazione                   |
| ------------- | ------------------------------ |
| `%d`          | `int *`                        |
| `%i`          | `int *`, base interpretata     |
| `%u`          | `unsigned int *`               |
| `%hd`         | `short *`                      |
| `%hu`         | `unsigned short *`             |
| `%ld`         | `long *`                       |
| `%lu`         | `unsigned long *`              |
| `%lld`        | `long long *`                  |
| `%llu`        | `unsigned long long *`         |
| `%f`          | `float *`                      |
| `%lf`         | `double *`                     |
| `%Lf`         | `long double *`                |
| `%c`          | `char *`                       |
| `%s`          | `char *`                       |
| `%x` / `%X`   | intero unsigned in esadecimale |
| `%o`          | intero unsigned in ottale      |
| `%p`          | puntatore, tramite `void **`   |
| `%%`          | cerca letteralmente `%`        |

La differenza tra `%f` e `%lf` in `scanf` è una delle più importanti da ricordare: `%f` richiede un `float *`, mentre `%lf` richiede un `double *`. ([Cppreference][7])

---

# ⚠️ 26. Il grande tranello: `float`, `double`, `printf`, `scanf`

Ecco una tabella da mettere mentalmente sul frigorifero.

| Tipo          | `printf` | `scanf` |
| ------------- | -------- | ------- |
| `float`       | `%f`     | `%f`    |
| `double`      | `%f`     | `%lf`   |
| `long double` | `%Lf`    | `%Lf`   |

Per esempio:

```c
float temperatura;
double altezza;

scanf("%f", &temperatura);
scanf("%lf", &altezza);
```

Perché questa differenza?

Perché gli argomenti variadici passati a `printf` subiscono le **default argument promotions**: un `float` viene promosso a `double`.

Quindi `printf` riceve normalmente un `double` quando gli passiamo un `float`.

Con `scanf`, invece, stiamo indicando **il tipo dell'oggetto in memoria nel quale scrivere**.

E quindi:

```c
float  → %f
double → %lf
```

in `scanf`.

🎯 È uno di quei casi in cui il C vi guarda negli occhi e dice:

> «Non ho intenzione di renderti la vita facile.»

---

# 🧭 27. E `%p`? Possiamo stampare gli indirizzi?

Sì.

Ed è qui che compare uno dei pezzi più interessanti della programmazione a basso livello.

```c
int x = 42;

printf("%p", (void*)&x);
```

`&x` significa:

> «dammi l'indirizzo di memoria di `x`».

`%p` serve a rappresentare un **puntatore/indirizzo**.

Il formato esatto visualizzato dipende dall'implementazione.

Per esempio potremmo vedere qualcosa come:

```text
0x7ffdb83a12c4
```

Non dovete preoccuparvi di leggere quell'indirizzo come un normale numero.

È un riferimento a **una posizione nella memoria del processo**.

Ed è proprio qui che il C comincia a farci vedere ciò che altri linguaggi spesso nascondono. 🧠🔬

---

# 📊 28. La tabella riassuntiva definitiva

### 🖨️ `printf`

| Formato | Cosa visualizza               | Esempio        |
| ------- | ----------------------------- | -------------- |
| `%d`    | intero signed                 | `42`           |
| `%i`    | intero signed                 | `42`           |
| `%u`    | unsigned                      | `42`           |
| `%o`    | ottale                        | `52`           |
| `%x`    | esadecimale                   | `2a`           |
| `%X`    | esadecimale                   | `2A`           |
| `%f`    | floating point                | `3.140000`     |
| `%.2f`  | floating point con 2 decimali | `3.14`         |
| `%e`    | scientifica                   | `3.14e+00`     |
| `%g`    | compatta                      | `3.14`         |
| `%a`    | floating esadecimale          | `0x1.91...p+1` |
| `%c`    | carattere                     | `A`            |
| `%s`    | stringa                       | `ciao`         |
| `%p`    | puntatore                     | `0x7ffd...`    |
| `%%`    | `%`                           | `%`            |

### ⌨️ `scanf`

| Formato | Tipo atteso            |
| ------- | ---------------------- |
| `%d`    | `int *`                |
| `%u`    | `unsigned int *`       |
| `%hd`   | `short *`              |
| `%hu`   | `unsigned short *`     |
| `%ld`   | `long *`               |
| `%lu`   | `unsigned long *`      |
| `%lld`  | `long long *`          |
| `%llu`  | `unsigned long long *` |
| `%f`    | `float *`              |
| `%lf`   | `double *`             |
| `%Lf`   | `long double *`        |
| `%c`    | `char *`               |
| `%s`    | `char *`               |
| `%x`    | unsigned esadecimale   |
| `%o`    | unsigned ottale        |
| `%p`    | puntatore              |

---

# 👀 29. Un'altra stranezza: `%i` non è proprio `%d`

Con `printf`:

```c
%d
```

e:

```c
%i
```

sono sostanzialmente equivalenti per gli interi signed.

Con `scanf`, invece, `%i` è più curioso.

```c
scanf("%i", &x);
```

può interpretare la base dalla rappresentazione del numero:

```text
42    → decimale
052   → ottale
0x2A  → esadecimale
```

mentre:

```c
scanf("%d", &x);
```

interpreta il valore come decimale.

Quindi:

> 🧠 **Stesso simbolo, comportamento leggermente diverso a seconda della funzione.**

Benvenuti nel C. ☕️

---

# 🚨 30. Occhio al tranello: `=` e `==`

Questo probabilmente lo conoscete già.

Ma merita una lapide commemorativa.

```c
x = 5;
```

significa:

> «assegna 5 a `x`».

Mentre:

```c
x == 5
```

significa:

> «`x` è uguale a 5?»

Quindi:

```c
if (x == 5)
```

è una domanda.

```c
x = 5;
```

è un'azione.

Un solo carattere.

Una differenza gigantesca. 💀

---

# 🚨 31. Occhio al tranello numero due: il nostro anno bisestile

C'è un piccolo problema interessante nel programma.

Abbiamo scritto:

```c
resto = anno % 4;

if (resto == 0)
    printf("L'anno è bisestile!");
```

Questa regola è **semplificata**.

Nel calendario gregoriano un anno è bisestile se:

```text
è divisibile per 4
```

ma:

```text
se è divisibile per 100
```

non è bisestile,

**a meno che**:

```text
sia divisibile per 400.
```

Quindi:

```text
2024 → bisestile ✅
1900 → NON bisestile ❌
2000 → bisestile ✅
```

Il nostro algoritmo è quindi perfetto come **esempio didattico dell'operatore `%` e della selezione**, ma non rappresenta completamente la regola del calendario gregoriano.

E questa è una lezione importante:

> 🧠 **Un programma può essere scritto correttamente e implementare comunque un modello incompleto del problema.**

Il computer esegue fedelmente quello che gli abbiamo detto.

Se gli abbiamo detto una sciocchezza con perfetta sintassi C, lui eseguirà la sciocchezza con perfetta sintassi C. 🤖

---

# 🔁 32. `for`: quando diciamo al computer "rifallo"

Nel secondo programma compare:

```c
for (int i = 0; i < 32; i++)
```

Il `for` contiene tre elementi:

```text
inizializzazione
       ↓
    condizione
       ↓
    incremento
```

Nel nostro caso:

```c
int i = 0
```

partiamo da zero.

Poi:

```c
i < 32
```

continuiamo finché la condizione è vera.

Infine:

```c
i++
```

incrementiamo `i` di uno.

Quindi:

```text
0
1
2
3
...
31
```

Sono esattamente **32 iterazioni**.

E attenzione:

```c
i < 32
```

non significa:

```text
0 ... 32
```

ma:

```text
0 ... 31
```

Perché `32` è escluso.

---

# 🧠 33. `i++`: un piccolo pezzo di C++ che ritrovate qui

Questa sintassi:

```c
i++;
```

è perfettamente valida anche in C.

Significa:

```text
incrementa i di 1
```

Analogamente:

```c
i--;
```

decrementa di uno.

Potete anche scrivere:

```c
i = i + 1;
```

oppure:

```c
i += 1;
```

Ma:

```c
i++;
```

è una delle forme storicamente più caratteristiche della famiglia C.

---

# 🧩 34. Il vero senso dei due programmi

Se guardiamo i due programmi nel loro insieme, scopriamo qualcosa di interessante.

### 📅 Programma 1

Ci insegna:

```text
variabili
   ↓
input
   ↓
operatore %
   ↓
confronto
   ↓
if / else
   ↓
output
```

### 🔢 Programma 2

Ci insegna:

```text
for
 ↓
variabile contatore
 ↓
basi numeriche
 ↓
format specifier
 ↓
ASCII
 ↓
caratteri
 ↓
rappresentazione dei dati
```

E insieme formano una piccola macchina didattica molto interessante:

> 🧠 **il primo programma ci insegna a ragionare sui dati; il secondo ci insegna a guardarli sotto prospettive diverse.**

---

# 🕵️ 35. Occhio al tranello finale: `%b`

Torniamo al nostro:

```c
%05b
```

Qui c'è una piccola trappola.

Nel **C standard ISO tradizionale**, `%b` non è il classico specificatore portabile di `printf`.

Alcuni compilatori possono supportarlo come **estensione**.

Quindi un programma che contiene:

```c
printf("%b", numero);
```

potrebbe funzionare perfettamente con un determinato compilatore e non funzionare con un altro.

Questo è un concetto molto importante:

> ⚠️ **"Funziona sul mio compilatore" non significa automaticamente "fa parte dello standard C".**

Quindi se il vostro ambiente didattico supporta `%b`, potete usarlo per l'esperimento sulle rappresentazioni binarie.

Ma sappiate che esiste una differenza fra:

```text
C standard
```

e:

```text
estensione specifica del compilatore
```

E questa differenza, prima o poi, vi salverà da parecchi:

> «Professore, ma sul computer di casa funziona!» 😭

---

# 👹 36. BOSS FINALE: riuscite a leggere questo?

Eccoci.

Non dovete scrivere il programma.

Non dovete compilarlo.

Dovete semplicemente **capire cosa sta facendo**. 🧠

```c
#include <stdio.h>

int main() {

    int x = 42;

    printf("dec: %d\n", x);
    printf("oct: %o\n", x);
    printf("hex: %04X\n", x);
    printf("char: %c\n", x + 23);

    if (x % 2 == 0) {
        printf("pari\n");
    }

    for (int i = 0; i < 4; i++) {
        printf("%d -> %02X\n", i, i);
    }

    return 0;
}
```

### 🧩 Domande da Boss

Senza eseguire il programma, provate a prevedere:

**1️⃣**

```c
x = 42;
```

Che cosa stamperà:

```c
printf("%d\n", x);
```

**2️⃣**

Che cosa rappresenta:

```c
%o
```

**3️⃣**

Che cosa significa:

```c
%04X
```

**4️⃣**

Che cosa verrà stampato da:

```c
printf("%c\n", x + 23);
```

**5️⃣**

Perché:

```c
x % 2 == 0
```

permette di riconoscere un numero pari?

**6️⃣**

Quante volte viene eseguito il `for`?

**7️⃣**

Quali valori assume `i`?

Se avete risposto senza bisogno di lanciare il programma, avete fatto una cosa molto più importante che ricordare una sintassi:

> 🧠 **avete iniziato a eseguire mentalmente un programma.**

Ed è uno degli strumenti più potenti che un programmatore possa sviluppare.

---

# 🧭 37. La mappa mentale da portarsi via

Se alla fine di questa guida doveste ricordare soltanto una cosa, ricordate questa:

```text
                    PROBLEMA
                       │
                       ▼
                    ALGORITMO
                       │
                       ▼
                 FLOWCHART
                       │
                       ▼
                LINGUAGGIO C
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       DATI        DECISIONI     CICLI
          │            │            │
       variabili     if/else       for
          │
          ▼
       OPERATORI
          │
          ▼
       INPUT/OUTPUT
       scanf/printf
          │
          ▼
     RAPPRESENTAZIONE
          │
     ┌────┼────┬────┐
     ▼    ▼    ▼    ▼
    dec  bin  oct  hex
          │
          ▼
        ASCII
          │
          ▼
        UTF-8
```

E improvvisamente il C smette di sembrare una collezione di simboli messi lì da qualcuno che aveva litigato con la punteggiatura. 😎

Diventa un sistema.

---

# 🧠 38. La cosa più importante: non state imparando C

Questa è forse la parte più importante dell'intera guida.

Non state imparando soltanto:

```c
if
for
printf
scanf
%
```

State imparando a **trasformare un ragionamento in una sequenza di istruzioni precise**.

Il C è lo strumento.

Domani potrebbe essere:

```text
C++
Java
Python
Rust
C#
JavaScript
```

La sintassi cambierà.

La capacità di ragionare rimarrà.

Per questo è perfettamente sensato che quest'anno vi venga chiesto di lavorare con un linguaggio apparentemente più semplice.

Il C vi costringe a guardare:

* 🧠 come vengono rappresentati i dati;
* 💾 dove vengono conservati;
* 🔢 come vengono rappresentati i numeri;
* 🔤 come vengono rappresentati i caratteri;
* 📍 cosa significa un indirizzo;
* ⚙️ cosa succede quando una funzione viene chiamata;
* 🔀 come un algoritmo prende decisioni;
* 🔁 come ripete operazioni.

E tutto questo tornerà utile anche quando tornerete a linguaggi più ricchi.

---

# 🌐 39. Per continuare a esplorare

Se volete approfondire senza perdervi in forum del 2007 dove tre programmatori litigano da 19 anni sulla differenza tra `char` e `unsigned char,` ecco alcune risorse decisamente più sane. 😄

* 📚 [cppreference: riferimento al linguaggio C](https://en.cppreference.com/w/c?utm_source=chatgpt.com)
* 🖨️ [cppreference: printf e formattazione](https://en.cppreference.com/c/io/fprintf?utm_source=chatgpt.com)
* ⌨️ [cppreference: scanf e funzioni correlate](https://en.cppreference.com/c/io/fscanf?utm_source=chatgpt.com)
* 🔢 [cppreference: tipi aritmetici del C](https://en.cppreference.com/w/c/language/arithmetic_types?utm_source=chatgpt.com)
* 📏 [cppreference: limiti numerici e `<limits.h>`](https://en.cppreference.com/w/c/types/limits?utm_source=chatgpt.com)
* 🔤 [Unicode: Basic Latin e caratteri di controllo C0](https://www.unicode.org/charts/nameslist/n_0000.html?utm_source=chatgpt.com)
* 🧠 [Stanford Encyclopedia of Philosophy: Church-Turing Thesis](https://plato.stanford.edu/entries/church-turing/?utm_source=chatgpt.com)

---

# 🏁 40. Fine. Ma solo per oggi. ☕️💻

La programmazione nasce da una richiesta apparentemente innocua:

> **«Come faccio a spiegare a una macchina quello che voglio?»**

La risposta non è:

> «Scrivo subito del codice.»

Prima viene il pensiero.

Poi l'algoritmo.

Poi la rappresentazione.

Poi il linguaggio.

Poi il programma.

E solo alla fine arriva il computer, che esegue tutto con assoluta obbedienza, anche quando abbiamo scritto una colossale stupidaggine. 🤖

Ed è proprio questa la parte meravigliosa della programmazione:

> 🧠 **un computer non vi insegna a pensare. Vi costringe a scoprire se avete pensato davvero.**

Quindi sì, ragazzi: avete fatto C++, siete arrivati agli array bidimensionali e ora vi ritrovate davanti a `printf`, `scanf`, ASCII, `%04X` e un misterioso operatore `%`.

Non è un passo indietro.

È un giro nel **cofano del computer**. 🔧💻

E, una volta capito cosa succede lì dentro, tornare a guidare una macchina più sofisticata sarà decisamente più interessante.

### ☕ **Benvenuti nel C. La moka è sul fuoco. Adesso proviamo a non bruciare il programma.** 🔥😎

[1]: https://plato.stanford.edu/archives/win2024/entries/church-turing/?utm_source=chatgpt.com "The Church-Turing Thesis (Stanford Encyclopedia of Philosophy/Winter 2024 Edition)"
[2]: https://en.cppreference.com/c/language/arithmetic_types?utm_source=chatgpt.com "Arithmetic types - cppreference.com"
[3]: https://en.cppreference.com/c/header/limits?utm_source=chatgpt.com "Standard library header <limits.h> - cppreference.com"
[4]: https://www.unicode.org/charts/nameslist/n_0000.html?utm_source=chatgpt.com "none"
[5]: https://en.cppreference.com/Template%3Acpp/io/c/printf_format?utm_source=chatgpt.com "Template:cpp/io/c/printf format - cppreference.com"
[6]: https://en.cppreference.com/cpp/io/c/printf?utm_source=chatgpt.com "std::printf, std::fprintf, std::sprintf, std::snprintf - cppreference.com"
[7]: https://en.cppreference.com/cpp/io/c/fscanf?utm_source=chatgpt.com "std::scanf, std::fscanf, std::sscanf - cppreference.com"
