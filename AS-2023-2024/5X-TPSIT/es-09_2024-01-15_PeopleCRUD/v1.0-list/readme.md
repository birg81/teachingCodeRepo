[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

<a name="TOP"></a>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇬🇧](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png) <a name="EN"></a>
# 🚀 Person CRUD Management with FastAPI ⚡️🤖

Welcome to the repository for managing a list of people implemented in Python with **FastAPI** ⚡️!
This project provides you with an easy and fast way to handle a list of people through a web-based graphical interface.

### 📢 Notice

🚀 This repository represents the porting of code originally written in Java with **Spring**.
The first thing that stands out is the significant reduction in code, making it much leaner compared to the *Java* counterpart.

👀 It's interesting to note that the *frontend* part has remained virtually unchanged, while the main changes have been focused on the *backend*!

🛣️ A relevant aspect is the organization of routes.
In this example, to avoid creating an excessively long [main](./main.py) file, we chose to divide the routes.
CRUD operations related to [Person](./entity/Person.py) objects were moved directly to the [PersonRouter.py](./routers/PersonRouter.py) file.
This division is also clearly visible in Swagger, the integrated service in FastAPI, where CRUD routes are distinct from others.

🌐 In general, this organization proves to be extremely useful as projects grow in size and scalability becomes a priority. 🚀

## 📁 Project Structure

### 📋 Main Files

- [`entity/Person.py`](./entity/Person.py): The definition of the `Person` class representing an individual using PyDantic.
- [`routers/PersonRouter.py`](./routers/PersonRouter.py): Definition of server-side endpoints for CRUD operations.
- [`src/script/crudscript.js`](./static/src/script/crudscript.js): Invoking server-side operations from client-side using endpoints.
- [`root.html`](./templates/root.html): Web UI for interacting with the management system.
- [`main.py`](./main.py): The core of the application, with the FastAPI server and CRUD operations.

### 🚥 FastAPI Server (main.py)

The FastAPI server handles operations such as:

- 🌟 **Create a Person:** Add new individuals to the list.
- 📋 **Retrieve People:** Get the complete list of individuals.
- 🔍 **Retrieve a Person by ID:** Find an individual based on the specified ID.
- ✏️ **Modify a Person:** Update the details of an existing individual.
- ❌ **Remove a Person:** Delete an individual from the list.

### 🎨 User Interface (static/root.html)

The user interface makes the experience intuitive with:

- 👁️ **View List:** Display details such as name, surname, and age.
- ✏️ **Modify a Person:** Edit details directly from the page.
- ➕ **Add a Person:** Insert new individuals into the management system.
- ❌ **Remove a Person:** Delete an individual from the list.

## 🚀 Getting Started

### Run the `main.py` file:

```bash
python main.py
```

### Open the User Interface:

Visit [http://localhost:3000](http://localhost:3000) in your browser.

You can also see all the endpoints using [Swagger](http://localhost:3000/docs) and test different services administratively!

### Manage People:

Use the graphical interface to easily perform CRUD operations on individuals.

## 🌐 FastAPI Server Configuration (main.py)

The FastAPI server is configured efficiently to ensure optimal performance.
It uses `uvicorn` to start the server on port 3000.

```python
if __name__ == '__main__':
	uvicorn.run(
		'main:webapp',
		host='0.0.0.0',
		port=3000,
		reload=True
	)
```

*Enjoy the adventure with **FastAPI** and Python* ⚡️


<hr/>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a> 🤍 <a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>
# 🚀 Person CRUD Management with FastAPI ⚡️🤖

Benvenuto nel repository per la gestione di una lista di persone implementato in Python con FastAPI ⚡️!
Questo progetto ti offre un modo facile e veloce per gestire una lista di persone attraverso un'interfaccia grafica web.

### 📢 Notice

🚀 Questo repository rappresenta il porting di un codice originariamente scritto in Java con **Spring**.
La prima cosa che salta all'occhio è la notevole riduzione del codice, risultando molto più snello rispetto alla controparte in *Java*.

👀 È interessante notare che la parte di *frontend* è rimasta praticamente invariata, mentre le modifiche principali si sono concentrate nel *backend*!

🛣️ Un aspetto rilevante è l'organizzazione delle rotte.
In questo esempio, per evitare la creazione di un file [main](./main.py) eccessivamente lungo, abbiamo scelto di suddividere le rotte.
Le operazioni CRUD relative agli oggetti [Person](./entity/Person.py) sono state spostate direttamente nel file [PersonRouter.py](./routers/PersonRouter.py).
Questa suddivisione è chiaramente visibile anche in Swagger, il servizio integrato in FastAPI, dove le rotte CRUD sono distinte dalle altre.

🌐 In generale, questa organizzazione si dimostra estremamente utile quando i progetti crescono in dimensioni e si vuole garantire la scalabilità del progetto. 🚀

## 📁 Struttura del Progetto

### 📋 Files Principali

- [`entity/Person.py`](./entity/Person.py): La definizione della classe `Person` che rappresenta una persona attraverso PyDantic
- [`routers/PersonRouter.py`](./routers/PersonRouter.py): definizione degli endpoints per la gestione, server-side, delle operazioni CRUD
- [`src/script/crudscript.js`](./static/src/script/crudscript.js): per invocare, client-side, le operazioni offerte dagli endpoints del server
- [`root.html`](./templates/root.html): Web UI per interagire con il gestionale.
- [`main.py`](./main.py): Il cuore dell'applicazione, con il server FastAPI e le operazioni CRUD.

### 🚥 FastAPI Server (main.py)

Il server FastAPI gestisce operazioni come:

- 🌟 **Creazione di una Persona:** Aggiungi nuove persone alla lista.
- 📋 **Recupero delle Persone:** Ottieni l'elenco completo delle persone.
- 🔍 **Recupero di una Persona per ID:** Trova una persona in base all'ID specificato.
- ✏️ **Modifica di una Persona:** Aggiorna i dettagli di una persona esistente.
- ❌ **Rimozione di una Persona:** Elimina una persona dalla lista.

### 🎨 Interfaccia Grafica (static/root.html)

L'interfaccia utente rende l'esperienza intuitiva con:

- 👁️ **Visualizzazione della Lista:** Mostra dettagli come nome, cognome ed età.
- ✏️ **Modifica di una Persona:** Modifica i dettagli direttamente dalla pagina.
- ➕ **Aggiunta di una Persona:** Inserisci nuove persone nel gestionale.
- ❌ **Rimozione di una Persona:** Elimina una persona dalla lista.

## 🚀 Come Iniziare

### Avvia il file `main.py`:

```bash
python main.py
```

### Apri l'Interfaccia Grafica:

Visita [http://localhost:3000](http://localhost:3000) nel tuo browser.

Potrai inoltre vedere tutti gli endpoints usando [Swagger](http://localhost:3000/docs) e testando così i diversi servizi in maniera amministrativa!

### Gestisci le Persone:

Utilizza l'interfaccia grafica per eseguire facilmente operazioni CRUD sulle persone.

## 🌐 FastAPI Server Configuration (main.py)

Il server FastAPI è configurato in modo efficiente per garantire prestazioni ottimali. Utilizza `uvicorn` per avviare il server sulla porta 3000.

```python
if __name__ == '__main__':
	uvicorn.run(
		'main:webapp',
		host='0.0.0.0',
		port=3000,
		reload=True
	)
```

*Goditi l'avventura con **FastAPI** e Python*⚡️


<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)
