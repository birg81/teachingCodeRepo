[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

<a name="TOP"></a>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇬🇧](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png) <a name="EN"></A>
# Super Fantastic Guide to Installing Apache Tomcat and Creating a Java Enterprise Project with Eclipse! 🚀
Welcome, ambitious young developers!
Today, we will guide you through an epic journey into the world of Apache Tomcat and Java Enterprise, step by step!
Ready?! 🤩

### Introduction
In this example, we will see how to approach Java Enterprise, now called [Jakarta EE](https://it.wikipedia.org/wiki/Jakarta_EE), and use it to create a dynamic web project in which we can embed Java code within HTML code.
Before we reach this final goal, we need to download a series of necessary resources.
You may be able to skip some steps, but for completeness, all the steps are provided.

## Step 1: Setting up the Java Environment ☕

1. Download the **Java Development Kit (JDK)** for Windows [here](https://www.oracle.com/it/java/technologies/downloads/).
2. Follow the instructions for JDK installation.
3. Don't forget to configure the **JAVA_HOME** system variable. Here's how: [Link to the instructions](https://www.wikihow.it/Configurare-Java-Home).

## Step 2: Preparing the Tomcat Server 🐱

1. Download the latest version of **Tomcat 10.1** for Windows [here](https://tomcat.apache.org/download-10.cgi).
2. Extract the ZIP file to a convenient location.
3. Edit the `conf/tomcat-users.xml` file following our fantastic custom configuration.
Alternatively, if you prefer, you can use this fantastic configuration.
Open the file and paste the following [this code](./tomcat-user.xml)

## Step 3: Setting up Eclipse Enterprise 🌌

1. Download and install **Eclipse Enterprise** from their official website [here](https://www.eclipse.org/downloads/).
2. Make sure to install the *Eclipse IDE for Enterprise Java and Web Development* version.
3. Add the **Apache Tomcat 10.1** server to Eclipse.

## Step 4: Creating a Dynamic Web Project 🌐

1. Create a new Dynamic Web Project in Eclipse.
2. The [`web.xml`](./1stpage/src/main/webapp/WEB-INF/web.xml) file is the heart of your project; make sure to take a close look at it.

## Step 5: Structure of the Web Project 📂

Here's what you will find in your project folder:
```
/<projectName>
-/src
--/java
---(classi java)
--/main
---/webapp
----/WEB-INF
-----web.xml
----index.jsp
```

Let's take a closer look at what it contains:

- `/<projectName>/src/java`: It contains Java source code just like traditional Java projects.
- `/<projectName>/src/main/webapp`: It contains HTML, JSP, CSS, and other static web files.
- `/<projectName>/src/main/webapp/WEB-INF/web.xml`: It contains the [`web.xml`](./1stpage/src/main/webapp/WEB-INF/web.xml) file (a very important file) and other configurations.

## Step 6: Starting the Project 🚀

1. Start your project on the Tomcat server directly from Eclipse.
2. Open your browser and go to `http://localhost:8080/<projectName>`.
In this case [`http://localhost:8080/1stpage/`](http://localhost:8080/1stpage/)

## Step 7: Sample Code in index.jsp 📝
After creating the project, it's a good practice to create a homepage.
The advantage of JSP pages is that they allow you to mix Java code with HTML code.
All code within angle brackets `<% /* Java code */ %>` is Java code.
To print strings in HTML code, you should use `<%= "Sample String" %>`.
Below is an example code of [`index.jsp`](./1stpage/src/main/webapp/index.jsp)

But this is just the first of many examples.
There is still a long way to go!

Good work, young developers!
This guide is just the beginning of your journey to web development epicness with Java Enterprise and **Apache Tomcat**.

*Now it's your turn to perform magic!* ✨🚀


<hr/>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a> 🤍 <a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>
# Guida Super Fantastica per Installare Apache Tomcat e Creare un Progetto Java Enterprise con Eclipse! 🚀
Benvenuti, giovani sviluppatori intraprendenti!
Oggi vi guideremo attraverso un viaggio epico nell'universo di Apache Tomcat e Java Enterprise, passo dopo passo!
Pronti?! 🤩

### Introduzione
In questo esempio vedremo come approcciarci a Java Enterprise oggi chiamata [Jakarta EE](https://it.wikipedia.org/wiki/Jakarta_EE) e grazie ad essa realizzare un progetto web dinamico attraverso il quale inserire codice Java all'interno di codice HTML.
Prima di arrivare a questo obbiettivo finale dobbiamo però scaricare una serie di risorse necessarie.
Probabilmente alcuni passi potrai saltarli, ma per completezza sono forniti tutti gli step

## Passo 1: Preparazione dell'ambiente Java ☕

1. Scarica la **Java Development Kit (JDK)** per Windows [qui](https://www.oracle.com/it/java/technologies/downloads/).
2. Segui le istruzioni per l'installazione della JDK.
3. Non dimenticare di configurare la variabile di sistema **JAVA_HOME**. Ecco come: [Link alle istruzioni](https://www.wikihow.it/Configurare-Java-Home).

## Passo 2: Preparazione del Server Tomcat 🐱

1. Scarica l'ultima versione di **Tomcat 10.1** per Windows [qui](https://tomcat.apache.org/download-10.cgi).
2. Estrai il file ZIP in una posizione comoda.
3. Modifica il file [`conf/tomcat-users.xml`](./tomcat-users.xml) seguendo la nostra fantastica configurazione personalizzata o se preferisci puoi adoperare questa fantastica configurazione, quindi apri il file e incolla al suo interno il [seguente codice](./tomcat-users.xml)

## Passo 3: Preparazione di Eclipse Enterprise 🌌

1. Scarica ed installa **Eclipse Enterprise** dal loro sito ufficiale [qui](https://www.eclipse.org/downloads/).
2. Assicurati di installare la versione *Eclipse IDE for Enterprise Java and Web Development*
3. Aggiungi il server **Apache Tomcat 10.1** a Eclipse.

## Passo 4: Creazione di un Progetto Web Dinamico 🌐

1. Crea un nuovo progetto Web Dinamico in Eclipse.
2. Il file [`web.xml`](./1stpage/src/main/webapp/WEB-INF/web.xml) è il cuore del tuo progetto, assicurati di darvi un'occhiata approfondita.

## Passo 5: Struttura del Progetto Web 📂

Ecco cosa troverai nella cartella del tuo progetto:
```
/<projectName>
-/src
--/java
---(classi java)
--/main
---/webapp
----/WEB-INF
-----web.xml
----index.jsp
```
Vediamo bene cosa contiene:
- `/<projectName>/src/java`: Contiene il codice sorgente Java esattamente come i progetti Java tradizionali.
- `/<projectName>/src/main/webapp`: Contiene HTML, JSP, CSS, e altri file web statici.
- `/<projectName>/src/main/webapp/WEB-INF/web.xml`: Contiene il file [`web.xml`](./1stpage/src/main/webapp/WEB-INF/web.xml) (un file molto importante) e altre configurazioni.

## Passo 6: Avvio del Progetto 🚀

1. Avvia il tuo progetto sul server Tomcat direttamente da Eclipse.
2. Apri il tuo browser e vai su `http://localhost:8080/<projectName>`.
In questo caso [`http://localhost:8080/1stpage/`](http://localhost:8080/1stpage/)

## Passo 7: Codice di Esempio in index.jsp 📝
Dopo la creazione del progetto è buona norma creare una home page.
Il vantaggio della pagine jsp è che queste permettono di mischiare codice java al codice html.
Tutto il codice nelle parentesi angolari `<% /* codice java */ %>` è codice java.
Per stampare delle stringhe nel codice html va invece adoperato `<%= "Stringa di prova" %>`.
Di seguito è proposto un codice di esempio di [`index.jsp`](./1stpage/src/main/webapp/index.jsp)

Ma questo è solo il primo di tantissimi esempi.
Tanta è la strada ancora da percorrere!

Buon lavoro, giovani sviluppatori!
Questa guida è solo l'inizio del vostro viaggio verso l'epicità nello sviluppo web con Java Enterprise e **Apache Tomcat**.

*Ora tocca a voi fare magie!* ✨🚀


<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)
