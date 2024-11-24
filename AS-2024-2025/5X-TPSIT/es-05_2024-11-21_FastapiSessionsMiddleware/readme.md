[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

<a name="TOP"></a>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇬🇧](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png) <a name="EN"></A>
# 📖 Web App 🌍 with FastAPI ⚡ and Sessions ✨

Welcome to the **Session Management with FastAPI** project! 🚀 This guide will take you through the essentials of Python programming 🐍, using the FastAPI web framework ⚡, and implementing sessions 🛠️ to manage persistent data across HTTP requests.

---

## 🌟 Introduction to Python Programming 🐍
Python is one of the most popular programming languages in the world 🌍, known for its simplicity and versatility.
It's perfect for developing web applications, data science, machine learning, and much more! 🧠
In this project, Python serves as the backbone for building a modern and dynamic web app.

### Key Features of Python:
- Readability 📖
- A rich ecosystem of libraries 🔧
- A vibrant and supportive community 🤝

---

## ⚡ What is FastAPI? ✨
**FastAPI** ⚡ is a modern, high-performance web framework designed to create APIs 🚀.
Its simplicity and powerful features make it an excellent choice for both beginners and experienced developers.

### ✅ Why Choose FastAPI? ⚡
- Blazing-fast performance 🚀
- Automatically generated API documentation 📚
- Full integration with Python's type hints 🛠️

---

## 🛠️ Sessions in FastAPI
Sessions enable storing user-specific data that persists across their interactions with the app 🌐.
In our project, sessions are used to track how many times a user reloads the page.

**Technology used:** `starlette.middleware.sessions` 🧩

---

## 🐾 Step-by-Step Guide 📑

### 🏗️ Setting Up a Virtual Environment
A **Virtual Environment (venv)** isolates the project's dependencies to avoid conflicts with other projects.

Follow these simple steps:

1. **Create a Virtual Environment**:
Run the following command in the terminal (**CLI** ⌨️):
```bash
python -m venv <your_venv_name>
```

2. **Activate the Virtual Environment**:
Depending on your operating system, use one of the following commands:

- On 🪟 Windows (**command prompt** 🔳):
	```bash
	.\<your_venv_name>\Scripts\activate.bat
	```
	Or for (**PowerShell** 🟦):
	```bash
	.\<your_venv_name>\Scripts\activate.ps1
	```

- On 🍏 Mac / 🐧 Linux:
	```bash
	source <your_venv_name>/bin/activate
	```

3. **Install the Dependencies**:
To streamline dependency management, the required packages are listed in a [`requirements.txt`](./requirements.txt) file. Install them all at once with:
```bash
python -m pip install -r requirements.txt
```

4. **Start the Web App**:
Simply run:
```bash
python main.py
```

5. **Test Your Web App**:
Open your browser and navigate to [http://localhost](http://localhost/) to see your app in action! 🌟

---

### 📜 Required Dependencies
- [`httptools`](https://pypi.org/project/httptools/): Handles connections from other hosts on the network.
- [`uvicorn`](https://pypi.org/project/uvicorn/): A fast Python web server.
- [`fastapi`](https://pypi.org/project/fastapi/): A framework for building RESTful APIs.
- [`fastapi-sessions`](https://pypi.org/project/fastapi-sessions/): A session management framework for FastAPI.
- [`jinja2`](https://pypi.org/project/Jinja2/): A template engine for mixing Python code with HTML.

---

### 📂 Main File: `main.py`

1. **Initializing FastAPI** 🏁
- The app is configured to handle HTTP requests and manage sessions seamlessly.

2. **Key Routes**:
- `GET /`: Increments a session-based counter each time the page is reloaded. 🧮
- `GET /clear-session`: Resets the session, clearing the counter. 🔄

3. **Middleware for Sessions**:
- Middleware acts as an intermediary layer that processes HTTP **requests** and **responses** 🚦.
- In this project, the `SessionMiddleware` manages user sessions.
- A `secret_key` ensures session data is encrypted and secure, protecting against unauthorized access. 🔒

4. **Starting the Server**:
- The app uses Uvicorn to run in development mode with the `uvicorn.run` command in [main.py](./main.py).

---

### 🎨 HTML Template: [`root.html`](./templates/root.html)

This simple template:
- Displays the session counter.
- Includes a button to reset the session.

---

## 🌈 Conclusion ✨

This project showcases:
- How to build a web app with FastAPI.
- How to use sessions for managing temporary user data.
- How to structure a Python project professionally.

Ready to dive into the code? 🧑‍💻💥

_Have fun coding and... happy hacking!_ 🚀🎉


<hr/>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a> 🤍 <a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>
# 📖 Web App 🌍 con FastAPI ⚡ e Sessioni ✨

Benvenuto al progetto **Gestione Sessioni con FastAPI**!
🚀 Questo progetto ti guiderà attraverso i fondamenti della programmazione in Python 🐍, l'uso del framework web FastAPI ⚡ e l'implementazione di sessioni 🛠️ per gestire dati persistenti tra richieste HTTP.

## 🌟 Introduzione alla Programmazione in Python 🐍
Python è uno dei linguaggi di programmazione più popolari al mondo 🌍 grazie alla sua semplicità e versatilità.
È perfetto per sviluppare applicazioni web, data science, machine learning e molto altro! 🧠
Questo progetto utilizza Python per creare una web app moderna e reattiva.

### Caratteristiche principali di Python:
- Leggibilità 📖
- Ampia disponibilità di librerie 🔧
- Comunita attiva e di supporto 🤝

## ⚡ Cos'è FastAPI? ✨
**FastAPI** ⚡ è un framework web moderno, ad alte prestazioni, progettato per la creazione di API 🚀.
Grazie alla sua semplicità e potenza, è ideale sia per principianti che per professionisti.

### ✅ Perché usare FastAPI ⚡?
- Velocità estrema 🚀
- Documentazione automatica delle API 📚
- Perfetta integrazione con Python type hints 🛠️

## 🛠️ Le Sessioni in FastAPI
Le sessioni permettono di mantenere informazioni specifiche per ogni utente durante la loro interazione con l'applicazione 🌐.
Nel nostro progetto, utilizziamo le sessioni per contare quante volte un utente ha ricaricato la pagina.

**Tecnologia utilizzata:** `starlette.middleware.sessions` 🧩

## 🐾 Guida Passo-Passo 📑

### 🏗️ Configurazione dell'Ambiente Virtuale
Un **Virtual Environment (*venv*)** isola le dipendenze del progetto per evitare conflitti.

Segui questi semplici passi:

1. **Creazione di un Virtual Envairoment**: basta dal terminale (**CLI** ⌨️) avviare il comando
```bash
python -m venv <nome_del_tuo_venv>
```

2. **Attivazione del venv**: a seconda che tu sia su Windows o su un sistema Unix-Like (MacOS/Linux) basta digitare dal terminale (**CLI** ⌨️) il comando:

- Su 🪟 Windows (**command prompt** 🔳):

```bash
.\nome_del_tuo_venv\Scripts\activate.bat
```

o anche (**power shell** 🟦):

```bash
.\nome_del_tuo_venv\Scripts\activate.ps1
```

- Su 🍏 Mac / 🐧 Linux:

```bash
source nome_del_tuo_venv/bin/activate
```

3. **Installazione delle dipendenze**:
Allo scopo di dimenticare le dipendenze da installare, o nel caso in cui occorra una specifica versione di una dipendenza, per comodità è consuetudine scrivere l'elenco delle dipendenze in un unico file di testo, solitamente chiamato [`requirements.txt`](./requirements.txt), in questo modo, con un solo comando sarà possibile installare con `pip` tutto; a tale scopo basterà lanciare il comando

```bash
python -m pip install -r requirements.txt
```

4. **Avviare la Web App**:
Basta lanciare il comando
```bash
python main.py
```

5. **Testare la tua web app**: apri adesso il browser e lancia il tuo codice scrivendo sulla barra dell'indirizzo l'url [http://localhost](http://localhost/)

### 📜 Dipendenze necessarie

* [`httptools`](https://pypi.org/project/httptools/): per gestire le connessioni provenienti da altri host nella stessa rete
* [`uvicorn`](https://pypi.org/project/uvicorn/): server in *python*
* [`fastapi`](https://pypi.org/project/fastapi/): framework per la creazione di *web api* (**ReST**)
* [`fastapi-sessions`](https://pypi.org/project/fastapi-sessions/): framework legato a fastapi per la gestione della persistenza dei dati con le sessioni
* [`jinja2`](https://pypi.org/project/Jinja2/) per il *template engining*, permette di creare pagine html e mischiare in esse codice python

### 📂 File Principale: `main.py`
1. **Inizializzazione di FastAPI** 🏁:
- L'app è configurata per gestire richieste HTTP e supportare sessioni.

2. **Rotte principali**:
- `GET /`: Incrementa un contatore nelle sessioni ogni volta che la pagina viene caricata. 🧮
- `GET /clear-session`: Resetta la sessione, azzerando il contatore. 🔄

3. **Middleware per le sessioni**:
- Un **middleware** è un componente intermedio che si interpone tra il server e le **request**/**response** (*richieste*/*riposte*) dell'applicazione web 🚦. Si occupa di **modificare**, **controllare** o **arricchire** le *richieste **HTTP*** (*input*) prima che arrivino alle rotte dell'applicazione e le *risposte **HTTP*** (*output*) prima di essere inviate al client. Nel nostro esempio è stato usato per la *gestione delle sessioni* 🗂️ ed è stato configurato usando il metodo `app.add_middleware` presente nel [main.py](main.py).
Allo scopo di proteggere i dati della sessione, verrà usata una *chiave segreta* (`secret_key`) utilizzata, tra l'altro, per criptare e firmare i cookie, impedendo accessi non autorizzati. 🔒

4. **Avvio del server**:
- Utilizza Uvicorn per eseguire l'app in modalità di sviluppo con il comando `uvicorn.run` presente nel file [main.py](./main.py).

### 🎨 Template HTML: [`root.html`](./templates/root.html)
Un semplice template che:
- Mostra il valore del contatore.
- Include un pulsante per resettare la sessione.


## 🌈 Conclusioni ✨
Questo progetto dimostra:
- Come creare una web app con FastAPI.
- Come utilizzare sessioni per gestire dati temporanei.
- Come strutturare un progetto Python in modo professionale.

Pronto a mettere le mani sul codice? 🧑‍💻💥

_Buon divertimento e... buon coding_! 🚀🎉

<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)