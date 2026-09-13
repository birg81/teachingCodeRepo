<img src="https://spring.io/favicon.svg" height="48px"/>

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Flag_of_Italy_(Pantone,_2003%E2%80%932006).svg/220px-Flag_of_Italy_(Pantone,_2003%E2%80%932006).svg.png" height="2px" width="250px">

# Spring

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/) [![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/) [![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

A seguire, verranno presentati due esempi di web app

* [1stwebapp](./1stwebapp) senza db, usa solo liste
* [2ndwebapp](./2ndwebapp) con db e approccio [orm](https://it.wikipedia.org/wiki/Object-relational_mapping)

I due esempi cambiano solo in base all'approccio ad i dati!
Infatti in entrambi cercano di mantenere lo stesso naming dei metodi, delle variabili, degli endpoints.

## Cosa fa l'esempio?

È una lista di persone

```Java
Person(id: Integer, firstname: String, lastname: String, age: int)
```

Attraverso la costrozione di alcuni endpoints sarà possibile effettuare le diverse operazioni CRUD.

È stato inoltre creato un front-end molto minimale con grafica ed icone (il front-end è il medesimo in entrambi gli esempi!) che usa anche Bootstrap, per presentare la lista di dati.

## Differenza tra le due versioni

### Primo esempio

Nel [primo esempio](./1stwebapp) si fa riferimento ad una lista di persone

```java
ArrayList<Person> people = new ArrayList<>();
```

### Secondo esempio

In questo [secondo esempio](./2ndwebapp) si è scelto di implementare la persistenza dei dati si e di far uso di un approccio ORM fa uso di DBMS

<img src="https://labs.mysql.com/common/logos/mysql-logo.svg" height="48px"/>

<img src="https://mariadb.org/wp-content/themes/twentynineteen-child/icons/logo_seal.svg" height="48px"/>

<img src="https://github.com/h2database/h2database/blob/master/h2/src/docsrc/images/h2-logo-2.png" height="48px"/>

L'esempio propone l'uso di [MySQL](https://www.mysql.com) (testato sul suo fork [MariaDB](https://mariadb.org) adoperato in [XAMPP](https://www.apachefriends.org)) ma come con opportune modifiche nei file [pom.xml](./2ndwebapp/pom.xml) e [application.properties](./2ndwebapp/src/main/resources/application.properties) è possibile adoperare qualsiasi dbms.

Visionando i suddetti file si può infatti notare come in fase di prototipazione è stato invece adoperato [H2](https://github.com/h2database/h2database), un db minimale con tecnologia [in-memory](https://it.wikipedia.org/wiki/In-memory_database) proprio come sqlite ma differentemente da questi H2 è pienamente supportato da Spring.

Attualmente Spring, o meglio Hibernate (il componente di Spring che adopera un approccio ORM), adopera moltissimi dialetti relativi ai diversi dbms, sfortunatamente tra questi sqlite non è disponibile!
