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
# 🌟 **Numerical Base Conversion Theory** 🔢

## 1️⃣ **Numerical Bases** 🌟

In mathematics and computer science, **numerical bases** are systems we use to represent numbers. Each base has a **set of digits** from which values are constructed. The most common bases are:

* **Base 10 (Decimal)**: The system we use every day! 📜 Numbers from **0 to 9**.
* **Base 2 (Binary)**: The system that uses only **0 and 1**. It's the language of the **computer**! 💻
* **Base 8 (Octal)**: Uses digits from **0 to 7**. It’s more compact than binary! 🔎
* **Base 16 (Hexadecimal)**: Uses digits from **0 to 9** and **A-F** (to represent 10-15). It's commonly used to represent memory values! 🧑‍💻

### 2️⃣ **Converting Between Bases** 🔄

To convert between these bases:

* **From Base 10 to Base 2**: Divide the number by 2 and record the remainders. 🔢
* **From Base 2 to Base 10**: Multiply the bits by powers of 2 and sum them. 🔌
* **From Base 2 to Base 8**: Group the bits in sets of 3, since 2^3 = 8. 🧑‍🔬
* **From Base 2 to Base 16**: Group the bits in sets of 4, since 2^4 = 16. 🖥️

Example:

* **Decimal 10** → **Binary 1010**
* **Binary 1010** → **Hexadecimal A** (10 in hexadecimal is **A**).

### 3️⃣ **One's and Two's Complement** 🧑‍🏫

**One’s Complement** and **Two’s Complement** are techniques used to represent **negative numbers** in binary systems:

* **One’s Complement**: Achieved by flipping all the bits of a positive number. 😕
* **Two’s Complement**: Achieved by flipping all the bits and adding 1 to the result. 😍

### 4️⃣ **Shift Operations** ⬆️⬇️

**Shifting** means moving the bits in a direction (left or right) to modify the numeric value.

* **Left Shift (`<<`)**: Multiplies the number by a power of 2. 🔼
* **Right Shift (`>>` or `>>>`)**: Divides the number by a power of 2. 🔽

### 💡 **Shift Example** 🦸‍♂️

```javascript
let x = 5; // 101 in binary
x = x << 1; // 10 in binary, equivalent to 10 in decimal (5 * 2)
```

## 🅰️ **ASCII vs UNICODE** 🖋️

### 1️⃣ **ASCII** 🌐

**ASCII** (American Standard Code for Information Interchange) is a **7-bit** encoding standard that represents characters with numbers from **0 to 127**. 📝 It’s limited, but **historic**, and mainly used for the English alphabet and basic symbols.

### 2️⃣ **UNICODE** 🗣️

**Unicode** is a system that can represent **all characters in the world** 🗺️: letters, symbols, emojis, and characters from different languages. It uses **8, 16, or 32 bits**, depending on the format. 🌍

**Key Difference**:

* **ASCII** is limited to **128 characters**.
* **UNICODE** is **global** and can represent **billions of characters**.

## 🖥️ **`var`, `let`, and `const` in JavaScript** 🏗️

### 1️⃣ **`var`** 🔄

**`var`** is the traditional **variable declaration** in JavaScript. It has **function scope**, not block scope, which can lead to hard-to-spot errors. 🚧

**Example**:

```javascript
var x = 10;
if (true) {
  var x = 20; // Overwrites the outer variable!
}
```

### 2️⃣ **`let`** 🔐

**`let`** introduces **block scope**. Variables declared with **`let`** are only accessible within the block they were declared. 🛡️

**Example**:

```javascript
let x = 10;
if (true) {
  let x = 20; // Does not overwrite the outer variable!
}
```

### 3️⃣ **`const`** ⛔

**`const`** is used to declare **immutable** variables. Once a value is assigned, it cannot be changed. ⛔

**Example**:

```javascript
const pi = 3.14159;
pi = 3.14; // Error! You cannot change the value of a constant.
```

## 🏁 **'use strict';** 🧐

**`'use strict';`** is a directive that enables **strict mode** in JavaScript, improving code security and preventing some errors. 🛡️

* **Prevents the use of undeclared variables**.
* **Stops the accidental creation of global variables**.

With **'use strict';**, dangerous features are **disabled**, and the risk of bugs is **reduced**! 🐞

## 📝 **Output Methods in JavaScript** 💬

### 1️⃣ **`document.write()`** ✍️

**`document.write()`** or **`document.writeln()`** directly writes to the HTML document. It is **obsolete** and **not recommended** in modern environments as it can **overwrite** the entire page content.

**Example**:

```javascript
document.write("Hello world!");
```

### 2️⃣ **`innerHTML`** 🖥️

**`innerHTML`** allows you to **modify the HTML content** of an element. It’s more powerful than `document.write()`, but **should be used with caution**, as it can introduce **security issues** (like **cross-site scripting**).

**Example**:

```javascript
document.getElementById("myDiv").innerHTML = "<p>New content!</p>";
```

Alternatively:

```javascript
document.querySelector("myDiv").innerHTML = "<p>New content!</p>";
```

It’s like **`.getElementById`**, but more powerful as it allows you to select tags without IDs using **CSS-style selectors**.

### 3️⃣ **`console.log()`** 💬

**`console.log()`** is used to **print debug messages** to the browser console. It’s very helpful for testing and checking the behavior of the code during development.

**Example**:

```javascript
console.log("Debug test!");
```

### 4️⃣ **Methods in the Example Code** 🔍

In the example code, we see several operations like:

* **`toString(2)`**: Converts a number to binary.
* **`padStart()`**: Adds leading zeros to a string to ensure a fixed length.
* **`String.fromCharCode(i)`**: Converts a number to an ASCII character.

These methods help display base conversions and represent numbers in various formats accurately.

---

# 🌟 **Description of the HTML Page** 📄

The HTML page we showed is an application that **displays a table** containing numbers and their **representations in different numerical bases** (binary, octal, hexadecimal), **ASCII**, and other related information. It’s a practical example of **base conversions** and how to use JavaScript to manipulate numbers and interact with the DOM.

## 🔍 **HTML Page Functionality** 🧑‍💻

1. **Interactive Table** 📊:
   The page contains a table that shows for each number (from **-128** to **255**) the following information:

   * **Original number (n)**: The number in **base 10** (decimal).
   * **Base 2 (binary)**: The representation of the number in **binary** (base 2).
   * **Base 8 (octal)**: The representation in **base 8** (octal).
   * **Base 16 (hexadecimal)**: The representation in **base 16** (hexadecimal).
   * **ASCII**: The corresponding **ASCII character** (if applicable).

2. **What the JavaScript Code Does** 📜:

   * **Number Conversion**: For each number **i** in the range from **-128 to 255**, the code converts **i** into its **binary**, **octal**, **hexadecimal** representations and, where applicable, its **ASCII character**.
   * **Using `toString()`**: The **binary**, **octal**, and **hexadecimal** representations are obtained using the **`toString()`** method with the appropriate parameters (for example, `toString(2)` for binary, `toString(8)` for octal, etc.).
   * **Using `padStart()`**: To ensure binary numbers have a fixed length (32 bits), the **`padStart()`** method is used to add leading zeros where necessary.
   * **Using `String.fromCharCode()`**: This method is used to get the corresponding **ASCII character** for a number, which is particularly useful for seeing what certain numbers represent in the **ASCII** character set.

3. **DOM Insertion** 📥:

   * The table is dynamically updated within the `<tbody id="


bases"></tbody>` tag using **`innerHTML`**.

* Each iteration of the `for` loop creates a new row `<tr>` in the table with the various base representations of the numbers and the corresponding ASCII characters, if applicable.

## ⚙️ **Technical Details of How the JavaScript Code Works** ⚙️

* The page starts with the `'use strict';` directive, which activates JavaScript’s "strict mode", making the code safer and preventing common errors, such as undeclared variables.
* **`console.log()`** is used to print the binary representation of a number (`7.5`) as an example of conversion.
* The **`for`** loop iterates from **-128 to 255** and, for each value of `i`, calculates:

  * **Binary representation**: With **`(i >>> 0).toString(2)`**, the number is treated as an unsigned integer and converted to binary.
  * **Octal representation**: With **`toString(8)`**, the number is converted to octal.
  * **Hexadecimal representation**: With **`toString(16)`**, the number is converted to hexadecimal.
  * **ASCII character**: Using **`String.fromCharCode(i)`**, the code retrieves the character associated with the number, if it exists in the **ASCII** set.

### 🔄 **How the Table Works** 📑

* Each row in the table (`<tr>`) displays a number **n** with its respective **base 2, 8, 16, and ASCII** representations.

* **Example**:

  * For **n = 65**:

    * In **binary**: `1000001` (in a 32-bit format: `00000000000000000000000101000001`)
    * In **octal**: `101`
    * In **hexadecimal**: `0x41`
    * The **ASCII character** is **`A`**.

* The page **fills the table** iteratively, adding new rows for each number in the range from -128 to 255.

### 🧑‍🏫 **Key Concepts in the Page** 🧑‍🏫

* **Base Conversion**: The code clearly demonstrates **base conversion** (decimal, binary, octal, hexadecimal), showing how numbers can be represented in different formats.
* **Bit Manipulation**: Techniques like **right shift** (`>>>`), **padding**, and **treating unsigned numbers** are used to obtain the desired representations.
* **DOM Interaction**: The use of **`innerHTML`** allows for **dynamic insertion** of results into the HTML document, creating an interactive and visible table for the user.

## 💥 **In Summary** 💥

This page is an excellent example of how **JavaScript** can be used to explore fundamental concepts like **base conversions**, **bit shifting**, **string manipulation**, and the representation of **ASCII** and **UNICODE** characters. The page structure is simple and clear, yet powerful in its ability to **visualize** and **educate** on complex **computer science** topics. 🌟

## 🚀 **Final Conclusion** ✨

JavaScript is a **powerful** and **versatile** language! Understanding **numerical bases** 🧮, **variables** (`var`, `let`, `const`), **output methods**, and the differences between **ASCII and Unicode** allows you to create **robust** and **secure** code. 💪

*Keep exploring, experimenting, and improving your **arsenal** of programming techniques.
Every step brings you closer to becoming a true coding master!* 🌟


<hr/>

![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>

<!-- Italian -->
# 🌐 Teoria delle Conversioni tra Basi di Numerazione 🔢

## 1️⃣ Le Basi di Numerazione 🌟

In matematica e informatica, **le basi di numerazione** sono i sistemi che utilizziamo per rappresentare i numeri. Ogni base ha un **radice di numeri** da cui costruire i valori. Le basi più comuni sono:

* **Base 10 (Decimale)**: Il sistema che usiamo quotidianamente! 📜 Numeri da **0 a 9**.
* **Base 2 (Binario)**: Il sistema che usa solo **0 e 1**. È la lingua del **computer**! 💻
* **Base 8 (Ottale)**: Usa numeri da **0 a 7**. È più compatto del binario! 🔎
* **Base 16 (Esadecimale)**: Usa numeri da **0 a 9** e **A-F** (per rappresentare i numeri 10-15). È molto usato per rappresentare valori in memoria! 🧑‍💻

### 2️⃣ **Conversione tra le Basi** 🔄

Per convertire tra queste basi:

* Da **Base 10 a Base 2**: Si divide il numero per 2 e si annotano i resti. 🔢
* Da **Base 2 a Base 10**: Si moltiplicano i bit per le potenze di 2 e si sommano. 🔌
* Da **Base 2 a Base 8**: Si raggruppano i bit in gruppi di 3, poiché 2^3 = 8. 🧑‍🔬
* Da **Base 2 a Base 16**: Si raggruppano i bit in gruppi di 4, poiché 2^4 = 16. 🖥️

Esempio:

* **Decimale 10** → **Binario 1010**
* **Binario 1010** → **Esadecimale A** (10 in esadecimale è **A**).

### 3️⃣ **Complemento a 1 e a 2** 🧑‍🏫

**Complemento a 1** e **Complemento a 2** sono tecniche utilizzate per rappresentare **numeri negativi** nei sistemi binari:

* **Complemento a 1**: Si ottiene invertendo tutti i bit di un numero positivo. 😕
* **Complemento a 2**: Si ottiene invertendo tutti i bit e poi aggiungendo 1 al risultato. 😍

### 4️⃣ **Operazioni di Shift** ⬆️⬇️

**Shift** significa spostare i bit in una direzione (destra o sinistra) per modificare il valore numerico.

* **Shift a sinistra (`<<`)**: Moltiplica il numero per una potenza di 2. 🔼
* **Shift a destra (`>>` o `>>>`)**: Divide il numero per una potenza di 2. 🔽

### 💡 **Esempio di Shift** 🦸‍♂️

```javascript
let x = 5; // 101 in binario
x = x << 1; // 10 in binario, equivale a 10 in decimale (5 * 2)
```
## 🅰️ **ASCII vs UNICODE** 🖋️

### 1️⃣ **ASCII** 🌐

**ASCII** (American Standard Code for Information Interchange) è uno standard di codifica a **7 bit** che rappresenta i caratteri con numeri da **0 a 127**. 📝 È limitato, ma **storico** ed è usato principalmente per l'alfabeto inglese e i simboli di base.

### 2️⃣ **UNICODE** 🗣️

**Unicode** è un sistema che può rappresentare **tutti i caratteri del mondo** 🗺️: lettere, simboli, emoji, caratteri di lingue diverse. Si usa **a 8, 16 o 32 bit**, a seconda del formato. 🌍

**Differenza chiave**:

* **ASCII** è limitato a **128 caratteri**.
* **UNICODE** è **globale** e può rappresentare **miliardi di caratteri**.

## 🖥️ **`var`, `let` e `const` in JavaScript** 🏗️

### 1️⃣ **`var`** 🔄

**`var`** è la **dichiarazione di variabili tradizionale** in JavaScript. Ha **scope** (ambito) di **funzione**, non di blocco, il che può portare a errori difficili da individuare nel codice. 🚧

**Esempio**:

```javascript
var x = 10;
if (true) {
	var x = 20; // Sovrascrive la variabile esterna!
}
```

### 2️⃣ **`let`** 🔐

**`let`** introduce il concetto di **scope di blocco**. Le variabili dichiarate con **`let`** sono accessibili solo nel blocco di codice dove sono state dichiarate. 🛡️

**Esempio**:

```javascript
let x = 10;
if (true) {
	let x = 20; // Non sovrascrive la variabile esterna!
}
```

### 3️⃣ **`const`** ⛔

**`const`** serve per dichiarare variabili **immutabili**. Una volta assegnato un valore, non può essere modificato. ⛔

**Esempio**:

```javascript
const pi = 3.14159;
pi = 3.14; // Errore! non puoi cambiare il valore di una costante.
```

## 🏁 **'use strict';** 🧐

**`'use strict';`** è una direttiva che attiva la modalità **strict** in JavaScript, migliorando la sicurezza del codice e prevenendo alcuni errori. 🛡️

* **Evita l'uso di variabili non dichiarate**.
* **Impedisce la creazione di variabili globali accidentali**.

Con **'use strict';**, si **disabilitano** alcune funzionalità pericolose e si **riduce la possibilità di bug**! 🐞

## 📝 **Metodi di Output in JavaScript** 💬

### 1️⃣ **`document.write()`** ✍️

**`document.write()`** o **`document.writeln()`** scrive direttamente sul documento HTML. È **obsoleto** e **non raccomandato** in ambienti moderni perché può **sovrascrivere** tutto il contenuto della pagina.

**Esempio**:

```javascript
document.write("Ciao mondo!");
```

### 2️⃣ **`innerHTML`** 🖥️

**`innerHTML`** permette di **modificare il contenuto HTML** di un elemento. È più potente di `document.write()`, ma **deve essere usato con cautela**, in quanto può introdurre **problemi di sicurezza** (es. **cross-site scripting**).

**Esempio**:

```javascript
document.getElementById("myDiv").innerHTML = "<p>Nuovo contenuto!</p>";
```

od equivalentemente

```javascript
document.querySelector("myDiv").innerHTML = "<p>Nuovo contenuto!</p>";
```

È come **`.getElementById`** ma più potente perché permette di selezionare anche tag senza id, con le stesse metriche dei *selettori css*.

### 3️⃣ **`console.log()`** 💬

**`console.log()`** è utilizzato per **stampare messaggi di debug** sulla console del browser. È molto utile per testare e verificare il comportamento del codice durante lo sviluppo.

**Esempio**:

```javascript
console.log("Test di debug!");
```

### 4️⃣ **Metodi nel Codice Esempio** 🔍

Nel codice dell’esempio, vediamo diverse operazioni come:

* **`toString(2)`**: Converte un numero in formato binario.
* **`padStart()`**: Aggiunge zeri alla stringa per ottenere una lunghezza fissa.
* **`String.fromCharCode(i)`**: Converte un numero in un carattere ASCII.

Questi metodi aiutano a visualizzare le conversioni tra le basi e a rappresentare i numeri in vari formati con precisione.

---

# 🌟 **Descrizione della Pagina HTML** 📄

La pagina HTML che ti abbiamo mostrato è un'applicazione che **visualizza una tabella** contenente numeri e le loro **rappresentazioni in diverse basi numeriche** (binaria, ottale, esadecimale), **ASCII**, e altre informazioni correlate. È un esempio pratico di **conversioni tra basi** e di come usare JavaScript per manipolare numeri e interagire con il DOM.

## 🔍 **Funzionalità della Pagina HTML** 🧑‍💻

1. **Tabella Interattiva** 📊:
   La pagina contiene una tabella che mostra per ogni numero (da **-128** a **255**) le seguenti informazioni:

   * **Numero originale (n)**: Il numero in **base 10** (decimale).
   * **Base 2 (binaria)**: La rappresentazione del numero in **binario** (base 2).
   * **Base 8 (ottale)**: La rappresentazione in **base 8** (ottale).
   * **Base 16 (esadecimale)**: La rappresentazione in **base 16** (esadecimale).
   * **ASCII**: Il **carattere ASCII** corrispondente al numero (se applicabile).

2. **Cosa fa il codice JavaScript** 📜:

   * **Conversione del numero**: Per ogni numero **i** nel range da **-128 a 255**, il codice converte **i** nelle sue rappresentazioni in **binario**, **ottale**, **esadecimale** e, quando possibile, il relativo **carattere ASCII**.
   * **Uso di `toString()`**: Per ottenere le rappresentazioni **binaria**, **ottale** e **esadecimale** del numero, viene utilizzato il metodo **`toString()`** con i parametri appropriati (ad esempio, `toString(2)` per il binario, `toString(8)` per l'ottale, ecc.).
   * **Uso di `padStart()`**: Per assicurare che i numeri binari abbiano una lunghezza fissa (32 bit), viene utilizzato il metodo **`padStart()`** per aggiungere zeri iniziali dove necessario.
   * **Uso di `String.fromCharCode()`**: Questo metodo viene utilizzato per ottenere il **carattere ASCII** corrispondente a un numero, che è particolarmente utile per vedere cosa rappresentano certi numeri nel contesto del set di caratteri **ASCII**.

3. **Inserimento nel DOM** 📥:

   * La tabella viene aggiornata dinamicamente all'interno del tag `<tbody id="bases"></tbody>` utilizzando **`innerHTML`**.
   * Ogni ciclo del `for` crea una nuova riga `<tr>` nella tabella con le rappresentazioni dei vari numeri in tutte le basi numeriche e i caratteri ASCII, se applicabili.

## ⚙️ **Dettagli Tecnici sul Funzionamento del Codice JavaScript** ⚙️

* La pagina inizia con la direttiva `'use strict';`, che attiva la modalità "strict" di JavaScript, rendendo il codice più sicuro e prevenendo errori comuni, come l'uso di variabili non dichiarate.
* Viene utilizzato **`console.log()`** per stampare in console la rappresentazione binaria di un numero (`7.5`) come esempio di conversione.
* Il ciclo **`for`** va da **-128** a **255** e, per ogni valore di `i`, calcola:

  * La **rappresentazione binaria**: Con **`(i >>> 0).toString(2)`**, il numero viene trattato come un intero senza segno e convertito in binario.
  * La **rappresentazione ottale**: Con **`toString(8)`**, il numero viene convertito in base 8.
  * La **rappresentazione esadecimale**: Con **`toString(16)`**, il numero viene convertito in esadecimale.
  * **Carattere ASCII**: Usando **`String.fromCharCode(i)`**, il codice ottiene il carattere associato al numero, se esistente nell'insieme **ASCII**.

### 🔄 **Come Funziona la Tabella** 📑

* Ogni riga della tabella (`<tr>`) mostra un numero **n** con le sue rispettive **rappresentazioni in base 2, 8, 16 e ASCII**.

* **Esempio**:

  * Per **n = 65**:

    * In **binario**: `1000001` (in un formato a 32 bit: `00000000000000000000000101000001`)
    * In **ottale**: `101`
    * In **esadecimale**: `0x41`
    * Il **carattere ASCII** corrispondente è **`A`**.

* La pagina **riempie la tabella** iterativamente, aggiungendo nuove righe per ogni numero nel range da -128 a 255.

### 🧑‍🏫 **Principi Fondamentali della Pagina** 🧑‍🏫

* **Conversione tra basi**: Il codice esegue in modo chiaro la **conversione tra basi** (decimale, binaria, ottale, esadecimale), mostrando come i numeri possono essere rappresentati in diversi formati.
* **Manipolazione dei bit**: Si utilizzano tecniche come lo **shift a destra** (`>>>`), il **padding** e il **trattamento dei numeri senza segno** per ottenere le rappresentazioni desiderate.
* **Interazione con il DOM**: L'uso di **`innerHTML`** permette di **inserire dinamicamente** i risultati nel documento HTML, creando una tabella interattiva e visibile per l'utente.

## 💥 **In Sintesi** 💥

Questa pagina è un eccellente esempio di come **JavaScript** possa essere utilizzato per esplorare concetti fondamentali come la **conversione tra basi numeriche**, l'uso dei **bit shifting**, la manipolazione delle **stringhe** e la rappresentazione dei **caratteri** in **ASCII** e **UNICODE**. La struttura della pagina è semplice e chiara, ma potente nella sua capacità di **visualizzare** e **educare** su temi complessi di **informatica**. 🌟

## 🚀 **Conclusione Finale** ✨

JavaScript è un linguaggio **potente** e **versatile**! La comprensione delle **basi numeriche** 🧮, delle **variabili** (`var`, `let`, `const`), dei **metodi di output**, e delle **differenze tra ASCII e Unicode** ti permette di creare codice **robusto** e **sicuro**. 💪

*Continua a esplorare, fare esperimenti e migliorare il tuo **arsenal** di tecniche di programmazione.
Ogni passo ti avvicina a diventare un vero maestro del codice!* 🌟

<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)