[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

<a name="TOP"></a>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇬🇧](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png) <a name="EN"></A>
# Welcome to the Magical World of *(web)* APIs 🚀

🌍 Welcome to my extraordinary collection of JavaScript examples to explore APIs and fetch! Are you ready for an unparalleled digital adventure? 🌟

## Introduction 🌍

This repository is a magical gateway that will transport you to the fascinating world of APIs, fetch, and even the creation of your very own APIs!
Yes, you read that right—you can become true wizards of APIs, but always remember the famous quote:
*"With great power comes great responsibility!"* 🧙‍♂️

## Contents

Within these pages, you will find two powerful spells, or rather, two amazing examples:

### Example 1: *List of [Cartoon Characters](./characters/)* 📺

This spell will unveil the secret to creating a list of cartoon characters using JavaScript.
And the most magical part? You can view these characters with a simple touch of a dropdown menu! ✨

#### Caution!
*This spell works only within a **webserver**.*
Without it, you might encounter issues with its execution.*

### Example 2: *Worldwide [State Information](./geography/)* 🌏

In this spell, we will reveal how to use a powerful WebAPI to obtain key information about a state in the world, simply by entering its name.
Yes, it's truly magical! 🌏🌟

## Fundamental Knowledge 🤖

### Web APIs

**Application Programming Interfaces (APIs)** are like digital spells.
They are sets of rules and protocols that allow different software applications to communicate with each other over a network, such as the Internet.
APIs enable programmers to access and use specific features of an application or an external service without needing to know all the inner workings of that service. 🌐

Often, APIs are used to conjure magical information from an external server, such as user information, weather data, or knowledge about the states of the world.

### Data Exchange Formats

**XML (*Extensible Markup Language*)** and **JSON (*JavaScript Object Notation*)** are two commonly used data exchange formats in web APIs.
Both are text-based and readable by humans, but they are structured in a way that computers can easily understand.

**JSON** is the preferred format for web APIs, thanks to its extreme simplicity, readable structure, and seamless integration with JavaScript.
However, **XML** is still used in some legacy situations or when a greater level of complexity is required.

### How Does JavaScript Retrieve Information?

JavaScript can conjure this information in essentially two magical ways:

- **AJAX (*Asynchronous JavaScript and XML*)**: This is like an ancient spell that allows making asynchronous requests to a web server from a web page without reloading the entire page.
A fundamental component of AJAX is the *XMLHttpRequest* object, often abbreviated as *xhr*.
However, nowadays, the direct use of *XMLHttpRequest* has become obsolete and less common due to newer APIs and more modern approaches that simplify asynchronous communication.

- **Fetch API**: The *Fetch API* is the trendy new spell! It simplifies the handling of asynchronous HTTP requests in JavaScript.
It's like the magic of promises, making the code more readable and maintainable compared to the old XMLHttpRequest.

Here's an example of code:
```javascript
fetch('https://api.example.com/data')
	.then(response => response.json())
	.then(data => console.log(data))
	.catch(error => console.error('Oh no! A magical error occurred:', error));
```

## Wrapping Up the Magic

Now it's time!

No more explanations!

It's time to program!

Summon the APIs with your fetches, harness the magic in your code, and seek web APIs created by others to learn to control these powers.

#### Remember
*Use your knowledge for good and create code that can enchant every programmer!* 🌟🧙‍♀️


<hr/>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a> 🤍 <a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>
# Benvenuti nell'Angolo Magico delle *(web)* API 🚀

🌍 Benvenuti alla mia straordinaria collezione di esempi JavaScript per esplorare le API e il fetch! Siete pronti per un'avventura digitale senza precedenti? 🌟

## Introduzione 🌍

Questo repository è una porta magica che vi condurrà nel mondo affascinante delle API, del fetch e persino nella creazione delle vostre API personali!
Sì, avete letto bene, potrete diventare dei veri maghi delle API, ma ricordate sempre la massima:
*"Da grandi poteri, derivano grandi responsabilità!"* 🧙‍♂️

## Contenuti

Dentro queste pagine troverete due incantesimi potentissimi, ovvero due esempi strepitosi:

### Esempio 1: *Elenco dei [Personaggi dei Cartoni](./characters/)* 📺

Questo incantesimo vi svelerà il segreto per creare un elenco di personaggi dei cartoni animati utilizzando JavaScript.
E la parte più magica? Potrete visualizzare questi personaggi con un semplice tocco di un menu a tendina! ✨

#### Attenzione!
*Questo incantesimo funziona solo all'interno di un **webserver**.*
Senza di esso, potreste riscontrare problemi nella sua esecuzione.*

### Esempio 2: *Info Sugli [Stati del Mondo](./geography/)* 🌏

In questo incantesimo, vi sveleremo come utilizzare una potentissima WebAPI per ottenere informazioni principali su uno stato nel mondo, tutto semplicemente inserendo il suo nome.
Sì, è davvero magico! 🌍🌟

## Le Conoscenze di Base 🤖

### Web API

**Application Programming Interface** sono un insieme di regole e protocolli che permettono a diverse applicazioni software di comunicare tra loro tramite una rete, come Internet.
Le API consentono ai programmatori di accedere e utilizzare funzionalità specifiche di un'applicazione o di un servizio esterno senza dover conoscere tutti i dettagli interni di come funziona quel servizio. 🌐

Spesso, le API sono usate per ottenere informazioni magiche da un server esterno, come le informazioni sugli utenti, dati meteorologici o conoscenze sugli stati del mondo.

### Formati di Interscambio Dati
**XML (*Extensible Markup Language*)** e **JSON (*JavaScript Object Notation*)** sono due formati di interscambio dati comunemente utilizzati nelle API web.
Entrambi sono testuali e leggibili per gli umani, ma sono strutturati in modo da essere facilmente processati da computer.

**JSON** è il formato preferito per le API web, grazie alla sua estrema semplicità, alla sua struttura leggibile e della sua facilità di utilizzo con JavaScript.
Tuttavia, **XML** viene ancora utilizzato in alcune situazioni legacy o quando è necessaria una maggiore complessità di struttura.

### In che modo Javascript preleva le informazioni?
JavaScript può recuperare queste informazioni essenzialmente in due modi:

- **AJAX (*Asynchronous JavaScript and XML*)**, è una tecnica di programmazione che consente di effettuare richieste asincrone a un server web da una pagina web senza dover ricaricare l'intera pagina.
Un componente fondamentale di AJAX è l'oggetto *XMLHttpRequest*, spesso abbreviato in *xhr*.
Tuttavia, oggi giorno, l'uso diretto di *XMLHttpRequest* è diventato obsoleto e sempre meno comune grazie a nuove API e approcci più moderni che semplificano la comunicazione asincrona.

- **Fetch API**: L'*API fetch* è una moderna API JavaScript che semplifica la gestione delle richieste HTTP asincrone.
È più pulita e basata su promisiss, rendendo il codice più leggibile e manutenibile rispetto all'XHR.

Ecco un esempio di codice:
```javascript
fetch('https://api.example.com/data')
	.then(response => response.json())
	.then(data => console.log(data))
	.catch(error => console.error('Si è verificato un errore:', error));
```

## Concludendo la Magia

Adesso è giuto il momento!

Basta spiegazioni!

È giunto il tempo di programmare!

Richiamate a voi le API con le vostre fetch, imbrigliate la magia nel codice e cercate in rete webAPI fatte da altri e imparate a controllare questi poteri.

#### Ricordate

*Mettete la vostra conoscenza al servizio del bene e create codice capace di incantare ogni programmatore* 🌟🧙‍♀️

<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)