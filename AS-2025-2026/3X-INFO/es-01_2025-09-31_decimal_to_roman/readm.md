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
# Decimal to Roman Converter 🏛️🔢✨

## 📋 What This Code Does 🛠️➡️🔣

This C program converts an integer number (between 1 and 3999) into its corresponding Roman numeral.
- It prompts the user to input a number 📥
- Checks if the number is within a valid range 🚦 (1 to 3999)
- Separates the number into thousands, hundreds, tens, and units 📏
- Converts each part into Roman numerals using `switch` statements 🔀
- Prints the full Roman numeral equivalent 🖨️

## 💡 How Number Separation Works: Thousands, Hundreds, Tens, and Units 🔍➗

To convert a number to Roman numerals, the program separates its digits based on their place values:
- **Units (ones) 🔢:** Extracted with `number % 10`
- **Tens (decine) 🔟:** Extracted with `(number - units) % 100`
- **Hundreds (centinaia) 💯:** Extracted with `(number - tens - units) % 1000`
- **Thousands (migliaia) 1000️⃣:** Extracted by subtracting units, tens, and hundreds from the number

This separation helps convert each digit group individually, following the Roman numeral rules.

## 🔄 Understanding Control Structures: if..else if..else vs. switch..case 🔧🤔

Both control structures allow decision-making in code, but differ in usage and clarity:

### if..else if..else 🧩

- Used for checking a range or multiple complex conditions
- Flexible: can evaluate expressions and compound conditions
- Syntax example:

```c
if (condition1) { ... }
else if (condition2) { ... }
else { ... }
```

- Good for broader logical checks

### switch..case 🔀

- Used specifically for comparing one variable against discrete constant values
- Cleaner and easier to read when handling many fixed cases
- Syntax example:

```c
switch(variable) {
	case value1: ...
	case value2: ...
	default: ...
}
```

- Ideal for this program since each digit corresponds to specific fixed Roman numeral patterns

## ⚙️ How to Compile and Run the Code 🖥️💻

1. Save the C code in a file, for example, [`main.c`](./main.c)
2. Open a terminal or command prompt
3. Compile the code using a C compiler like gcc:

```bash
gcc main.c -o roman_converter
```

4. Run the compiled program:

```bash
./roman_converter
```

5. Enter a number in the range [1..3999] when prompted and see the Roman numeral output! 🎉

## 📚 Summary and Key Points 🔑📌

- Input validation ensures only numbers from 1 to 3999 are processed ❗
- The number is broken down into thousands, hundreds, tens, and units for precise conversion 🏗️
- `switch` statements map each digit range to the proper Roman numerals directly 🔄
- Helps understand practical uses of control flow and arithmetic operations in real-world coding 🧑‍💻
- Simple, well-structured, and educational example of C programming basics ✅

*Enjoy converting numbers with Roman style*! 🏛️✨


---

![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>

<!-- Italian -->
# Convertitore di Numeri in notazione Romana 🏛️🔢✨


## 📋 Cosa Fa Questo Codice 🛠️➡️🔣

Questo programma in C converte un numero intero (tra 1 e 3999) nel suo corrispondente numerale romano.
- Chiede all'utente di inserire un numero 📥
- Verifica se il numero è in un intervallo valido 🚦 (da 1 a 3999)
- Divide il numero in migliaia, centinaia, decine e unità 📏
- Converte ogni parte in numeri romani usando istruzioni `switch` 🔀
- Stampa il numero romano completo 🖨️


## 💡 Come Funziona la Separazione del Numero: Migliaia, Centinaia, Decine e Unità 🔍➗

Per convertire un numero in numeri romani, il programma divide le cifre in base al loro valore posizionale:
- **Unità (ones) 🔢:** estratta con `number % 10`
- **Decine (tens) 🔟:** estratta con `(number - units) % 100`
- **Centinaia (hundreds) 💯:** estratta con `(number - tens - units) % 1000`
- **Migliaia (thousands) 1000️⃣:** estratta sottraendo unità, decine e centinaia dal numero

Questa separazione aiuta a convertire ciascuna parte singolarmente, secondo le regole dei numeri romani.

## 🔄 Comprendere le Strutture di Controllo: if..else if..else vs. switch..case 🔧🤔

Entrambe le strutture consentono di prendere decisioni nel codice, ma differiscono nell’uso e nella chiarezza:

### if..else if..else 🧩

- Usato per verificare intervalli o condizioni complesse multiple
- Flessibile: può valutare espressioni e condizioni composte
- Esempio di sintassi:
```c
if (condition1) { ... }
else if (condition2) { ... }
else { ... }
```
- Adatto per controlli logici più ampi

### switch..case 🔀

- Usato specificatamente per confrontare una variabile con valori costanti discreti
- Più pulito e leggibile quando si gestiscono molti casi fissi
- Esempio di sintassi:

```c
switch(variable) {
	case value1: ...
	case value2: ...
	default: ...
}
```

- Ideale in questo programma dato che ogni cifra corrisponde a schemi romani fissi

## ⚙️ Come Compilare ed Eseguire il Codice 🖥️💻

1. Salvare il codice in un file, ad esempio [`main.c`](./main.c)
2. Aprire un terminale o prompt dei comandi
3. Compilare con un compilatore C come gcc:

```bash
gcc main.c -o roman_converter
```

4. Eseguire il programma compilato:

```bash
./roman_converter
```

5. Inserire un numero nell'intervallo [1..3999] quando richiesto e vedere il numero romano risultante! 🎉

## 📚 Riepilogo e Punti Chiave 🔑📌

- La validazione dell’input garantisce che vengano processati solo numeri da 1 a 3999 ❗
- Il numero viene suddiviso in migliaia, centinaia, decine e unità per una conversione precisa 🏗️
- Gli `switch` mappano ciascun intervallo di cifre nei numerali romani corretti 🔄
- Aiuta a comprendere l’uso pratico del controllo di flusso e delle operazioni aritmetiche nella programmazione reale 🧑‍💻
- Esempio semplice, ben strutturato ed educativo di basi di programmazione in C ✅

*Divertiti a convertire numeri in stile romano*! 🏛️✨


<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)