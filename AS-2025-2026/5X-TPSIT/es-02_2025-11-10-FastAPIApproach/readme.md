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
# 💡 Introduction to ReST and FastAPI ⚡

## 🌐 ReST: Representational State Transfer

### What is ReST? 🤔

**ReST** (*Representational State Transfer*) is an architectural style used to design web services.
Its core idea is that every resource (user, product, page, etc.) can be represented in multiple formats (JSON, HTML, XML…) and manipulated through standard operations provided by the *HTTP protocol*.

### Core Principles 🔧

* **Client–Server** 🖥️➡️🖥️ A clear separation between the system requesting data and the one providing it.
* **Stateless** ❌💾 Each request must contain all the necessary information; the server does not “remember” previous interactions.
* **Uniform Interface** 🎯 APIs should be consistent, predictable, and easy to use.
* **Cacheability** 🗂️ Responses should be cacheable to improve performance.

### Request / Response on the Web 🌍

Every interaction between a client and a server is based on two key concepts:

* **Request** 👉
	Contains:

	* HTTP method (GET, POST…)
	* URL
	* parameters
	* body
	* headers

* **Response** 👈
	Contains:

	* status code (200, 404, 500…)
	* content (HTML, JSON…)
	* headers

**FastAPI** ⚡ builds directly upon this model.

## ⚡ FastAPI: *the modern Python framework*

### What is FastAPI? 🚀

FastAPI is a high-performance Python framework for building web APIs and server-side applications.
It is designed to be:

* **fast** (powered by Starlette + Pydantic)
* **strongly typed** (leverages Python type hints)
* **self-documenting** (Swagger and Redoc out of the box)
* **async-friendly** (full support for async/await)

### Why use it? ⭐

* Extremely fast development ✨
* Clean, maintainable code thanks to type annotations 🧼
* Automatic data validation 🔍
* Auto-generated documentation 📚

## 🛠️ Installing and Setting Up the Project

In **Python** 🐍 you install external dependencies using:

```
pip install <package_name>
```

### requirements.txt 📄

When a project needs many dependencies, it’s best practice to place them inside a `requirements.txt` file.
This file works like a “shopping list,” allowing you to install everything quickly with a single command:

```bash
python -m pip install -r ./requirements.txt
```

Project dependencies:

* **uvicorn** ⚙️ → ASGI server running the app
* **fastapi** 🚀 → main framework
* **jinja2** 🖼️ → HTML template engine
* **pydantic** ✔️ → data validation
* **httptools** ⚡ → high-performance HTTP parser

### Installing via pip 📦

After activating your virtual environment (see final chapter):

```bash
python -m pip install -r requirements.txt
```

# 🧪 The Virtual Environment: Why It Matters

### What is a *virtual environment*? 🧩

A **virtual environment (venv)** is an isolated **Python** workspace with its own libraries and versions, separate from the system-wide installation.

#### 🔐 Why is it essential?

* Avoids conflicts between different projects
* Ensures consistent behavior across machines
* Makes dependency management via `requirements.txt` reliable

### Creating one (*on Windows*) 🪟

From the terminal, inside your project folder:

```
python -m venv .env
```

This generates the folder 📁 `.env`.
You may name it however you like—but keep in mind that names starting with `.` are hidden on Unix-like systems.

## Activating it (*Windows*) ⚡

Preferably from **Command Prompt**, run:

```bash
.env\Scripts\activate.bat
```

Your prompt will change, indicating activation:

```bash
(.env) C:\Users\...
```

Now you can install the dependencies:

```bash
pip install -r requirements.txt
```

To deactivate:

```bash
.env\Scripts\deactivate.bat
```

## 🧩 Code Explanation: [`main.py`](./main.py)

### Main imports 📥

* **FastAPI** → creates the web application
* **Request** → represents the HTTP request object
* **Jinja2Templates** → used to generate dynamic HTML
* **Pydantic BaseModel** → validates incoming POST data
* **Uvicorn** → runs the server

### Person model 👤

```python
class Person(BaseModel):
	firstname: str = Field(default='Turanga')
	lastname: str = Field(default='Leela')
```

Used to receive JSON data in the `/approach3` POST endpoint.

### Creating the app 🌱

```python
app = FastAPI()
```

FastAPI automatically generates documentation (Swagger), available at:
👉 [http://localhost:8000/docs](http://localhost:8000/docs)

### Configuring Jinja2 🧩

```python
templates = Jinja2Templates(directory='templates')
```

This tells FastAPI where to find your dynamic HTML pages—templates that mix standard HTML with Python expressions using the *mustache notation* (double curly braces), named so because they resemble a mustache.

In this example, the [templates](./templates/) folder contains [`greeting.html`](./templates/greeting.html), which receives *dynamic variables* at runtime.

## Analysis of the Endpoints 🔍

### 🔹 GET ['/'](http://localhost:8000/)

```python
@app.get('/', response_class = HTMLResponse)
async def greeting0(req:Request):
```

Sends fixed values to the HTML page:

* firstname = Hubert J.
* lastname = Farnsworth

✔️ A basic example to demonstrate static data rendering.

### 🔹 GET ['/approach1'](http://localhost:8000/approach1) (*query parameters*)

**URL:**
[`/approach1?firstname=Bender&lastname=Rodriguez`](http://localhost:8000/approach1?firstname=Bender&lastname=Rodriguez)

The function receives parameters through the query string:

```python
async def greeting1(firstname: str, lastname: str, req:Request):
```

✔️ Useful for GET forms and filtering.

### 🔹 GET ['/approach2/{firstname}/{lastname}'](http://localhost:8000/approach2/Philip/Fray) (*path parameters*)

**URL:**
[`/approach2/Philip/Fray`](http://localhost:8000/approach2/Philip/Fray)

✔️ Parameters are part of the path.
✔️ Ideal for hierarchical resources (e.g., `/user/15/order/3`).

### 🔹 POST ['/approach3'](http://localhost:8000/approach3) (**JSON** + **Pydantic**)

Example request:

```
POST /approach3
{
	"firstname": "Homer",
	"lastname": "Simpson"
}
```

The body is automatically validated using the **Person** model:

```python
async def greeting3(p: Person, req: Request):
```

✔️ A perfect demonstration of modern ReST APIs.
✔️ Ideal for advanced forms and AJAX calls.

## Running the App with **Uvicorn** 🚀

Normally launched from the terminal with:

```bash
uvicorn 'main:app' --http httptools --host '0.0.0.0' --port 8000 --reload
```

Since there are many options, it’s practical to include this in the [main](./main.py) file:

```python
uvicorn.run(
	'main:app',
	http ='httptools',
	host = '0.0.0.0',
	port = 8000,
	reload = True
)
```

Then you can simply run:

```bash
python main.py
```

The app is now available at: 👉 [http://localhost:8000](http://localhost:8000)

### What do these parameters mean? 🤔

Some of them are straightforward, others less so:

* `reload=True` → automatically restarts the server when files change
* `http='httptools'` → enables a high-performance HTTP parser

# 📘 Conclusion

Throughout this guide you’ve learned:

* what ReST is
* how the Request/Response model works
* what FastAPI is and why it’s powerful
* how HTML templates function
* how GET, path, and POST parameters are handled
* why a virtual environment is essential

## 🚀 Remember:

Mastering these tools means more than just learning to code—
it means *building your future, one app at a time.* 💡👨‍💻👩‍💻


---

![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>

<!-- Italian -->

# 💡 Introduzione a ReST e FastAPI ⚡

## 🌐 ReST: Representational State Transfer

### Cos’è ReST? 🤔

**ReST** (*Representational State Transfer*) è uno stile architetturale per progettare servizi web.
Si basa sull’idea che ogni risorsa (utente, prodotto, pagina, ecc.) può essere rappresentata in vari formati (JSON, HTML, XML…) e manipolata tramite operazioni standard del *protocollo **HTTP***.

### I principi fondamentali 🔧

* **Client–Server** 🖥️➡️🖥️ Separazione tra chi chiede dati e chi li fornisce.
* **Stateless** ❌💾 Ogni richiesta deve contenere tutte le informazioni necessarie, il server non “ricorda” lo stato del client.
* **Uniform Interface** 🎯 Le API devono essere intuitive e coerenti.
* **Cacheability** 🗂️ Le risposte possono essere memorizzate per migliorare le prestazioni.

### Request / Response nel web 🌍

Ogni comunicazione tra client e server avviene tramite due concetti fondamentali:

* **Request (richiesta)** 👉
  Contiene:

	* metodo HTTP (GET, POST…)
	* URL
	* parametri
	* body
	* headers

* **Response (risposta)** 👈
  Contiene:

	* codice di stato (200, 404, 500…)
	* contenuto (HTML, JSON…)
	* headers

**FastAPI** ⚡ si basa esattamente su questo sistema.

## ⚡ FastAPI: *il framework Python moderno*

### Cos’è FastAPI? 🚀

È un framework Python ad alte prestazioni per creare API web e applicazioni server-side.
È progettato per essere:

* **veloce** (basato su Starlette + Pydantic)
* **tipizzato** (usa type hints Python)
* **automatico nella documentazione** (Swagger e Redoc)
* **asynchronous-friendly** (async/await)

### Perché usarlo? ⭐

* Sviluppo rapidissimo ✨
* Codice pulito grazie alle type annotation 🧼
* Validazione automatica dei dati 🔍
* Documentazione generata automaticamente 📚

## 🛠️ Installazione e setup del progetto

In **Python** 🐍 per installare delle dipendenze esterne si usa il comando `pip install <nome_pacchetto>`.

### file requirements.txt 📄
Quando devo installare multe dipendenza è buona norma creare un file esterno, chiamato [`requirements.txt`](./requirements.txt), si comporta come una sorta di lista della spesa, al suo interno sono indicati i nomi dei pacchetti da installare in modo da poterli installare velocemente

``` bash
python -m pip install -r ./requirements.txt
```

Le dipendenze del progetto sono:

* **uvicorn** ⚙️ → server ASGI che esegue la tua app
* **fastapi** 🚀 → framework principale
* **jinja2** 🖼️ → template engine per generare HTML
* **pydantic** ✔️ → validazione dati
* **httptools** ⚡ → parser HTTP super veloce

### Installazione tramite pip 📦

Dopo aver attivato il virtual environment (vedi capitolo finale):

```bash
python -m pip install -r requirements.txt
```

# 🧪 Il Virtual Environment: perché è fondamentale

### Cos’è un ***virtual environment***? 🧩

Un **virtual environment (venv)** è un ambiente **Python** isolato, con librerie e versioni indipendenti dal sistema operativo.

#### 🔐 Perché è importante?

* Evita conflitti tra librerie di progetti diversi
* Garantisce che il progetto funzioni sempre allo stesso modo
* Permette di distribuire un requirements.txt affidabile

### Come crearlo (*sotto Windows*) 🪟

Nel terminale, nella cartella del progetto:

```
python -m venv .env
```

Verrà creata la cartella 📁 `.env`, tale cartella può essere chiamata con un nome qualsiasi, la scelta è arbitraria, ma se il nome inizia con `.` nei sistemi Unix Like sarà una cartella invisibile!

## Come attivarlo (*Windows*) ⚡

Preferibilmente da **Command prompt** avviare il comando:

```bash
.env\Scripts\activate.bat
```

Vedrai il prompt cambiare indicando l’attivazione:

```bash
(.env) C:\Users\...
```

Ora puoi installare i requirements:

```bash
pip install -r requirements.txt
```

Per disattivarlo:

```bash
.env\Scripts\deactivate.bat
```

## 🧩 Spiegazione del codice [`main.py`](./main.py)

### import principali 📥

* **FastAPI** → crea l’app
* **Request** → oggetto che rappresenta la richiesta HTTP
* **Jinja2Templates** → per generare HTML
* **Pydantic BaseModel** → per validare dati in POST
* **Uvicorn** → per avviare il server

### model Person 👤

```python
class Person(BaseModel):
	firstname: str = Field(default='Turanga')
	lastname: str = Field(default='Leela')
```

Serve per ricevere dati JSON nel POST del metodo `/approach3`.

### Creazione dell’app 🌱

```python
app = FastAPI()
```

FastAPI genera automaticamente la documentazione (Swagger) adesso visibile all'indirizzo 👉 [http://localhost:8000/docs](http://localhost:8000/docs)

### Configurazione Jinja2 🧩

```python
templates = Jinja2Templates(directory='templates')
```

Serve ad indicare la cartelle nella quale sono presenti le pagine dinamiche ovvero pagine html speciali nelle quali possiamo mischiare al codice html anche porzioni di codice Python mediante la *mustache notation*, letteralmente *notazione a baffi*, perché le porzioni di codice sono racchiuse tra parentesi graffe che ricordano per la loro forma i baffi.

Nel nostro esempio la cartella [templates](./templates/) contiene il file [`greeting.html`](./templates/greeting.html) che è di fatto un template al quale verranno passate *variabili dinamiche*.

## Analisi degli endpoint 🔍

### 🔹 GET ['/'](http://localhost:8000/)

```python
@app.get('/', response_class = HTMLResponse)
async def greeting0(req:Request):
```

Invia alla pagina HTML valori fissi:

* firstname = Hubert J.
* lastname = Farnsworth

✔️ È un esempio base per mostrare una pagina HTML con valori statici.

### 🔹 GET ['/approach1'](http://localhost:8000/approach1) (*query parameters*)

**URL**: [`/approach1?firstname=Bender&lastname=Rodriguez`](http://localhost:8000/approach1?firstname=Bender&lastname=Rodriguez)

La funzione riceve parametri tramite query string:

```python
async def greeting1(firstname: str, lastname: str, req:Request):
```

✔️ Utile per moduli GET e filtri.

### 🔹 GET ['/approach2/{firstname}/{lastname}'](http://localhost:8000/approach2/Philip/Fray) (*path parameters*)

**URL**: [`/approach2/Philip/Fray`](http://localhost:8000/approach2/Philip/Fray)

✔️ I parametri fanno parte del percorso.
✔️ Usato per risorse gerarchiche (es. /user/15/order/3).

### 🔹 POST ['/approach3'](http://localhost:8000/approach3) (***JSON*** + ***Pydantic***)

URL:

```
POST /approach3
{
  "firstname": "Homer",
  "lastname": "Simpson"
}
```

Il body viene automaticamente validato dal modello **Person**:

```python
async def greeting3(p: Person, req: Request):
```

✔️ Esempio perfetto di API ReST moderne.
✔️ Ideale per form avanzati e chiamate AJAX.

## Avvio dell’app con **Uvicorn** 🚀

Normalmente si avvia da terminale scrivendo

```bash
uvicorn 'main:app' --http httptools --host '0.0.0.0' --port 8000 --reload
```

Essendoci troppi parametri da settare, può essere opportuno includere nel file [main](./main.py) un'apposita riga di comando, la seguente:

```python
uvicorn.run(
	'main:app',
	http ='httptools',
	host = '0.0.0.0',
	port = 8000,
	reload = True
)
```

in modo che basterà scrivere da terminale semplicemente:

```bash
python main.py
```

Adesso l'App è raggiungibile su: 👉 [http://localhost:8000](http://localhost:8000)

### Cosa significano certi parametri? 🤔

Ci sono alcuni paramentri il cui significato può sembrare ovvio, altri meno.
Vediamo il significato dei seguenti:

* `reload=True` → riavvio automatico ad ogni modifica
* `http='httptools'` → usa il parser HTTP più veloce

# 📘 Conclusione

Con questo percorso hai visto:

* cos’è ReST
* come funziona il modello Request/Response
* cosa sia FastAPI e perché è potente
* come funzionano i template HTML
* come si gestiscono parametri GET, path e POST
* perché un virtual environment è indispensabile

## 🚀 Ricordate:

Padroneggiare questi strumenti non significa solo imparare a programmare, ma *imparare a costruire il vostro futuro, un’app alla volta.* 💡👨‍💻👩‍💻


<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)