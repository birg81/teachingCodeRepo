[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

<a name="TOP"></a>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇬🇧](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png) <a name="EN"></a>
# Web Application with Jakarta EE, Tomcat 😺, and Maven 🚀

Welcome to this exciting web development adventure with [Jakarta Enterprise Edition (EE)](https://en.wikipedia.org/wiki/Jakarta_EE), [Tomcat](https://en.wikipedia.org/wiki/Apache_Tomcat), [Maven](https://en.wikipedia.org/wiki/Apache_Maven), and more! 🌐 In this space, we'll guide you through creating a powerful web app using various modern and flexible IDEs that will make your development process a unique experience.

## What Will You Find Here? 🧐

Discover fascinating features, including:

* Detailed information on *URL Query Strings* 📊
* Implementation of complete CRUD operations
* REST services with endpoints and web API development 🔄
* Creation of a WebApp and CRUD operations on different entities 💡
* Development of both *back end* and *front end* with or without the use of frameworks ⚙️
* Building modern and responsive Web UIs with CSS Frameworks like [Bootstrap](https://getbootstrap.com) 🎨

## Back-End with Jakarta EE and Maven

We'll start by exploring the use of servlets to intelligently respond to requests:

* Creating a servlet that provides JSON information about URL query strings 🎯
* Implementing a servlet to simulate a complete CRUD 🔄
* Skillfully solving data extraction issues from requests using the powerful Java Stream API 🌊

Our destination is the implementation of modern technologies like [Spring Boot](https://spring.io/projects/spring-boot) for a complete CRUD in a production environment.

## Initial Setup

Before anything else, make sure to download the right IDE for you. We recommend:
* [Eclipse](https://www.eclipse.org/)
* [IntelliJ IDEA](https://www.jetbrains.com/idea/)
* [Visual Studio Code](https://code.visualstudio.com/)
* [VS Codium](https://github.com/VSCodium/vscodium/releases).

However, we'll focus on the last two.

We'll guide you step by step in configuring the IDE, installing necessary plugins, and downloading essential complementary software for fabulous development.

To simplify things, we suggest creating a dedicated folder for your Java projects and another for complementary software.

Try running this command from the terminal:

```bash
md %USERPROFILE%\vs-workspace\java-workspace\.__apache__
```

This way, you'll have created specific folders within your user folder:
* `vs-workspace`: your personal folder for all projects, in any language
* `java-workspace`: the folder for Java projects
* `.__apache__`: will contain complementary software like [Tomcat](http://tomcat.apache.org/) and [Maven](https://maven.apache.org/download.cgi).

## Configure Your IDE 🛠️

Open Visual Studio Code, press `CTRL + SHIFT + P`, type `User Settings (JSON)`, and paste the following configuration into the [settings.json](/es-01_2023-09-13/settings.json) file, allowing your IDE to give you the best experience.

## Essential Extensions 🧩

Add the following extensions:

* [Maven for Java](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-maven)
* [Community Server Connector](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-community-server-connector)

## Download Complementary Software 📥

Next, download:

* The **binary zip archive** of [Maven](https://maven.apache.org/download.cgi) and extract it into the `.__apache__` folder.
* The latest **64-bit .zip version** of [Tomcat](http://tomcat.apache.org/), extract it into the same folder.
* Configure the extensions by indicating the paths to the Maven and Tomcat folders.
* Rewrite the [apache-tomcat-*version*\conf\tomcat-users.xml](./es-01_2023-09-13/tomcat-users.xml) file.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<tomcat-users
	version="1.0"
	xmlns="http://tomcat.apache.org/xml"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://tomcat.apache.org/xml tomcat-users.xsd"
>
	<role rolename="admin"/>
	<role rolename="admin-script"/>
	<role rolename="admin-gui"/>
	<role rolename="manager"/>
	<role rolename="manager-status"/>
	<role rolename="manager-script"/>
	<role rolename="manager-jmx"/>
	<role rolename="manager-gui"/>
	<user username="admin" password="admin" roles="admin,admin-script,admin-gui,manager,manager-status,manager-script,manager-jmx,manager-gui"/>
	<user username="root" password="root" roles="admin,admin-script,admin-gui,manager,manager-status,manager-script,manager-jmx,manager-gui"/>
	<user username="user" password="1234" roles="admin,admin-script,admin-gui,manager,manager-status,manager-script,manager-jmx,manager-gui"/>
	<user username="sa" password="sa" roles="admin,admin-script,admin-gui,manager,manager-status,manager-script,manager-jmx,manager-gui"/>
</tomcat-users>
```

## Project Creation 🚀

Open Visual Studio Code, press `CTRL + SHIFT + P`, type **Maven: Create Maven Project**, select `maven-archetype-webapp` as the archetype, and follow the instructions to provide the necessary information.

## Configure the Project 🛠️

After downloading all dependencies, modify the `pom.xml` file by replacing the Java version with the latest one using this snippet:

```xml
<maven.compiler.source>21</maven.compiler.source>
<maven.compiler.target>21</maven.compiler.target>
```

Also, insert the [**Tomcat Catalina**](https://mvnrepository.com/artifact/org.apache.tomcat/tomcat-catalina) dependency in the `<dependencies>` section:

```xml
<dependency>
	<groupId>org.apache.tomcat</groupId>
	<artifactId>tomcat-servlet-api</artifactId>
	<version>10.1.18</version>
</dependency>
```

Ensure you configure your project correctly to leverage Jakarta EE and Maven to the fullest.

## Testing and Deploy 🚧

To test the application, create the WAR package and start the Tomcat server. Deploy the WAR file on the server and test your application at [localhost:8080/<artifactId>](http://localhost:8080/). Remember, any code changes require creating a new WAR file for updating on Tomcat.

## Agility Note 🏎️

Although this approach may seem less immediate than Eclipse, once accustomed, the advantages are significant and guaranteed by the enormous versatility of Maven. *Be agile, be creative, and enjoy developing your web app*! 🚀✨

<hr/>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a> 🤍 <a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></a>
# Applicazione Web con Jakarta EE, Tomcat 😺 e Maven 🚀

Benvenuto in questa emozionante avventura di sviluppo web con [Jakarta Enterprise Edition (EE)](https://it.wikipedia.org/wiki/Jakarta_EE), [Tomcat](https://it.wikipedia.org/wiki/Apache_Tomcat), [Maven](https://it.wikipedia.org/wiki/Apache_Maven) e non solo! 🌐
In questo spazio, ti guideremo attraverso la creazione di una potente web app usando diversi IDE moderni e flessibili che renderanno il tuo processo di sviluppo un'esperienza unica.

## Cosa Troverai Qui? 🧐

Scoprirai funzionalità affascinanti, tra cui:

* Informazioni dettagliate sulle *URL Query String* 📊
* Implementazione di oprazioni CRUD complete
* servizi REST con endpoint e sviluppo di webapi 🔄
* Creazione di una WebApp e operazioni CRUD su diverse entità 💡
* Sviluppo di un *back end* e di un *front end* con e senza utilizzo di framework ⚙️
* Creazione di Web UI moderne e responsive grazie a CSS Framework come [Bootstrap](https://getbootstrap.com) 🎨

## Back-End con Jakarta EE e Maven

Partiremo esplorando l'uso di servlet per rispondere alle richieste in modo intelligente:

* Creeremo una servlet che fornirà informazioni in formato JSON sulle query string delle URL 🎯
* Implementeremo una servlet per simulare un completo CRUD 🔄
* Risolveremo abilmente problemi di estrazione dei dati dalle richieste utilizzando la potente Stream API di Java 🌊

La nostra destinazione l'implementazione di tecnologie moderne come [Spring Boot](https://spring.io/projects/spring-boot) per un CRUD completo in un ambiente di produzione.

## Configurazione Iniziale

Prima di tutto, assicurati di scaricare l'IDE giusto per te, noi ti proponiamo:
* [Eclipse](https://www.eclipse.org/)
* [IntelliJ IDEA](https://www.jetbrains.com/idea/)
* [Visual Studio Code](https://code.visualstudio.com/)
* [VS Codium](https://github.com/VSCodium/vscodium/releases).

Ci soffermeremo però sull'uso di questi ultimi due.

Ti guideremo passo passo nella configurazione IDE con installazione dei plugin necessari e con il download dei software complementari essenziale per un favoloso sviluppo.

Per semplificare le cose, ti consigliamo di creare una cartella dedicata per i tuoi progetti Java e un'altra per i software complementari.

Prova a eseguire questo comando dal terminale:

```bash
md %USERPROFILE%\vs-workspace\java-workspace\.__apache__
```

In questo modo, avrai creato dentro la cartella del tuo utente una serie di cartelle specifiche:
* `vs-workspace` la tua cartella personale per tutti i progetti, di qualsiasi linguaggio
* `java-workspace` la cartella per i progetti Java
* `.__apache__` conterrà i software complementari come [Tomcat](http://tomcat.apache.org/) e [Maven](https://maven.apache.org/download.cgi).

## Configura il Tuo IDE 🛠️

Apri Visual Studio Code, premi `CTRL + MAIUSC + P`, scrivi `User Settings (JSON)` e incolla nel file [settings.json](/es-01_2023-09-13/settings.json) la seguente configurazione grazie alla quale il tuo IDE ti permetterà di ottenere il massimo.

## Estensioni Essenziali 🧩

Aggiungi le seguenti estensioni:

* [Maven for Java](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-maven)
* [Community Server Connector](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-community-server-connector)

## Scarica i Software Complementari 📥

Successivamente, scarica:

* L'**archivio zip binario** di [Maven](https://maven.apache.org/download.cgi) e estrailo nella cartella `.__apache__`.
* L'ultima **versione .zip a 64 bit** di [Tomcat](http://tomcat.apache.org/), estraila nella stessa cartella.
* Configura le estensioni indicando i percorsi delle cartelle di Maven e Tomcat.
* riscrivi il file [apache-tomcat-*versione*\conf\tomcat-users.xml](./es-01_2023-09-13/tomcat-users.xml)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<tomcat-users
	version="1.0"
	xmlns="http://tomcat.apache.org/xml"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://tomcat.apache.org/xml tomcat-users.xsd"
>
	<role rolename="admin"/>
	<role rolename="admin-script"/>
	<role rolename="admin-gui"/>
	<role rolename="manager"/>
	<role rolename="manager-status"/>
	<role rolename="manager-script"/>
	<role rolename="manager-jmx"/>
	<role rolename="manager-gui"/>
	<user username="admin" password="admin" roles="admin,admin-script,admin-gui,manager,manager-status,manager-script,manager-jmx,manager-gui"/>
	<user username="root" password="root" roles="admin,admin-script,admin-gui,manager,manager-status,manager-script,manager-jmx,manager-gui"/>
	<user username="user" password="1234" roles="admin,admin-script,admin-gui,manager,manager-status,manager-script,manager-jmx,manager-gui"/>
	<user username="sa" password="sa" roles="admin,admin-script,admin-gui,manager,manager-status,manager-script,manager-jmx,manager-gui"/>
</tomcat-users>
```

## Creazione del Progetto 🚀

Apri Visual Studio Code, premi `CTRL + MAIUSC + P`, scrivi **Maven: Create Maven Project**, seleziona `maven-archetype-webapp` come Archetype e segui le istruzioni per fornire le informazioni necessarie.

## Configura il Progetto 🛠️

Dopo aver scaricato tutte le dipendenze, modifica il file `pom.xml` sostituendo la versione di java con l'ultima attravero questo snippet

```xml
<maven.compiler.source>21</maven.compiler.source>
<maven.compiler.target>21</maven.compiler.target>
```

Inoltre va inserito nella sessione `xml <dependencies>` la dipendenza di [**Tomcat Catalina**](https://mvnrepository.com/artifact/org.apache.tomcat/tomcat-catalina)

```xml
<dependency>
	<groupId>org.apache.tomcat</groupId>
	<artifactId>tomcat-servlet-api</artifactId>
	<version>10.1.18</version>
</dependency>
```

Assicurati di configurare correttamente il tuo progetto per sfruttare Jakarta EE e Maven al massimo.

## Testing e Deploy 🚧

Per testare l'applicazione, crea il pacchetto WAR e avvia il server Tomcat.
Esegui il deploy del file WAR sul server e prova la tua applicazione su [localhost:8080/<artifactId>](http://localhost:8080/).
Ricorda, ogni modifica del codice richiede la creazione di un nuovo file WAR per l'aggiornamento su Tomcat.

## Agility Note 🏎️

Anche se questo approccio potrebbe sembrare meno immediato rispetto ad Eclipse, una volta abituati, i vantaggi sono notevoli e garantiti dall'enorme versatilità di Maven.
*Sii agilmente creativo e divertiti a sviluppare la tua web app*! 🚀✨


<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)
