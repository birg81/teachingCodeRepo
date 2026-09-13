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

# 🧭 Academic Year 2022/2023

## 💾 It's not just a repository. It's the log of a journey.

This repository grew out of a deceptively simple idea: **to collect the material produced during the 2022/2023 school year**.
At first, it was mainly meant to be a dedicated space for **Python** 🐍.
Then something happened.
The project began to expand, gradually evolving into a sort of **digital computer science lab**—where code, databases, SQL, web programming, Java, APIs, and frameworks all coexist under one roof.

You won't find just executable programs here.
You'll find **problems to solve, databases to query, SQL statements to optimize, APIs to build, and architectures to navigate**. ⚙️💻
And, sprinkled throughout, a few subtle attempts to convince students that a `JOIN` isn't a particularly sophisticated form of torture. 😈

# 🗺️ The Roadmap

| 🧩 Step | 🔧 Technology / Concept | 🎯 What you'll encounter |
| --- | --- | --- |
| 🐍 **Python** | Python | Programming fundamentals & early experiments |
| 🗄️ **Database** | MySQL / MariaDB | Data modeling, tables, relationships |
| 🔎 **SQL** | SELECT, WHERE, JOIN, GROUP BY, HAVING | Turning raw data into meaningful information |
| 🧠 **Advanced Queries** | Subqueries, functions, aggregations | When a SELECT query gets down to business |
| ☕ **Java** | JDBC, Servlets, JSON | The database meets the Web |
| 🌐 **REST** | HTTP / API / JSON | The backend starts talking to the outside world |
| 🐍 **FastAPI** | Python + Web API | Tackling the same problem with a different tech stack |
| 🍃 **Spring** | Java / WebAPI / ORM | The leap into a modern enterprise framework |

That is precisely what makes the end result interesting:

> **the exact same concept can be viewed from completely different perspectives.** 🔭

# 🗄️ Chapter I — When data stops being just data

One of the first major milestones takes us straight into the world of **relational databases**.
Here, a model designed to manage **students, subjects, lessons, and exams** makes its appearance.
We start from the **E/R diagram** and trace its journey down to a concrete SQL implementation.

- 🎓 `Students`
- 📚 `Subjects`
- 📝 `Exams`
- 🕐 `Lessons`

These aren't just tables.
They are building blocks of a model that reflects real-world domain logic.
And when relationships become crucial, *she* enters the stage:

## 🔗 The JOIN

A first query retrieves information about students who have taken exams.
Then comes a second version of the exact same query.
The result is essentially identical.

**However, the way we get there changes.**

On one side, the traditional syntax:

```sql
FROM Students, Exams, Subjects
WHERE ...
```

on the other, an explicit structure built upon:

```sql
INNER JOIN
```

At this point, the repository stops being merely about *how to write a query*.
It starts asking a much more intriguing question:

> ⚡ **Are two queries that yield the exact same result necessarily equivalent in terms of performance?**

And right here, one of the fundamental truths of computer science reveals itself:
**getting the right answer isn't enough. You have to understand how you arrived at it.** 🧠

# 🧬 Chapter II — Birth of a mini digital population

Enter `PersonList5X`.
And suddenly, the database grows.
*Extensively.*

- 👤 People
- 🏙️ Cities
- 🩸 Blood types
- ♈ Zodiac signs
- 🏠 Residences
- 💼 Workplaces
- 📅 Dates
- 📱 Phone numbers
- 🧾 Tax codes / SSNs

The database no longer holds just a few dummy rows inserted to prove that a `SELECT` statement works.
It acquires a rich enough schema to allow for **real-world questions**.
And so, the challenge begins.

# ⚔️ The Saga of the CABALLEROS

Here, the repository takes on a whole new tone.
Queries turn into a **level-based progression**. 🎮
Every ten queries, you level up.

### 🥉 CABALLERO

You've conquered the first 10 queries.
By now, you're comfortable handling:

* `SELECT` 🔎
* `WHERE` 🎯
* `ORDER BY` 📐
* `LIMIT` ✂️
* `LIKE` 🔤
* `BETWEEN` ↔️
* Mathematical functions 🧮

But that was just the tutorial.

### 🥈 CABALLERO BAILANTE

Queries 11–20 hit the table.
And suddenly, the database demands more.
You'll need to work your way through:

* Provinces & Regions 🗺️
* Tax IDs / SSNs 🧾
* Dates 📅
* Birthdays 🎂
* Zodiac signs ♌
* Blood types 🩸
* Privacy constraints 🔐
* Land registry details 🏠

For instance, one query might ask you to calculate a person's **zodiac sign** directly from their date of birth.
Another challenges you to pinpoint individuals born outside the province of Naples.
Yet another requires displaying only masked portions of a surname.
SQL begins to feel less like a query language for tables and more like a **digital detective's toolkit**. 🕵️‍♂️

# ☠️ CABALLERO LOCO

Now, the game completely changes.
Queries start combining multiple relationships simultaneously.
A person can be:

- 🏡 Born in one city
- 🏠 Residing in another
- 💼 Working in a third

Which leads to a deceptively simple question:

> **Where was this person born, where do they live, and where do they work?**

Answering this requires traversing multiple tables in a single run.
And then comes the follow-up question:

> **Who has *any* connection to Castellammare?**

- Born there?
- Living there?
- Working there?
- Any single condition is enough.

The database is no longer just "looking for rows".

It's **reconstructing knowledge through relationships**. 🔗🧠

# 🎬 Chapter III — Sakila: the database becomes a world

Next enters **Sakila**.
A sample database themed around the movie industry. 🎥🍿

- Actors
- Films
- Categories
- Languages
- Addresses
- Cities
- Countries
- Inter-entity relationships
- And a long sequence of queries.

It begins innocently enough:

```text
6 + 5
```

and evolves, dozens of queries later, into questions like:

> Who are the top 5 actors who have starred in the highest number of films?

or:

> Which films have a running time longer than the average duration?

or even:

> For every film, how many actors were cast?

The difficulty curve rises steadily. 📈

- Basic selections first.
- Then sorting.
- Then filtering.
- Then aggregations.
- Then `GROUP BY`.
- Then `HAVING`.
- Then `JOIN`s.
- Then subqueries.
- And finally, queries that force you to pull together virtually everything you've learned.

# 🏆 The Caballero Leaderboard

| 🏅 Rank | 🔢 Query Count | ☠️ Scenario |
| --- | ---: | --- |
| 🗡️ **Caballero** | 10 | You've learned how to fight |
| 💃 **Caballero Bailante** | 20 | You're starting to get the hang of it |
| 🤪 **Caballero Loco** | 30 | The database is beginning to take control |
| 💀 **Caballero de la Muerte** | ~40 | You've walked through SQL hell and back |

The final stage doesn't just test your SQL syntax.

It forces you to orchestrate:

`JOIN` + `GROUP BY` + `HAVING` + `COUNT` + `AVG` + subqueries + sorting + filtering.

☠️

Repository legend has it that someone actually made it to the end.
Documentation remains silent on what happened to them afterward.

# ☕ Chapter IV — What if the database needs to talk to the Web?

At this point, a major shift occurs.

The database is no longer an isolated island.

**Java** steps into the ring. ☕

A lightweight Web application appears, querying the `sakila` database on the fly.

- The user types a film title.
- The browser dispatches a request.
- The backend catches the parameters.
- Java leverages **JDBC** to query MySQL.
- The result set is mapped into **JSON**.
- And finally, the browser dynamically renders an HTML table.

The pipeline looks like this:

```text
👤 User
	↓
🌐 Browser
	↓
📡 HTTP
	↓
☕ Java Servlet
	↓
🔌 JDBC
	↓
🗄️ MySQL
	↓
📦 JSON
	↓
🌐 Browser
```

In a compact footprint, this small project already captures a core architectural slice of modern web applications.


# ⚡ Chapter V — Same problem, different path

Here comes one of the most compelling parts of the journey.

The exact same concept is revisited using **Python**.

This time, the stage belongs to:

🐍 **FastAPI**

Movie searches now flow through a Web API.
The request takes a clean shape like:

```text
/api/{title}
```

and the server directly returns a structured JSON payload.

- Same underlying problem.
- Same database schema.
- Same core concept.
- But a completely different stack.

From:

```text
Java + Servlets + JDBC
```

To:

```text
Python + FastAPI + MySQL
```

And right here, a fundamental lesson emerges:

> 🧠 **Technologies change; the core computer science problem remains.**

A true engineer shouldn't be married to a single programming language.
They should instantly recognize the architecture of a problem, regardless of the weapon chosen to solve it. ⚔️


# 🍃 Chapter VI — Enter Spring

Just when it seems the journey has reached its conclusion...

**Spring** arrives.

And the repository unlocks yet another door.

- WebAPI
- JSON
- Backend engineering
- REST
- ORMs
- Database abstraction
- API Testing
- Postman

This time, the goal goes beyond writing a couple of servlets or building a quick API endpoint.
We step firmly into **framework territory**.
The application scales.
Responsibilities are cleanly separated.
The database layer is handled via an ORM.
The backend exposes clean RESTful APIs.
The client becomes completely decoupled from the server.
Once again, the architectural view evolves:

```text
Application
	│
	├── 🌐 REST API
	│
	├── 🧠 Business Logic
	│
	├── 🗃️ ORM Layer
	│
	└── 💾 Database
```

This is where simple classroom exercises start looking like systems you'd encounter in real-world enterprise software.

# 🔬 Not just a collection of solutions

This repository shouldn't be read simply as:

> "Here are the exercises that were completed."

It's far more interesting to view it as a **snapshot of a learning path**.

A timeline where you can clearly trace the evolution:

```text
🐍 Programming Fundamentals
		↓
🗄️ Data Modeling
		↓
🔎 SQL
		↓
🔗 Relational Mapping
		↓
🧠 Complex Querying
		↓
☕ Java
		↓
📡 WebAPIs
		↓
📦 JSON
		↓
🐍 FastAPI
		↓
🍃 Spring
		↓
🏗️ Web Architectures
```

Each step introduces a new layer of abstraction.
Each layer hides lower-level mechanics while unlocking new capabilities.
And above all, every single technology brings a fresh set of questions.

# 🧪 A laboratory, not a museum

The code in these folders isn't guaranteed to be flawless.
And that's precisely what makes it valuable. 🔍
- You'll find experiments.
- Architectural design choices.
- Different iterations of the same concept.
- Basic queries alongside "PRO" solutions.
- Trial and error.
- Solutions & bug fixes.
- Fine details left to refine.
- Continuous evolutions.

Because an educational repository shouldn't be an untouchable museum of code.

It should be a **laboratory**.

A playground where code can be opened up, executed, broken, debugged, refactored, and ultimately understood. 🧪💻

# 🚀 So... what's actually inside?

A bit of everything.
But above all, a driving mindset:

### starting from a single line of code and growing to understand the whole system. 🌐

- A database isn't just a table.
- A query isn't just an SQL string.
- An API isn't just an endpoint.
- A framework isn't just a library.
- And a program isn't just something that happens to "work".
- Behind every snippet of code lies a problem.
- Behind every problem lies a model.
- And behind every model, there's someone who had to figure out **how to translate an idea into something a machine could execute**. ⚙️

# 🧭 Last stop?

*Probably not.*

Because this repository is, above all, about **the start of a mindset**.

Inside, you can follow the path that leads:

**from data to information,
from information to models,
from models to code,
from code to services,
from services to full applications.**

And all of this started with a simple thought:

> **"Let's drop some Python code in here."** 🐍

- A small idea.
- A repository.
- A school year.

And tucked away between `SELECT`s, `JOIN`s, `Servlet`s, `JDBC`, `FastAPI`, JSON, and Spring...

*a fair amount of real computer science.* 💻🔥

## 👀 Enough reading for now.

The main spoiler has already been dropped.

*The code is right there.*

Queries are waiting to be run.
Databases are waiting to be explored.
APIs are waiting for requests.
And a few `JOIN`s, somewhere down the folder tree, are still looking for someone brave enough to write them. 😈🔗

### 🚪 Open the folders.

*The journey begins right at the very first line of code.*

---

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

---

![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>

<!-- Italiano -->

# 🧭 AS 2022/2023

## 💾 Non è soltanto un repository. È la traccia di un viaggio.

Questo repository nasce da un'idea apparentemente semplice: **raccogliere il materiale prodotto durante l'anno scolastico 2022/2023**.
All'inizio doveva essere soprattutto un luogo dedicato a **Python** 🐍.
Poi è successo qualcosa.
Il progetto ha cominciato ad allargarsi, fino a trasformarsi in una sorta di **laboratorio digitale dell'informatica**, dove codice, database, SQL, programmazione Web, Java, API e framework convivono nello stesso spazio.

Non troverete quindi soltanto programmi da eseguire.
Troverete **problemi da risolvere, database da interrogare, query da ottimizzare, API da costruire e architetture da attraversare**. ⚙️💻
E, qua e là, anche qualche tentativo di convincere lo studente che una `JOIN` non sia una forma particolarmente sofisticata di tortura. 😈

# 🗺️ La mappa del viaggio

| 🧩 Tappa | 🔧 Tecnologia / concetto | 🎯 Cosa si incontra |
| --- | --- | --- |
| 🐍 **Python** | Python | Programmazione e primi esperimenti |
| 🗄️ **Database** | MySQL / MariaDB | Modellazione, tabelle, relazioni |
| 🔎 **SQL** | SELECT, WHERE, JOIN, GROUP BY, HAVING | Dati trasformati in informazioni |
| 🧠 **Query avanzate** | Subquery, funzioni, aggregazioni | Quando una SELECT comincia a diventare seria |
| ☕ **Java** | JDBC, Servlet, JSON | Il database incontra il Web |
| 🌐 **REST** | HTTP / API / JSON | Il backend comincia a parlare con il mondo |
| 🐍 **FastAPI** | Python + Web API | Lo stesso problema affrontato con un'altra tecnologia |
| 🍃 **Spring** | Java / WebAPI / ORM | Il salto verso un framework moderno |

Il risultato è interessante proprio per questo motivo:

> **lo stesso concetto può essere osservato da prospettive differenti.** 🔭

# 🗄️ Capitolo I — Quando i dati smettono di essere semplici dati

Una delle prime grandi tappe porta direttamente nel mondo dei **database relazionali**.
Qui compare un modello dedicato alla gestione di **studenti, materie, lezioni ed esami**.
Si parte dall'idea dello schema **E/R** e si arriva alla sua traduzione concreta in SQL.

-  🎓 `Students`
- 📚 `Subjects`
- 📝 `Exams`
- 🕐 `Lessons`

Non sono semplicemente tabelle.
Sono pezzi di un modello che descrive una realtà.
E quando le relazioni diventano importanti, arriva lei:

## 🔗 La JOIN

Una prima interrogazione permette di ottenere informazioni sugli studenti che hanno sostenuto esami.
Poi arriva una seconda versione della stessa interrogazione.
Il risultato è sostanzialmente lo stesso.

**Il modo di arrivarci, però, cambia.**

Da una parte la sintassi tradizionale:

```sql
FROM Students, Exams, Subjects
WHERE ...
```

dall'altra una struttura esplicita basata su:

```sql
INNER JOIN
```

E qui il repository smette di limitarsi a insegnare *come scrivere una query*.
Comincia a porre una domanda molto più interessante:

> ⚡ **Due query che producono lo stesso risultato sono necessariamente equivalenti anche dal punto di vista delle prestazioni?**

Ed è proprio qui che compare una delle idee più importanti dell'informatica:
**non basta ottenere il risultato. Bisogna capire come lo si ottiene.** 🧠

# 🧬 Capitolo II — Nasce una piccola popolazione digitale

Poi arriva `PersonList5X`.
E improvvisamente il database cresce.
Molto.

- 👤 Persone
- 🏙️ Città
- 🩸 Gruppi sanguigni
- ♈ Segni zodiacali
- 🏠 Residenze
- 💼 Luoghi di lavoro
- 📅 Date
- 📱 Numeri di telefono
- 🧾 Codici fiscali

Il database non contiene più soltanto qualche riga inserita per dimostrare che una `SELECT` funziona.
Comincia ad avere una struttura sufficientemente ricca da permettere **domande vere**.
E quindi parte la sfida.

# ⚔️ La saga dei CABALLEROS

Qui il repository cambia completamente tono.
Le query diventano una **progressione a livelli**. 🎮
Ogni dieci interrogazioni si sale di grado.

### 🥉 CABALLERO

Hai superato le prime 10 query.
A questo punto sai già muoverti tra:

* `SELECT` 🔎
* `WHERE` 🎯
* `ORDER BY` 📐
* `LIMIT` ✂️
* `LIKE` 🔤
* `BETWEEN` ↔️
* funzioni matematiche 🧮

Ma era soltanto il tutorial.

### 🥈 CABALLERO BAILANTE

Arrivano le query 11–20.
E improvvisamente il database comincia a pretendere qualcosa in più.
Bisogna ragionare su:

* province 🗺️
* codici fiscali 🧾
* date 📅
* compleanni 🎂
* segni zodiacali ♌
* gruppi sanguigni 🩸
* privacy 🔐
* informazioni catastali 🏠

Una query, per esempio, può chiedere di ricostruire il **segno zodiacale** di una persona partendo dalla sua data di nascita.
Un'altra deve individuare persone nate fuori dalla provincia di Napoli.
Un'altra ancora deve visualizzare soltanto una parte del cognome.
SQL comincia a sembrare meno un linguaggio per interrogare tabelle e più un piccolo **linguaggio investigativo**. 🕵️‍♂️

# ☠️ CABALLERO LOCO

A questo punto il gioco cambia.
Le query iniziano a mettere insieme più relazioni.
Una persona può essere:

- 🏡 nata in una città
- 🏠 residente in un'altra
- 💼 lavorare in una terza.

E quindi nasce una domanda apparentemente semplice:

> **Dove è nata, dove vive e dove lavora questa persona?**

La risposta richiede di attraversare più tabelle contemporaneamente.
E poi arriva la domanda successiva:

> **Chi ha qualcosa a che fare con Castellammare?**

- Nato lì?
- Ci vive?
- Ci lavora?
- Basta una di queste condizioni.

Il database, a questo punto, non sta più semplicemente "cercando righe".

Sta **ricostruendo informazioni attraverso relazioni**. 🔗🧠

# 🎬 Capitolo III — Sakila: il database diventa un mondo

Poi entra in scena **Sakila**.
Un database didattico costruito attorno al mondo del cinema. 🎥🍿

- Attori.
- Film.
- Categorie.
- Lingue.
- Indirizzi.
- Città.
- Paesi.
- Relazioni tra entità.
- E una lunga sequenza di interrogazioni.

Si parte quasi innocenti:

```text
6 + 5
```

e si arriva, parecchie query più tardi, a domande come:

> Quali sono i 5 attori che hanno partecipato al maggior numero di film?

oppure:

> Quali film hanno una durata superiore alla durata media?

oppure ancora:

> Per ogni film, quanti attori hanno partecipato?

La difficoltà cresce gradualmente. 📈

- Prima le semplici selezioni.
- Poi gli ordinamenti.
- Poi i filtri.
- Poi le aggregazioni.
- Poi `GROUP BY`.
- Poi `HAVING`.
- Poi le `JOIN`.
- Poi le subquery.
- E infine le query che costringono a mettere insieme praticamente tutto ciò che si è imparato.

# 🏆 La classifica dei Caballeros

| 🏅 Grado | 🔢 Query | ☠️ Situazione |
| --- | ---: | --- |
| 🗡️ **Caballero** | 10 | Hai imparato a combattere |
| 💃 **Caballero Bailante** | 20 | Cominci a prendere gusto |
| 🤪 **Caballero Loco** |30 | Il database comincia a prendere il controllo |
| 💀 **Caballero de la Muerte** | 40 circa | Hai attraversato l'inferno delle query |

L'ultima tappa non si limita a verificare la conoscenza di SQL.

Costringe a combinare:

`JOIN` + `GROUP BY` + `HAVING` + `COUNT` + `AVG` + subquery + ordinamenti + filtri.

☠️

La leggenda del repository racconta che qualcuno sia arrivato fino alla fine.
La documentazione non chiarisce cosa sia successo dopo.

# ☕ Capitolo IV — E se il database dovesse parlare con il Web?

A questo punto succede qualcosa di importante.

Il database non è più isolato.

Entra in gioco **Java**. ☕

Compare una piccola applicazione Web che interroga il database `sakila`.

- L'utente scrive il titolo di un film.
- Il browser invia una richiesta.
- Il backend riceve il parametro.
- Java utilizza **JDBC** per interrogare MySQL.
- Il risultato viene trasformato in **JSON**.
- E infine il browser costruisce dinamicamente una tabella HTML.

La catena diventa:

```text
👤 Utente
	↓
🌐 Browser
	↓
📡 HTTP
	↓
☕ Servlet Java
	↓
🔌 JDBC
	↓
🗄️ MySQL
	↓
📦 JSON
	↓
🌐 Browser
```

Questo piccolo progetto contiene già, in forma compatta, una parte significativa dell'architettura di una moderna applicazione Web.

# ⚡ Capitolo V — Lo stesso problema, un'altra strada

Ed ecco una delle parti più interessanti.

Lo stesso concetto viene riproposto in **Python**.

Questa volta entra in scena:

🐍 **FastAPI**

La ricerca dei film passa attraverso una Web API.
La richiesta diventa qualcosa del tipo:

```text
/api/{title}
```

e il server restituisce direttamente una struttura JSON.

- Il problema è lo stesso.
- Il database è lo stesso.
- L'idea è la stessa.
- Ma cambia lo strumento.

Da:

```text
Java + Servlet + JDBC
```

a:

```text
Python + FastAPI + MySQL
```

Ed è proprio qui che emerge una lezione fondamentale:

> 🧠 **la tecnologia cambia; il problema informatico rimane.**

Chi conosce davvero l'informatica non dovrebbe essere legato a un solo linguaggio.
Dovrebbe saper riconoscere la struttura del problema, indipendentemente dall'arma utilizzata per affrontarlo. ⚔️

# 🍃 Capitolo VI — E poi arriva Spring

Quando ormai sembra che il viaggio sia terminato...

compare **Spring**.

E il repository apre un'altra porta.

- WebAPI.
- JSON.
- Backend.
- REST.
- ORM.
- Database.
- Testing delle API.
- Postman.

Questa volta l'obiettivo non è più semplicemente scrivere qualche servlet o costruire una piccola API.
Si comincia a entrare nel territorio dei **framework**.
L'applicazione cresce.
Le responsabilità possono essere separate.
Il database può essere raggiunto attraverso un livello ORM.
Il backend può esporre API REST.
Il client può essere completamente indipendente dal server.
La prospettiva cambia ancora una volta:

```text
Applicazione
	│
	├── 🌐 API REST
	│
	├── 🧠 Logica applicativa
	│
	├── 🗃️ ORM
	│
	└── 💾 Database
```

Ed è qui che il semplice esercizio scolastico comincia ad assomigliare a qualcosa che potremmo incontrare in un vero progetto software.

# 🔬 Non è una collezione di soluzioni

Questo repository non va letto soltanto come:

> "Ecco gli esercizi che sono stati svolti."

È più interessante leggerlo come una **fotografia del percorso**.

Una fotografia nella quale si può vedere l'evoluzione:

```text
🐍 Programmazione
		↓
🗄️ Modellazione dei dati
		↓
🔎 SQL
		↓
🔗 Relazioni
		↓
🧠 Query complesse
		↓
☕ Java
		↓
📡 WebAPI
		↓
📦 JSON
		↓
🐍 FastAPI
		↓
🍃 Spring
		↓
🏗️ Architetture Web
```

Ogni passaggio aggiunge un livello di astrazione.
Ogni livello nasconde qualcosa e ne rivela un'altra.
E soprattutto, ogni tecnologia porta con sé una domanda nuova.

# 🧪 Un laboratorio, non un museo

Il codice presente nelle cartelle non è necessariamente perfetto.
Ed è proprio questo uno degli aspetti più interessanti. 🔍
- Ci sono esperimenti.
- Scelte progettuali.
- Versioni differenti dello stesso concetto.
- Query semplici e query "PRO".
- Tentativi.
- Soluzioni.
- Piccoli dettagli da correggere.
- Evoluzioni.

Perché un repository didattico non dovrebbe essere un museo di codice intoccabile.

Dovrebbe essere un **laboratorio**.

Un luogo nel quale il codice può essere aperto, eseguito, modificato, rotto, corretto e infine capito. 🧪💻


# 🚀 E quindi... cosa c'è davvero qui dentro?

C'è un po' di tutto.
Ma soprattutto c'è un'idea:

### partire da una riga di codice e arrivare a vedere l'intero sistema. 🌐

- Un database non è soltanto una tabella.
- Una query non è soltanto una stringa SQL.
- Un'API non è soltanto un endpoint.
- Un framework non è soltanto una libreria.
- E un programma non è soltanto qualcosa che "funziona".
- Dietro ogni pezzo di codice c'è un problema.
- Dietro ogni problema c'è un modello.
- E dietro ogni modello c'è qualcuno che ha dovuto capire **come trasformare un'idea in qualcosa che una macchina potesse eseguire**. ⚙️

# 🧭 Ultima fermata?

*Probabilmente no.*

Perché questo repository racconta soprattutto **l'inizio di un modo di pensare**.

Qui dentro si può seguire il percorso che porta:

**dal dato all'informazione,
dall'informazione al modello,
dal modello al codice,
dal codice al servizio,
dal servizio all'applicazione.**

E tutto questo partendo da una semplice idea:

> **"Mettiamo qui dentro un po' di codice Python."** 🐍

- Una piccola idea.
- Un repository.
- Un anno scolastico.

E, nascosta tra `SELECT`, `JOIN`, `Servlet`, `JDBC`, `FastAPI`, JSON e Spring...

*una discreta quantità di informatica.* 💻🔥


## 👀 Adesso però basta leggere.

Perché il vero spoiler è già stato dato.

*Il codice è lì.*

Le query aspettano di essere interrogate.
I database aspettano di essere esplorati.
Le API aspettano una richiesta.
E qualche `JOIN`, da qualche parte, sta ancora cercando qualcuno abbastanza coraggioso da scriverla. 😈🔗

### 🚪 Apri le cartelle.

*Il viaggio comincia esattamente dalla prima riga di codice.*

<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)
[![gmail](https://img.shields.io/badge/gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:birg81@gmail.com)