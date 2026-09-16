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

### Let's reset our thinking and recap what we know



## 🚀 We aren't learning anything new



These exercises serve as a quick **hands-on refresher of core programming concepts**.

You've already seen this code before; the point here is to pause for a second and recognize **the logical patterns we rely on when writing software**. 💻

> 🎯 **Syntax fades. Analytical thinking needs continuous training.**
>

# 📦 1. Variables and Data Types



## 🧱 Software runs on memory



Every application must store and manipulate data.

```cpp
float weight, height, bmi;
int timeOfDay;
```

A **variable** is simply a named space in memory tied to a specific data type.

| Type | Use Case | Example |
| --- | --- | --- |
| `int` 🔢 | whole numbers | `18` |
| `float` 🔢 | floating-point numbers | `72.5` |
| `char` 🔤 | single characters | `'A'` |
| `bool` ✅ | logical values | `true` |

🧠 **Choosing the right data type boils down to defining what kind of information you want to model.**

# 📥 2. Input and Output

## 💬 The program communicates with the user

With:

```cpp
cin >> weight;
```

we collect user input.

With:

```cpp
cout << "Your BMI is " << bmi;
```

we return a result.

This gives us the standard flow:

```text
👤 USER
	↓
📥 INPUT
	↓
⚙️ PROCESSING
	↓
📤 OUTPUT
	↓
👤 USER
```

🎯 The **input → processing → output** blueprint sits at the heart of almost every program.

---

# 🧮 3. Operators and Expressions

## ⚙️ Transforming data

In this calculation:

```cpp
bmi = weight / (height * height);
```

we use standard arithmetic operators:

`+` ➕  `-` ➖  `*` ✖️  `/` ➗  `%` 🔢

The expression:

```cpp
height * height
```

is an **expression**: a combination of values, variables, and operators that resolves to a single result.

💡 The computer doesn't actually "understand" what [BMI](./main_es-01v0_bmi_calculator.cpp) is. **It just blindly carries out the exact instructions we give it.**

# ⚖️ 4. Conditions and Comparisons

## 🔀 Programs make dynamic choices

Inside the code, we find:

```cpp
if (bmi >= 25)
```

This condition evaluates directly to:

```text
✅ true
or
❌ false
```

Here are the main comparison operators:

| Operator | Meaning |
| ---: | --- |
| `>` | greater than |
| `<` | less than |
| `>=` | greater than or equal to |
| `<=` | less than or equal to |
| `==` | equal to |
| `!=` | not equal to |

⚠️ Keep this distinction in mind:

```cpp
x = 10;
```

➡️ **assignment**

```cpp
x == 10;
```

➡️ **comparison**

# 🔗 5. Logical Operators

## 🧠 Handling composite conditions

In our [time example](./main_es-02v0_time_greeting_if.cpp):

```cpp
if (timeOfDay >= 8 && timeOfDay <= 12)
```

we bridge two distinct conditions using `&&`, which stands for **AND**.
The whole statement evaluates to true **only if both conditions hold true**.

```text
timeOfDay >= 8
	&&
timeOfDay <= 12
```

🎯 This pattern lets us check against ranges and build compound logic.

# 🚦 6. Decision Structures

## 🔀 `if`, `else if`, `else`

A control structure like:

```cpp
if (condition1)
	...
else if (condition2)
	...
else
	...
```

allows us to sequence logic into clear decision trees.

Visualized:

```text
🤔 Condition 1?
	├── ✅ yes → execute
	└── ❌ no
	↓
	🤔 Condition 2?
		├── ✅ yes → execute
		└── ❌ no → else
```

🧠 This is how we convert **logical rules into runnable algorithms**.

# 🔘 7. `switch`: Handling Multiple Discrete Values

## 🎯 When evaluating against fixed choices

The [alternative approach](./main_es-02v1_time_greeting_switch.cpp) solves the exact same problem using:

```cpp
switch (timeOfDay)
```

with matching:

```cpp
case
```

For example:

```cpp
case 8:
case 9:
case 10:
	cout << "good morning";
	break;
```

The `switch` statement shines when you need to match **a single value against specific static cases**.

| `if` 🔀 | `switch` 🎯 |
| ---: | --- |
| generic conditions | explicit values/cases |
| continuous ranges | discrete choices |
| complex comparisons | multi-way branching |

💡 **A single logical problem almost always admits multiple algorithmic approaches.**

# 🔄 8. The Modulo Operator (`%`)

## 🕐 Small operator, broad utility

In the program, you'll spot:

```cpp
timeOfDay %= 24;
```

which expands to:

```cpp
timeOfDay = timeOfDay % 24;
```

The `%` operator returns the **remainder of integer division**.

```text
27 % 24 = 3
```

This comes in handy whenever you need to wrap numbers around inside a repeating cycle.

🔄 **Modulo is a fundamental building block in algorithmic design.**

# 🧠 9. The Core Takeaway: Algorithms

## 🗺️ Logic always precedes code

Behind every task, we followed this implicit workflow:

```text
📌 PROBLEM DEFINITION
	↓
📥 INPUT DATA
	↓
⚙️ DATA PROCESSING
	↓
🔀 CONDITIONAL LOGIC
	↓
📤 FINAL OUTPUT
```

For instance:

**Calculating BMI**

```text
⚖️ weight + height
	↓
🧮 BMI formula
	↓
⚖️ threshold comparisons
	↓
📤 health category output
```

🎯 **Code is simply the translation of an algorithm into a language the machine can process.**

# 🧰 10. Our Coding Toolkit

## 🚀 Key concepts consolidated

| 🧠 Concept | 🔧 Concrete Element |
| ---: | --- |
| Variables | `int`, `float` |
| Input | `cin` |
| Output | `cout` |
| Assignment | `=` |
| Arithmetic | `+ - * / %` |
| Comparisons | `> < >= <= == !=` |
| Boolean Logic | `&&` |
| Branching Logic | `if / else if / else` |
| Multi-case Selection | `switch / case` |
| Scope Blocks | `{ }` |
| Algorithms | sequence + evaluation + decisions |

# 🔥 The Big Picture

## 🧠 Code is just the tip of the iceberg

When reading a line like this:

```cpp
if (timeOfDay >= 8 && timeOfDay <= 12)
```

look beyond raw C++ syntax.
Train yourself to see the underlying chain:

**📦 variables → ⚖️ comparisons → 🔗 boolean logic → 🔀 branching → 🎯 algorithm**

These are the **core building blocks of software engineering**.

💡 True proficiency isn't about memorizing syntax by heart—it's knowing **which tool to pick to break down a real-world problem into actionable steps for a computer to execute**. 🚀

---

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

---

![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>

<!-- Italiano -->

# 🧠 C++ Review:
### Rimettiamo in moto il ragionamento e facciamo il recap delle nostre conoscenze

## 🚀 Non stiamo imparando qualcosa di nuovo

Questi esercizi rappresentano un breve **ripasso operativo dei concetti fondamentali della programmazione**.
Il codice è già conosciuto: l'obiettivo è fermarsi un momento e riconoscere **quali meccanismi logici utilizziamo quando scriviamo un programma**. 💻
> 🎯 **La sintassi si dimentica. Il ragionamento va allenato.**

# 📦 1. Variabili e tipi di dato

## 🧱 Il programma ha bisogno di memoria

Ogni programma deve conservare e manipolare informazioni.

```cpp
float peso, altezza, bmi;
int orario;
```

Una **variabile** è uno spazio in memoria identificato da un nome e associato a un determinato tipo di dato.

| Tipo | Utilizzo | Esempio |
| --- | --- | --- |
| `int` 🔢 | numeri interi | `18` |
| `float` 🔢 | numeri decimali | `72.5` |
| `char` 🔤 | caratteri | `'A'` |
| `bool` ✅ | valori logici | `true` |

🧠 **Scegliere il tipo significa stabilire che genere di informazione vogliamo rappresentare.**

# 📥 2. Input e output

## 💬 Il programma comunica con l'utente

Con:

```cpp
cin >> peso;
```

acquisiamo un dato.

Con:

```cpp
cout << "il tuo bmi vale " << bmi;
```

produciamo un risultato.

Possiamo quindi schematizzare:

```text
👤 UTENTE
	↓
📥 INPUT
	↓
⚙️ ELABORAZIONE
	↓
📤 OUTPUT
	↓
👤 UTENTE
```

🎯 Questo schema **input → elaborazione → output** è alla base di moltissimi programmi.

---

# 🧮 3. Operatori ed espressioni

## ⚙️ Trasformare i dati

Nel calcolo:

```cpp
bmi = peso / (altezza * altezza);
```

utilizziamo operatori aritmetici:

`+` ➕  `-` ➖  `*` ✖️  `/` ➗  `%` 🔢

La parte:

```cpp
altezza * altezza
```

è un'**espressione**: una combinazione di valori, variabili e operatori che produce un risultato.

💡 Il programma non "capisce" il [BMI](./main_es-01v0_bmi_calculator.cpp). **Esegue semplicemente le operazioni che gli abbiamo indicato.**

# ⚖️ 4. Condizioni e confronti

## 🔀 Il programma può prendere decisioni

Nel codice troviamo:

```cpp
if (bmi >= 25)
```

La condizione viene valutata come:

```text
✅ true
oppure
❌ false
```

Gli operatori di confronto principali sono:

| Operatore | Significato |
| ---: | --- |
| `>` | maggiore |
| `<` | minore |
| `>=` | maggiore o uguale |
| `<=` | minore o uguale |
| `==` | uguale |
| `!=` | diverso |

⚠️ Da ricordare:

```cpp
x = 10;
```

➡️ **assegnazione**

```cpp
x == 10;
```

➡️ **confronto**

# 🔗 5. Operatori logici

## 🧠 Quando una condizione diventa più complessa

Nel programma dell'[orario](./main_es-02v0_time_greeting_if.cpp):

```cpp
if (orario >= 8 && orario <= 12)
```

abbiamo due condizioni collegate da: `&&` che significa **AND**, cioè "e".
La condizione è vera solo quando **entrambe** sono vere.

```text
orario >= 8
	&&
orario <= 12
```

🎯 In questo modo possiamo rappresentare intervalli e condizioni composte.

# 🚦 6. Strutture decisionali

## 🔀 `if`, `else if`, `else`

Una struttura come:

```cpp
if (condizione1)
	...
else if (condizione2)
	...
else
	...
```

permette di costruire una sequenza di decisioni.
In pratica:

```text
🤔 Condizione 1?
	├── ✅ sì → esegui
	└── ❌ no
	↓
	🤔 Condizione 2?
		├── ✅ sì → esegui
		└── ❌ no → else
```

🧠 È uno dei meccanismi fondamentali con cui trasformiamo una **regola logica in un algoritmo**.

# 🔘 7. `switch`: scegliere tra alternative

## 🎯 Quando abbiamo diversi valori possibili

L'[altro esercizio](./main_es-02v1_time_greeting_switch.cpp) risolve lo stesso problema utilizzando:

```cpp
switch (orario)
```

con diversi:

```cpp
case
```

Ad esempio:

```cpp
case 8:
case 9:
case 10:
	cout << "buongiorno";
	break;
```

`switch` è particolarmente utile quando dobbiamo confrontare **un valore con una serie di casi specifici**.

| `if` 🔀 | `switch` 🎯 |
| ---: | --- |
| condizioni | valori/casi |
| intervalli | alternative discrete |
| confronti complessi | selezione multipla |

💡 **Uno stesso problema può avere più soluzioni algoritmiche.**

# 🔄 8. L'operatore `%`

## 🕐 Un piccolo operatore, tante applicazioni

Nel programma compare:

```cpp
orario %= 24;
```

equivalente a:

```cpp
orario = orario % 24;
```

L'operatore `%` restituisce il **resto della divisione intera**.

```text
27 % 24 = 3
```

Questo permette, ad esempio, di riportare un valore all'interno di un intervallo ciclico.

🔄 **Il modulo è uno strumento molto importante nella programmazione algoritmica.**

# 🧠 9. Il concetto più importante: algoritmo

## 🗺️ Prima del codice viene il ragionamento

Dietro ogni esercizio abbiamo seguito, anche implicitamente, questo percorso:

```text
📌 PROBLEMA
	↓
📥 DATI IN INGRESSO
	↓
⚙️ ELABORAZIONE
	↓
🔀 DECISIONI
	↓
📤 RISULTATO
```

Per esempio:

**Calcolare il BMI**

```text
⚖️ peso + altezza
	↓
🧮 formula BMI
	↓
⚖️ confronto con le soglie
	↓
📤 classificazione
```

🎯 **Il codice è la traduzione dell'algoritmo in un linguaggio comprensibile al computer.**

# 🧰 10. La nostra cassetta degli attrezzi

## 🚀 Cosa abbiamo fissato

| 🧠 Concetto | 🔧 Elemento utilizzato |
| ---: | --- |
| Variabili | `int`, `float` |
| Input | `cin` |
| Output | `cout` |
| Assegnazione | `=` |
| Calcoli | `+ - * / %` |
| Confronti | `> < >= <= == !=` |
| Logica | `&&` |
| Decisioni | `if / else if / else` |
| Scelta multipla | `switch / case` |
| Blocchi | `{ }` |
| Algoritmi | sequenza + elaborazione + decisione |

# 🔥 In sintesi

## 🧠 Il codice è la punta dell'iceberg

Quando guardiamo:

```cpp
if (orario >= 8 && orario <= 12)
```

non dovremmo vedere soltanto una riga di C++.

Dovremmo riconoscere:

**📦 variabili → ⚖️ confronti → 🔗 logica → 🔀 decisione → 🎯 algoritmo**

Questi sono i **mattoni fondamentali della programmazione**.

💡 E la vera abilità non consiste nel ricordare ogni singola istruzione, ma nel saper riconoscere **quale strumento utilizzare per trasformare un problema in una sequenza di operazioni che il computer possa eseguire**. 🚀

<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)
[![gmail](https://img.shields.io/badge/gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:birg81@gmail.com)