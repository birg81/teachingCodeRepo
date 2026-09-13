
<img src="https://spring.io/favicon.svg" height="48px"/>

# Spring

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/) [![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/) [![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

## Introduzione

**LEGGI FINO ALLA FINE!!!**

In questo esempio viene fatto uso della persistenza dei dati, la quale, a titolo di esempio viene svolta da due db (l'esempio è testato per MySQL/MariaDB e h2database), ma con la giusta configurazione dei file [application.properties](./src/main/resources/application.properties) e [pom.xml](./pom.xml) è possibile adoperare un gran numero di altri DBMS.

## Uso di MySQL/MariaDB

<a href="https://mariadb.org"/><img src="https://mariadb.org/wp-content/themes/twentynineteen-child/icons/logo_seal.svg" height="20px"/></a> Lasciando la configurazione inalterata del file [application.properties](./src/main/resources/application.properties) verrà adoperato il DB MySQL/MariaDB adoperato da XAMPP.

Allo scopo di usare questo **R-DBMS** è importante creare preventivamente il DB PersonDB, ovvero, recandosi nel pannello amministrativo di XAMPP e aver avviato APACHE e MySQL, premere su admin di MySQL quindi cliccare sulla scheda SQL e dare il seguente comando
```SQL
CREATE DATABASE IF NOT EXISTS PersonDB;
```
Di seguito, sarà possibile avviare l'applicazione e verificare che la tabella People viene man mano popolata e modificata.

## Uso di H2db

<a href="https://github.com/h2database/h2database"><img src="https://github.com/h2database/h2database/blob/master/h2/src/docsrc/images/h2-logo-2.png" height="20px"/></a> L'uso di questo R-DBMS è spesso rilegato per la prototipazione.

Per adoperare questo R-DBMS è necessario in primo luogo modificare il file [pom.xml](./pom.xml), disabilitando lo starter relativo a MySQL, ovvero, commentando le righe:
```xml
<dependency>
	<groupId>com.mysql</groupId>
	<artifactId>mysql-connector-j</artifactId>
	<scope>runtime</scope>
</dependency>
```
ed abilitando quindi lo starter relativo ad H2db, ovvero rimuovendo i commenti dalle righe
```xml
<dependency>
	<groupId>com.h2database</groupId>
	<artifactId>h2</artifactId>
	<scope>runtime</scope>
</dependency>
```
Di seguito, è inoltre necessario modificare il file [application.properties](./src/main/resources/application.properties) commentando dalla riga 10 alla 18, e decommentare le seguenti righe 19, 21, 22, 24, 25, 27 nel seguente modo
```ini
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.H2Dialect
spring.datasource.driver-class-name=org.h2.Driver
spring.datasource.url=jdbc:h2:mem:PersonDB
spring.datasource.username=sa
spring.datasource.password=
spring.h2.console.enabled=true
```
in particolare, l'ultima riga
```ini
spring.h2.console.enabled=true
```
Abilita un pannello web per il controllo dei dati nel DB, del tutto simile a phpmyadmin per MariaDB.

Per accedere a tale db basta andare sul link [http://localhost:5000/h2-console/](http://localhost:5000/h2-console/) indicando alla riga **JDBC URL** l'url specificato nel file di configurazione ovvero ```jdbc:h2:mem:PersonDB```.

Attraverso tale pannello potranno anche essere fatte manualmente operazioni CRUD a livello amministrativo.

Così come configurato H2, ad ogni riavvio dell'applicazione, il DB verrà ricreato, in quanto viene settato ```jdbc:h2:mem```, dove ```mem``` sta ad indicare che il DB viene memorizzato nella memoria RAM, quindi viene ricreato ad ogni avvio.

Tale approccio sembrerebbe andare contro la necessità della persistenza dei dati!

Ovviamente questa funzionalità viene adoperata solo in fase di prima prototipazione per avere una web app molto veloce a discapito del mantenimento dei dati.
Utilizzando lo stesso DBMS si può adoperare la memorizzazione su file, ovvero il DB intero viene salvato su un file che ha per nome lo stesso nome del db ed estensione, .mv.db; per far ciò sarà necessario sostituire la riga
```ini
spring.datasource.url=jdbc:h2:mem:PersonDB
```
con la seguente
```ini
spring.datasource.url=jdbc:h2:file:./src/main/resources/PersonDB
```
dove ```file``` in luogo di ```mem```, sta ad indicare che in seguito al primo avvio, verrà creato nella cartella [/src/main/resources/](./src/main/resources/) il file PersonDB.mv.sb contenente il DB con tutte le tabelle popolate; cancellare questo file equivale a cancellare il DB, che verrebbe rigenerato dal SPRING.

Infine per accedere alla console web di H2, in maniera analoga a quella precendente, ricordandosi di indicare in corrispondenza di **JDBC URL** la stringa ```jdbc:h2:file:./src/main/resources/PersonDB```.

### GOOD LOOK
