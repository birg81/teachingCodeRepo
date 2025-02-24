[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

<a name="TOP"></a>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇬🇧](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png) <a name="EN"></A>
# 📖 People List Manager 🚀

## 🎯 Introduction

Welcome to the **People List Manager** repository! 🎉
This project leverages [**FastAPI ⚡**](https://fastapi.tiangolo.com/) and [**SQLModel 🗄️**](https://github.com/tiangolo/sqlmodel) to create a REST API for managing a list of people with full CRUD (Create, Read, Update, Delete) operations. 🏆

Designed to be **clear**, **scalable**, and **efficient**, this project is perfect for learning the fundamentals of modern web development with [**Python 🐍**](https://en.wikipedia.org/wiki/Python_(programming_language)) and relational databases 🛢️, specifically [**MySQL 🐬**](https://www.mysql.com)/[**MariaDB 🦭**](https://mariadb.org). 🔥

## 📂 Project Structure

* 📁 Root
	- 📜 [`main.py`](./main.py) - Application entry point 🏁
	- 📜 [`requirements.txt`](./requirements.txt) - List of dependencies 📦

* 📁 db/
	- 📜 [`connection.py`](./db/connection.py) - Database connection management 🛢️

* 📁 model/
	- 📜 [`Person.py`](./model/Person.py) - Defines the **Person** table using [**SQLModel 🗄️**](https://github.com/tiangolo/sqlmodel) 👤

* 📁 router/
	- 📜 [`peopleRouter.py`](./router/peopleRouter.py) - API endpoints for managing people 🔄

## What is [**FastAPI ⚡**](https://fastapi.tiangolo.com/)?

[**FastAPI ⚡**](https://fastapi.tiangolo.com/) is a modern and high-performance framework for building RESTful APIs with Python. 🎯
Here are some of its key features:

* ✅ **Blazing fast** 🚀 thanks to Starlette and Pydantic 🔥
* ✅ **Automatic OpenAPI and Swagger UI** integration 📜
* ✅ Easy-to-use **Python type annotations** 📝
* ✅ Ideal for **asynchronous applications** with `async` and `await` ⚡

## 🛠️ Project Setup

### 🔧 Creating the Virtual Environment
To keep dependencies isolated, create a virtual environment:

```bash
python -m venv .<YOUR-VIRTUAL-ENV>
```

Activate it with:

- **Windows** 🖥️:

```bash
.<YOUR-VIRTUAL-ENV>\Scripts\activate.bat
```

- **Linux/macOS** 🐧🍏:

```bash
source .<YOUR-VIRTUAL-ENV>/bin/activate
```

### 📦 Installing Dependencies

```bash
python -m pip install -r requirements.txt
```

This command installs [**FastAPI ⚡**](https://fastapi.tiangolo.com/), [**SQLModel 🗄️**](https://github.com/tiangolo/sqlmodel), `pymysql` (the driver for connecting to [**MySQL 🐬**](https://www.mysql.com)/[**MariaDB 🦭**](https://mariadb.org)), and other necessary libraries. 📜

## 🏗️ Database & ORM with SQLModel

An **ORM (Object-Relational Mapping)** allows interaction with the database using Python classes instead of writing raw SQL queries. 🎯

🚀 [**SQLModel 🗄️**](https://github.com/tiangolo/sqlmodel) combines **SQLAlchemy** ⚗️ (database management) and **Pydantic** 🛡️ (data validation), offering:
- Automatic table creation 📄
- Advanced data validation ✅
- Seamless integration with FastAPI ⚡

### 📌 Defining the `Person` Model 👤

The [`Person.py`](./model/Person.py) file defines the `People` table. It is essentially a class without explicit methods, only field definitions.

* ✅ `Field` sets constraints (e.g., min length, valid values) 🔍
* ✅ `table = True` marks the class as a database table 🏛️

The `Field` constructor allows setting default values, defining nullable attributes, enforcing simple checks, and specifying primary keys.

## 🚀 Running the Application

Once everything is set up, launch the project with:

```bash
python main.py
```

Or manually using `uvicorn`:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --http=httptools --reload
```

The app will be available at: 🌐 [http://127.0.0.1:8000](http://127.0.0.1:8000)

* ✅ **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 📝
* ✅ **OpenAPI JSON**: [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json) 📜

## 🌟 API CRUD - Endpoints

CRUD operations are handled in [`peopleRouter.py`](./router/peopleRouter.py):

| Method | Endpoint | Description |
|--------|---------------|----------------------------|
| GET | `/api/person/` | Retrieve all people 👤 |
| GET | `/api/person/{id}` | Retrieve a person by ID 🔍 |
| POST | `/api/person/` | Add a new person ➕ |
| PUT | `/api/person/{id}` | Update a person ✏️ |
| DELETE | `/api/person/{id}` | Delete a person ❌ |

## 🔥 Conclusion

*Awesome*! 🎉
You now have a fully functional, **fast**, and **scalable** REST API built with [**FastAPI ⚡**](https://fastapi.tiangolo.com/) and [**SQLModel 🗄️**](https://github.com/tiangolo/sqlmodel)! 💪🚀

If you have any questions, feel free to contribute or open an issue! 🚀

*Happy coding*! 💻🔥

<hr/>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a> 🤍 <a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>
# 📖 People List Manager 🚀

## 🎯 Introduzione

Benvenuto nel repository **People List Manager**! 🎉
Questo progetto utilizza [**FastAPI ⚡**](https://fastapi.tiangolo.com/) e [**SQLModel 🗄️**](https://github.com/tiangolo/sqlmodel) per creare una REST API che gestisce una lista di persone con operazioni CRUD (Create, Read, Update, Delete). 🏆

Questo progetto è strutturato per essere **chiaro**, **scalabile** e **performante**, perfetto per imparare i concetti fondamentali dello sviluppo web moderno con [**Python 🐍**](https://it.wikipedia.org/wiki/Python) e database relazionali🛢️, nello specifico [**MySQL 🐬**](https://www.mysql.com)/[**MariaDB 🦭**](https://mariadb.org). 🔥

## 📂 Struttura del Progetto

* 📁 Root
	- 📜 [`main.py`](./main.py) - Punto di ingresso dell'applicazione 🏁
	- 📜 [`requirements.txt`](./requirements.txt) - Elenco delle dipendenze 📦

* 📁 db/
	- 📜 [`connection.py`](./db/connection.py) - Gestione della connessione al database 🛢️

* 📁 model/
	- 📜 [`Person.py`](./model/Person.py) - Definizione della tabella **Person** con [**SQLModel 🗄️**](https://github.com/tiangolo/sqlmodel) 👤

* 📁 router/
	- 📜 [`peopleRouter.py`](./router/peopleRouter.py) - Definizione delle API per la gestione delle persone 🔄


## Cos'è [**FastAPI ⚡**](https://fastapi.tiangolo.com/)?

[**FastAPI ⚡**](https://fastapi.tiangolo.com/) è un framework moderno e performante per la creazione di API RESTful con Python. 🎯
Ecco alcune delle sue caratteristiche principali:

* ✅ Estremamente **veloce** 🚀 grazie a Starlette e Pydantic 🔥
* ✅ Supporta **OpenAPI e Swagger UI** automaticamente 📜
* ✅ Semplice da usare con **annotazioni di tipo Python** 📝
* ✅ Perfetto per applicazioni **asincrone** con `async` e `await` ⚡


## 🛠️ Configurazione del Progetto

### 🔧 Creazione dell'Ambiente Virtuale
Per gestire le dipendenze del progetto in modo isolato, creiamo un ambiente virtuale:

```bash
python -m venv .<YOUR-VIRTUAL-ENV>
```

Attiviamolo con:

- **Windows** 🖥️:

```bash
.<YOUR-VIRTUAL-ENV>\Scripts\activate.bat
```

- **Linux/macOS** 🐧🍏:

```bash
source .<YOUR-VIRTUAL-ENV>/bin/activate
```

### 📦 Installazione delle Dipendenze

```bash
python -m pip install -r requirements.txt
```

Questo comando installerà [**FastAPI ⚡**](https://fastapi.tiangolo.com/), [**SQLModel 🗄️**](https://github.com/tiangolo/sqlmodel), pymysql (driver per connettersi al R-DBMS [**MySQL 🐬**](https://www.mysql.com)/[**MariaDB 🦭**](https://mariadb.org)) e altre *librerie necessarie*. 📜


## 🏗️ Database & ORM con SQLModel

Un **ORM (Object-Relational Mapping)** è una tecnica che permette di **interagire con il database** utilizzando classi Python anziché scrivere query SQL manualmente. 🎯

🚀 [**SQLModel 🗄️**](https://github.com/tiangolo/sqlmodel) è una fusione tra **SQLAlchemy** ⚗️ (gestione del database) e **Pydantic** 🛡️ (validazione dei dati), offrendo:
	- Creazione automatica delle tabelle 📄
	- Validazione avanzata dei dati ✅
	- Interoperabilità con FastAPI ⚡

### 📌 Definizione del Modello `Person` 👤

Il file [`Person.py`](./model/Person.py) definisce la tabella `People`, in pratica è una classe nella quale non è in generale definito alcun metodo ma solo i campi.

* ✅ `Field` specifica vincoli sui dati (es. lunghezza minima, valori accettabili) 🔍
* ✅ `table = True` indica che questa classe rappresenta una tabella nel database 🏛️

Field è uno speciale costruttore che permette di impostare valori predefiniti per i campi, indicare se nello schema sql il campo può o meno essere nullo e definire dei semplici check; infine permette di indicare se un attributo è o meno una `PRIMARY KEY`

## 🚀 Avvio dell'Applicazione

Una volta configurato tutto, possiamo eseguire il progetto con:

```bash
python main.py
```

Oppure, usando manualmente `uvicorn`:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --http=httptools --reload
```

L'app sarà disponibile su: 🌐 [http://127.0.0.1:8000](http://127.0.0.1:8000)

* ✅ **Swagger UI** sarà accessibile su: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 📝
* ✅ **OpenAPI JSON** sarà su: [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json) 📜


## 🌟 API CRUD - Endpoints

Le operazioni CRUD sono gestite in [`peopleRouter.py`](./router/peopleRouter.py):

|	Metodo	|	Endpoint	|	Descrizione	|
|--------|---------------|----------------------------|
|	GET	|	`/api/person/`	|	Recupera tutte le persone 👤	|
|	GET	|	`/api/person/{id}`	|	Recupera una persona per ID 🔍	|
|	POST	|	`/api/person/`	|	Aggiunge una nuova persona ➕	|
|	PUT	|	`/api/person/{id}`	|	Modifica una persona ✏️	|
|	DELETE	|	`/api/person/{id}`	|	Cancella una persona ❌	|

## 🔥 Conclusione

*Fantastico*! 🎉
Hai ora un'API REST **completa**, **performante** e **scalabile** con [**FastAPI ⚡**](https://fastapi.tiangolo.com/) e [**SQLModel 🗄️**](https://github.com/tiangolo/sqlmodel)! 💪🚀

Se hai domande, sentiti libero di contribuire o aprire una issue! 🚀

*Buon coding*! 💻🔥

<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)