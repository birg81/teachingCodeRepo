[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

<a name="TOP"></a>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇬🇧](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png) <a name="EN"></A>

<!-- English -->
# 🔐✨ SimpleAuth — The ABCs of Login Without Data Persistence 💻🎓🚫

## 🎯 Goal:

Understand, explore, and build a basic authentication system **without a database** and **without sessions**, purely for learning purposes 👶📘🧠

## 🧩 What is this project about? 🤔🎯🔍

**`simpleauth`** is a micro-project 🧪 designed for anyone who wants to understand how login systems work 🔐 — **without the complexity** 💥:

- ❌ **No DBMS** (no MySQL, Postgres, etc.) 📉
- ❌ **No sessions** (no cookies, tokens, or JWT) 🍪🚫
- ✅ **Just Java + JSP code** ✍️🧑‍💻
- ✅ **Learning-focused**: experiment, test, and explore 🤓🛠️

---

## 🧠 How does it work? ⚙️💬🧪

### 🔎 1. Collecting login credentials 📥📧🔑

✉️ The user enters their **email** and **password** in an HTML form 🧾 ([index.jsp](./src/main/webapp/index.jsp))
➡️ The data is then sent to [signin.jsp](./src/main/webapp/signin.jsp) 📩

```jsp
String email = request.getParameter("email") != null ? request.getParameter("email").strip() : "";
String password = request.getParameter("password") != null ? request.getParameter("password").strip() : "";
````

🧹 The inputs are lightly sanitized (trimmed) to remove extra spaces 🧽🧼

### 🧪 2. Credential check 🔍🔐🆚

📦 A static method `UsersManager.checkUser(email, password)` 🚀 is called from the [UsersManager.java](./src/main/java/controller/UsersManager.java) class
🔍 This method checks the input against a list of predefined users 🧍‍♂️🧍‍♀️ (hardcoded in the file) 📘

```jsp
User u = UsersManager.checkUser(email,password);
```

The `User` type 🧍‍♀️ is defined in [User.java](./src/main/java/model/User.java)

### 🧾 3. HTML Response 💬✅❌

📋 If the credentials match ✅, a welcome message is displayed 👋😃

```jsp
<h1>Welcome, <%= u.toString() %></h1>
```

🙈 If they don’t ❌, a friendly error message is shown 🚫⚠️

```jsp
<p>Sorry, there's no user with email <strong><%= email %></strong> and password <em><%= password %></em></p>
```

## 🏗️ Technical Requirements 🧰💻🔧

* ☕ Java (JDK 8+ recommended) 🧃
* 🧩 Apache Tomcat (v11.0+ suggested) 🏭
* 📄 JSP support enabled ✨
* 🧠 Basic understanding of:

	* Java & OOP 👨‍🏫
	* HTML & JSP 🌐
	* Servlet containers 🌡️

## 🎯 Learning Objectives 📚🧪🎓

* Understand the **core logic of authentication** 🔄
* Practice with **pure Java & JSP**, without frameworks 🧼
* Keep things simple: **no databases, no sessions** ❌🗃️❌
* Learn the importance of **separating responsibilities** (Controller vs Model) 🎭

## 📦 Project Structure 📁🧱

```
simpleauth/
│
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   ├── controller/
│   │   │   │   └── UsersManager.java   # 🔐 Login logic
│   │   │   └── model/
│   │   │       └── User.java           # 👤 User model
│   │   └── webapp/
│   │       ├── index.jsp               # 📩 Login form
│   │       └── signin.jsp              # 🔍 Credential check
│
├── .gitignore                          # 🚫 Git ignore rules
├── pom.xml                             # ⚙️ Maven project config
└── README.md                           # 📖 You’re here!
```

### 🧭 Note:

This is a standard Maven project, so you can open it easily with any modern IDE, such as:

* IntelliJ IDEA
* Eclipse
* VS Code
* …and others 🚀🛠️

## ⚠️ Warnings & Limitations 🧯⚠️🛑

* 🚫 **DO NOT use in production** — this project is **for educational use only** 📚🔒
* 🔓 No encryption, no session protection, no input validation 🚫🔐
* 🛡️ The goal is to **understand the basics**, not to build secure systems 💣

## 🧑‍🏫 Conclusion 📍💡🎓

With `simpleauth` 🎉 you're holding a **starter kit for authentication** 🧰
It’s a **clean**, **simple**, and **educational** example for anyone starting from scratch 🌱

🚀 *Start playing, make changes, add features, and have fun!* 😄

<hr/>

![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>

<!-- Italian -->
# 🔐✨ SimpleAuth — L'ABC del Login senza usare la persistenza dei dati 💻🎓🚫

## 🎯 Obiettivo:

Capire, esplorare e costruire un sistema di autenticazione di base senza database né sessioni, solo per scopi didattici 👶📘🧠

## 🧩 Cos'è questo progetto? 🤔🎯🔍

**`simpleauth`** è un micro-progetto 🧪 pensato per chi vuole imparare come funziona il login 🔐 **senza complicarsi la vita** 💥:

- ❌ **Niente DBMS** (niente MySQL, Postgres, ecc.) 📉
- ❌ **Niente sessioni** (niente cookies, token, JWT) 🍪🚫
- ✅ **Solo codice Java + JSP** ✍️🧑‍💻
- ✅ **Scopo didattico**: imparare, testare, smanettare 🤓🛠️

## 🧠 Come funziona? ⚙️💬🧪

### 🔎 1. Raccolta credenziali 📥📧🔑

✉️ L’utente inserisce **email** e **password** in una form HTML 🧾 ([index.jsp](./src/main/webapp/index.jsp)).
➡️ I dati vengono inviati alla pagina [signin.jsp](./src/main/webapp/signin.jsp) 📩.

```jsp
String email = request.getParameter("email") != null ? request.getParameter("email").strip() : "";
String password = request.getParameter("password") != null ? request.getParameter("password").strip() : "";
````

🧹 Viene fatta una piccola "pulizia" dei dati ricevuti (trim/spazi) 🧽🧼.

### 🧪 2. Verifica credenziali 🔍🔐🆚

📦 Si chiama una funzione statica `UsersManager.checkUser(email, password)` 🚀 definita nella classe [UsersManager.java](./src/main/java/controller/UsersManager.java)
🔍 Questa funzione confronta le credenziali con utenti predefiniti 🧍‍♂️🧍‍♀️ (contenuti nel file) 📘.

```jsp
User u = UsersManager.checkUser(email,password);
```

Il tipo Utente (User 🧍‍♀️)  è definito nella classe [User.java](./src/main/java/model/User.java))

### 🧾 3. Risposta HTML 💬✅❌

📋 Se l’utente viene trovato ✅, si mostra un saluto personalizzato 👋😃:

```jsp
<h1>Salve, <%= u.toString() %></h1>
```

🙈 Se le credenziali sono errate ❌, si mostra un messaggio d'errore simpatico ma chiaro 🚫⚠️:

```jsp
<p>Spiacente ma non esiste un utente con credenziali <strong><%= email %></strong> e <em><%= password %></em></p>
```

## 🏗️ Requisiti Tecnici 🧰💻🔧

* ☕ Java (JDK 8+ consigliato) 🧃
* 🧩 Apache Tomcat (es. v11.0+ o superiore) 🏭
* 📄 JSP support abilitato ✨
* 🧠 Conoscenze base di:

	* Java e OOP 👨‍🏫
	* HTML e JSP 🌐
	* Servlet container 🌡️

## 🎯 Obiettivi Didattici 📚🧪🎓

* Capire il **meccanismo base dell'autenticazione** 🔄
* Lavorare con **JSP e Java puro**, senza framework 🧼
* Evitare complicazioni: **niente database, niente sessioni** ❌🗃️❌
* Capire l'importanza della **separazione dei ruoli** (Controller vs Model) 🎭

## 📦 Struttura del Progetto 📁🧱🧱

```
simpleauth/
│
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   ├── controller/
│   │   │   │   └── UsersManager.java   # 🔐 Logica di verifica credenziali
│   │   │   └── model/
│   │   │       └── User.java           # 👤 Rappresentazione di un utente
│   │   └── webapp/
│   │       ├── index.jsp               # 📩 Form di login
│   │       └── signin.jsp              # 🔍 Verifica delle credenziali
│
├── .gitignore                          # 🚫 Esclude file inutili dal repository
├── pom.xml                             # ⚙️ Configurazione del progetto Maven
└── README.md                           # 📖 Questo file!
```

### 🧭 Nota:
Il progetto segue lo standard Maven, quindi potrai facilmente integrarlo in qualsiasi IDE compatibile, quali
* IntelliJ IDEA
* Eclipse,
* VS Code,
* ecc. 🚀🛠️

## ⚠️ Limiti & Avvisi 🧯⚠️🛑

* 🚫 **NON USARE IN PRODUZIONE**: questo progetto è **solo didattico** 📚🔒
* 🔓 Nessuna crittografia, nessuna protezione sessione, nessuna validazione avanzata 🚫🔐
* 🛡️ Serve solo a **capire le basi**, non a costruire sistemi sicuri 💣

## 🧑‍🏫 Conclusione 📍💡🎓

Con `simpleauth` 🎉 hai tra le mani uno **starter pack per l’autenticazione** 🧰
Un esempio **pulito**, **semplice**, e **istruttivo** per chi vuole iniziare da zero senza perdersi 🌱

🚀 *Inizia a sperimentare, modifica, aggiungi funzionalità e divertiti*! 😄

<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)