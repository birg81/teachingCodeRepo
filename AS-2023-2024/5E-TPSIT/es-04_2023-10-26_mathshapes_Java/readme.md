[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

<a name="TOP"></a>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇬🇧](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png) <a name="EN"></A>
# 🔶 Mathematical Shapes: Inheritance and Polymorphism with Java Interfaces 🚀

## Introduction

This code aims to illustrate concepts of *inheritance* and *polymorphism* typical of *OOP* in **Java**.
Specifically, it creates classes related to 2D and 3D geometric shapes to demonstrate the workings of *interfaces* and the mechanism of *inheritance*, especially for 3D shapes, where the base is a 2D shape, and its characteristics are *inherited*.

## Java Inheritance 🔗

In the Java realm, *inheritance* allows a class to inherit the properties of another.
With the `extends` keyword, we can create *child classes* that derive their powers from a *parent class*.
This relationship is the essence of *inheritance*.

## Abstract Classes 🧩

An *abstract class* is a class that cannot be directly instantiated but provides a mysterious framework for its descendants.
It employs the `abstract` keyword and contains both *abstract* and *concrete* methods.
*Abstract methods* are methods without a body, to be invoked and implemented in child classes.

## Interfaces and the `implements` keyword 🤝

An *interface* is a class that contains only abstract methods! In this world, *interfaces*, through the `implements` keyword, define a common set of things to do, sealing solemn contracts that child classes commit to uphold.
In *interfaces*, there are no method implementations; only method names.
Technically, an interface is a container of **method signatures**.

## Our Example 📦

In our code, we've created two *interfaces*:

* [`Shape`](./src/main/java/model/Shape.java), for 2D shapes; it contains the method signatures:
  - `double perimeter()` to calculate the *perimeter* of a 2D shape.
  - `double area()` to calculate its *area*.
* [`Shape3D`](./src/main/java/model/Shape3D.java), for 3D shapes, contains the method signatures:
  - `double totSurfaceArea()` to calculate the *total surface area*.
  - `double volume()` to calculate the *volume* of the solid.

### Override and Polymorphism 🔄

Classes in the project:
* [`Rectangle`](./src/main/java/shapes/Rectangle.java) (**rectangle** with *base* and *height*)
* [`Square`](./src/main/java/shapes/Square.java) (**square** of side *s*)
* [`RegularShape`](./src/main/java/shapes/RegularShape.java) (**regular polygon** with *N sides*)
* [`Prism`](./src/main/java/shapes3D/Prism.java) (**Prism** with a **regular base**)

While `Rectangle`, `Square`, and `RegularShape` *implement* the `Shape` interface, `Prism* extends* `RegularShape` and *implements* the `Shape3D` interface.
Through *override*, the methods defined in the *interfaces* are implemented and redefined.
This is the essence of *polymorphism*, where different objects are treated uniformly.

#### Some Mathematics 🧮
Here are some formulas used in calculations:
* $\text{p} = N \cdot l$
* $\text{A} = \frac{N \cdot l^2}{4 \cdot \tan\left(\frac{\pi}{N}\right)}$
* $S_{\text{Tot}} = 2 \cdot A + p \cdot w$
* $\text{V} = A \cdot w$

where:
- $N$ is the *number of sides* of the regular plane figure.
- $l$ is the *length* of each side.
- $\pi$ is the value of *pi* (approximately 3.1415926).
- $p$ is the *perimeter* of the regular plane figure.
- $A$ is the *area* of the regular plane figure (base area of the prism).
- $\tan\left(\frac{\pi}{N}\right)$ is the tangent of the angle formed by the sides of the figure with the center of the figure.
- $S_{\text{Tot}}$ is the *total surface area* of the regular solid figure (*prism* / *parallelepiped*).
- $V$ is the *volume* of the regular solid figure.
- $w$ is the *height* of the regular solid figure.

### Special Methods 💼

#### Waterfall Constructors

Here are the *waterfall constructors*!
These methods allow the creation of different constructors based on specific use, without rewriting the new constructor from scratch but by using previously created constructors, greatly simplifying development.
This is possible through the concept of **overloading**, which allows writing two methods with the same name but with a different number and type of parameters.

#### Getters and Setters

Each class has *getters / setters* methods to access and modify data and control access.

#### String Casting

All classes have the `toString()` method.
This method allows converting an object into a string, making it easy to print the internal state of the object.

## Main: Code in Action 🌟

In the [Main](./src/main/java/mainpkg/Main.java), we've created an array of `Shape` and `Shape3D`.
Thanks to *polymorphism*, we can use the same code to handle different shapes.
This is the beauty of Java inheritance and interfaces.

## May This Guide Illuminate Your Path! 👏📚

**Java** is a magical and powerful language.
We hope this guide has illuminated the ancient secrets of inheritance and interfaces, revealing the path to cleaner and more flexible spells.

May your code always be *clean and enchanting*! 🌟😊


<hr/>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a> 🤍 <a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>
# 🔶 Mathematical Shapes: Inheritance and Polymorphism with Java Interfaces 🚀

## Introduzione

Questo codice ha come scopo mostrare concetti di *ereditarietà* e *polimorfismo* tipici della *OOP* in **Java**.
Nello specifico, vengono create classi relative a figure geometriche piane e tridimensionali nelle quali viene mostrato il funzionamento delle *interfacce* e il meccanismo dell'*ereditarietà*, in quanto, specificamente per le figure tridimensionali, la base è una figura piana, quindi vengono *ereditate* le sue caratteristiche.

## Java Inheritance 🔗

Nel mondo Java, l'*ereditarietà* permette a una classe di ereditare le proprietà di un'altra.
Con la keyword `extends`, possiamo creare *classi figlie* che derivano i loro poteri da una *classe genitore*.
Questa relazione è al'essenza dell'*ereditarietà*.

## Abstract Classes 🧩

Una *classe astratta* è una classe che non può essere creata direttamente ma fornisce un misterioso scheletro per le sue discendenti.
Adopera la keyword `abstract` e contiene sia metodi *astratti* che *concreti*.
I *metodi astratti* sono metodhi senza un corpo, che devono essere richiamati e implementati nelle classi figlie.

## Interfaces and `implements` keyword 🤝

Un'*interfaccia* è una classe che contiene solo metodi astratti!
In questo mondo le *interfacce*, attraverso la keyword `implements` definiscono un insieme comune di cose da fare, ovvero le *interfacce* suggellano dei *contratti*, dei *patti solenni*, che le classi figlie si impegnano a mantenere.
Nelle *interfacce* non ci sono implementazione di metodi ma **solo i nomi**, tecnicamente una interfaccia è un contenitore di **firme**

## Il nostro esempio 📦

Nel nostro codice, abbiamo creato due *interfacce*:

* [`Shape`](./src/main/java/model/Shape.java), per le forme piane; contiene le firme dei metodi:
  - `double perimeter()` per il calcolo del *perimetro* di una forma 2D.
  - `double area()` per calcolarne l'*area*.
* [`Shape3D`](./src/main/java/model/Shape3D.java), per le forme 3d, contiene invece le firme dei metodi:
  - `double totSurfaceArea()` per il calcolo della *superficie totale*.
  - `double volume()` per quello del *volume* del solido.

### Un po' di matematica 🧮
Ecco alcune formule usate nei calcoli:
* $\text{p} = N \cdot l$
* $\text{A} = \frac{N \cdot l^2}{4 \cdot \tan\left(\frac{\pi}{N}\right)}$
* $S_{\text{Tot}} = 2 \cdot A + p \cdot w$
* $\text{V} = A \cdot w$

dove:
- $N$ è il *numero di lati* della figura piana regolare.
- $l$ è la *lunghezza* di ciascun lato.
- $\pi$ è il valore di *pi greco* (circa 3.1415926).
- $p$ è il *perimetro* della figura piana regolare
- $A$ è l'*area* della figura piana regolare (area della base del prisma).
- $\tan\left(\frac{\pi}{N}\right)$ rappresenta la tangente dell'angolo formato dai lati della figura con il centro della figura.
- $S_{\text{Tot}}$ è l'area della *superfice totale* della figura solida regolare (*prisma* / *parallelepipedo*).
- $V$ è il *volume* della figura solida regolare.
- $w$ è l'*altezza* della figura solida regolare.

### Override e Polymorphism 🔄

Classi presenti nel progetto:
* [`Rectangle`](./src/main/java/shapes/Rectangle.java) (**rettangolo** con *base* e *altezza*)
* [`Square`](./src/main/java/shapes/Square.java) (**quadrato** di lato *l*)
* [`RegularShape`](./src/main/java/shapes/RegularShape.java) (**figura regolare** di *N lati*)
* [`Prism`](./src/main/java/shapes3D/Prism.java) (**Parallelepipedo** che ha per base una **figura regolare**)

Mentre `Rectangle`, `Square` e `RegularShape`, *implementano* l'interfaccia `Shape`; `Prism`, invece *estende* `RegularShape` e *implementa* l'interfaccia `Shape3D`.
Attraverso l'*override*, vengono quindi definiti e ridefiniti i metodi presenti nelle *interfacce*.
Questa è l'essenza del *polimorfismo*, dove oggetti diversi sono trattati uniformemente.

### Special Methods 💼

#### Waterfall Contructors

Ecco i *costruttori a cascata*! Questi metodi consentono la creazione di altri costruttori diversi in base allo specifico utilizzo, senza riscrivere il nuovo costruttore da zero ma adoperando i costruttori precedentemetne creati, semplificando notevolmente lo sviluppo.
Ciò è possibile attraverso il concetto di **overload**, ovvero la possibilità di scrivere due metodi con lo stesso nome ma con un numero e un tipo di parametri diverso.

#### Getters and Setters

Ogni classe ha metodi *getters / setters* per accedere e modificare i dati e controllarne gli accessi.

#### String Casting

Le classi possiedono tutti il metodo `toString()`, questo metodo permette di convertire un oggetto in una stringa e in questo modo poter stampare facilmente lo stato interno dell'oggetto.

## Main: Codice in Azione 🌟

Nel [Main](./src/main/java/mainpkg/Main.java), abbiamo creato un array di `Shape` e `Shape3D`.
Grazie al *polimorfismo*, possiamo utilizzare lo stesso codice per gestire figure diverse.
Questa è la bellezza dell'ereditarietà e delle interfacce in Java!

## Possa questa Guida Illuminare il Tuo Cammino! 👏📚

**Java** è un linguaggio magico e potente.
Speriamo che questa guida abbia illuminato gli antichi segreti dell'ereditarietà e delle interfacce, svelando la via verso incantesimi più puliti e flessibili.

Possa il tuo codice essere sempre *pulito e sbalorditivo*! 🌟😊

<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)
