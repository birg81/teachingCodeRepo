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

# ⚔️ Java Dungeon Arena: *Design your 1st Creature*! 🐉

Hey Devs! 👋🔥

Welcome to your brand new coding challenge! 🚀💎
Today you'll take an epic leap into the world of *Dungeons* 🏰 and object-oriented programming (**OOP**) 🧱.
You'll learn how to bring advanced digital entities to life, manage their state safely, and make them *fight to the death in an arena*! 💥⚡

## 🎯 The Goal 🎯

Your task is to build a mini combat engine in Java ☕ made of two core classes:
- 🧬 [**model**.`Creature`](./src/model/Creature.java): the model class that defines our enhanced game entity.
- 🧪 [**test**.`Main`](./src/test/Main.java): the test class used to simulate epic battles! 🎬

## 🧬 Part 1: The [**model**.`Creature`](./src/model/Creature.java) Class 🧬

Create the class inside the model package 📦, applying the principles of encapsulation 🔒 and robustness.

### 🛡️ Attributes (Private)
- 🏷️ `name` (String): The creature's name (trimmed of extra whitespace).
- 🔴 `healthPoints` (int): The creature's health points (HP) (default 100).
- ⚔️ `attackPower` (int): The creature's attack value (default 10).

### 🏗️ Constructors and Extras
- 🟢 **Default Constructor**: Takes no parameters and relies on the main constructor, passing default values.
- 🔵 **Custom Constructor**: Takes a `name`, validates it, and sets `healthPoints = 100` and `attackPower = 10`.
- 🧬 **Copy Constructor**: Creates a clone of an existing creature by copying its full state (`healthPoints` and `attackPower`).
- ✨ **Helper Method `healToFull()`**: Instantly restores health points to the maximum (100 HP).

### 🔍 Methods and Accessors
- 📖 **Getters**: For `name`, `healthPoints` and `attackPower`.
- ✏️ **Setter**: Only for `name` (with built-in validation).
- 📄 `toString()`: Returns an enhanced visual and textual representation of the state (e.g. `🧌['Warewolf' >> 💓 100% | ⚔️ 10]`).
- 💓 `isAlive()`: Returns `true` if `healthPoints > 0`, otherwise `false` ☠️.

### 💥 The Advanced *Clash Logic* (`clash`) 💥

#### Method `public boolean clash(Creature o)`

Represents the attack launched by the current creature (`this`) against the opposing creature (`o`).

The clash is resolved according to these rules of engagement 📜:

- 🎲 **Dynamic Damage Calculation**: A `damage` factor is computed from the difference in `attackPower`, combined with a balanced random component ranging over `[-5, 5]` (i.e. `(11 * Math.random()) - 5`).

- ⚖️ **Outcome Resolution**:
	- If the damage is **positive** 🗡️, the **opponent** loses `5` HP.
	- If the damage is **negative** 🛡️, **we** lose `5` HP.
	- If the damage is **zero** (a draw), **both** creatures take a fixed penalty of `-2` HP.
- 🔥 **Victory / Defeat Bonus**: If one of the fighters dies as a result of the clash (`!isAlive()` or `!o.isAlive()`), the survivor gets a permanent `+5` boost to its `attackPower`!

#### ⚠️ Warnings
🛡️ It is **important** to perform an **Initial Validation**, so the edge cases listed below are blocked upfront:
- Clashes can be repeated as many times as you like, as long as both creatures are still alive!
- A creature must not fight itself.
- The opponent and the creature must not be the same object!!!

If validation fails, the method returns `false`; otherwise it proceeds and returns `true`.

## 🧪 Part 2: The [**test**.`Main`](./src/test/Main.java) Class 🧪

Create the class with the main method inside the test package 📦.
- 🎬 Instantiate iconic creatures (e.g. `Warewolf` 🐺 and `Vampire` 🧛🏻).
- ⚔️ Simulate a controlled loop of repeated clashes (as long as **both are alive**).
- 📊 Print the detailed state before, during and after each fight to show how HP and AP evolve!

💡 *Happy coding, everyone, and may the best algorithm win!* 🏆⚡

***

# 📖 Quick Guide to the Solution & Code Walkthrough 🛠️

In this section we walk through the key code snippets that implement the smartest and most robust solutions of the engine.

## 1. Robust Name Handling (Ternary Operators & Strings)
In the constructor and the setter of the `Creature` class, we avoid empty or null strings thanks to compact checks based on ternary operators and Java string utility methods:

```java
public Creature(String name) {
	this.name = name != null && !name.isBlank() ? name.strip() : "(creature)";
	this.healthPoints = 100;
	this.attackPower = 10;
}
```
- `!name.isBlank()`: Checks that the string is not empty or made up only of whitespace.
- `name.strip()`: Automatically removes unwanted spaces at the start and end of the string (safer than the classic `trim()`).
- **Ternary Operator** `(? :)`: Assigns the cleaned name if it is valid, otherwise falls back to the default value `"(creature)"`.

## 2. Crash Protection & Edge Cases in the `boolean clash(Creature)` Method
The warnings in the assignment (preventing *self-clashes* and handling *dead creatures* or *null references*) are neatly handled by a single guard line at the beginning of the `clash(...)` method:

```java
public boolean clash(Creature o) {
	if (o == null || this == o || !isAlive() || !o.isAlive())
		return false;
	// ... combat logic
}
```

- `o == null`: Avoids `NullPointerException`.
- `this == o`: Strictly prevents a creature from `fighting itself`.
- `!isAlive() || !o.isAlive()`: Blocks the clash if either fighter has already passed away (HP <= 0).

If any of these conditions is true, the method returns `false` immediately.

## 3. Advanced Simulation in the [`Main`](./src/test/Main.java)
The execution block in [`Main`](./src/test/Main.java) runs a controlled loop that visually prints how the match unfolds round after round:
```java
int i = 0;
while(warewolf.isAlive() && vampire.isAlive()) {
	System.out.printf("%d. FIGHT\n%s 🆚 %s\n", i + 1, warewolf, vampire);
	System.out.printf("%s\n%s - %s\n",
		warewolf.clash(vampire) ? "💥" : "❤️‍🩹",
		warewolf, vampire
	);
	i++;
}
```
- *Loop condition*: The loop stops automatically as soon as one of the two creatures *loses its life*.
- *Ternary Operator* for feedback: Prints the explosion icon (💥) if the clash took place successfully (`true`), or a bandaged heart (❤️‍🩹) if the clash was blocked by the safety rules.

What can we say, coders...

- Put your hands on the keyboard,
- make the compiler roar,
- and may inspiration be with you!

See you at the next challenge and... *happy coding!* 🚀🔥💻

---

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

---

![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>

<!-- Italiano -->


# ⚔️ Java Dungeon Arena: *Design your 1st Creature*! 🐉

Hey Devs! 👋🔥

Benvenuti alla vostra nuovissima sfida di programmazione! 🚀💎
Oggi farete un salto epico nel mondo dei *Dungeon* 🏰 e della programmazione ad oggetti (**OOP**) 🧱.
Imparerete a dare vita a entità digitali avanzate, a gestirne lo stato in modo sicuro e a *farle scontrare in un'arena all'ultimo sangue*! 💥⚡

## 🎯 L'Obiettivo 🎯

Il vostro compito è realizzare una mini-engine di combattimento in Java ☕ composta da due classi fondamentali:
- 🧬 [**model**.`Creature`](./src/model/Creature.java): la classe modello che definisce la nostra entità di gioco potenziata.
- 🧪 [**test**.`Main`](./src/test/Main.java): la classe di test per simulare gli scontri epici! 🎬

## 🧬 Parte 1: La Classe [**model**.`Creature`](./src/model/Creature.java) 🧬

Create la classe all'interno del package model 📦 applicando i principi dell'incapsulamento 🔒 e della robustezza.

### 🛡️ Attributi (Private)
- 🏷️ `name` (String): Il nome della creatura (pulito da spazi superflui).
- 🔴 `healthPoints` (int): I punti vita (HP) della creatura (default 100).
- ⚔️ `attackPower` (int): Il valore di attacco della creatura (default 10).

### 🏗️ Costruttori ed Extra
- 🟢 **Costruttore di Default**: Non accetta parametri e sfrutta il costruttore principale impostando parametri di default.
- 🔵 **Costruttore Personalizzato**: Accetta il `name`, validandolo e impostando `healthPoints = 100` e `attackPower = 10`.
- 🧬 **Costruttore di Copia**: Permette di clonare una creatura esistente clonandone lo stato completo (`healthPoints` e `attackPower`).
- ✨ **Metodo di Supporto `healToFull()`**: Ripristina istantaneamente i punti vita al massimo (100 HP).

### 🔍 Metodi e Accessori
- 📖 **Getters**: Per `name`, `healthPoints` e `attackPower`.
- ✏️ **Setter**: Solo per `name` (con validazione integrata).
- 📄 `toString()`: Restituisce una rappresentazione visiva e testuale avanzata dello stato (es. `🧌['Warewolf' >> 💓 100% | ⚔️ 10]`).
- 💓 `isAlive()`: Restituisce `true` se `healthPoints > 0`, altrimenti `false` ☠️.

### 💥 La *Logica di Scontro* Avanzata (`clash`) 💥

#### Metodo `public boolean clash(Creature o)`

Rappresenta l'attacco sferrato dalla creatura corrente (`this`) contro la creatura avversaria (`o`).

La risoluzione dello scontro segue queste regole di ingaggio 📜:

- 🎲 **Calcolo del Danno Dinamico**: Viene calcolato un fattore di danno `damage` basato sulla differenza di `attackPower` combinato con una componente di casualità bilanciata che oscilla tra `[-5, 5]` (ovvero `(11 * Math.random()) - 5`).

- ⚖️ **Risoluzione degli Esiti**:
	- Se il danno è **positivo** 🗡️, l'**avversario** subisce la perdita di `5` HP.
	- Se il danno è **negativo** 🛡️, siamo **noi** a subire la perdita di `5` HP.
	- Se il danno è **nullo** (pareggio), **entrambi** subiscono una penalità fissa di `-2` HP.
- 🔥 **Bonus Vittoria / Sconfitta**: Se uno dei contendenti muore a seguito dello scontro (`!isAlive()` o `!o.isAlive()`), il superstite riceve un boost permanente di `+5` al proprio `attackPower`!

#### ⚠️ Avvertimenti
🛡️ È **importante** procedere con la **Validazione Iniziale**: quindi verranno bloccati preventivamente i casi limite (sotto elencati):
- È possibile effettuare/rieffettuare tutti gli scontri possibili a patto che le due creature siano ancora vive!
- Che la creatura non lotti con se stessa
- Che l'avversario e la creatura non siano la stessa cosa!!!

Se la validazione fallisce, il metodo ritorna `false`, altrimenti prosegue e ritorna `true`.

## 🧪 Parte 2: La Classe [**test**.`Main`](./src/test/Main.java) 🧪

Create la classe con il metodo main all'interno del package test 📦.
- 🎬 Istanziate creature iconiche (es. `Warewolf` 🐺 e `Vampire` 🧛🏻).
- ⚔️ Simulate un ciclo di scontri iterativi controllati (finché **entrambi sono vivi**).
- 📊 Stampate a video lo stato dettagliato prima, durante e dopo ogni combattimento per mostrare l'evoluzione dinamica di HP e AP!

💡 *Buon codice a tutti, e che il miglior algoritmo vinca!* 🏆⚡

***

# 📖 Guida Rapida allo Svolgimento & Analisi del Codice 🛠️

In questa sezione analizziamo i frammenti chiave del codice che implementano le soluzioni più ingegnose e robuste dell'engine.

## 1. Gestione Robusta dei Nomi (Operatori Ternari & Stringhe)
Nel costruttore e nel setter della classe `Creature`, evitiamo stringhe vuote o nulle grazie a controlli compatti basati su operatori ternari e metodi di utilità delle stringhe Java:

```java
public Creature(String name) {
	this.name = name != null && !name.isBlank() ? name.strip() : "(creature)";
	this.healthPoints = 100;
	this.attackPower = 10;
}
```
- `!name.isBlank()`: Controlla che la stringa non sia vuota o composta unicamente da spazi bianchi.
- `name.strip()`: Rimuove automaticamente gli spazi indesiderati all'inizio e alla fine della stringa (più sicuro del classico `trim()`).
- **Operatore Ternario** `(? :)`: Assegna il nome pulito se valido, altrimenti ripiega sul valore di fallback `"(creature)"`.

## 2. Protezione Anti-Crash & Edge Cases nel Metodo `boolean clash(Creature)`
Le avvertenze della traccia (impedire l'*auto-scontro*, gestire *creature morte* o *riferimenti nulli*) sono risolte elegantemente in un'unica riga protettiva all'inizio del metodo `clash(...)`:

```java
public boolean clash(Creature o) {
	if (o == null || this == o || !isAlive() || !o.isAlive())
		return false;
	// ... logica di combattimento
}
```

- `o == null`: Evita eccezioni di tipo NullPointerException.
- `this == o`: Impedisce categoricamente che una creatura `lotti contro se stessa`.
- `!isAlive() || !o.isAlive()`: Blocca lo scontro se uno dei due contendenti è già passato a miglior vita (HP < 0).

Se una di queste condizioni è vera, il metodo esce subito restituendo `false`.

## 3. Simulazione Avanzata nel [`Main`](./src/test/Main.java)
Il blocco di esecuzione nel [`Main`](./src/test/Main.java) gestisce un loop controllato che stampa visivamente l'andamento del match round dopo round:
```java
int i = 0;
while(warewolf.isAlive() && vampire.isAlive()) {
	System.out.printf("%d. FIGHT\n%s 🆚 %s\n", i + 1, warewolf, vampire);
	System.out.printf("%s\n%s - %s\n",
		warewolf.clash(vampire) ? "💥" : "❤️‍🩹",
		warewolf, vampire
	);
	i++;
}
```
- *Condizione del ciclo*: Il loop si interrompe automaticamente se una delle due creature *perde la vita*.
- *Operatore Ternario* di Feedback: Stampa l'icona dell'esplosione (💥) se lo scontro è avvenuto con successo (`true`), oppure un cuore bendato (❤️‍🩹) se lo scontro è stato bloccato dalle regole di sicurezza.

Che dire, coder...

- Mettete le mani sulla tastiera,
- fate ruggire il compilatore
-  e che l'ispirazione sia con voi!

Alla prossima sfida e... *happy coding!* 🚀🔥💻


<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)
[![gmail](https://img.shields.io/badge/gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:birg81@gmail.com)