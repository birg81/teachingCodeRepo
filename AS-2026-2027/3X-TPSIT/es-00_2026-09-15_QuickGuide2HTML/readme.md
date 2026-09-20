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

# 🌐 HTML: A Quick Guide to Start Building the Web

## 🚀 1. Before We Start: What Is HTML?

🌐 **HTML** stands for **HyperText Markup Language**.
🧠 HTML is the language used to **describe the structure of a Web page**.

#### 💡 Important:
*HTML is not really a programming language*.

🏷️ It is a **markup language**, which means that we use special elements called **tags** to tell the browser what the different parts of a page represent.

🌍 When we open a Web page, the browser reads the HTML document and interprets its structure, turning the code into a page displayed on the screen.

🎯 In other words, HTML tells the browser **"what is on the page"**, while other technologies, such as CSS and JavaScript, will later take care of its appearance and behavior.

## 🏷️ 2. The Fundamental Concept: the TAG

🏷️ A **tag** is an element HTML uses to describe a part of a page.
🔓 A tag is generally opened with `<` and `>` and closed with `</` and `>`.

💻 Here is a very simple example:

| 🧱 Element | 🔎 Meaning |
| --- | --- |
| `<p>` 🟢 | opening tag |
| `This is a paragraph.` 📝 | content |
| `</p>` 🔴 | closing tag |

🎯 The browser therefore interprets the code as **a text paragraph**.

💡 We can visualize the structure like this:

```text
<p>			→ opening
	text	→ content
</p>		→ closing
```

🧠 This idea is fundamental because it will accompany us throughout practically our entire journey into HTML.

## 🧱 3. An Element and a Tag Are Not Exactly the Same Thing

🧠 In school you will often hear "tag" and "element" used almost interchangeably, but technically there is a difference.

🏷️ The **tag** is the part enclosed in angle brackets.

🧩 An **HTML element**, on the other hand, includes the opening tag, content, and closing tag.

```html
<p>Hello students!</p>
```

- 🏷️ `<p>` is the opening tag.
- 🏷️ `</p>` is the closing tag.

🧩 The entire `<p>Hello students!</p>` block is the HTML element.

🎯 For now, though, let's not give ourselves a headache: *first learn to recognize and use tags correctly*. 😎

## 📁 4. HTML Files

📄 An HTML page is normally saved with the `.html` extension, 💻 for example:

`index.html` (this is the conventional name commonly used for an HTML page; when a folder contains several HTML files, a file named `index.html`, or sometimes `home.html`, is typically the one opened first)

🏷️ The `.html` extension tells the operating system and other tools that the file contains an HTML document.

🌐 The browser can then interpret the document and display it as a Web page.
⚠️ Do not confuse `page.html` with ❌ `page.txt`.
🧠 Even if both files contained exactly the same text, their extensions identify two different file types.

## 💻 5. Our Tool: Visual Studio Code

🛠️ To write HTML we will use **Visual Studio Code**, commonly abbreviated to **VS Code**.

💡 Technically, VS Code is a **source-code editor**, not a traditional full-featured IDE like Visual Studio, but for Web development it provides practically everything we need to get started.

🌍 It is available for **Windows, macOS, and Linux**.

🔗 **Official Visual Studio Code download:** [Download Visual Studio Code](https://code.visualstudio.com/Download)

🪟 If you use Windows, you can normally download the appropriate **Windows User Installer** for your architecture, such as x64.

🎯 Do not download strange versions from unknown websites: **get the software from the official website**. 🔐

## 📂 6. First Rule: WORK WITH FOLDERS

📁 When starting a new Web project, a good habit is to create a **dedicated project folder** first.

🧠 For example:

```text
HTML/
```

📂 Inside it we can then have:

```text
HTML/
└── index.html
```

🚀 But why open the folder in VS Code instead of opening `index.html` directly?

🧠 Because a Web project can grow quickly.

📁 Tomorrow we might have:

```text
HTML/
├── index.html
├── contact.html
├── about.html
├── css/
│	└── style.css
├── js/
│	└── script.js
└── images/
	├── logo.png
	└── photo.jpg
```

🎯 If we open a single file directly, we lose much of the project overview.
🚀 If we open **the project folder**, VS Code instead shows the whole structure in the **Explorer** panel.

## 🖱️ 7. Open the Folder in VS Code

📁 Create a folder, for example: `HTML`

- 💻 Launch VS Code.
- 📂 Select: `File → Open Folder`
- 🖱️ Choose the `HTML` folder.
- 👀 The project structure will appear on the left.
- 💡 Alternatively, you can **drag the folder directly into VS Code**.
- 🎯 This will soon become second nature: **one folder = one project**. 📂

## 📄 8. Create Our First HTML File

📁 In the **Explorer** section of VS Code, select our folder.

- ➕ Create a new file.
- ✏️ Name it: `index.html`

🌐 The name `index.html` is a very common convention for the home page of a Web site.

💡 For now, we do not need to worry about servers, databases, frameworks, or any other dark magic. 🧙‍♂️

- 🎯 We have a folder.
- 🎯 We have an HTML file.
- 🎯 Now we can write our first piece of Web code.

## 🧱 9. The Basic Structure of an HTML Page

🌐 An HTML page has a hierarchical structure.

💻 A minimal structure can be:

```html
<html>
	<head>
		<title>My page</title>
	</head>
	<body>
		<p>Hello world!</p>
	</body>
</html>
```

🧠 Let's pause for a moment and read this structure from the outside in.

- 🌐 `<html>` represents the HTML document.
- 🧠 `<head>` contains information about the document.
- 🏷️ `<title>` defines the page title displayed, for example, in the browser tab.
- 👁️ `<body>` contains the content that belongs to the visible page.
- 📝 `<p>` represents a paragraph.

## 🌐 10. The `<html>` Tag

🌐 The `<html>` tag represents the root element of the HTML document.

💻 In practice, the entire document lives inside it:

```html
<html>
	...
</html>
```

🧠 We can think of it as the **main container** of our page. 📦

## 🧠 11. The `<head>` Tag

🧠 `<head>` contains information and settings related to the document.

💻 For example:

```html
<head>
	<title>My page</title>
</head>
```

🎯 What we find inside `<head>` is not normally the main content displayed on the page.

⚙️ Later we will also find things such as metadata, links to CSS stylesheets, and other important elements here.

## 🏷️ 12. The `<title>` Tag

🏷️ `<title>` defines the title associated with the HTML document.

💻 Example:

```html
<title>My First Website</title>
```

🌐 When the page is opened in a browser, the title will normally appear in the page tab.

🧠 Important: `<title>` **does not mean "a title visible inside the page"**.

🎯 For headings displayed in the page content, we will use `<h1>`, `<h2>`, and so on.

## 👁️ 13. The `<body>` Tag

👁️ `<body>` contains the main content of the page.

💻 For example:

```html
<body>
	<h1>Welcome!</h1>
	<p>This is my first Web page.</p>
</body>
```

🌐 These elements will be displayed in the browser window.

🎯 If `head` contains information about the document, `body` mainly contains **the content the user is meant to see and interact with**.

## 📝 14. The `<p>` Tag

📝 The `<p>` tag represents a **paragraph**.

💻 Example:

```html
<p>HTML is the language used to describe the structure of Web pages.</p>
```

🧩 We can have multiple paragraphs:

```html
<p>This is the first paragraph.</p>
<p>This is the second paragraph.</p>
<p>This is the third paragraph.</p>
```

🎯 Each `<p>` element represents a separate paragraph.

## ↩️ 15. The `<br>` Tag

↩️ `<br>` means **line break**, that is, a new line.

💻 We can write:

```html
<p>
	First line<br>
	Second line<br>
	Third line
</p>
```

🌐 The browser will display the text on three lines.

⚠️ `<br>` is special because it normally has no content enclosed between an opening and closing tag.

❌ We do not write:

```html
<br></br>
```

🎯 We simply use:

```html
<br>
```

#### ⚠️ Note

Although browsers do not report an error, for tags that do not require a closing tag it is often good practice to use this form:

```html
<br/>
```

## 📚 16. Headings: from `<h1>` to `<h6>`

📚 HTML provides six levels of headings.

💻 They are:

```html
<h1>Main heading</h1>
<h2>Second-level heading</h2>
<h3>Third-level heading</h3>
<h4>Fourth-level heading</h4>
<h5>Fifth-level heading</h5>
<h6>Sixth-level heading</h6>
```

🧠 The `h` stands for **heading**.

📊 We can summarize them like this:

| 🏷️ Tag | 📚 Level | 🎯 Use |
| ---: | ---: | --- |
| `<h1>` | 1️⃣ | main heading |
| `<h2>` | 2️⃣ | main section |
| `<h3>` | 3️⃣ | subsection |
| `<h4>` | 4️⃣ | next level |
| `<h5>` | 5️⃣ | secondary heading |
| `<h6>` | 6️⃣ | most specific level |

🎯 `<h1>` represents the most important heading level.

📉 As we move toward `<h6>`, the heading's hierarchical level decreases.

⚠️ Do not choose `<h3>` simply because "I like it bigger".

🧠 Heading levels primarily represent **the logical structure of the document**, not just font size.

## 🧩 17. Putting It All Together

🚀 Now we can build a complete first page.

```html
<html>
	<head>
		<title>My First Website</title>
	</head>

	<body>
		<h1>Welcome to my website!</h1>
		<h2>About me</h2>
		<p>
			My name is Mario and I am learning
			how to build Web pages.
		</p>

		<h2>What I am learning</h2>
		<p>
			I am studying HTML.<br>
			Next I will study CSS.<br>
			Then JavaScript will arrive!
		</p>
	</body>
</html>
```

🎯 This small program already contains several fundamental concepts.

- 🧠 We have an HTML structure.
- 🧠 We have a `head` section.
- 🧠 We have a document title.
- 🧠 We have a `body`.
- 🧠 We have headings.
- 🧠 We have paragraphs.
- 🧠 We have line breaks.
- 🔥 And most importantly, we have written a real Web page.

## 📐 18. Indentation: Code Should Be Readable

📐 **Indentation** means moving code to the right to visually represent its hierarchical structure.

💻 Consider this example:

```html
<html>
	<head>
		<title>My page</title>
	</head>
	<body>
		<h1>Hello!</h1>
		<p>
			This is a paragraph.
		</p>
	</body>
</html>
```

👀 By looking at the code, we can immediately understand which elements are contained inside other elements.

🧠 Indentation is not required by the browser to understand the structure in this case, but it is **extremely important for us humans**.

🎯 A programmer writes code not only to make it work, but also to make it easier for other programmers to read and modify.

## ⌨️ 19. TAB or Spaces?

⌨️ VS Code can use tabs or spaces for indentation.

🎯 For this course we will follow one simple rule:

> 📐 **One indentation level = one TAB.**

💻 So:

```html
<html>
→	<head>
→	→	<title>My page</title>
→	</head>
</html>
```

🧠 The `→` symbol graphically represents a tab.

⚙️ In VS Code, we can check this setting from the status bar and the editor settings.

🔧 It is important that all files in a project follow a consistent convention.

## ↩️ 20. LF: the Line Ending Character

🧠 Every operating system needs a way to represent the end of a text line.

💻 Historically, different conventions have been used.

🪟 Windows normally uses **CRLF**.

🐧 Linux and many Unix environments use **LF**.

🍎 Modern macOS also uses **LF**.

🎯 In our project we can choose to use **LF**, so the code follows a convention consistent with many tools and development environments.

## ⚙️ 21. How to Set LF in VS Code

🖥️ Open your HTML file in VS Code.

👀 In the status bar at the bottom of the window, you will find the current line-ending format, for example: `CRLF`

- 🖱️ Click `CRLF`.
- 📋 A menu with the available options will appear.
- 🐧 Select: `LF`

🎯 From that point on, the file will use LF as its line-ending format.

⚙️ If you want to make this the default behavior, you can change the VS Code settings by searching for: `EOL`
🔧 The corresponding setting is: `Files: Eol`
🎯 Set it to: `\n`

🐧 VS Code will then use LF as the default line ending.

## 🧠 22. A Web Page Is a Hierarchical Structure

🌳 One of the most important ideas to take away is that HTML builds a **tree structure**.

💻 For example:

```text
html
├── head
│	└── title
│
└── body
	├── h1
	├── h2
	├── p
	└── p
```

🌳 Each element can contain other elements.

🧠 This characteristic is called **nesting**.

💻 For example:

```html
<body>
	<h1>My website</h1>
	<p>
		This text is inside
		the paragraph.
	</p>
</body>
```

🎯 `<body>` contains `<h1>` and `<p>`.

🎯 `<p>` contains the text.

🔥 Later, this structure will become essential when we work with CSS and JavaScript.

## 🐛 23. The Most Common Errors

🚨 When you are starting out, some mistakes are practically unavoidable.

🔴 **Forgetting the closing tag:**

```html
<p>This is a paragraph
```

🟢 Better:

```html
<p>This is a paragraph</p>
```

🔴 **Using the wrong tag name:**

```html
<paragraph>
```

🧠 HTML does not let us invent tags arbitrarily: we must use the elements defined by the standard.

🔴 **Incorrect nesting:**

```html
<p>
	<h1>Heading</p>
</h1>
```

🧠 Tags must be nested correctly.

🟢 For example:

```html
<h1>
	Heading
</h1>

<p>
	Paragraph
</p>
```

🎯 Learning HTML also means learning to **read the structure of the code** and identify where we opened and closed elements. 🔍

## ⚡ 24. A Powerful Shortcut: Emmet

🚀 VS Code includes tools that can make writing HTML dramatically faster.

💡 One of the most important is **Emmet**.

⌨️ For example, type: `!` or `html:5`

⚡ and press `TAB`. VS Code can automatically generate the initial structure of an HTML document.

💻 We will get something similar to:

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>

</body>
</html>
```

🎯 This shortcut will soon become one of your main tools. ⚔️💻
🧠 That does not mean we should learn only shortcuts.
🎯 First, we need to understand **what we are generating**.

## 🌐 25. From Code to Browser

- 🚀 We have written our HTML.
- 💾 Save the file: `Ctrl+S`
- 🌐 Now we can open `index.html` in a browser.
- 🖱️ We can double-click the file from the project folder.
- 🌍 The browser will read the HTML document and render it as a Web page.
- 💡 The basic cycle is therefore:

```text
⌨️ Write HTML
		↓
💾 Save the file
		↓
🌐 Open/refresh the browser
		↓
👀 See the result
		↓
🔧 Modify the code
		↓
🔄 Reload the page
```

🔥 This is one of the most enjoyable things about Web development: **you write code and can see the result immediately**.

## 🧪 26. Mini Lab: Build Your First Page

🎯 Now it's your turn.

- 📁 Create a folder called: `my-first-website`
- 📂 Open the folder in VS Code.
- 📄 Create: `index.html`

✏️ Write a page containing:

* 🌐 a complete HTML structure;
* 🏷️ a `<title>`;
* 📚 an `<h1>` containing your name;
* 📚 at least two `<h2>` headings;
* 📝 at least three `<p>` paragraphs;
* ↩️ at least one `<br>`;
* 📐 consistent indentation;
* 🐧 LF line endings.

#### 🔥 Goal:
create a page that introduces **yourself, your interests, and what you are currently learning about computer science**.

## 🧠 27. The Mental Map to Remember

🎯 If you remember this structure at the end of the first lesson, we have already hit the target. 🎯

```text
🌐 HTML
│
├── 🏷️ TAGS
├── 📁 .html FILES
├── 💻 VS CODE
├── 📂 PROJECT FOLDER
├── 🧱 STRUCTURE
│	├── <html>
│	├── <head>
│	├── <title>
│	└── <body>
├── 📝 CONTENT
│	├── <p>
│	├── <br>
│	└── <h1> ... <h6>
├── 📐 INDENTATION
└── 🐧 LF
```

🚀 From this point on, HTML stops being a mysterious acronym and becomes a concrete tool.

- 💻 You have a folder.
- 📄 You have a file.
- 🏷️ You have learned your first tags.
- 🌐 You have built a page.

🔥 And you have just started talking to the Web using its structural language.

---

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

---

![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>

<!-- Italiano -->
# 🌐 HTML: la guida veloce per iniziare a costruire il Web

## 🚀 1. Prima di cominciare: che cos'è HTML?

🌐 **HTML** significa **HyperText Markup Language**, cioè *linguaggio di marcatura per ipertesti*.
🧠 HTML è il linguaggio utilizzato per **descrivere la struttura di una pagina Web**.

#### 💡 Attenzione:
*HTML non è propriamente un linguaggio di programmazione*.

🏷️ È un **linguaggio di markup**, cioè un linguaggio nel quale utilizziamo speciali elementi chiamati **tag** per indicare al browser che cosa rappresentano le varie parti di una pagina.

🌍 Quando apriamo una pagina Web, il browser legge il documento HTML e ne interpreta la struttura, trasformando il codice in una pagina visualizzata sullo schermo.

🎯 In altre parole, HTML dice al browser **"che cosa c'è nella pagina"**, mentre altri strumenti, come CSS e JavaScript, ci permetteranno successivamente di occuparci dell'aspetto e del comportamento.

## 🏷️ 2. Il concetto fondamentale: il TAG

🏷️ Un **tag** è un elemento utilizzato da HTML per descrivere una parte della pagina.
🔓 Generalmente un tag viene aperto utilizzando `<` e `>` e viene chiuso utilizzando `</` e `>`.
💻 Ecco un esempio semplicissimo:

| 🧱 Elemento | 🔎 Significato |
| --- | --- |
| `<p>` 🟢 | apertura del tag |
| `Questo è un paragrafo.` 📝 | contenuto |
| `</p>` 🔴 | chiusura del tag |

🎯 Il browser interpreta quindi il codice come **un paragrafo di testo**.

💡 Possiamo rappresentare la struttura così:

```text
<p>        → apertura
   testo   → contenuto
</p>       → chiusura
```

🧠 Questa idea è fondamentale perché accompagnerà praticamente tutto il nostro viaggio nell'HTML.

## 🧱 3. Elemento e tag non sono esattamente la stessa cosa

🧠 Nella pratica scolastica spesso sentirete usare "tag" ed "elemento" quasi come sinonimi, ma tecnicamente c'è una differenza.

🏷️ Il **tag** è la parte racchiusa tra parentesi angolari.

🧩 L'**elemento HTML** comprende invece apertura, contenuto e chiusura.

```html
<p>Ciao studenti!</p>
```

- 🏷️ `<p>` è il tag di apertura.
- 🏷️ `</p>` è il tag di chiusura.

🧩 L'intero blocco `<p>Ciao studenti!</p>` è l'elemento HTML.

🎯 Per iniziare, però, non facciamoci venire il mal di testa: *impariamo prima a riconoscere e utilizzare correttamente i tag*. 😎


## 📁 4. I file HTML

📄 Una pagina HTML viene normalmente salvata con estensione: `.html`, 💻 per esempio:

`index.html` (questo è il nome predefinito che si da ad una pagina html, in oltre in caso di una cartella piena di file html, il file che si chiamerà `index.html`, od `home.html` sarà quello che verrà aperto come primo filo)

🏷️ L'estensione `.html` comunica al sistema operativo e agli strumenti che il file contiene un documento HTML.

🌐 Il browser può quindi interpretare il documento e visualizzarlo come pagina Web.
⚠️ Non confondiamo `pagina.html` con ❌ `pagina.txt`
🧠 Anche se dentro entrambi scrivessimo lo stesso testo, l'estensione identifica due tipi di file differenti.

## 💻 5. Il nostro strumento: Visual Studio Code

🛠️ Per scrivere HTML utilizzeremo **Visual Studio Code**, comunemente abbreviato in **VS Code**.

💡 Tecnicamente VS Code è un **editor di codice sorgente**, non un IDE tradizionale completo come Visual Studio, ma per lo sviluppo Web offre praticamente tutto ciò che ci serve per iniziare.

🌍 È disponibile per **Windows, macOS e Linux**.

🔗 **Download ufficiale di Visual Studio Code:** [Scarica Visual Studio Code](https://code.visualstudio.com/Download)

🪟 Se utilizzate Windows, potete scaricare normalmente il **Windows User Installer** appropriato alla vostra architettura, per esempio x64.

🎯 Non scaricate versioni strane da siti sconosciuti: **il software si scarica dal sito ufficiale**. 🔐


## 📂 6. Prima regola: lavoriamo con le CARTELLE

📁 Quando iniziamo un nuovo progetto Web, una buona abitudine è creare prima una **cartella dedicata al progetto**.

🧠 Per esempio:

```text
HTML/
```

📂 All'interno potremo poi avere:

```text
HTML/
└── index.html
```

🚀 Ma perché aprire la cartella in VS Code invece di aprire direttamente `index.html`?

🧠 Perché un progetto Web crescerà rapidamente.

📁 Domani potremmo avere:

```text
HTML/
├── index.html
├── contatti.html
├── chi-siamo.html
├── css/
│	└── style.css
├── js/
│	└── script.js
└── immagini/
	├── logo.png
	└── foto.jpg
```

🎯 Se apriamo direttamente un singolo file, perdiamo gran parte della visione del progetto.
🚀 Se apriamo **la cartella del progetto**, VS Code ci mostra invece l'intera struttura nella sezione **Esplora**.


## 🖱️ 7. Apriamo la cartella in VS Code

📁 Create una cartella, per esempio: `HTML`

- 💻 Avviate VS Code.
- 📂 Selezionate: `File → Apri cartella`
- 🖱️ Scegliete la cartella `HTML`.
- 👀 A sinistra comparirà la struttura del progetto.
- 💡 In alternativa, potete anche **trascinare la cartella direttamente dentro VS Code**.
- 🎯 Questo diventerà un gesto naturale: **una cartella = un progetto**. 📂

## 📄 8. Creiamo il nostro primo file HTML

📁 Nella sezione **Esplora** di VS Code selezioniamo la nostra cartella.

- ➕ Creiamo un nuovo file.
- ✏️ Chiamiamolo: `index.html`

🌐 Il nome `index.html` è una convenzione molto utilizzata come pagina iniziale di un sito Web.

💡 Per ora non dobbiamo preoccuparci di server, database, framework o altre magie nere. 🧙‍♂️

- 🎯 Abbiamo una cartella.
- 🎯 Abbiamo un file HTML.
- 🎯 Adesso possiamo scrivere il nostro primo codice Web.

## 🧱 9. La struttura fondamentale di una pagina HTML

🌐 Una pagina HTML ha una struttura gerarchica.

💻 Una struttura minima può essere:

```html
<html>
	<head>
		<title>La mia pagina</title>
	</head>
	<body>
		<p>Ciao mondo!</p>
	</body>
</html>
```

🧠 Fermiamoci un attimo e leggiamo questa struttura dall'esterno verso l'interno.

- 🌐 `<html>` rappresenta il documento HTML.
- 🧠 `<head>` contiene informazioni relative al documento.
- 🏷️ `<title>` definisce il titolo della pagina visualizzato, per esempio, nella scheda del browser.
- 👁️ `<body>` contiene ciò che appartiene al contenuto della pagina visualizzata.
- 📝 `<p>` rappresenta un paragrafo.

## 🌐 10. Il tag `<html>`

🌐 Il tag `<html>` rappresenta l'elemento radice del documento HTML.

💻 In pratica, tutto il documento si trova al suo interno:

```html
<html>
	...
</html>
```

🧠 Possiamo immaginarlo come il **contenitore principale** della nostra pagina. 📦

## 🧠 11. Il tag `<head>`

🧠 `<head>` contiene informazioni e configurazioni relative al documento.

💻 Per esempio:

```html
<head>
	<title>La mia pagina</title>
</head>
```

🎯 Quello che troviamo nel `<head>` non rappresenta normalmente il contenuto principale mostrato nella pagina.

⚙️ Qui troveremo in seguito anche informazioni come metadati, collegamenti ai fogli CSS e altri elementi importanti.

## 🏷️ 12. Il tag `<title>`

🏷️ `<title>` definisce il titolo associato al documento HTML.

💻 Esempio:

```html
<title>Il mio primo sito</title>
```

🌐 Aprendo la pagina nel browser, il titolo sarà normalmente visibile nella scheda della pagina.

🧠 Attenzione: `<title>` **non significa "titolo visibile dentro la pagina"**.

🎯 Per i titoli visualizzati nel contenuto useremo invece `<h1>`, `<h2>` e così via.

## 👁️ 13. Il tag `<body>`

👁️ `<body>` contiene il contenuto principale della pagina.

💻 Per esempio:

```html
<body>
	<h1>Benvenuti!</h1>
	<p>Questa è la mia prima pagina Web.</p>
</body>
```

🌐 Questi elementi saranno visualizzati nella pagina del browser.

🎯 Se `head` contiene informazioni sul documento, `body` contiene principalmente **il contenuto che l'utente deve vedere e utilizzare**.

## 📝 14. Il tag `<p>`

📝 Il tag `<p>` rappresenta un **paragrafo**.

💻 Esempio:

```html
<p>HTML è il linguaggio utilizzato per descrivere la struttura delle pagine Web.</p>
```

🧩 Possiamo avere più paragrafi:

```html
<p>Questo è il primo paragrafo.</p>
<p>Questo è il secondo paragrafo.</p>
<p>Questo è il terzo paragrafo.</p>
```

🎯 Ogni elemento `<p>` rappresenta un paragrafo distinto.

## ↩️ 15. Il tag `<br>`

↩️ `<br>` significa **line break**, cioè interruzione di riga.

💻 Possiamo scrivere:

```html
<p>
	Prima riga<br>
	Seconda riga<br>
	Terza riga
</p>
```

🌐 Il browser visualizzerà il testo su tre righe.

⚠️ `<br>` è particolare perché non contiene normalmente un contenuto da racchiudere tra apertura e chiusura.

❌ Non scriviamo:

```html
<br></br>
```

🎯 Utilizziamo semplicemente:

```html
<br>
```

#### ⚠️ Precisazione

Anche se i browser non restituiscono errore, nel caso di tag che non prevedono chiusura è buona norma usare questo tipo di scrittura

```html
<br/>
```

## 📚 16. I titoli: da `<h1>` a `<h6>`

📚 HTML mette a disposizione sei livelli di intestazione.

💻 Sono:

```html
<h1>Titolo principale</h1>
<h2>Titolo di secondo livello</h2>
<h3>Titolo di terzo livello</h3>
<h4>Titolo di quarto livello</h4>
<h5>Titolo di quinto livello</h5>
<h6>Titolo di sesto livello</h6>
```

🧠 La `h` significa **heading**, cioè intestazione.

📊 Possiamo schematizzarli così:

| 🏷️ Tag | 📚 Livello | 🎯 Utilizzo |
| ---: | ---: | --- |
| `<h1>`  | 1️⃣ | titolo principale |
| `<h2>`  | 2️⃣ | sezione principale |
| `<h3>`  | 3️⃣ | sottosezione |
| `<h4>`  | 4️⃣ | livello successivo |
| `<h5>`  | 5️⃣ | intestazione secondaria |
| `<h6>`  | 6️⃣ | livello più specifico |

🎯 `<h1>` rappresenta il livello più importante.

📉 Scendendo verso `<h6>` diminuisce il livello gerarchico dell'intestazione.

⚠️ Non scegliamo `<h3>` semplicemente perché "mi piace più grande".

🧠 I livelli delle intestazioni rappresentano soprattutto **la struttura logica del documento**, non soltanto la dimensione del carattere.


## 🧩 17. Mettiamo tutto insieme

🚀 Adesso possiamo costruire una prima pagina completa.

```html
<html>
	<head>
		<title>Il mio primo sito</title>
	</head>

	<body>
		<h1>Benvenuti nel mio sito!</h1>
		<h2>Chi sono</h2>
		<p>
			Mi chiamo Mario e sto imparando
			a sviluppare pagine Web.
		</p>

		<h2>Cosa sto imparando</h2>
		<p>
			Sto studiando HTML.<br>
			In seguito studierò CSS.<br>
			Poi arriverà JavaScript!
		</p>
	</body>
</html>
```

🎯 Questo piccolo programma contiene già diversi concetti fondamentali.

- 🧠 Abbiamo una struttura HTML.
- 🧠 Abbiamo una sezione `head`.
- 🧠 Abbiamo un titolo del documento.
- 🧠 Abbiamo un `body`.
- 🧠 Abbiamo intestazioni.
- 🧠 Abbiamo paragrafi.
- 🧠 Abbiamo interruzioni di riga.
- 🔥 E soprattutto abbiamo scritto una vera pagina Web.

## 📐 18. L'indentazione: il codice deve essere leggibile

📐 L'**indentazione** consiste nello spostare il codice verso destra per rappresentare visivamente la struttura gerarchica.

💻 Guardiamo questo esempio:

```html
<html>
	<head>
		<title>La mia pagina</title>
	</head>
	<body>
		<h1>Ciao!</h1>
		<p>
			Questo è un paragrafo.
		</p>
	</body>
</html>
```

👀 Guardando il codice possiamo capire immediatamente quali elementi sono contenuti dentro altri elementi.

🧠 L'indentazione non serve al browser per capire la struttura in questo caso, ma serve **enormemente a noi esseri umani**.

🎯 Un programmatore scrive codice non soltanto per farlo funzionare, ma anche per permettere ad altri programmatori di leggerlo e modificarlo.

## ⌨️ 19. TAB oppure spazi?

⌨️ VS Code può utilizzare tabulazioni oppure spazi per l'indentazione.

🎯 Per questo corso adotteremo una regola semplice:

> 📐 **Un livello di indentazione = una TAB.**

💻 Quindi:

```html
<html>
→	<head>
→	→	<title>La mia pagina</title>
→	</head>
</html>
```

🧠 Il simbolo `→` rappresenta graficamente la tabulazione.

⚙️ In VS Code possiamo controllare questa impostazione dalla barra di stato e dalle impostazioni dell'editor.

🔧 È importante che tutti i file di un progetto seguano una convenzione coerente.

## ↩️ 20. LF: il carattere di fine riga

🧠 Ogni sistema operativo deve stabilire come rappresentare la fine di una riga di testo.

💻 Storicamente esistono convenzioni differenti.

🪟 Windows utilizza normalmente **CRLF**.

🐧 Linux e molti ambienti Unix utilizzano **LF**.

🍎 Anche macOS moderno utilizza **LF**.

🎯 Nel nostro progetto possiamo scegliere di utilizzare **LF**, così il codice mantiene una convenzione coerente con molti strumenti e ambienti di sviluppo.

## ⚙️ 21. Come impostare LF in VS Code

🖥️ Aprite il vostro file HTML in VS Code.

👀 Nella barra di stato, nella parte inferiore della finestra, troverete l'indicazione del formato delle terminazioni di riga, per esempio: `CRLF`

- 🖱️ Fate clic su `CRLF`.
- 📋 Comparirà un menu con le opzioni disponibili.
- 🐧 Selezionate: `LF`

🎯 Da quel momento il file utilizzerà LF come terminazione di riga.

⚙️ Se volete impostarlo come comportamento predefinito, potete intervenire nelle impostazioni di VS Code cercando: `EOL`
🔧 L'impostazione corrispondente è:`Files: Eol`
🎯 Impostandola su: `\n`

🐧 VS Code utilizzerà LF come terminazione di riga predefinita.

## 🧠 22. Una pagina Web è una struttura gerarchica

🌳 Una delle idee più importanti da portarsi a casa è che HTML costruisce una **struttura ad albero**.

💻 Per esempio:

```text
html
├── head
│	└── title
│
└── body
	├── h1
	├── h2
	├── p
	└── p
```

🌳 Ogni elemento può contenere altri elementi.

🧠 Questa caratteristica si chiama **annidamento**, o *nesting*.

💻 Per esempio:

```html
<body>
	<h1>Il mio sito</h1>
	<p>
		Questo testo si trova
		dentro il paragrafo.
	</p>
</body>
```

🎯 `<body>` contiene `<h1>` e `<p>`.

🎯 `<p>` contiene il testo.

🔥 Più avanti questa struttura diventerà fondamentale anche quando incontreremo CSS e JavaScript.


## 🐛 23. Gli errori più comuni

🚨 Quando si comincia, alcuni errori sono praticamente inevitabili.

🔴 **Dimenticare la chiusura:**

```html
<p>Questo è un paragrafo
```

🟢 Meglio:

```html
<p>Questo è un paragrafo</p>
```

🔴 **Confondere il nome del tag:**

```html
<paragrafo>
```

🧠 HTML non inventa tag a piacere: bisogna utilizzare gli elementi previsti dallo standard.

🔴 **Annidamento sbagliato:**

```html
<p>
	<h1>Titolo</p>
</h1>
```

🧠 I tag devono essere annidati correttamente.

🟢 Per esempio:

```html
<h1>
	Titolo
</h1>

<p>
	Paragrafo
</p>
```

🎯 Imparare HTML significa anche imparare a **leggere la struttura del codice** e individuare dove abbiamo aperto e chiuso gli elementi. 🔍

## ⚡ 24. Una scorciatoia potentissima: Emmet

🚀 VS Code integra strumenti che possono velocizzare enormemente la scrittura dell'HTML.

💡 Uno dei più importanti è **Emmet**.

⌨️ Per esempio, digitando: `!` o `html:5`

⚡ e premendo `TAB`, VS Code può generare automaticamente la struttura iniziale di un documento HTML.

💻 Otterremo una struttura simile a:

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>

</body>
</html>
```

🎯 Questa scorciatoia diventerà presto una delle vostre armi principali. ⚔️💻
🧠 Non significa però che dobbiamo imparare soltanto le scorciatoie.
🎯 Prima bisogna capire **che cosa stiamo generando**.

## 🌐 25. Dal codice al browser

- 🚀 Abbiamo scritto il nostro HTML.
💾 Salviamo il file: `Ctrl+S`
🌐 Ora possiamo aprire `index.html` con un browser.
🖱️ Possiamo fare doppio clic sul file dalla cartella del progetto.
🌍 Il browser leggerà il documento HTML e lo renderizzerà come pagina Web.
💡 Il ciclo fondamentale è quindi:

```text
⌨️ Scrivo HTML
		↓
💾 Salvo il file
		↓
🌐 Apro/aggiorno il browser
		↓
👀 Vedo il risultato
		↓
🔧 Modifico il codice
		↓
🔄 Ricarico la pagina
```

🔥 Questa è una delle caratteristiche più divertenti dello sviluppo Web: **scrivi codice e puoi vedere immediatamente il risultato**.

## 🧪 26. Mini laboratorio: costruisci la tua prima pagina

🎯 Adesso tocca a voi.

- 📁 Create una cartella chiamata: `mio-primo-sito`
- 📂 Aprite la cartella in VS Code.
- 📄 Create: `index.html`

✏️ Scrivete una pagina contenente:

* 🌐 una struttura HTML completa;
* 🏷️ un `<title>`;
* 📚 un `<h1>` con il vostro nome;
* 📚 almeno due `<h2>`;
* 📝 almeno tre paragrafi `<p>`;
* ↩️ almeno un `<br>`;
* 📐 indentazione coerente;
* 🐧 terminazioni di riga LF.

#### 🔥 Obiettivo:
realizzare una pagina che presenti **voi stessi, i vostri interessi e ciò che state imparando di informatica**.

## 🧠 27. La mappa mentale da ricordare

🎯 Se alla fine della prima lezione ricordate questa struttura, abbiamo già fatto centro. 🎯

```text
🌐 HTML
│
├── 🏷️ TAG
├── 📁 FILE .html
├── 💻 VS CODE
├── 📂 CARTELLA DEL PROGETTO
├── 🧱 STRUTTURA
│	├── <html>
│	├── <head>
│	├── <title>
│	└── <body>
├── 📝 CONTENUTO
│	├── <p>
│	├── <br>
│	└── <h1> ... <h6>
├── 📐 INDENTAZIONE
└── 🐧 LF
```

🚀 Da qui in poi HTML smette di essere una sigla misteriosa e diventa uno strumento concreto.

- 💻 Avete una cartella.
- 📄 Avete un file.
- 🏷️ Avete imparato i primi tag.
- 🌐 Avete costruito una pagina.

🔥 E avete appena iniziato a parlare con il Web usando il suo linguaggio strutturale.

<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)
[![gmail](https://img.shields.io/badge/gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:birg81@gmail.com)