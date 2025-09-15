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
# Master Python 🐍: The Pro Way to Build Projects 💻

## 🎬 **Code Like a True Professional**

🔥 *Do you want to take your Python projects to the next level, just like a pro?*

🚀 Then you absolutely need to learn how to use *virtual environments*!

Without them, you risk dependency conflicts, weird bugs, and libraries haunting your projects from one folder to another.

Today we’ll cover 💡:

* What is a virtual environment?
* How to create one
* How to manage dependencies
* And why it’s essential if you plan to publish your project on GitHub!

---

## 🐍 **What Is a Virtual Environment in Python?**

👉 A *virtual environment* (`venv`) is an **isolated Python bubble** where you install only the libraries your project needs.
⚡ This means if one project needs `FastAPI 0.109` and another requires `FastAPI 0.116.1`, you can run both on the same machine without conflicts!

🎯 In short: venv guarantees **order, control, and portability**.

---

## 🛠️ **How to Create a Virtual Environment**

📌 The `venv` module is built into Python, so no extra installations are needed.
Here’s the universal command:

```bash
python -m venv env_name
```

* 🔵 **Windows (CMD or PowerShell)**

  ```bash
  python -m venv .birg81env
  ```
* 🟢 **Linux / macOS**

  ```bash
  python3 -m venv .birg81env
  ```

💡 Tip: the name is up to you, but best practice is to call it simply `venv` or use a hidden name like `.birg81env`, which we’ll use throughout this guide.

---

## ⚡ **How to Activate a Virtual Environment**

* 🔵 **Windows (CMD)** (recommended over PowerShell)

  ```bash
  .birg81env\Scripts\activate.bat
  ```
* 🔵 **Windows (PowerShell)**

  ```bash
  .\.birg81env\Scripts\Activate.ps1
  ```
* 🟢 **Linux / macOS (Bash/Zsh)**

  ```bash
  source .birg81env/bin/activate
  ```

✨ Once activated, you’ll see `(.birg81env)` in your terminal prompt → meaning you’re inside your protected bubble.

---

## 📦 **Installing Dependencies in the venv**

Once your venv is active, you can install libraries *without polluting your global system*:

```bash
pip install package_name
```

Example:

```bash
pip install fastapi uvicorn
```

👉 Everything stays neatly contained inside `.birg81env`.

---

## 📜 **The requirements.txt File**

💾 If you want to share your project or replicate it on another machine, you need to save the list of installed libraries.

In practice, `requirements.txt` is just a text file — think of it as your project’s **shopping list** of dependencies.
You can create it manually before coding, or generate it from your current setup using:

```bash
pip freeze > requirements.txt
```

🔄 To install everything from `requirements.txt`:

```bash
pip install -r requirements.txt
```

⚡ This ensures anyone can recreate your environment exactly as you built it.

---

## 🌍 **If You Publish on GitHub: README.md & .gitignore**

When collaborating on GitHub, two small but essential text files make your project shine:

### 📖 **README.md**

Your project’s **business card**. Here you explain:

* What it’s about 💡
* How to install it ⚙️
* How to use it 🚀

### 🚫 **.gitignore**

Prevents **unnecessary files** (like the venv) from being uploaded to GitHub.
Inside [`.gitignore`](./.gitignore) add:

```
venv/
__pycache__/
*.pyc
```

👉 This keeps your repository clean, lightweight, and professional.

---

## 🏁 **Conclusion**

🔥 Now you know what a *virtual environment* is, how to create and activate it, install dependencies, work with `requirements.txt`, and structure a GitHub-ready project with `README.md` and `.gitignore`.

✨ **Remember**: every time you start a new Python project, **create a venv first**!
It’s the secret to coding like a pro — with no chaos, no conflicts.

🌟 *May your Python projects grow stronger, cleaner, and ready to conquer the open-source world!* 🚀🐍💻


<hr/>

![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>

<!-- Italian -->
# Master Python 🐍: The Pro Way to Build Projects 💻

## 🎬 **Programmare come un vero profesisonista**

🔥 *Vuoi portare i tuoi progetti Python al livello successivo, come un vero professionista?*

🚀 Allora devi assolutamente imparare a usare i *virtual environment*!

Senza di loro rischi conflitti, bug assurdi e dipendenze che ti inseguono da un progetto all’altro.

Oggi ti spiego 💡:

- cos’è una virtual environment?
- come crearla
- come gestire le dipendenze
- e perché è fondamentale se pubblichi il tuo progetto su GitHub!

---

## 🐍 **Cos’è un Virtual Environment in Python?**

👉 Un *virtual environment* (`venv`) è una **bolla isolata di Python** in cui installi solo le librerie necessarie al tuo progetto.
⚡ Questo significa che se un progetto ha bisogno di `FastAPI 0.109` e un altro di `FastAPI 0.116.1`, puoi avere entrambe le versioni sullo stesso computer senza conflitti!

🎯 In sintesi: il venv ti garantisce **ordine, controllo e portabilità**.

---

## 🛠️ **Come Creare un Virtual Environment**

📌 Il modulo `venv` è incluso in Python, quindi non devi installare nulla.
Ecco il comando universale:

```bash
python -m venv nome_venv
```

* 🔵 **Windows (CMD o PowerShell)**

  ```bash
  python -m venv .birg81env
  ```
* 🟢 **Linux / macOS**

  ```bash
  python3 -m venv .birg81env
  ```

💡 Consiglio: il nome della `venv` è a scelta, buona norma può essere chiamalo sempre `venv` od in alternativa usare un nome che inizia col punto e finisce con env, nel nostro esempio `.birg81env`, che di seguito verrà riproposto.

---

## ⚡ **Come Attivare un Virtual Environment**

* 🔵 **Windows (CMD)** (è preferibile a PowerShell)

  ```bash
  .birg81env\Scripts\activate.bat
  ```
* 🔵 **Windows (PowerShell)**

  ```bash
  .\.birg81env\Scripts\Activate.ps1
  ```
* 🟢 **Linux / macOS (Bash/Zsh)**

  ```bash
  source .birg81env/bin/activate
  ```

✨ Quando attivi il venv, nel prompt compare `(.birg81env)` → significa che sei dentro la tua bolla protetta.

---

## 📦 **Installare Dipendenze nel venv**

Una volta attivato il venv, puoi installare librerie *senza sporcare il sistema globale*:

```bash
pip install nome_pacchetto
```

Esempio:

```bash
pip install fastapi uvicorn
```

👉 Tutto rimane confinato dentro `.birg81env`.

---

## 📜 **Il File requirements.txt**

💾 Se vuoi condividere il progetto o replicarlo altrove, devi salvare l’elenco delle librerie installate:

In pratica `requirements.txt` è un semplice file di testo, possiamo immaginarlo come una sorta di lista della spesa che contiene tutte le dipendenze installate nel nostro progetto.
Dunque possiamo creare questo file prima di iniziare il progetto e scrivere ciò che ci serve o a progetto in corso copiando la lista delle dipendenze installate, in tal caso digiteremo:

```bash
pip freeze > requirements.txt
```

🔄 Per installare tutto da `requirements.txt`:

```bash
pip install -r requirements.txt
```

⚡ In questo modo chiunque potrà ricreare il tuo ambiente esattamente come il tuo.

---

## 🌍 **Se Pubblici su GitHub: README.md & .gitignore**

Lavorando in un team di sviluppo capita di spesso di condividere il lavoro su **GitHub** e a tal scopo è fondamentale aggiungere al nostro progetto due tasselli fondamentali, ovvero due file di testo piccoli ma indispensabili:

### 📖 **README.md**
  È il **biglietto da visita** del tuo progetto. Qui spieghi:

  * Di cosa si tratta 💡
  * Come installarlo ⚙️
  * Come usarlo 🚀

### 🚫 **.gitignore**
  Serve a **non caricare file inutili** (come il venv) su GitHub.
  Dentro [`.gitignore`](./.gitignore) aggiungi:

  ```
  venv/
  __pycache__/
  *.pyc
  ```

👉 Così il tuo repo rimane pulito, leggero e professionale.

---

## 🏁 **Conclusione**

🔥 Ora sai cos’è un *virtual environment*, come crearlo, attivarlo, installare dipendenze, usare `requirements.txt` e strutturare un progetto da GitHub-ready con `README.md` e `.gitignore`.

✨ **Ricorda**: ogni volta che crei un nuovo progetto Python, **crea prima un venv**!!.
È il segreto per sviluppare come un vero professionista, senza caos né conflitti.

🌟 *Che i tuoi progetti Python diventino sempre più solidi, eleganti e pronti a conquistare il mondo open source!* 🚀🐍💻


<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)