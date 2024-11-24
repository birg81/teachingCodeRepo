[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

<a name="TOP"></a>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇬🇧](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png) <a name="EN"></A>
# 📖 Web App with FastAPI ⚡, Jinja2 🌟, and Pydantic 🧩

Welcome to the **Person Management with FastAPI** project! 🎉
🚀 In this project, you'll explore the fundamentals of **FastAPI** ⚡, use **Jinja2** 🌟 for **HTML templating**, and validate data with **Pydantic** 🧩, which will help you easily convert JSON objects into Python models 🚀.
You will also learn how to manage and return data in JSON format using an API 🖥️.

## 🐍 Introduction to Python Programming

Python is a very powerful, easy-to-learn, and incredibly versatile programming language 🧠. It is perfect for a wide range of applications, from **web apps** to **data science**, **machine learning**, and **scripting automation**. 🎯

In this project, we use **Python** to create an interactive web application that displays a list of people through the **FastAPI** ⚡ framework and utilizes **Pydantic** 🧩 for data management and validation.

### ✅ Key Features of Python:
- **Ease of reading and writing** 📖
- **Wide ecosystem of libraries** 🔧
- **Active community and continuous support** 🤝

## ⚡ What is FastAPI? ✨

**FastAPI** is a high-performance web framework 🚀 for creating APIs, designed to be both simple and powerful! Thanks to **Python typing**, **FastAPI** allows you to automatically generate API documentation 📝 and easily validate data 🚦.

### ✅ Why choose FastAPI?
- *Super fast* 🚀
- *Automatic documentation* 📚
- *Seamless integration with Python typing* 🔧

## 🎨 What is Jinja2? 🖌️

**Jinja2** is a templating engine for Python that allows you to separate logic from presentation in your web app 🎭. With Jinja2, you can make your HTML pages dynamic by inserting variables and loops directly into your HTML code.

### ✅ Why use Jinja2?
- **Easy integration with FastAPI** ⚡
- **Create dynamic HTML pages** 💥
- **Simple and powerful syntax** 🧠

## 🧩 What is Pydantic? ⚙️

**Pydantic** is a Python library for data validation 🔒. With Pydantic, you can easily convert JSON objects into Python models with clear and powerful syntax 🔧. Thanks to **BaseModel**, you can define data models with automatic validations, such as in our **Person** class 🧑‍🤝‍🧑.

### ✅ Why use Pydantic?
- *Automatic data validation* ✅
- *Conversion from JSON to Python objects* 🔄
- *Error handling support* ⚠️

## 🛠️ Sessions in FastAPI

Sessions in **FastAPI** allow you to store specific information between HTTP requests 🖥️. In this project, we don’t use sessions directly, but the concept of **data management** and returning data as **JSON** is similar to session behavior 🤖.

## 📂 File Structure

### 🏗️ The `main.py` File

The `main.py` file is the core of our project. Here's what it does:

1. **Initialize FastAPI**: Our application is set up with a title, description, and support for rendering HTML pages using **Jinja2**.

2. **Load Data**: In this file, we load data from a JSON file (`characters.json`) and transform it into a list of **Person** objects using **Pydantic**.

3. **Main Routes**:
- `GET /`: Returns a dynamic HTML page using **Jinja2** to display the list of people.
- `GET /api/v2/characters.json`: Returns the data in JSON format via a simple API. 🎯

4. **Mount Static Files**: We configure the server to serve static files (like images, CSS, and JavaScript) from the `/static` folder 🚀.

### 🧩 The [`Person.py`](./Person.py) File

In **Person.py**, we've created the **Person** class that extends **BaseModel** from **Pydantic**.
This class helps us validate data before using it, ensuring that each person has:

- An **ID** greater than 0 (`gt=0`) 🔢
- A **firstname** and **lastname** with at least 3 characters (`min_length=3`) ✍️
- A **gender** that can only be "m" (male) or "f" (female) ⚤

With Pydantic, data validation is quick and automatic ⚡!

### 🔗 What is the `url_for()` Function? 🚀

One of the most powerful functions in **FastAPI** is `url_for()`.
This function allows you to dynamically generate URLs for your routes directly from your Python code, instead of hardcoding them in HTML.
This offers several advantages:

1. **Prevents link errors**: You won’t have to worry about writing URLs manually, saving time and reducing the risk of mistakes.
2. **Greater flexibility**: If you change the URL of a route, you don’t need to modify every occurrence in the app. Just update the route name, and `url_for()` will automatically adjust! 🔄

Here’s how it works in our case:

- In **FastAPI**, you can use `url_for()` to dynamically generate the link to a specific route, such as:
```python
url_for('index')
```
This will return the URL for the `GET /` route without manually writing the path.

- In **Jinja2**, you can use `url_for()` directly in your HTML template to get a dynamic URL, such as when we want to create a link to the homepage:
```html
<a href="{{ url_for('index') }}">Go to the homepage</a>
```

In this way, the templating engine will correctly resolve the URL, even if the endpoint changes in the future.

### 🛠️ Installation and Running the App

1. **Create a Virtual Environment**:
Create a virtual environment with the following command:
```bash
python -m venv venv
```

2. **Activate the Virtual Environment**:
Activate the virtual environment:
- On **Windows**:
```bash
.\venv\Scripts\activate
```
- On **Mac/Linux**:
```bash
source venv/bin/activate
```

3. **Install Dependencies**:
Install the necessary libraries with the command:
```bash
pip install -r requirements.txt
```

4. **Run the Server**:
Start the server with:
```bash
python main.py
```

5. **Test the App**:
Visit [http://localhost](http://localhost/) in your browser to see your web app in action! 🚀

### 📜 Required Dependencies

- [`httptools`](https://pypi.org/project/httptools/): For managing HTTP connections
- [`uvicorn`](https://pypi.org/project/uvicorn/): Python server
- [`fastapi`](https://pypi.org/project/fastapi/): Web framework for creating APIs
- [`pydantic`](https://pypi.org/project/pydantic/): Library for data validation
- [`jinja2`](https://pypi.org/project/jinja2/): HTML templating engine for Python

### 🖥️ Conclusion

With this project, you’ve learned how to:
- Create a web app with **FastAPI**.
- Manage and display data in **JSON** format.
- Use **Pydantic** for data validation and conversion to Python objects.
- Create a dynamic UI with **Jinja2**.

Ready for the next level? 🚀🎉

_Have fun and... happy coding_! 😎💻


<hr/>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a> 🤍 <a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>
# 📖 Web App con FastAPI ⚡, Jinja2 🌟 e Pydantic 🧩

Benvenuto nel progetto **Gestione Persone con FastAPI**! 🎉
🚀 In questo progetto, esplorerai i fondamenti di **FastAPI** ⚡, l'uso di **Jinja2** 🌟 per il **templating HTML**, e la validazione dei dati con **Pydantic** 🧩, che ti permetterà di convertire facilmente oggetti JSON in modelli Python 🚀.
Imparerai anche come gestire e restituire i dati in formato JSON usando un'API 🖥️.

## 🐍 Introduzione alla Programmazione Python

Python è un linguaggio di programmazione molto potente, semplice da imparare e incredibilmente versatile 🧠. È perfetto per una vasta gamma di applicazioni, dalle **web app** alla **data science**, dal **machine learning** alla **scripting automation**. 🎯

In questo progetto, utilizziamo **Python** per creare un'applicazione web interattiva che mostra una lista di persone tramite il framework **FastAPI** ⚡ e usa **Pydantic** 🧩 per la gestione e validazione dei dati.

### ✅ Caratteristiche principali di Python:
- **Facilità di lettura e scrittura** 📖
- **Ampio ecosistema di librerie** 🔧
- **Comunità attiva e supporto continuo** 🤝

## ⚡ Cos'è FastAPI? ✨

**FastAPI** è un framework web di altissime prestazioni 🚀 per la creazione di API, progettato per essere semplice e potente al tempo stesso! Grazie a **Python typing**, **FastAPI** ti permette di generare automaticamente la documentazione delle API 📝 e di convalidare facilmente i dati 🚦.

### ✅ Perché scegliere FastAPI?
- *Velocità supersonica* 🚀
- *Documentazione automatica* 📚
- *Integrazione perfetta con Python typing* 🔧

## 🎨 Cos'è Jinja2? 🖌️

**Jinja2** è un motore di templating per Python che ti permette di separare la logica dalla presentazione nella tua web app 🎭. Con Jinja2, puoi rendere dinamiche le tue pagine HTML, inserendo variabili e cicli direttamente nel tuo codice HTML.

### ✅ Perché usare Jinja2?
- **Facilità di integrazione con FastAPI** ⚡
- **Creazione di pagine HTML dinamiche** 💥
- **Sintassi semplice e potente** 🧠

## 🧩 Cos'è Pydantic? ⚙️

**Pydantic** è una libreria Python per la validazione dei dati 🔒. Con Pydantic, puoi convertire facilmente oggetti JSON in modelli Python con una sintassi chiara e potente 🔧. Grazie a **BaseModel**, puoi definire modelli di dati con validazioni automatiche, come nel caso della nostra classe **Person** 🧑‍🤝‍🧑.

### ✅ Perché usare Pydantic?
- *Convalida automatica dei dati* ✅
- *Conversione da JSON a oggetti Python* 🔄
- *Supporto per la gestione degli errori* ⚠️

## 🛠️ Le Sessioni in FastAPI

Le sessioni in **FastAPI** permettono di mantenere informazioni specifiche tra le richieste HTTP 🖥️. In questo progetto, non usiamo direttamente le sessioni, ma il concetto di **gestione dei dati** e la loro restituzione come **JSON** è simile a un comportamento di sessione 🤖.

## 📂 Struttura dei File

### 🏗️ Il file `main.py`

Il file `main.py` è il cuore del nostro progetto. Ecco cosa fa:

1. **Inizializzazione di FastAPI**: La nostra applicazione viene configurata con un titolo, una descrizione e supporto per il rendering delle pagine HTML tramite **Jinja2**.

2. **Caricamento dei Dati**: In questo file, carichiamo i dati da un file JSON (`characters.json`) e li trasformiamo in una lista di oggetti **Person** con **Pydantic**.

3. **Rotte principali**:
- `GET /`: Restituisce una pagina HTML dinamica usando **Jinja2** per visualizzare la lista di persone.
- `GET /api/v2/characters.json`: Restituisce i dati in formato JSON tramite una semplice API. 🎯

4. **Mounting Static Files**: Configuriamo il server per servire file statici (come immagini, CSS e JavaScript) dalla cartella `/static` 🚀.

### 🧩 Il file [`Person.py`](./Person.py)

In **Person.py**, abbiamo creato la classe **Person** che estende **BaseModel** di **Pydantic**.
Questa classe ci aiuta a convalidare i dati prima di usarli, assicurandoci che ogni persona abbia:

- Un **ID** maggiore di 0 (`gt=0`) 🔢
- Un **firstname** e un **lastname** con almeno 3 caratteri (`min_length=3`) ✍️
- Un **gender** che può essere solo "m" (maschile) o "f" (femminile) ⚤

Con Pydantic, la validazione dei dati è facile e automatica ⚡!

### 🔗 Cos'è la funzione `url_for()`? 🚀

Una delle funzioni più potenti in **FastAPI** è `url_for()`.
Questa funzione ti permette di generare dinamicamente gli URL per le tue rotte direttamente dal tuo codice Python, anziché hardcodificarli in HTML.
Questo ti offre diversi vantaggi:

1. **Evita errori di collegamento**: Non dovrai mai preoccuparti di scrivere manualmente l'URL di una rotta, risparmiando tempo e riducendo il rischio di errori.
2. **Maggiore flessibilità**: Se cambi l'URL di una rotta, non devi modificare ogni singola occorrenza nell'app. Basta aggiornare il nome della rotta e il `url_for()` si aggiornerà automaticamente! 🔄

Ecco come funziona nel nostro caso:

- In **FastAPI**, puoi usare `url_for()` per generare dinamicamente il link a una rotta specifica, come ad esempio:
```python
url_for('index')
```
Questo restituirà l'URL della rotta `GET /` senza che tu debba scrivere manualmente il percorso.

- In **Jinja2**, puoi utilizzare `url_for()` direttamente nel tuo template HTML per ottenere un URL dinamico, come nel caso in cui vogliamo creare un link alla pagina principale:
```html
<a href="{{ url_for('index') }}">Vai alla homepage</a>
```

In questo modo, il motore di templating si occuperà di risolvere correttamente l'URL, anche se cambi in futuro l'endpoint.

### 🛠️ Installazione e Avvio dell'App

1. **Creazione di un Virtual Environment**:
Crea un ambiente virtuale con il comando:
```bash
python -m venv venv
```

2. **Attivazione dell'Ambiente Virtuale**:
Attiva l'ambiente virtuale:
- Su **Windows**:
```bash
.\venv\Scripts\activate
```
- Su **Mac/Linux**:
```bash
source venv/bin/activate
```

3. **Installazione delle Dipendenze**:
Installa le librerie necessarie con il comando:
```bash
pip install -r requirements.txt
```

4. **Avvio del Server**:
Avvia il server con:
```bash
python main.py
```

5. **Test dell'App**:
Visita [http://localhost](http://localhost/) nel tuo browser per vedere la tua web app in azione! 🚀

### 📜 Dipendenze Necessarie

- [`httptools`](https://pypi.org/project/httptools/): Per la gestione delle connessioni HTTP
- [`uvicorn`](https://pypi.org/project/uvicorn/): Server per Python
- [`fastapi`](https://pypi.org/project/fastapi/): Framework web per creare API
- [`pydantic`](https://pypi.org/project/pydantic/): Libreria per la validazione dei dati
- [`jinja2`](https://pypi.org/project/jinja2/): Motore di templating HTML per Python


### 🖥️ Conclusioni

Con questo progetto, hai imparato a:
- Creare una web app con **FastAPI**.
- Gestire e visualizzare dati in formato **JSON**.
- Utilizzare **Pydantic** per la validazione dei dati e la loro conversione in oggetti Python.
- Creare una UI dinamica con **Jinja2**.

Pronto per il prossimo livello? 🚀🎉

_Buon divertimento e... buon coding_! 😎💻

<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)