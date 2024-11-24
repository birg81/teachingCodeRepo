[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

<a name="TOP"></a>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇬🇧](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png) <a name="EN"></a>
# 🛒 **ShoppingList** WebApp 🛍️ *ver 1.0*

## 🚀 Overview

Welcome to the **ShoppingList** web application!
This WebApp is a simple web example that helps you manage your shopping list.
The application is built using [**FastAPI** ⚡️](https://fastapi.tiangolo.com/), a modern and fast web framework for creating APIs with Python.
**FastAPI** ⚡️ is based on standard Python type hints and is designed to be easy to use and efficient.

## 🛠️ Technologies Used

- **FastAPI** ⚡️: The web framework that makes it easy to create APIs with Python, providing automatic validation, interactive documentation, and high performance.

- **uvicorn** 🦄: An extremely fast ASGI server, serving as the interface between FastAPI and the web.

- **Jinja2** 🐱‍👤⛩️: A modern and designer-friendly templating engine for Python. It allows dynamic content generation and rendering of HTML templates.

## 📂 Project Structure

The project is organized into the following modules:

- 🎮 **main.py**: This is the main file containing the FastAPI application (`webapp`).
It defines routing and related functions.

- 🎨 **templates/**: This directory contains HTML templates for web pages.
The templates use **Jinja2** for dynamically rendering content.

- 🗄️ **static/**: This directory is used to serve static files such as stylesheets, JavaScript, and images.

## 🌐 Web Paths

### 🏠 **Home Page - / (Root)**
- Displays the sorted shopping list.
- URL: `./`
- Example: [http://localhost:3000/](http://localhost:3000/)

### 🛍️ **Create Item - /create**
- Adds a new item to the shopping list.
- URL: `./create?item=your_item`
- Example: [http://localhost:3000/create?item=apples](http://localhost:3000/create?item=apples)

### 🔄 **Update Item - /update**
- Modifies an existing item in the shopping list.
- URL: `./update?id=item_id&item=new_value`
- Example: [http://localhost:3000/update?id=1&item=bananas](http://localhost:3000/update?id=1&item=bananas)

### ❌ **Delete Item - /delete**
- Removes an item from the shopping list.
- URL: `./delete?id=item_id`
- Example: [http://localhost:3000/delete?id=2](http://localhost:3000/delete?id=2)

## 🚀 Running the Application

To run the application, execute the following command in your terminal:

```bash
python main.py
```

Before starting the application, it might be a good idea to check if you have all the necessary frameworks.

### 🛠️ What You Need?

In the [requirements.txt](./requirements.txt) file, there are dependencies; to install them, simply run the following command:

```bash
pip install -r requirements.txt
```

or alternatively

```bash
python -m pip install -r requirements.txt
```

### 🧪 How to Test the Application

Now that the application is running, just type [http://localhost:3000/](http://localhost:3000/) into the address bar of your favorite browser, and magically your webApp will open.

## 🛒 Conclusion 🛍️

Have fun managing your shopping list!

Feel free to explore, modify, and improve this simple *ShoppingList* web application! 🌐🛒✨


<hr/>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a> 🤍 <a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>
# 🛒 **ShoppingList** WebApp 🛍️ *ver 1.0*

## 🚀 Panoramica

Benvenuto nell'applicazione web **ShoppingList**!
Questo WebApp è un semplice esempio web che ti aiuta a gestire la tua lista della spesa.
L'applicazione è costruita utilizzando [**FastAPI** ⚡️](https://fastapi.tiangolo.com/), un moderno e veloce framework web per la creazione di API con Python.
**FastAPI** ⚡️ è basato su suggerimenti di tipo Python standard ed è progettato per essere facile da usare ed efficiente.

## 🛠️ Tecnologie Utilizzate

- **FastAPI** ⚡️: Il framework web che facilita la creazione di API con Python, fornendo convalida automatica, documentazione interattiva e prestazioni elevate.

- **uvicorn** 🦄: Un server ASGI estremamente veloce, che funge da interfaccia tra FastAPI e il web.

- **Jinja2** 🐱‍👤⛩️: Un motore di templating moderno e amico del designer per Python.
Consente la generazione dinamica di contenuti e il rendering di modelli HTML.

## 📂 Struttura del Progetto

Il progetto è organizzato nei seguenti moduli:

- 🎮 **main.py**: Questo è il file principale contenente l'applicazione FastAPI (`webapp`).
Definisce il routing e le relative funzioni.

- 🎨 **templates/**: Questa directory contiene i modelli HTML per le pagine web.
I modelli utilizzano **Jinja2** per il rendering dinamico dei contenuti.

- 🗄️ **static/**: Questa directory viene utilizzata per servire file statici come fogli di stile, JavaScript e immagini.

## 🌐 Percorsi Web

### 🏠 **Pagina Principale - / (Root)**
- Mostra l'elenco della spesa ordinato.
- URL: `./`
- Esempio: [http://localhost:3000/](http://localhost:3000/)

### 🛍️ **Creare Articolo - /create**
- Aggiunge un nuovo articolo alla lista della spesa.
- URL: `./create?item=il_tuo_articolo`
- Esempio: [http://localhost:3000/create?item=mele](http://localhost:3000/create?item=mele)

### 🔄 **Aggiornare Articolo - /update**
- Modifica un articolo esistente nella lista della spesa.
- URL: `./update?id=id_articolo&item=nuovo_valore`
- Esempio: [http://localhost:3000/update?id=1&item=banane](http://localhost:3000/update?id=1&item=banane)

### ❌ **Eliminare Articolo - /delete**
- Rimuove un articolo dalla lista della spesa.
- URL: `./delete?id=id_articolo`
- Esempio: [http://localhost:3000/delete?id=2](http://localhost:3000/delete?id=2)

## 🚀 Esecuzione dell'Applicazione

Per eseguire l'applicazione, esegui il seguente comando nel tuo terminale:

```bash
python main.py
```

Prima di avviare l'applicazione può essere una buona idea controllare se hai tutti i framework che ti servono.

### 🛠️ Cosa serve?

Nel file [requirements.txt](./requirements.txt) ci sono le dipendenze; per poterle installare ti basterà eseguire il seguente comando

```bash
pip install -r requirements.txt
```

o in alternativa

```bash
python -m pip install -r requirements.txt
```

### 🧪 Come testare l'applicazione

Ora che l'applicazione sarà avviata basta scrivere sulla barra del url del tuo browser di fiducia l'indirizzo [http://localhost:3000/](http://localhost:3000/) e per magina si aprirà la tua webApp.

## 🛒 Conclusioni 🛍️

Buon divertimento nella gestione della tua lista della spesa!

Sentiti libero di esplorare, modificare e migliorare questa semplice applicazione web *ShoppingList*! 🌐🛒✨


<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)