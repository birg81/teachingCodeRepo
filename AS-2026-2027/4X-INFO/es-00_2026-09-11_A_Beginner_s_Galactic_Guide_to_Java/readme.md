[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

<a name="TOP"></a>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

---

![🇬🇧](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png) <a name="EN"></A>

<!-- English -->

# ☕🚀 Galactic Guide to Java: From C to the JVM World 🌍💻

> 🎬 **Get ready, everyone: we are not learning programming from scratch. 😎🧠**
> 🚀 You've already spent a year fighting C, `printf()`, `scanf()`, arrays, pointers, and curly braces. ⚔️💻
> ☕ Now we are switching languages, but we aren't changing how we think: *we're bringing everything we know and discovering how much smoother writing code can be with Java.* 🔥

## ☕ 1. 🌍 **Java**: The Language That Wanted to Go Everywhere 🚀

### 🕰️ Where Does Java Come From? 🌱☕

Java was created in the 1990s at **Sun Microsystems** with an ambitious goal: to create a language capable of running the same program across different platforms. 🌍💻

#### 🎯 The revolutionary idea is summarized in the famous motto:

> ☕ *Write Once, Run Anywhere* 🌍🚀

🧱 In C, on the other hand, programs are typically compiled for a specific platform, producing machine code tied to the architecture and operating system. 💻⚙️

☕ Java introduces an intermediate step: the program isn't converted directly into machine code, but into **bytecode**, which is then executed by the **JVM**. 🔄🧠

🇨 C
```text
Source code
	↓
Compiler
	↓
Machine code
	↓
CPU / Operating system
```

☕ Java
```text
Source code
	↓
Compiler
	↓
Bytecode
	↓
JVM
	↓
Operating system
```

🎯 And this is where **Java** *changes the game*. ☕🎮

## ⚙️ 2. 🧠 **JVM**, **JRE**, and **JDK**: *The Java Family* 👨‍👩‍👧‍👦☕

### 🧠 **JVM**: *Java Virtual Machine* ⚙️

☕ The [**JVM**](https://en.wikipedia.org/wiki/Java_virtual_machine) (*Java Virtual Machine*) is the **virtual machine** that executes Java **bytecode**. 💻🔄

🎯 A Java program produces bytecode, and the JVM takes care of running it on the current operating system. 🌍⚙️

`Java → Bytecode → JVM → 🪟 Windows / 🐧 Linux / 🍎 macOS`

🚀 This is one of the key reasons Java can keep its promise of *"Write Once, Run Anywhere"*. 🌍☕

### 🏃 **JRE**: *Java Runtime Environment* ☕

📦 The [**JRE**](https://en.wikipedia.org/wiki/Java_Runtime_Environment) represents the environment required to run Java applications. ▶️💻

🧠 Conceptually, we can think of it as:

☕ **JRE** = *environment to run Java*. ▶️

> ⚠️ In modern development, however, you don't need to install a standalone **JRE** separately like in the past: installing a modern **JDK** gives you everything needed to run Java programs. 🛠️☕

### 🛠️ **JDK**: *Java Development Kit* 🚀

🎯 The [**JDK**](https://en.wikipedia.org/wiki/Java_Development_Kit) is what matters to us developers. 💻👨‍💻

📦 It contains the essential tools needed to develop, compile, and run Java programs. ⚙️☕

```
JDK 🛠️
	├── development tools
	├── javac compiler
	├── JVM
	└── Java libraries
```

🧠 Simply put:

> 🔥 **JDK** = the Java developer's toolbox. 🧰☕

## 📥 3. 🛠️ What Do We Need to Install? 💻☕

### ☕ JDK 26: The Java Engine 🚀

📦 For our work, we will use JDK 26, which contains the tools needed to write and compile our Java programs. 🛠️☕

- 🌐 Official **Oracle JDK 26** Download: [https://www.oracle.com/java/technologies/downloads/](https://www.oracle.com/java/technologies/downloads/)
- 🌐 Alternative **OpenJDK 26**: [https://jdk.java.net/26/](https://jdk.java.net/26/)

* 🪟 **Windows**: download the version matching your architecture, usually `x64` on modern PCs. 💻
* 🍎 **macOS**: select the installer corresponding to your processor, Intel or Apple Silicon. 🖥️
* 🐧 **Linux**: choose the package compatible with your distribution or use your system's package manager. 🐧

#### 🎯 Crucial detail:
> Eclipse does not replace the JDK. 🚨

☕ The JDK provides the Java tools; Eclipse is the environment we use to work comfortably with those tools. 🛠️🖥️

### 🖥️ 4. 🌌 **Eclipse**: *Our Java Lab* 🔬☕

#### 🧰 What is Eclipse? 💻

[Eclipse IDE](https://en.wikipedia.org/wiki/Eclipse_(software)) is an integrated development environment—a program designed to help us write, organize, compile, run, and debug our code. 🧠⚙️

🎯 We will use:
☕ ***Eclipse IDE for Enterprise Java and Web Developers*** 💻🚀

* 🌐 Official Eclipse Download:
[https://www.eclipse.org/downloads/packages/release/2026-09/r/eclipse-ide-enterprise-java-and-web-developers](https://www.eclipse.org/downloads/packages/release/2026-09/r/eclipse-ide-enterprise-java-and-web-developers)

📦 Eclipse provides everything in one unified environment:

- ✍️ code editor;
- ▶️ program execution;
- 🐞 debugging tools;
- 📁 project management;
- 🔎 auto-completion;
- ⚡ shortcuts and code suggestions;
- 🚨 error highlighting.

> 💡 The **JDK** is the engine. **Eclipse** is the dashboard. 🚗☕

## 🧱 5. 🏁 The First Java Program: Why Is There a Class? ☕
🇨 In C, we start from `main()` 🚀
```C
#include <stdio.h>

int main() {
	printf("Forza Napoli!\n");
	return 0;
}
```

🎯 The entry point of the program is the `main()` function.

☕ In Java, the main program is written inside a class instead:
```java
public class Main {
	public static void main(String[] args) {
		System.out.println("Forza Napoli!");
	}
}
```

#### ⚠️ Keep in mind:
> in this guide, we are not diving into object-oriented programming yet. 🚫🧱

📦 For now, treat the class simply as the container required by Java syntax to hold the main function. 🧠📦

🎯 *OOP will come later*. Right now, we just want to get comfortable writing Java. ☕🗣️

## 🧩 6. 🔍 The Mysterious public static void main(String[] args) 🧠☕

### 🧱 Breaking it down without panic 🔬

```java
public static void main(String[] args)
```

🧠 For this first guide, all you need to know is that this is the method signature Java uses as the entry point for your program. 🚪☕

📌 The key part to compare with C is:
```java
String[] args
```
🇨 In C, we write:
```C
int main(int argc, char *argv[])
```
☕ In Java:
```java
public static void main(String[] args)
```

#### 📋 What are these arguments? 🤔

💻 In both languages, we can pass information to the program directly from the command line. ⌨️🚀

🇨 In C:

* `argc` tells us how many arguments were passed;
* `argv` contains the arguments as array of strings.

☕ In Java:
* `args` is an array of `String`s;
* each element holds one argument passed to the program.

🎯 So the core concept is very similar:

🇨
- `argc` → how many arguments
- `argv` → which arguments

☕
- `args` → the arguments, inside a String array

💡 The naming is different, *but the concept is completely familiar*. 🧠☕

## 🖨️ 7. 📢 `printf()` vs `System.out` 💻🔥

### 🇨 Our old friend `printf()` 🤝

In C, you're used to:
```C
printf("Hello world!\n");
```

☕ In Java, we write:
```java
System.out.println("Hello world!");
```

🎯 Java offers a few ways to produce output. 🖨️☕

|☕ Java	| 🎯 What does it do? |
| ---: | --- |
| System.out.print() | prints without adding a new line |
| System.out.println() | prints and moves to the next line |
| System.out.printf() | prints formatted text |

### ➡️ `print()` 🖨️
```java
System.out.print("Hello ");
System.out.print("world!");
```

📺 Output: `Hello world!`

### ↩️ `println()` 📝
```java
System.out.println("Hello");
System.out.println("world!");
```

📺 Output:

```
Hello
world!
```

### 🎯 `printf()` makes a comeback 😎

If you know C, this will feel familiar right away:
```C
printf("Number: %d", n);
```

☕ Java:

```java
System.out.printf("Number: %d%n", n);
```

🔥 The idea is identical: *format specifiers and values are combined in a single call*.

#### ⚡ Eclipse Pro Tip: *Don't type everything manually*! ⌨️🚀

😱 Typing this every time:

```java
System.out.println();
```

can get repetitive pretty quickly. 😂⌨️

💡 In Eclipse, simply type `sout` and press `CTRL + SPACE`.

⚡ Eclipse will complete it automatically to:

```java
System.out.println();
```

🎯 **The IDE won't program for you**: *it just saves you unnecessary typing*. 🧠🛠️

## 📚 8. 🔌 `#include` in C vs `import` in Java 🧠☕

### 🇨 In C: `#include`

To use standard functions like `printf()` and `scanf()`, we used:

```C
#include <stdio.h>
```

🧠 We're telling the compiler that we want to use the declarations from the `stdio.h` header file. 📚

☕ In Java, we use `import` instead:

```java
import java.util.Scanner;
```

🎯 We are telling the compiler that we want to use the `Scanner` class from the `java.util` package. 📦☕

## 📦 9. 🗂️ **Packages**: *Keeping Code Organized* 🧭

☕ Java organizes classes into packages. 📦

Think of a package as an organizational namespace for grouping related code together. 🗂️🧠

#### Example:

```java
package school.programs;
```

📁 Imagine a folder structure like:

```
school
└── programs
	├── Main.java
	├── Calculations.java
	└── Utility.java
```

🎯 No need to overcomplicate it for now: just keep in mind that Java uses a clear system for organizing large codebases. 🧠📚

## 🔢 10. 🧮 Primitive Types: Java Speaks C ☕

### 🧠 A lot of this will look familiar 👀

Java comes with several primitive data types:

| Type ☕ | Example 🔢 | Usage |
| ---: | --- | --- |
| byte | 100 | small integers |
| short	| 1000 | short integers |
| int | 42 | standard integers (most common) |
| long | 100000L | large integers |
| float | 3.14f | floating-point numbers |
| double | 3.14159 | double-precision floating point |
| char | 'A' | single character (Unicode / UTF-8) |
| boolean | true / false | logical boolean values |

🎯 Here's the reassuring part:
```java
int age = 18;
double height = 1.75;
char initial = 'B';
boolean passed = true;
```

🧠 If you know how to declare variables in C, you're already right at home. 🚀

## 🧵 11. 💬 String: *Working with Text* ☕

### 🇨 In C, strings are character arrays 🧩

You've probably used:

```c
char name[] = "Mario";
```

☕ In Java, we simply write:
```java
String name = "Mario";
```

🎯 This is one of the first convenient differences you'll notice. ⚡
```java
String message = "Hello students!";
```

📌 `String` is not a primitive type like `int` or `double`: it is a class from Java's built-in library. 🧠

🚦 *We don't need to dive into the details yet—just focus on using it effectively*. ☕

## ⚠️ 12. 🧠 `==` vs `.equals()`: A Common Pitfall 🎭

When comparing numbers, we do:

```java
int a = 10;
int b = 10;

if (a == b) {
	...
}
```

👍 Pretty straightforward.

🚨 However, with `String` objects, we need to be careful.

To compare the actual contents of two strings, use `.equals()`:

```java
String a = "hello";
String b = "hello";

if (a.equals(b)) {
	System.out.println("The strings contain the exact same text.");
}
```

🎯 Golden rule to keep in mind:

> 🧠 `String` → use `.equals()` to compare text contents. ☕

⚠️ Don't use `==` as a general rule for comparing string values, as it checks whether two variables point to the same object in memory, not whether the text is identical. 🔍

📌 We don't need to go deeper into memory references right now: we'll revisit this distinction when covering Object-Oriented concepts. 🚪🧱

## ⌨️ 13. 🎤 Keyboard Input: Reading User Data ☕

### 🇨 In C, we used `scanf()` 🎯

```C
int n;

printf("Enter a number: ");
scanf("%d", &n);
```

☕ In Java, we use `Scanner`:

```java
import java.util.Scanner;
```

Then:

```java
Scanner scan = new Scanner(System.in);

System.out.print("Enter a number: ");
int n = scan.nextInt();
```

🎯 Notice the variable name:

```java
Scanner scan
```

💡 Naming it `scan` is a deliberate nod to C's `scanf()`—the underlying concept of reading input from the keyboard remains identical. 🧠🔗

📌 No need to memorize every method in `Scanner` right away; just treat it as your tool for reading user input. ⌨️☕

## 🧮 14. 🔥 C vs Java: Calculating a Square Root 📐

### 🇨 C Version 🧠

In **C**, we include the math library:
```C
#include <stdio.h>
#include <math.h>

int main() {
	double n;

	printf("Enter a number: ");
	scanf("%lf", &n);

	printf("The square root is: %.2f", sqrt(n));

	return 0;
}
```

📚 Here we have:

```c
#include <math.h>
```

and we use:

```c
sqrt(n)
```

🎯 `sqrt()` calculates the square root.

### ☕ Java Version 🚀
```java
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter a number: ");
		double n = scan.nextDouble();
		System.out.printf("The square root is: %.2f%n", Math.sqrt(n));
	}
}
```

🔥 Look at how the concepts map across:

| 🇨 C | ☕ Java |
| --- | --- |
| `#include <stdio.h>` | `import java.util.Scanner` |
| `#include <math.h>` | `Math` is in `java.lang`, automatically available |
| `scanf()` | `scan.nextDouble()` |
| `printf()` | `System.out.printf()` |
| `sqrt(n)` | `Math.sqrt(n)` |

🧠 This exact mental mapping makes picking up Java much faster.

## 🧠 15. 📦 `java.util.Scanner` vs `java.lang.Math` 🔬

### 🎯 Two tools, two different import behaviors

In our previous program, we wrote:

```java
import java.util.Scanner;
// Scanner belongs to package: java.util
```

📦 But for square root, we used:

```java
Math.sqrt(n)
```

without needing:

```java
import java.lang.Math;
```

#### 🤔 Why?

☕ Classes inside the `java.lang` package are automatically imported into every Java file. ⚙️

🎯 In summary:

```java
Scanner
```

- ➡️ belongs to `java.util`
- ➡️ requires an explicit `import`.

```java
Math
```

- ➡️ belongs to `java.lang`
- ➡️ imported automatically.

💡 Not every standard utility requires a manual import statement. 🧠☕

## 📦 16. 🧱 Arrays: Where Java Starts Getting Clever 😎

### 🇨 In C

You're probably used to writing:

```C
int a[10];
```

📌 The array size is specified directly in the variable declaration.

☕ In Java, we declare the variable like this:

```java
int[] a;
```

🎯 This declaration means:

> 🧠 `a` is a variable that can refer to an array of integers.

To actually allocate the memory for the array:

```java
a = new int[10];
```

Or combined into a single line:

```java
int[] a = new int[10];
```

🔥 This syntax style:

```java
int[] a;
```

is preferred in Java because it clearly indicates that `a` is of type "integer array".

## 📏 17. 🔍 `a.length`: Arrays Know Their Own Size ☕

### 🇨 In C

When working with:

```C
int a[10];
```

you have to manually track or pass around the array size.

### ☕ In Java:

```java
int[] a = new int[10];
System.out.println(a.length);
```

📺 Output: `10`

🎯 An array's size is always accessible via:
```java
a.length
```

⚠️ **Note:** for arrays, it's `.length` (a property), not `.length()` (a method).

## 🔄 18. 🏃‍♂️ The `for` Loop: Feel Right at Home 🏠☕

### 🇨 C

```C
for (int i = 0; i < 10; i++) {
	printf("%d
", a[i]);
}
```

### ☕ Java:

```java
for (int i = 0; i < a.length; i++) {
	System.out.println(a[i]);
}
```

🎯 The structure is identical:

```
initialization
	↓
condition
	↓
increment
```

🔥 The main takeaway: you don't need to relearn control flow from scratch.

## 🎁 19. 🐇 Bonus Track: The `for-each` Loop ☕

Java provides an even cleaner syntax to iterate through elements of an array:

```java
for (int value : a) {
	System.out.println(value);
}
```

🧠 You can read this as:

> 🔎 “For each `value` in array `a`, run this block.”

🇨 Standard C doesn't have a native syntax like this.

☕ In Java:

```java
for (int value : a)
```

🔥 Fewer counters, fewer indices, and zero chance of off-by-one errors like `i <= ...`.

## 🧪 20. 🚀 Complete Mini Program: Input + Calculation + Output

🎯 Let's combine everything we've covered into a single clean script, without OOP syntax getting in the way. 🧠☕

```java
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		System.out.print("Enter a number: ");

		double n = scan.nextDouble();
		double result = Math.sqrt(n);

		System.out.printf("The square root of %.2f is %.2f%n", n, result);
	}
}
```

🔍 We've already put into practice:

- 📚 `import`
- 📦 package structures
- 🧱 class wrappers
- 🚪 `main` entry points
- ⌨️ user input
- 🔢 `double` types
- 🧮 `Math.sqrt()`
- 📢 `System.out.printf()`
- ☕ Java 26 environment

🎯 And we haven't even had to touch complex OOP patterns yet. 😎

## 🆚 21. ⚔️ C → Java: Mental Cheat Sheet 🧠

| 🧩 Concept | 🇨 C | ☕ Java |
| --- | --- | --- |
| Entry Point | `main()` | `main()` inside a class |
| Header / Libraries | `#include` | `import` |
| Code Organization | files / headers | `package` |
| Simple Output | `printf()` | `System.out.print()` |
| Output with Newline | `printf(... "\n")` | `System.out.println()` |
| Formatted Output | `printf()` | `System.out.printf()` |
| Input | `scanf()` | `Scanner` |
| Reading Variables | `scanf("%d", &n)` | `scan.nextInt()` |
| Integers | `int` | `int` |
| Floating Point | `double` | `double` |
| Character | `char` | `char` |
| Boolean | `_Bool` / `bool` (via library) | `boolean` |
| Strings | `char[]` | `String` |
| String Comparison | `strcmp()` | `.equals()` |
| Array Declaration | `int a[N]` | `int[] a` |
| Array Length | tracked manually | `a.length` |
| Standard For Loop | `for` | `for` |
| For-Each Loop | not native | `for (type x : array)` |
| Square Root | `sqrt()` | `Math.sqrt()` |


## 🧠 22. 🎯 The Main Takeaway: You're Not Starting Over 🚀

💡 Moving from C to Java, the core logic and constructs remain familiar. 🔄

| 🇨 C | ☕ Java |
| --- | --- |
| variables | variables |
| if statements | if statements |
| while loops | while loops |
| for loops | for loops |
| arrays | arrays |
| functions | methods |
| input | input |
| output | output |

☕ The syntax adapts in a few places, the tooling improves, and how code gets compiled and executed changes. ⚙️

🔥 Most importantly, Java raises the abstraction level, handling low-level boilerplate for you.

🎯 Your goal isn't to unlearn C.

🚀 It's to use C as a solid foundation to pick up Java effortlessly.

## 🧭 23. 🗺️ What Lies Ahead

📌 In this first guide, we deliberately bypassed object-oriented programming. 🚫🧱

🎯 Instead, we built solid foundations:

- ☕ Java's background and core philosophy;
- 🌍 The JVM and cross-platform portability;
- 🛠️ The JDK toolchain;
- 🖥️ Eclipse IDE setup;
- 🚪 The `main` method;
- 📢 Printing output;
- ⌨️ Keyboard input;
- 📚 `import` statements;
- 📦 `package` structure;
- 🔢 Primitive data types;
- 🧵 The `String` class;
- ⚠️ `==` vs `.equals()`;
- 🧮 Math operations with `Math.sqrt()`;
- 📦 Working with `array`s;
- 🔄 Standard `for` loops;
- 🐇 The `for-each` loop.

🔥 Everything else will follow naturally.

🧠 First we learn to walk in this new ecosystem.

🚀 Then we run.

## 🏁☕ 24. 🔥 Wrap-up: The Hard Times Are Over… Maybe 😏

😂 After a year in C, you've survived `printf()`, `scanf()`, `&`, `*`, raw arrays, manual memory management, and all those low-level hurdles. 🧨💻

### ☕ Now comes Java.

🚀 A language designed to automate tedious manual work so you can focus directly on application logic. 🧠⚡

😎 ***The tough days of C are behind you***.

☕ *Java makes things cleaner*.

😏 **...at least until we introduce OOP**.

🔥 ***But that's a story for another day*** 😵‍💫.

---

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

---

![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>

<!-- Italiano -->

# ☕🚀 Guida Galattica a Java: dal C al mondo JVM 🌍💻

> 🎬 **Ragazzi, preparatevi: non stiamo imparando a programmare da zero. 😎🧠**
> 🚀 Avete già passato un anno a combattere con il C, `printf()`, `scanf()`, array, puntatori e parentesi graffe. ⚔️💻
> ☕ Adesso cambiamo linguaggio, ma non cambiamo il modo di ragionare: *portiamo con noi tutto quello che sappiamo e scopriamo quanto può diventare più snello scrivere codice con Java.* 🔥

## ☕ 1. 🌍 **Java**: il linguaggio che voleva andare ovunque 🚀

### 🕰️ Da dove arriva Java? 🌱☕

Java nasce negli anni '90 all'interno di **Sun Microsystems**, con un obiettivo ambizioso: creare un linguaggio capace di eseguire lo stesso programma su piattaforme differenti. 🌍💻

#### 🎯 L'idea rivoluzionaria viene riassunta nel celebre motto:

> ☕ *Write Once, Run Anywhere* 🌍🚀

💡 **Scrivi una volta, esegui ovunque**. 🧠⚡

🧱 Con il C, invece, il programma viene normalmente compilato per una specifica piattaforma, producendo codice macchina legato all'architettura e al sistema operativo. 💻⚙️

☕ Java introduce un passaggio intermedio: il programma non viene trasformato direttamente nel linguaggio della macchina, ma in **bytecode**, eseguito poi dalla **JVM**. 🔄🧠

🇨 C
```text
Codice sorgente
	↓
Compilatore
	↓
Codice macchina
	↓
CPU / Sistema operativo
```

☕ Java
```text
Codice sorgente
	↓
Compilatore
	↓
Bytecode
	↓
JVM
	↓
Sistema operativo
```

🎯 Ed è qui che **Java** *cambia le regole del gioco*. ☕🎮

## ⚙️ 2. 🧠 **JVM**, **JRE** e **JDK**: *la famiglia Java* 👨‍👩‍👧‍👦☕

### 🧠 **JVM**: *Java Virtual Machine* ⚙️

☕ La [**JVM**](https://it.wikipedia.org/wiki/Macchina_virtuale_Java) (*Java Virtual Machine*) è la **macchina virtuale** che esegue il **bytecode** Java. 💻🔄

🎯 Il programma Java produce bytecode e la JVM si occupa di eseguirlo sul sistema operativo in uso. 🌍⚙️

`Java → Bytecode → JVM → 🪟 Windows / 🐧 Linux / 🍎 macOS`

🚀 Questo è uno dei motivi per cui Java può mantenere la promessa di *"Write Once, Run Anywhere"*. 🌍☕

### 🏃 **JRE**: *Java Runtime Environment* ☕

📦 Il [**JRE**](https://it.wikipedia.org/wiki/Java_Runtime_Environment) rappresenta l'ambiente necessario per eseguire applicazioni Java. ▶️💻

🧠 In termini concettuali possiamo pensarlo come:

☕ **JRE** = *ambiente per eseguire Java*. ▶️

> ⚠️ Nello sviluppo moderno, però, non è necessario installare separatamente un vecchio **JRE** come si faceva in passato: installando una **JDK** moderna abbiamo già ciò che serve per eseguire programmi Java. 🛠️☕

### 🛠️ **JDK**: *Java Development Kit* 🚀

🎯 La [**JDK**](https://it.wikipedia.org/wiki/Java_Development_Kit) è quella che interessa a noi programmatori. 💻👨‍💻

📦 Contiene gli strumenti necessari per sviluppare, compilare ed eseguire programmi Java. ⚙️☕

```
JDK 🛠️
	├── strumenti di sviluppo
	├── compilatore javac
	├── JVM
	└── librerie Java
```

🧠 In parole semplici:

> 🔥 **JDK** = la cassetta degli attrezzi del programmatore Java. 🧰☕

## 📥 3. 🛠️ Cosa dobbiamo installare? 💻☕

### ☕ JDK 26: il motore di Java 🚀

📦 Per lavorare useremo JDK 26, che contiene gli strumenti necessari per scrivere e compilare i nostri programmi Java. 🛠️☕

- 🌐 Download ufficiale **Oracle JDK 26**: [https://www.oracle.com/java/technologies/downloads/](https://www.oracle.com/java/technologies/downloads/)
- 🌐 Alternativa **OpenJDK 26**: [https://jdk.java.net/26/](https://jdk.java.net/26/)

* 🪟 **Windows**: scaricate la versione adatta alla vostra architettura, normalmente `x64` sui PC moderni. 💻
* 🍎 **macOS**: scegliete il pacchetto corrispondente al vostro processore, Intel oppure Apple Silicon. 🖥️
* 🐧 **Linux**: scegliete il pacchetto compatibile con la vostra distribuzione o utilizzate il metodo di installazione previsto dal sistema. 🐧

#### 🎯 La cosa importante:
> Eclipse non sostituisce la JDK. 🚨

☕ La JDK contiene gli strumenti Java; Eclipse è l'ambiente che useremo per lavorare più comodamente con quegli strumenti. 🛠️🖥️

### 🖥️ 4. 🌌 **Eclipse**: *il nostro laboratorio Java* 🔬☕

#### 🧰 Che cos'è Eclipse? 💻

[Eclipse IDE](https://it.wikipedia.org/wiki/Eclipse_IDE) è un ambiente di sviluppo integrato, cioè un programma progettato per aiutarci a scrivere, organizzare, compilare, eseguire e controllare il nostro codice. 🧠⚙️

🎯 Noi useremo:
☕ ***Eclipse IDE for Enterprise Java and Web Developers*** 💻🚀

* 🌐 Download ufficiale Eclipse:
[https://www.eclipse.org/downloads/packages/release/2026-09/r/eclipse-ide-enterprise-java-and-web-developers](https://www.eclipse.org/downloads/packages/release/2026-09/r/eclipse-ide-enterprise-java-and-web-developers)

📦 Eclipse ci permette di avere in un unico ambiente:

- ✍️ editor del codice;
- ▶️ esecuzione dei programmi;
- 🐞 strumenti di debugging;
- 📁 gestione dei progetti;
- 🔎 completamento automatico;
- ⚡ suggerimenti e scorciatoie;
- 🚨 segnalazione degli errori.

> 💡 La **JDK** è il motore. **Eclipse** è il cruscotto. 🚗☕

## 🧱 5. 🏁 Il primo programma Java: perché c'è una classe? ☕
🇨 In C partiamo da `main()` 🚀
```C
#include <stdio.h>

int main() {
	printf("Forza Napoli!\n");
	return 0;
}
```

🎯 Il punto di ingresso del programma è la funzione: `main()`

☕ In Java il programma principale è invece scritto all'interno di una classe:
```java
public class Main {
	public static void main(String[] args) {
		System.out.println("Forza Napoli!");
	}
}
```

#### ⚠️ Attenzione:
> in questa guida non stiamo studiando la programmazione a oggetti. 🚫🧱

📦 Per ora consideriamo semplicemente la classe come il contenitore sintattico nel quale Java richiede che si trovi il main. 🧠📦

🎯 *L'OOP arriverà più avanti*. Adesso ci interessa imparare a parlare Java. ☕🗣️

## 🧩 6. 🔍 Il misterioso public static void main(String[] args) 🧠☕

### 🧱 Scomponiamolo senza paura 🔬

```java
public static void main(String[] args)
```

🧠 Per questa prima guida ci basta sapere che questa è la firma del metodo che Java utilizza come punto di ingresso del programma. 🚪☕

📌 La parte che ci interessa confrontare con C è:
```java
String[] args
```
🇨 In C possiamo avere:
```C
int main(int argc, char *argv[])
```
☕ In Java:
```java
public static void main(String[] args)
```

#### 📋 E cosa sono questi argomenti? 🤔

💻 In entrambi i casi possiamo fornire informazioni al programma direttamente dalla riga di comando. ⌨️🚀

🇨 In C:

* `argc` indica quanti argomenti sono stati forniti;
* `argv` contiene gli argomenti sotto forma di stringhe.

☕ In Java:
* `args` è un array di `String`;
* ogni elemento contiene un argomento passato al programma.

🎯 Quindi il concetto è molto simile:

🇨
- `argc` → quanti argomenti
- `argv` → quali argomenti

☕
- `args` → gli argomenti, dentro un array di String

💡 Il nome cambia, *ma l'idea non è poi così aliena*. 🧠☕

## 🖨️ 7. 📢 `printf()` contro `System.out` 💻🔥

### 🇨 Il vecchio amico `printf()` 🤝

In C siete abituati a:
```C
printf("Ciao mondo!\n");
```

☕ In Java troviamo:
```java
System.out.println("Ciao mondo!");
```

🎯 E qui Java ci offre più forme di output. 🖨️☕

|☕ Java	| 🎯 Cosa fa? |
| ---: | --- |
| System.out.print() | stampa senza andare a capo |
| System.out.println() | stampa e va a capo |
| System.out.printf() | stampa usando una formattazione |

### ➡️ `print()` 🖨️
```java
System.out.print("Ciao ");
System.out.print("mondo!");
```

📺 Risultato: `Ciao mondo!`

### ↩️ `println()` 📝
```java
System.out.println("Ciao");
System.out.println("mondo!");
```

📺 Risultato:

```
Ciao
mondo!
```

### 🎯 `printf()` ritorna in scena 😎

Se conoscete C, questa vi sembrerà subito familiare:
```C
printf("Numero: %d\n", n);
```

☕ Java:

```java
System.out.printf("Numero: %d%n", n);
```

🔥 La filosofia è molto simile: *specificatori di formato e valori vengono combinati nello stesso comando*.

#### ⚡ Bonus Eclipse: *non scrivere tutto*! ⌨️🚀

😱 Scrivere ogni volta:

```java
System.out.println();
```

può diventare un piccolo esercizio di resistenza delle dita. 😂⌨️

💡 In Eclipse potete digitare: `sout` e premere: `CTRL + SPAZIO`

⚡ Eclipse completerà automaticamente:

```java
System.out.println();
```

🎯 **L'IDE non programma al posto vostro**: *elimina semplicemente il lavoro meccanico*. 🧠🛠️

## 📚 8. 🔌 `\#include` in C, `import` in Java 🧠☕

### 🇨 In C: `#include`
Per utilizzare funzioni come `printf()` e `scanf()` abbiamo visto:
```C
#include <stdio.h>
```
🧠 Stiamo dicendo al compilatore che vogliamo utilizzare le dichiarazioni presenti nell'header `stdio.h`. 📚

☕ In Java utilizziamo invece `import`.

```java
import java.util.Scanner;
```


🎯 Stiamo dicendo al compilatore che nel nostro codice vogliamo utilizzare la classe `Scanner` appartenente al package `java.util`. 📦☕

## 📦 9. 🗂️ **Package**: *mettere ordine nel codice* 🧭

☕ Java organizza le classi all'interno di package. 📦

Un package può essere visto come uno spazio organizzativo che permette di raggruppare codice correlato. 🗂️🧠

#### Esempio:

```java
package scuola.programmi;
```

📁 Possiamo immaginare:

```
scuola
└── programmi
	├── Main.java
	├── Calcoli.java
	└── Utility.java
```

🎯 Per ora non serve approfondire oltre: ci interessa capire che Java possiede un sistema strutturato per organizzare grandi quantità di codice. 🧠📚

## 🔢 10. 🧮 I tipi primitivi: Java parla come il C ☕

### 🧠 Molte cose vi sembreranno familiari 👀

Java possiede diversi tipi primitivi:

|Tipo ☕ | Esempio 🔢 | Utilizzo |
| ---: | --- | --- |

| byte | 100 | interi piccoli |
| short	|1000 | interi |
| int |42 | interi, il più comune |
| long | 100000L | interi grandi |
| float | 3.14f	decimali |
| double | 3.14159 | decimali più precisi |
| char | 'A' | singolo carattere (ma unicode: `utf-8`) |
| boolean | true / false | valori logici |

🎯 Ecco una cosa rassicurante:
```java
int eta = 18;
double altezza = 1.75;
char iniziale = 'B';
boolean promosso = true;
```

🧠 Se sapete dichiarare variabili in C, qui non partite da zero. 🚀

## 🧵 11. 💬 String: *quando il testo entra in gioco* ☕

### 🇨 In C le stringhe sono array di caratteri 🧩

Avete probabilmente incontrato:

```c
char nome[] = "Mario";
```

☕ In Java possiamo scrivere semplicemente:
```java
String nome = "Mario";
```

🎯 Questa è una delle differenze che noterete immediatamente. ⚡
```java
String messaggio = "Ciao studenti!";
```

📌 `String` non è un tipo primitivo come `int` o `double`: è una classe della libreria Java. 🧠

🚦 *Non approfondiamo ancora il motivo: per ora ci interessa usarla correttamente*. ☕

## ⚠️ 12. 🧠 `==` oppure `.equals()`? Il piccolo tranello 🎭

Con i numeri siamo abituati a:

```java
int a = 10;
int b = 10;

if (a == b) {
	...
}
```

👍 Fin qui tutto tranquillo.

🚨 Con le `String`, invece, dobbiamo fare attenzione.

Per confrontare il contenuto di due stringhe usiamo:

```java
String a = "ciao";
String b = "ciao";

if (a.equals(b)) {
	System.out.println("Le stringhe contengono lo stesso testo.");
}
```

🎯 Regola pratica da ricordare:

> 🧠 `String` → `.equals()` per confrontare il contenuto. ☕

⚠️ `==` non va usato come regola generale per confrontare il contenuto delle stringhe, perché confronta i riferimenti agli oggetti e non il testo contenuto. 🔍

📌 Per ora non serve andare oltre: questa distinzione tornerà molto più avanti quando parleremo seriamente di oggetti. 🚪🧱

## ⌨️ 13. 🎤 Input da tastiera: facciamo parlare l'utente ☕

### 🇨 In C abbiamo `scanf()` 🎯

```C
int n;

printf("Inserisci un numero: ");
scanf("%d", &n);
```

☕ In Java possiamo utilizzare `Scanner`.

```java
import java.util.Scanner;
```

Poi:

```java
Scanner scan = new Scanner(System.in);

System.out.print("Inserisci un numero: ");
int n = scan.nextInt();
```

🎯 Notate il nome della variabile:

```java
Scanner scan
```

💡 `scan` richiama volutamente `scanf()` del **C**: il concetto didattico è lo stesso, cioè acquisire dati dalla tastiera. 🧠🔗

📌 Non ci interessa ancora studiare tutti i metodi di `Scanner`: per ora ci basta sapere che è uno strumento per leggere input dall'utente. ⌨️☕

## 🧮 14. 🔥 C vs Java: calcoliamo una radice quadrata 📐

### 🇨 Versione C 🧠

In **C** possiamo utilizzare la libreria matematica:
```C
#include <stdio.h>
#include <math.h>

int main() {
	double n;

	printf("Inserisci un numero: ");
	scanf("%lf", &n);

	printf("La radice quadrata è: %.2f\n", sqrt(n));

	return 0;
}
```

📚 Qui incontriamo:

```c
#include <math.h>
```

e utilizziamo:

```c
sqrt(n)
```

🎯 `sqrt()` calcola la radice quadrata.

### ☕ Versione Java 🚀
```java
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.print("Inserisci un numero: ");
		double n = scan.nextDouble();
		System.out.printf("La radice quadrata è: %.2f%n", Math.sqrt(n));
	}
}
```

🔥 Guardate cosa è successo:

| 🇨 C | ☕ Java |
| --- | --- |
| `#include <stdio.h>` | `import java.util.Scanner` |
| `#include <math.h>` | `Math` è in `java.lang`, disponibile automaticamente |
| `scanf()` | `scan.nextDouble()` |
| `printf()` | `System.out.printf()` |
| `sqrt(n)` | `Math.sqrt(n)` |

🧠 Questo è esattamente il tipo di traduzione mentale che vogliamo imparare.

## 🧠 15. 📦 `java.util.Scanner` e `java.lang.Math` 🔬

### 🎯 Due strumenti, due situazioni diverse

Nel programma precedente abbiamo utilizzato:

```java
import java.util.Scanner;
// Scanner appartiene al package: java.util
```

📦 Invece abbiamo scritto:

```java
Math.sqrt(n)
```

senza:

```java
import java.lang.Math;
```

#### 🤔 Perché?

☕ Perché le classi del package `java.lang` vengono rese disponibili automaticamente ai programmi Java. ⚙️

🎯 Quindi:

```java
Scanner
```

- ➡️ appartiene a `java.util`
- ➡️ lo importiamo esplicitamente.

```java
Math
```

- ➡️ appartiene a `java.lang`
- ➡️ non dobbiamo importarlo.

💡 Non tutte le librerie Java devono essere importate manualmente. 🧠☕

## 📦 16. 🧱 Gli array: qui Java comincia a diventare interessante 😎

### 🇨 In C

Probabilmente avete scritto:

```C
int a[10];
```

📌 La dimensione dell'array compare direttamente nella dichiarazione.

☕ In Java possiamo scrivere:

```java
int[] a;
```

🎯 Questa dichiarazione significa:

> 🧠 `a` sarà una variabile che può riferirsi a un array di interi.

Per creare effettivamente l'array:

```java
a = new int[10];
```

Oppure direttamente:

```java
int[] a = new int[10];
```

🔥 Questa forma è generalmente preferibile:

```java
int[] a;
```

perché rende immediatamente evidente che stiamo dichiarando un array di `int`.

## 📏 17. 🔍 a.length: l'array conosce la propria dimensione ☕

### 🇨 In C

Se abbiamo:

```C
int a[10];
```

dobbiamo sapere che l'array contiene 10 elementi.

### ☕ In Java:

```java
int[] a = new int[10];
System.out.println(a.length);
```

📺 Risultato: `10`

🎯 La dimensione è disponibile tramite:
```java
a.length
```

⚠️ **Attenzione:** per gli array è `.length`, non `.length()`.

## 🔄 18. 🏃‍♂️ Il for: qui vi sentirete a casa 🏠☕

### 🇨 C

```C
for (int i = 0; i < 10; i++) {
	printf("%d\n", a[i]);
}
```

### ☕ Java:

```java
for (int i = 0; i < a.length; i++) {
	System.out.println(a[i]);
}
```

🎯 La struttura è praticamente la stessa:

```
inizializzazione
	↓
condizione
	↓
incremento
```

🔥 E questo è importante: non dovete reimparare la programmazione da capo.

##🎁 19. 🐇 Bonus Track: il `for-each` ☕

Java offre anche una forma più compatta per attraversare tutti gli elementi di un `array`:

```java
for (int valore : a) {
	System.out.println(valore);
}
```

🧠 Si può leggere così:

> 🔎 “Per ogni valore contenuto nell'array a, esegui questo blocco.”

🇨 In C non avete una sintassi equivalente nativa con questa forma.

☕ In Java:

```java
for (int valore : a)
```

🔥 Meno contatori, meno indici, meno possibilità di inciampare in `i < ...`.

## 🧪 20. 🚀 Mini programma completo: input + calcolo + output

🎯 Mettiamo insieme quello che abbiamo imparato senza introdurre OOP. 🧠☕

```java
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		System.out.print("Inserisci un numero: ");

		double n = scan.nextDouble();
		double ris = Math.sqrt(n);

		System.out.printf("La radice quadrata di %.2f è %.2f%\n", n, ris);
	}
}
```

🔍 Qui dentro abbiamo già incontrato:

- 📚 `import`
- 📦 package
- 🧱 classe contenitore
- 🚪 `main`
- ⌨️ input da tastiera
- 🔢 `double`
- 🧮 `Math.sqrt()`
- 📢 `System.out.printf()`
- ☕ Java 26

🎯 E non abbiamo ancora toccato l'OOP. 😎

## 🆚 21. ⚔️ C → Java: la tabella di conversione mentale 🧠

| 🧩 Concetto | 🇨 C | ☕ Java |
| --- | --- | --- |
| Punto di ingresso | `main()` | `main()` dentro una classe |
| Librerie/header | `#include` | `import` |
| Organizzazione | file/header | `package` |
| Output semplice | `printf()` | `System.out.print()` |
| Output con newline | `printf(... "\n")` | `System.out.println()` |
| Output formattato | `printf()` | `System.out.printf()` |
| Input | `scanf()` | `Scanner` |
| Variabile input | `scanf("%d", &n)` | `scan.nextInt()` |
| Interi | `int` | `int` |
| Decimali | `double` | `double` |
| Carattere | `char | char` |
| Booleano | `_Bool` / `bool` con libreria appropriata | `boolean` |
| Stringa | `char[]` | `String` |
| Confronto stringhe | `strcmp()` | `.equals()` |
| Array | `int a[N]` | `int[] a` |
| Dimensione array | spesso gestita separatamente | `a.length` |
| For classico | `for` | `for` |
| For-each | non nativo | `for (tipo x : array)` |
| Radice quadrata | `sqrt()` | `Math.sqrt()` |


## 🧠 22. 🎯 La vera lezione: non state ricominciando da zero 🚀

💡 Quando passate dal C a Java, molte strutture che conoscete rimangono familiari. 🔄

| 🇨 C | ☕ Java |
| --- | --- |
| variabili | variabili |
| if | if |
| while | while |
| for | for |
| array | array |
| funzioni | metodi |
| input | input |
| output | output |

☕ Cambia la sintassi in alcuni punti, cambiano gli strumenti, cambia il modo in cui il programma viene eseguito. ⚙️

🔥 Ma soprattutto cambia il livello di astrazione che il linguaggio mette a disposizione del programmatore.

🎯 Il vostro compito non è dimenticare il C.

🚀 È usarlo come trampolino per capire Java.

## 🧭 23. 🗺️ Il percorso che ci aspetta

📌 In questa prima tappa abbiamo volutamente evitato la programmazione a oggetti. 🚫🧱

🎯 Abbiamo costruito invece le fondamenta:

- ☕ nascita e filosofia di Java;
- 🌍 JVM e portabilità;
- 🛠️ JDK;
- 🖥️ Eclipse;
- 🚪 `main`;
- 📢 output;
- ⌨️ input;
- 📚 `import`;
- 📦 `package`;
- 🔢 tipi primitivi;
- 🧵 `String`;
- ⚠️ `==` e `.equals()`;
- 🧮 `Math.sqrt()`;
- 📦 `array`;
- 🔄 `for`;
- 🐇 `for-each`.

🔥 Il resto arriverà.

🧠 Prima impariamo a camminare nel nuovo linguaggio.

🚀 Poi inizieremo a correre.

## 🏁☕ 24. 🔥 Chiusura: i tempi duri sono finiti… forse 😏

😂 Dopo un anno di C avete affrontato `printf()`, `scanf()`, `&`, `*`, array, gestione manuale della memoria e altre piccole gioie della vita del programmatore. 🧨💻

### ☕ Ora arriva Java.

🚀 Un linguaggio che prova a togliervi una parte del lavoro meccanico e a farvi concentrare maggiormente sulla logica del programma. 🧠⚡

😎 ***I tempi duri del C sono finiti***.

☕ *Java è più snello*.

😏 **...almeno fino a quando non arriverà l'OOP**.

🔥 ***Ma quella è un'altra storia*** 😵‍💫.

<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)
[![gmail](https://img.shields.io/badge/gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:birg81@gmail.com)