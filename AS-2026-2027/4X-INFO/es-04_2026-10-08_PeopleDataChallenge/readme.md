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

# 👤 People Data Challenge 🎯

🚀 Welcome, rookie coders and future senior developers! 💻🔥 Today we're going to dig into a piece of Java code like real pros! ☕😎 Not the usual boring class from dusty textbooks, 📚😴 but a rockstar implementation of the `Person` class 🎸👤 packed with advanced goodies like `instanceof` pattern matching, 🧩 a bulletproof bitwise `switch expression` ⚡💥 and an epic `Main` that puts everything through the "Trial by Fire"! 🔥🧪 Get your keyboards ready, ⌨️ here we go! 🚀🎉

## 🏗️ 1. Anatomy of the `Person` Class (`model` Package) 📦🧬

At the heart of our app, 💓 inside the `model` package, 📂 lives our [`Person`](./src/model/Person.java) entity. 👤 To keep the data safe from careless changes, 🛡️ all the attributes are strictly `private`: 🔒

* `firstName` and `lastName` (`String`): 📝 hold the first and last name. 🏷️
* `isMale` (`boolean`): ♂️ tells us the person's sex as registered (`true` for male, `false` for female). ♀️
* `age` (`int`): 🎂 keeps track of the exact age. ⏳

### 🛡️ Constructors: Solid and Safe, with Fallbacks 🧱🛟

A good programmer never trusts user input! 🚫🙅‍♂️ That's why the constructors clean up the incoming data: 🧼✨

* **Full Constructor:** 🎯 Takes all 4 parameters and uses ternary operators to check the strings (`!isBlank()`) and block negative ages, 📉 falling back to Gennaro Esposito if anything looks wrong! 🇮🇹👨‍🦱
* **Copy Constructor:** 👥 Uses `this(...)` to hand everything over to the full constructor, after checking that the source object isn't `null`. 🛡️🔍
* **No-Args (Default) Constructor:** 🐣 Sets up the object by calling the full constructor straight away with the required default values: `new Person("Gennaro", "Esposito", true, 16)`. 👶👑

## 🧠 2. Smart Methods and Pro-Level Algorithms ⚡💡

The real magic 🪄 is in the utility methods, 🛠️ written so elegantly that even modern frameworks would be jealous! ✨🔥

| ⚙️ Method | 📝 Return Type | 🎯 What It Does | 🚀 Pro Touch |
| --- | --- | --- | --- |
| `getGender()` | `String` | Returns `"m"` or `"f"` depending on `isMale`. 🚻 | Clean, quick ternary operator. ⚡ |
| `isAdult()` | `boolean` | Checks if the age is 18 or more. 🔞 | Plain boolean logic, no pointless `if`. 🎯 |
| `getFullname()` | `String` | Joins first and last name with a space. 👥 | Uses Java's modern `.formatted()` method! 🔠 |
| `getHonorific()` | `String` | Works out the right title based on sex and age. 👑 | **Pure magic!** Uses a bitwise expression on a bit mask! 🧙‍♂️🧩 |

### 🧙‍♂️ The ninja trick behind `getHonorific()`: 🧠🔥

Want to wow your teachers and teammates? 🤩 Check out how we get the title without a messy chain of `if-else`: 📉

```java
return switch((isMale ? 2 : 0) | (isAdult() ? 1 : 0)) {
	case 0 -> "la sig.na";
	case 1 -> "la sig.ra";
	case 2 -> "il sig.ino";
	case 3 -> "il sig.";
	default -> "";
};
```

We build a bit mask by combining sex (bit 2) and adult status (bit 1)! 🧬🔬 In one shot we get an index from 0 to 3, perfect for the `switch expression`! ⚡🎯 100% computational efficiency! 🚀💯

## 🧪 3. The Trial by Fire: the `test.Main` Class 🔥🏁

To test our whole ecosystem, 🌍 the `test` package has the [`test.Main`](./src/test/Main.java) class 🚀 which works as the entry point of the application! 🚪✨

* **Multiple Instantiation:** 🏭 We create objects to test the default constructor (`gennaro`), 👶 the full constructor for adults and minors of both sexes (`tony`, `jennifer`, `wanda`), 🧑‍🤝‍🧑 the copy constructor (`tonyClone`) 🧬 and even an edge case with blank spaces and a negative age (`anonimo`) to check the safety fallbacks! 🛡️🛟
* **Polymorphism and Custom `toString()`:** 🎨 Each object is printed directly using the built-in string formatting: *"Sono il sig. Antony Edward Stark, ed ho 53 anni."* (in English: "I'm Mr. Antony Edward Stark, and I'm 53 years old.") 🎤📜
* **`equals()` Pattern Matching:** 🧩 In the `Person` class you'll also find an advanced `equals()` override that uses pattern matching (`o instanceof Person p`) to check logical equality based on the `toString()` output. 🔍🤖

🌟 So, developer? 💻🔥 Did you enjoy this trip through copy constructors, bit masks and advanced pattern matching in Java? ☕🚀 Any other questions, or do you want to dig deeper into a specific part of this code? 👇💬



---

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

---

![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>

<!-- Italiano -->

# 👤 People Data Challenge 🎯

🚀 Benvenuti, coder in erba e futuri senior developer! 💻🔥 Oggi analizzeremo insieme un pezzo di codice Java da veri professionisti! ☕😎 Non la solita classe noiosa vista nei libri polverosi, 📚😴 ma un'implementazione rockstar della classe `Person` 🎸👤 arricchita con chicche avanzate come il pattern matching di `instanceof`, 🧩 lo `switch expression` bitwise a prova di bomba ⚡💥 e una `Main` epica che fa la "Prova del Fuoco"! 🔥🧪 Preparate le tastiere, ⌨️ si parte! 🚀🎉

## 🏗️ 1. L'Anatomia della Classe `Person` (Package `model`) 📦🧬

Nel cuore della nostra applicazione, 💓 all'interno del package `model`, 📂 risiede la nostra entità [`Person`](./src/model/Person.java). 👤 Per proteggere i dati da modifiche sconsiderate, 🛡️ tutti gli attributi sono rigorosamente `private`: 🔒

* `firstName` e `lastName` (`String`): 📝 custodiscono nome e cognome. 🏷️
* `isMale` (`boolean`): ♂️ definisce il sesso biologico/anagrafico (`true` per maschio, `false` per femmina). ♀️
* `age` (`int`): 🎂 traccia l'età esatta. ⏳

### 🛡️ I Costruttori: Robustezza e Fallback 🧱🛟

Un buon programmatore non si fida mai dell'input dell'utente! 🚫🙅‍♂️ Per questo i costruttori sanitizzano i dati in ingresso: 🧼✨

* **Costruttore Completo:** 🎯 Prende i 4 parametri e usa operatori ternari per validare le stringhe (`!isBlank()`) e prevenire età negative, 📉 impostando i valori di fallback su Gennaro Esposito se qualcosa va storto! 🇮🇹👨‍🦱
* **Costruttore di Copia:** 👥 Sfrutta l'invocazione `this(...)` delegando tutto al costruttore completo dopo aver controllato che l'oggetto sorgente non sia `null`. 🛡️🔍
* **Costruttore No-Args (Default):** 🐣 Inizializza l'oggetto chiamando direttamente il costruttore completo con i valori di default richiesti: `new Person("Gennaro", "Esposito", true, 16)`. 👶👑

## 🧠 2. Metodi Smart e Algoritmi da Pro ⚡💡

La vera magia 🪄 risiede nei metodi di servizio, 🛠️ scritti con un'eleganza che fa invidia ai framework moderni! ✨🔥

| ⚙️ Metodo | 📝 Tipo di Ritorno | 🎯 Cosa fa esattamente | 🚀 Tocco Pro |
| --- | --- | --- | --- |
| `getGender()` | `String` | Restituisce `"m"` o `"f"` in base a `isMale`. 🚻 | Operatore ternario pulito e immediato. ⚡ |
| `isAdult()` | `boolean` | Verifica se l'età è maggiore o uguale a 18. 🔞 | Logica booleana diretta senza `if` inutili. 🎯 |
| `getFullname()` | `String` | Concatena nome e cognome con uno spazio. 👥 | Uso del metodo `.formatted()` moderno di Java! 🔠 |
| `getHonorific()` | `String` | Calcola l'appellativo esatto basato su sesso ed età. 👑 | **Magia pura!** Sfrutta un'espressione bitwise su bit mask! 🧙‍♂️🧩 |

### 🧙‍♂️ Il trucco ninja di `getHonorific()`: 🧠🔥

Volete stupire i vostri professori e colleghi? 🤩 Guardate come calcoliamo l'appellativo senza una sfilza di `if-else` caotici: 📉

```java
return switch((isMale ? 2 : 0) | (isAdult() ? 1 : 0)) {
	case 0 -> "la sig.na";
	case 1 -> "la sig.ra";
	case 2 -> "il sig.ino";
	case 3 -> "il sig.";
	default -> "";
};
```

Creiamo una maschera di bit combinando sesso (bit 2) ed età adulta (bit 1)! 🧬🔬 In un sol colpo otteniamo un indice da 0 a 3 perfetto per lo `switch expression`! ⚡🎯 Efficienza computazionale al 100%! 🚀💯

## 🧪 3. La Prova del Fuoco: La Classe `test.Main` 🔥🏁

Per testare tutto il nostro ecosistema, 🌍 nel package `test` troviamo la classe [`.Main`](./src/test/Main.java) 🚀 che funge da entry-point dell'applicazione! 🚪✨

* **Istanziazione Multipla:** 🏭 Creiamo oggetti testando il costruttore di default (`gennaro`), 👶 il completo per maggiorenni e minorenni di ambo i sessi (`tony`, `jennifer`, `wanda`), 🧑‍🤝‍🧑 il costruttore di copia (`tonyClone`) 🧬 e persino un caso limite con spazi bianchi e età negativa (`anonimo`) per testare i fallback di sicurezza! 🛡️🛟
* **Polimorfismo e `toString()` personalizzato:** 🎨 Ogni oggetto viene stampato direttamente usando la formattazione stringa integrata: *"Sono il sig. Antony Edward Stark, ed ho 53 anni."* 🎤📜
* **Pattern Matching `equals()`:** 🧩 Nel codice della classe `Person` trovate anche un override avanzato di `equals()` che sfrutta il pattern matching (`o instanceof Person p`) per confrontare l'uguaglianza logica basandosi sull'output del `toString()`. 🔍🤖

🌟 Allora, developer? 💻🔥 Ti è piaciuto questo viaggio tra costruttori di copia, maschere di bit e pattern matching avanzato in Java? ☕🚀 Hai qualche altra curiosità o vuoi approfondire un pezzo specifico di questo codice? 👇💬

<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)
[![gmail](https://img.shields.io/badge/gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:birg81@gmail.com)
