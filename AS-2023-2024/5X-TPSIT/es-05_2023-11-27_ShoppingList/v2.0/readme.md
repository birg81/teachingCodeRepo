[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

<a name="TOP"></a>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇬🇧](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png) <a name="EN"></a>
# 🛒 **ShoppingList** WebApp 🛍️ *ver 2.0*

## 🚀 Overview

Welcome to the **ShoppingList** web application! This WebApp is a practical example of managing your shopping list with a RESTful style, using the [**FastAPI** ⚡️](https://fastapi.tiangolo.com/) framework, known for its speed and ease of use.

In this new version, a different approach has been introduced compared to the previous one, which is widely used and allows significant data savings by concentrating processing on the client and reducing data sent by the server.

## 🛠️ Technologies Used

- **FastAPI** ⚡️: A fast web framework for creating APIs with Python.
- **uvicorn** 🦄: A fast ASGI server, serving as an interface between FastAPI and the web.
- **Jinja2** 🐱‍👤⛩️: A modern templating engine for Python, for dynamically generating HTML content.

## 📈 Project Upgrade

Compared to the previous version, this one offers a **REST** architecture and complies with CRUD operations. Let's see in detail what this means:

### 🏢 REST Architecture

**REST** (*Representational State Transfer*) is a web-based architecture that uses a stateless approach and operates through a set of standard operations on resources, defined by URIs (Uniform Resource Identifiers) and indicated through HTTP methods.

### 🏗️ CRUD Operations

The CRUD operations represent the four fundamental functions on persistent data. By using HTTP methods, we have:
- 🌱 **C** ➔ *Create*: **POST** method to *create*/*add* a new item.
- 🔍 **R** ➔ *Read*: **GET** method to *read*/*query*/*request*/*search* one or more/all items.
- ♻️ **U** ➔ *Update*: **PUT** method to *modify* an item.
- ❌ **D** ➔ *Delete*: **DELETE** method to *delete* an item.

## WebApp Operations

### ➕🛍️ Create
- 📝 note: Add an item
- 🛠️ Method: **POST**
- 🌐 URL Example: `(POST) ./api/apple`

### ❓🛍️ Read
- 📝 note: Request the list of items
- 🛠️ Method: **GET**
- 🌐 URL Example: `(GET) ./api`

### ✍️🛍️ Update
- 📝 note: Modify an item
- 🛠️ Method: **PUT**
- 🌐 URL Example: `(PUT) ./api/1/flour`

### ❌🛍️ Delete
- 📝 note: Delete an item from the list
- 🛠️ Method: **DELETE**
- 🌐 URL Example: `(DELETE) ./api/1`

## 🚀 Running the Application

Use the following command in your terminal:

```bash
python main.py
```

# 🧪 How to Test the Application

Now that the application is running, visit [http://localhost:3000/](http://localhost:3000/) in your favorite browser and start managing your shopping list! 🛍️

# 🚀 Happy Shopping! 🛒

Thank you for choosing our **ShoppingList WebApp**! 🌟

*Now you can manage your shopping list easily and quickly*.

*Start exploring and having fun with your new online shopping experience*.

Enjoy! 👋


<hr/>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a> 🤍 <a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>
# 🛒 **ShoppingList** WebApp 🛍️ *ver 2.0*

## 🚀 Panoramica

Benvenuto nell'applicazione web **ShoppingList**!
Questo WebApp è un esempio pratico di come gestire la tua lista della spesa con uno stile RESTful e utilizzando il framework [**FastAPI** ⚡️](https://fastapi.tiangolo.com/), noto per la sua velocità e facilità d'uso.

In questa nuova versione è stato introdotto uno approccio diverso dal precedente che è largamente usato e permette un grande risparmio dati in quanto concentra l'elaborazione sul Client e riduce i dati inviati dal Server.

## 🛠️ Tecnologie Utilizzate

- **FastAPI** ⚡️: Framework web veloce per la creazione di API con Python.
- **uvicorn** 🦄: Server ASGI veloce, interfaccia tra FastAPI e il web.
- **Jinja2** 🐱‍👤⛩️: Motore di templating moderno per Python, per la generazione dinamica di contenuti HTML.

## 📈 Upgrade al progetto

Rispetto la precedente versione questa offre un'architettura **ReST** e compie con essa operazioni **CRUD**.
Vediamo nel dettaglio cosa significa:

### 🏢 Architettura REST

**ReST** (*Representational State Transfer*) è un'architettura basata su web che utilizza un approccio stateless (senza stato) e opera attraverso una serie di operazioni standard su risorse, definite da URI (Uniform Resource Identifiers) e indicate tramite i metodi HTTP.

### 🏗️ Operazioni CRUD

Le operazioni **CRUD** rappresentano le quattro funzionalità fondamentali su dati persistenti, ovvero adoperando i metodi HTTP avremo che:
- 🌱 **C** ➔ *Create*: metodo **POST** per *creare*/*aggiungere* un nuovo elemento.
- 🔍 **R** ➔ *Read*: metodo **GET** per *leggere*/*interrogare*/*richiedere*/*ricercare* uno o più / tutti gli elementi.
- ♻️ **U** ➔ *Update*: metodo **PUT** per *modificare* uno elemeno.
- ❌ **D** ➔ *Delete*: metodo **DELETE** per *eliminare* un elemento

## Operazioni della WebApp

### ➕🛍️ Create
- 📝 note: Aggiunge un articolo
- 🛠️ Method: **POST**
- 🌐 URL Example: `(POST) ./api/mela`

### ❓🛍️ Read
- 📝 note: Richiede la lista degli articoli
- 🛠️ Method: **GET**
- 🌐 URL Example: `(GET) ./api`

### ✍️🛍️ Update
- 📝 note: Modifica un articolo
- 🛠️ Method: **PUT**
- 🌐 URL Example: `(PUT) ./api/1/farina`

### ❌🛍️ Delete
- 📝 note: Elimina un articolo dalla lista
- 🛠️ Method: **DELETE**
- 🌐 URL Example: `(DELETE) ./api/1`

## 🚀 Esecuzione dell'Applicazione

Usa il seguente comando nel tuo terminale:

```bash
python main.py
```

# 🧪 Come testare l'applicazione

Ora che l'applicazione è in esecuzione, visita [http://localhost:3000/](http://localhost:3000/) nel tuo browser preferito e inizia a gestire la tua lista della spesa! 🛍️

# 🚀 Happy Shopping! 🛒

Grazie per aver scelto la nostra **ShoppingList WebApp**! 🌟

*Ora puoi gestire la tua lista della spesa in modo semplice e veloce*.

*Inizia a esplorare e divertirti con la tua nuova esperienza di shopping online*.

Buon divertimento! 👋


<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)