[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

<a name="TOP"></a>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇬🇧](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png) <a name="EN"></A>
# 🎃 Introduction to PHP with a Halloween Emoji Table 🧙‍♂️

Welcome to this introductory guide to **PHP**, a server-side programming language used to create dynamic and interactive web pages. In this example, we’ll look at some core PHP concepts, like **variables**, **arrays**, **string concatenation**, and **looping** to generate an HTML table filled with Halloween-themed emojis! 👻

## 🛠️ What is PHP?

PHP is a server-side scripting language, meaning it runs on the server before sending the final HTML code to the browser. It’s widely used in web development for its ability to interact with databases and produce dynamic content. 📄

- In this project, PHP and HTML are combined to dynamically generate a table filled with colorful emojis. 🎨
- PHP handles the calculations and logic, while HTML is used to structure the layout of the content. 🖥️

## 📊 Using Arrays in PHP

In PHP, an **array** is a data structure that holds a list of items, which can be either **numerically indexed** or **associative**.

### Emoji and Color Arrays
In this example, we use two arrays: `$emojiList` and `$colorsList`. 🗂️
- **`$emojiList`** holds Unicode codes for the emoji characters 🎃.
- **`$colorsList`** stores hex color values that will be used as background colors for each table cell. 🎨

```php
$emojiList = [0x1f52e, 0x1f47b, 0x1f9db, 0x1f9df, 0x1f315];
$colorsList = [0xff8c00, 0x4b0082, 0xa4d65e, 0xa9a9a9, 0x8b4513];
```

Arrays allow us to access elements through an **index** and select them dynamically as we build the table. 🔄

## 🔤 Variables and String Concatenation

**Variables** in PHP are declared with the `$` symbol, like `$ROWS` and `$COLS` in this example, which determine the number of rows and columns in the table.

```php
$ROWS = 10;
$COLS = 10;
```

### String Concatenation
PHP uses the dot (`.`) operator to concatenate strings. In our code, concatenation is used to insert dynamically generated values into the HTML code.

```php
echo "<td style='background-color: #$color'>&#{$emojiList[($i + $j) % $N]};</td>\n";
```

This line of code sets the background color of each table cell and displays the selected emoji through dynamic concatenation. 🎨✨

## 🔄 Loops and Control Structures

The code uses a **for loop** to build each row (`<tr>`) and cell (`<td>`) of the table, applying **variables** to position each emoji and set the background color. 🔁

```php
for ($i = 0; $i < $ROWS; $i++) {
    echo "<tr>\n";
    for ($j = 0; $j < $COLS; $j++) {
        $color = str_pad(dechex($colorsList[($i + $j) % $M]), 6, 0, STR_PAD_LEFT);
        echo "<td style='background-color: #$color'>&#{$emojiList[($i + $j) % $N]};</td>\n";
    }
    echo "</tr>\n";
}
```

In this example:
- `$i` and `$j` act as indices to position elements in the table correctly.
- The **modulo operator (`%`)** helps "wrap around" the indices, cycling through the emoji and color arrays to create a repeating visual pattern.

## 📚 Conclusion

This example offers a snapshot of how PHP can generate dynamic HTML content through **variables**, **arrays**, **string concatenation**, and **for loops**. 🚀
With these basics, you can build dynamic pages with auto-generated and easily modifiable content.

Happy coding, and Happy Halloween! 🕸️🕷️


<hr/>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a> 🤍 <a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>
# 🎃 Guida Introduttiva a PHP con Tabelle di Emoji di Halloween 🧙‍♂️

Benvenuti a questa guida introduttiva a **PHP**, un linguaggio di programmazione lato server usato per creare pagine web dinamiche e interattive.
In questo esempio, esploreremo vari elementi del linguaggio, come **variabili**, **array**, **concatenazione di stringhe** e l’uso del **looping** per generare una tabella HTML di emoji di Halloween! 👻

## 🛠️ Cos'è PHP?
PHP è un linguaggio di scripting lato server, il che significa che viene eseguito sul server prima di inviare il codice HTML finale al browser.
È ampiamente utilizzato nello sviluppo web per la sua capacità di interagire facilmente con database e produrre contenuti dinamici. 📄

- Il file PHP è stato scritto in HTML e PHP per generare dinamicamente una tabella piena di emoji colorati. 🎨
- PHP si occupa del calcolo e della logica, mentre l’HTML viene usato per strutturare il layout del contenuto. 🖥️

## 📊 Uso degli Array in PHP

In PHP, un **array** è una struttura dati che contiene una lista di elementi, e può essere di diversi tipi, come **array numerici** o **array associativi**.

### Emoji e Colori in Array
In questo file, abbiamo due array: `$emojiList` e `$colorsList`. 🗂️
- **`$emojiList`** memorizza i codici Unicode delle emoji 🎃.
- **`$colorsList`** contiene valori esadecimali di colore che verranno utilizzati come sfondo delle celle della tabella. 🎨

```php
$emojiList = [0x1f52e, 0x1f47b, 0x1f9db, 0x1f9df, 0x1f315];
$colorsList = [0xff8c00, 0x4b0082, 0xa4d65e, 0xa9a9a9, 0x8b4513];
```

Gli array ci permettono di accedere agli elementi tramite un **indice** e di selezionarli in maniera dinamica. 🔄

## 🔤 Variabili e Concatenazione di Stringhe

Le **variabili** in PHP vengono dichiarate con il simbolo `$`, come `$ROWS` e `$COLS` in questo esempio, che determinano il numero di righe e colonne della tabella.

```php
$ROWS = 10;
$COLS = 10;
```

### Concatenazione di Stringhe
PHP utilizza il punto (`.`) per concatenare le stringhe.
Nell'esempio, usiamo concatenazione per inserire i valori generati dinamicamente nel codice HTML.

```php
echo "<td style='background-color: #$color'>&#{$emojiList[($i + $j) % $N]};</td>\n";
```

Questa riga di codice imposta lo sfondo di ogni cella della tabella e visualizza l’emoji selezionata tramite concatenazione dinamica. 🎨✨

## 🔄 Cicli e Struttura di Controllo

Il codice usa un **ciclo for** per costruire ogni riga (`<tr>`) e cella (`<td>`) della tabella, applicando le **variabili** per posizionare l’emoji e impostare il colore di sfondo. 🔁

```php
for ($i = 0; $i < $ROWS; $i++) {
	echo "<tr>\n";
	for ($j = 0; $j < $COLS; $j++) {
		$color = str_pad(dechex($colorsList[($i + $j) % $M]), 6, 0, STR_PAD_LEFT);
		echo "<td style='background-color: #$color'>&#{$emojiList[($i + $j) % $N]};</td>\n";
	}
	echo "</tr>\n";
}
```

In questo caso:
- `$i` e `$j` sono indici per posizionare correttamente l’elemento nella tabella.
- **Modulo (`%`)** viene usato per "riavvolgere" l'indice e ciclarlo attraverso gli array di emoji e colori, creando un pattern visivo.

## 📚 Conclusione

Questo esempio fornisce una panoramica di come PHP può generare contenuto HTML dinamico attraverso **variabili**, **array**, **concatenazione di stringhe**, e **cicli for**. 🚀
Con queste basi, è possibile creare pagine dinamiche con contenuti generati in modo automatico e facilmente modificabile.

Buona codifica e felice Halloween! 🕸️🕷️

<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)