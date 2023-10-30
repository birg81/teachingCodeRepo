[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

<a name="TOP"></a>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇬🇧](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png) <a name="EN"></a>
# 🌐 SSC Napoli Team 💙⚽ Servlet 🐱

## 📂 Repository Contents

This repository is a treasure 💰 of examples that will guide us through the engaging and informative use of **Servlets**, **JSP Pages**, and **JSON**.
Get ready to discover how to fully harness the potential of these technologies in the Java ☕ and Java Enterprise ([Jakarta EE](https://jakarta.ee)) web world.

### 📢 Attention:
*There's more to each example than meets the eye*! 😲✨🔮

## Example 0: 🌟 Initial Servlet 🌐

In our journey, we will encounter an initial **servlet** that responds to the addresses [index.html](http://localhost:8080/sscnapoliservlet/index.html) o [index.jsp](http://localhost:8080/sscnapoliservlet/index.jsp).
This URL is a fictional URL behind which there is no static web page but a servlet that responds with HTML content.
This seemingly simple example is a *gateway* 🚪 that opens the door to subsequent examples.

### 💡 Info

List of files involved in this example:

* [`ServletV0.java`](./src/main/java/controller/ServletV0.java) - This file is the class containing our **servlet** and, through the `doGet()` method, returns an HTML page.

Routing:

*As indicated by `@WebServlet`, it responds to the following addresses:*

* [`http://localhost:8080/sscnapoliservlet/`](http://localhost:8080/sscnapoliservlet/)
* [`http://localhost:8080/sscnapoliservlet/index.html`](http://localhost:8080/sscnapoliservlet/index.html)
* [`http://localhost:8080/sscnapoliservlet/index.jsp`](http://localhost:8080/sscnapoliservlet/index.jsp)

## Example 1: 🔄 The Dispatcher and the Magic of Redirection

This example is an intriguing adventure.
First, the **servlet** responds under a URL that corresponds to a fictional HTML page; however, under the hood, the **servlet** uses the **Dispatcher** to pass control to a **JSP page**.

### ⚽ A Legendary Team 🏆

The **JSP page** that receives control makes a masterful move.
Before passing control to the **JSP page**, the **servlet** also passes some data that Java understands perfectly.
The page then retrieves a *special list*: an `ArrayList<Soccer>`, where `Soccer` is a class representing soccer players, in fact, they are historic players; these are the champions of **SSC Napoli** ⚽ during the first Serie A championship in the **1986-1987 season** 🏆.

The **JSP page**, upon receiving this data, uses Java code that cooperates with HTML code within the **JSP pages** to translate the list into an HTML table to display the player names on the web page.

### 💡 Info

List of files involved in this example:

* [`ServletV1.java`](./src/main/java/controller/ServletV1.java) - This file is the class containing our **servlet**, which uses the **Dispatcher** to pass control to the **JSP page**.
* [`v1.jsp`](./src/main/webapp/v1.jsp) - The **JSP page** that receives the `ArrayList<Soccer> players` list and transforms it into an HTML table.

**Routing**:

*As indicated by `@WebServlet`, it responds to the following addresses:*

* [`http://localhost:8080/sscnapoliservlet/v1.html`](http://localhost:8080/sscnapoliservlet/v1.html)
* [`http://localhost:8080/sscnapoliservlet/v1.jsp`](http://localhost:8080/sscnapoliservlet/v1.jsp) - If the servlet is called directly, it results in an error since it expects to receive the list.

In this case, since the list is not transmitted, the page produces errors!

## Example 2: 🐱 A JSON Response

This example turns our preconceived notions upside down.
**Servlets**, as it turns out, can also return data in **JSON** format!

### JSON is Among Us 🎫👀

In many web architectures, this approach is used: a *backend* sends data to the *frontend* in **JSON** format.
This way, less data is transmitted compared to a giant web page, and the computational load of translating the **JSON** file and subsequent display shifts from the *backend*, which sees a significant reduction in workload, to the *frontend*, resulting in improved network performance.

In this example, the servlet provides an extraordinary response.

Thanks to the powerful [*Gson*](https://mvnrepository.com/artifact/com.google.code.gson/gson) library (which must be included separately), it transforms an `ArrayList<Soccer>` into a **JSON**-formatted string.
The data is received, interpreted, and processed by the *frontend*, which uses JavaScript to transform the received data into an HTML table.
This time, the **JSON** represents the players of **SSC Napoli** 💙 in the *2023-2024 season* 🏟️.

### 💡 Info

List of files involved in this example:

* [`ServletV2.java`](./src/main/java/controller/ServletV2.java) - This file is the class containing our **servlet**, which responds with data in **JSON** format.
* [`v2.html`](./src/main/webapp/v2.html) - A static HTML page that receives the **JSON**.
* [`soccerplayers.js`](./src/main/webapp/script/soccerplayers.js) - The script that uses the `fetch()` method to receive, interpret, and display the **JSON** on the page.

**Routing**:

*As indicated by `@WebServlet`, it responds to the following address:*

* [`http://localhost:8080/sscnapoliservlet/v2.html`](http://localhost:8080/sscnapoliservlet/v2.html) - A static web page that displays the data.

## 🚀 Exploring Servlets and JSP Pages

🚀 **Servlets** and 🚀 **JSP Pages** represent the dynamic foundations of Java web applications.
This journey into the world of servlets and JSP pages will reveal the secrets of these technologies and show you how to use them effectively.

## 🌐 Servlet: 🧡😸 The Heart of the Server

😽 **Servlets** are Java classes that extend `HttpServlet` and override methods such as `doGet()`, `doPost()`, and others.
Through a convenient system of annotations, these classes respond to URLs specified in the code.
The URL is a fictional address; it's possible to invent paths that don't exist, such as imaginary pages in `.html` format.
This allows better system security, as any unwanted intrusions can be redirected to non-existent addresses.
Servlets, by default, respond in HTML format but can be configured to respond in other formats.

## JSP: 🌐 Technology for Dynamic Web Content

A **JSP page** (*JavaServer Pages*) is a Java technology that allows you to embed Java code ☕ within HTML pages.
**JSP pages** enable the creation of dynamic web content using Java, with the Java code embedded directly into the HTML page, making the code more.

 readable and similar to a traditional web page.
In practice, a **JSP page**, before being executed, is transformed into a **servlet** and run at the appropriate URL, establishing a strong correlation between **servlets** and **JSP pages**.

## 🌐 Correlation Between Servlets and JSP Pages

Before diving in, it's important to understand that **JSP pages** are an extension of **servlets**.
**JSP pages** are, in fact, special dynamic HTML pages that can contain embedded Java code.
These pages will be transformed into servlets and then executed.
This correlation is the secret to their strength because they provide a very practical way of writing **servlets**, which, although powerful tools, can also be complex to write.

## 🧩 Modularity with Dispatcher and Redirect

Servlets are not isolated.
They can work together in a modular way.
By using 🧩 **Dispatcher** and 🧩 **Redirect**, servlets can communicate with each other or intelligently redirect clients.

### 🌟 Dispatcher: The Address of Intelligence

The 🌟 **Dispatcher** is like a precise indication of an event.
Servlets can delegate control to other servlets or JSP pages.
It's like physically moving people to a new location, but in this case, control is intelligently passed to a different servlet or JSP page.

### 🔄 Redirect: The Quest for New Adventures

🔄 **Redirect** is like giving people instructions on how to reach a new location on their own.
A servlet sends a new URL to the client, and the client makes a new request to the server.
This creates a new experience without previous connections.

## 🚀 JSON, the Secret Language

In our repository, there's a servlet that responds with a **JSON file**.
This file is like a secret message that only the wizard can understand! 📜🔍

### 🔮 The Magic of Gson

The [*Gson library*](https://mvnrepository.com/artifact/com.google.code.gson/gson)
is the book of magic formulas.
The servlet uses it to transform data into **JSON** format, making it comprehensible to everyone! 📚🔮

### The Magic 🔍🔮 of Display

An HTML page receives this data through a `fetch()` function.
It's like receiving a secret letter.
Then, with the help of Bootstrap, it creates a spectacular table to display the data attractively! 🌐📊

## 💡 Conclusion

🚀 **Servlets** and 🚀 **JSP Pages** offer a wide range of possibilities for creating dynamic and interactive web applications.
Both 🌟 **Dispatcher** and 🔄 **Redirect** are useful tools for handling requests and providing personalized user experiences.
Now you're ready to explore further details and fully utilize the potential of servlets and JSP pages in your web projects.

*Have a great journey in the world of servlets and JSP pages*! 🌐🚀


<hr/>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a> 🤍 <a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>
# 🌐 SSC Napoli Team 💙⚽ Servlet 🐱

## 📂 Contenuti del Repository

Questo repository è un tesoro 💰 di esempi che ci guiderà attraverso l'uso di **Servlet**, **pagine JSP** e **JSON** in modo avvincente e informativo.
Preparati a scoprire come sfruttare pienamente il potenziale di queste tecnologie nel mondo web *Java* ☕ e *Java Enterprice* ([Jakarta EE](https://jakarta.ee)).

### 📢 Attenzione:
*Dietro ogni esempio c'è molto di più di ciò che sembra*! 😲✨🔮

## Esempio 0: 🌟 Servlet Iniziale 🌐

Nel nostro viaggio, incontreremo una **servlet** iniziale che risponde agli indirizzi [index.html](http://localhost:8080/sscnapoliservlet/index.html) o [index.jsp](http://localhost:8080/sscnapoliservlet/index.jsp).
Questo url è un url fittizio dietro al quale non c'è una *pagina web statica* ma servlet che risponde con un formato html.
Questo esempio apparentemente semplice è una *porta* 🚪 che apre gli orizzonti agli esempi successivi.

### 💡 info

Elenco dei file coinvolti in questo esempio:

* [`ServletV0.java`](./src/main/java/controller/ServletV0.java) questo file è la classe che contiene la nostra **servlet** e nella quale, attraverso il metodo `doGet()`, restituisce una pagina html

Routing:

*Come indicato da `@WebServlet`, risponde ai seguenti indirizzi*

* [`http://localhost:8080/sscnapoliservlet/`](http://localhost:8080/sscnapoliservlet/)
* [`http://localhost:8080/sscnapoliservlet/index.html`](http://localhost:8080/sscnapoliservlet/index.html)
* [`http://localhost:8080/sscnapoliservlet/index.jsp`](http://localhost:8080/sscnapoliservlet/index.jsp)

## Esempio 1: 🔄 Il Dispatcher e la magia del Reindirizzamento

Questo esempio è un'avventura intrigante.
In primo luogo la **servlet** risponde sotto un url che corrisponde ad una pagina html fittizia, in realtà sotto la scocca, la **servlet**, utilizza il **Dispatcher** passando il controllo ad una pagina **JSP**.

### ⚽ Una Squadra Leggendaria 🏆

La pagina **JSP** che riceve il controllo e fa una mossa magistrale.
La **servlet** prima di passare il controllo, passa alla **pagina JSP** anche dei dati che Java comprende perfettamente.
La pagina quindi preleva una *lista speciale*: un `ArrayList<Soccer>`, dove `Soccer` è una classe che rappresenta dei giocatori di calcio, infatti sono i giocatori storici; questi sono i campioni del **SSC Napoli** ⚽ durante il primo scudetto nella **stagione 1986-1987** 🏆.

La **pagina JSP**, una volta ricevuti questi dati, attravero il codice Java che coopera al codice html all'interno delle **pagine JSP**, traduce la lista in una tabella HTML in modo da mostrare i nomi dei giocatori sulla pagina web.

### 💡 info

Elenco dei file coinvolti in questo esempio:

* [`ServletV1.java`](./src/main/java/controller/ServletV1.java) questo file è la classe che contiene la nostra **servlet**, la quale mediante il **Dispatcher** passa il controllo alla **pagina jsp**.
* [`v1.jsp`](./src/main/webapp/v1.jsp) è la **pagina jsp** che riceve la lista `ArrayList<Soccer> players` che viene trasformato in una tabella html

**Routing**:

*Come indicato da `@WebServlet`, risponde ai seguenti indirizzi*

* [`http://localhost:8080/sscnapoliservlet/v1.html`](http://localhost:8080/sscnapoliservlet/v1.html)
* [`http://localhost:8080/sscnapoliservlet/v1.jsp`](http://localhost:8080/sscnapoliservlet/v1.jsp) se viene richiamata direttamente la servlet da errore in quanto si aspetta di ricevere la lista, v*isto che in questo caso non viene trasmessa, la pagina da errori*!

## Esempio 2: 🐱 Una risposta in formato JSON

Questo esempio ribalta le cose che pensavamo di sapere.
Le **servlet** a quanto pare possono restituire dati anche in formato **JSON**!.

### I JSON sono tra di noi 🎫👀

In molte architetture web, viene adoperato questo approccio: un *back-end* che invia al *front-end* in formato **JSON**; in questo modo vengono spedi meno dati rispetto una pagina web gigantesta e il carico computazionale di traduzione del file **JSON** e conseguente visualizzazione passa dal *back-end*, che si vede alleggerire di molto il lavoro, al *front-end* con conseguente aumento delle performance della rete.

In questo esempio quindi la servlet fornisce una risposta straordinaria.
Grazie alla potente libreria [*gson*](https://mvnrepository.com/artifact/com.google.code.gson/gson) (è libreria deve essere inclusa a parte), trasforma un `ArrayList<Soccer>` in una stringa formato **JSON**.
Il dato viene ricevuto, interpretato ed elaborato dal *front-end* il quale attraverso JavaScript trasforma i dati ricevuti in una tabella HTML.
Questa volta, il **JSON** è una lista che rappresenta i giocatori del **SSC Napoli** 💙 nella *stagione 2023-2024* 🏟️.

### 💡 info

Elenco dei file coinvolti in questo esempio:

* [`ServletV2.java`](./src/main/java/controller/ServletV2.java) questo file è la classe che contiene la nostra **servlet**, la quale risponde con un dato in formato **json**.
* [`v2.html`](./src/main/webapp/v2.html) è la *pagina html statica* che riceve i **JSON**.
* [`soccerplaysers.js`](./src/main/webapp/script/soccerplayers.js) è lo *script* che attraverso il `fetch()` riceve, interpreta e mostra il **json** lo mostra nella pagina.

**Routing**:

*Come indicato da `@WebServlet`, risponde ai seguenti indirizzi*

* [`http://localhost:8080/sscnapoliservlet/v2.html`](http://localhost:8080/sscnapoliservlet/v2.html) *pagina web statica* che mostra i dati.

## 🚀 Esplorazione delle Servlet e delle Pagine JSP

Le 🚀 **servlet** e le 🚀 **pagine JSP** rappresentano le fondamenta dinamiche delle applicazioni web Java.
Questo viaggio nel mondo delle servlet e delle pagine JSP ti svelerà i segreti di queste tecnologie e ti mostrerà come utilizzarle in modo efficace.

## 🌐 Servlet: 🧡😸 Il Cuore del Server

Le 😽 **Servlet** sono classi Java che estendono la `HttpServlet` ed effettuano l'override dei metodi `doGet()`, `doPost()` ed altri metodi.
Attraverso un pratico sistema di annotazioni, queste classi rispondono agli url indicati nel codice, l'url è un indirizzo fittizio, infatti è possibile inventare percorsi che non esistono, come delle immaginarie pagine in formato `.html`.
Ciò permette di proteggere meglio il nostro sistema in quanto eventuali intrusioni indesiderate possono essere redirette verso indirizzi inesistenti.
Le servlet rispondono, in maniera predefinita, in formato html, ma possono essere configurate per rispondere anche in altro tipo di formato.

## JSP: 🌐 Tecnologia per Contenuto Web Dinamico

Una **pagina JSP** (*JavaServer Pages*) è una tecnologia Java che consente di incorporare codice *Java* ☕ all'interno di pagine HTML.
Le **pagine JSP** consentono di creare contenuto web dinamico utilizzando Java, ma il codice Java è incorporato direttamente nella pagina HTML, rendendo il codice più leggibile e più simile a una pagina web tradizionale.
In pratica una **pagina JSP** prima di venir eseguita, viene trasformata in una **servlet** ed eseguita nell'indirizzo opportuno, quindi esiste una forte correlazione tra **servlet** e **pagine JSP**.

## 🌐 Correlazione tra Servlet e JSP

Prima di immergerci, è importante capire che le **pagine JSP** sono un'estensione delle **servlet**.
Le **pagine JSP** sono infatti speciali pagine HTML Dinamiche che possono contenere al loro interno codice Java.
Queste pagine verranno trasformate in servlet in seguito e quindi eseguite.
Questa correlazione è il segreto della loro forza, perché sono un modo molto pratico di scrivere **servlet**, le quali anche se rappresentano uno strumento molto potente, possono essere anche complesse da scrivere.

## 🧩 Modularità con Dispatcher e Redirect

Le servlet non sono isolate.
Possono lavorare insieme in modo modulare.
Usando 🧩 **Dispatcher** e 🧩 **Redirect**, le servlet possono comunicare tra loro o redirigere i client in modo intelligente.

### 🌟 Dispatcher: L'Indirizzo dell'Intelligenza

Il 🌟 **Dispatcher** è come un'indicazione precisa di un evento.
Le servlet possono delegare il controllo ad altre servlet o pagine JSP.
È come spostare fisicamente le persone in un nuovo luogo, ma in questo caso, il controllo passa in modo intelligente a una servlet o a una pagina JSP diversa.

### 🔄 Redirect: La Ricerca di Nuove Avventure

Il 🔄 **Redirect** è come dare istruzioni alle persone su come raggiungere un nuovo luogo da sole.
Una servlet invia al client un nuovo URL, e il client fa una nuova richiesta al server.
Questo crea una nuova esperienza, senza connessioni pregresse.

## 🚀 JSON, il Linguaggio Segreto
Nel nostro repository, c'è una servlet che risponde con un file **JSON**.
Questo file è come un messaggio segreto che solo il mago può comprendere! 📜🔍

### 🔮 La Magia del Gson
La [*libreria Gson*](https://mvnrepository.com/artifact/com.google.code.gson/gson) è il libro delle formule magiche.
La servlet lo usa per trasformare dati in formato **JSON**, rendendoli comprensibili a tutti! 📚🔮

### La Magia 🔍🔮 della Visualizzazione
Una pagina HTML riceve questi dati attraverso una funzione `fetch()`.
È come ricevere una lettera segreta.
Poi, con l'aiuto di Bootstrap, crea una tabella spettacolare per mostrarli in modo attraente! 🌐📊

## 💡 Conclusioni

e 🚀 **servlet** e le pagine 🚀 **JSP** offrono un'ampia gamma di possibilità per creare applicazioni web dinamiche e interattive.
Sia il 🌟 **Dispatcher** che il 🔄 **Redirect** sono strumenti utili per gestire le richieste e offrire esperienze utente personalizzate.
Ora sei pronto per esplorare ulteriori dettagli e sfruttare appieno il potenziale delle **servlet** e delle **pagine JSP** nei tuoi progetti web.

*Buon viaggio nell'universo delle servlet e delle pagine JSP*! 🌐🚀


<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)
