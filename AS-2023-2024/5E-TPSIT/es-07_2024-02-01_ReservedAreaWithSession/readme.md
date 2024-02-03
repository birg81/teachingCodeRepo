[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

<a name="TOP"></a>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇬🇧](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png) <a name="EN"></A>
# Reserved Area! 🚀

This repository houses a Java Web application built on **Jakarta Servlet** for user authentication through an interactive login page.
But wait, it's not just your ordinary login app; it's **AWESOME**! 😎

## What Will You Find Here? 📁

- 😎 **Dynamic Web Pages**
	* The [`index.jsp`](./src/main/webapp/index.jsp) page welcomes users, allowing them to access the reserved area.
	* The [`welcome.jsp`](./src/main/webapp/welcome.jsp) page displays a warm welcome to the user's reserved space.
- 🎨 **Java Servlet Controllers**:
	* The [`Login.java`](./src/main/java/controller/Login.java) class manages the user authentication process.
	* The [`Logout.java`](./src/main/java/controller/Logout.java) class handles user logout, destroying session data.
- 🧑‍💻 **User Model (User)**: A simple [`User`](./src/main/java/model/User.java) class represents a user with a `username` and `secret`.

## How Does It Work? 🚦

1. 🚀 **User Initialization**: In the constructor of the [`Login`](./src/main/java/controller/Login.java) class, dummy (yet authentic) users are created to test the application.

2. 📤 **Parameter Reception**: When a login request is made via POST, the `username` and `secret` parameters are read and placed into a [`User`](./src/main/java/model/User.java) object. This ensures that the data is cleansed.
Through the `equals()` method override, you can check if two users match—i.e., have the same `username` and `secret`.

3. 🔍 **Credential Verification**: The credentials are compared with those of stored users.
If there's a match, the user is authenticated, and the session is set.

4. 🚪 **Secure Redirection**: If someone attempts to access the servlet directly via a GET request, they'll be automatically redirected to the logout page.

## How Can I Get Started? 🚀

* Ensure you have a properly configured Java development environment.
* Download the repository.
* Run the application on a Jakarta Servlet-compatible web server.
* Access the login page and experience the AWESOME user journey!

**Important Note**:
This is just the beginning! You can expand the application by adding new features, enhancing the user interface, or making it even more secure.
The reader is then empowered to fetch information from a database and implement user registration, modification, and deletion functions.
*Make your changes and make this application shine brighter than ever*! 💎

### Thank You for Being Here! 🙌

If you have questions, suggestions, or would like to contribute, feel free to do so.
We have an awesome community waiting for you! 🚀

<hr/>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a> 🤍 <a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>
# Reserved Area! 🚀

Questo repository contiene un'applicazione Java Web basata su **Jakarta Servlet** che gestisce l'autenticazione degli utenti tramite una pagina di login interattiva.
Ma aspetta, non è solo un'applicazione di login ordinaria, è **AWESOME**! 😎

## Cosa troverai qui? 📁

- 😎 **Pagine web Dinamiche**
	* La pagine [`index.jsp`](./src/main/webapp/index.jsp) accoglie gli utenti permettendo loro di accedere all'area riservata
	* La pagina [`welcome.jsp`](./src/main/webapp/welcome.jsp) mostra un benvenuto nell'area riservata agli utenti
- 🎨 **Controller Java Servlet**:
	* La classe [`Login.java`](./src/main/java/controller/Login.java) gestisce il processo di autenticazione degli utenti.
	* La classe [`Logout.java`](./src/main/java/controller/Logout.java) gestisce il logout degli utenti e distrugge i dati contenuti nelle sessioni
- 🧑‍💻 **Modello Utente (User)**: Una semplice classe [`User`](./src/main/java/model/User.java) rappresenta un utente con `username` e `secret`.

## Come Funziona? 🚦

1. 🚀 **Inizializzazione Utenti**: Nel costruttore della classe [`Login`](./src/main/java/controller/Login.java), vengono creati utenti fittizi (ma autentici) per testare l'applicazione.

2. 📤 **Ricezione dei Parametri**: Quando effettui una richiesta di login tramite POST, i parametri `username` e `secret` vengono letti e inseriti in un oggetto [`User`](./src/main/java/model/User.java), in questo modo i dati verranno ripuliti e attravero l'overload del metodo `equals()` sarà possibile vedere se due utenti corrispondono, ovvero se hanno la stessa `username` e lo stesso `secret`.

3. 🔍 **Verifica delle Credenziali**: Le credenziali vengono confrontate con quelle degli utenti memorizzati.
Se c'è una corrispondenza, l'utente viene autenticato e la sessione viene impostata.
4. 🚪 **Redirezione Sicura**: Nel caso in cui qualcuno tenti di accedere alla servlet direttamente tramite una richiesta GET, verrà rediretto automaticamente verso la pagina di logout.

## Come Posso Iniziare? 🚀

* Assicurati di avere un ambiente di sviluppo Java configurato correttamente.
* Scarica il repository.
* Esegui l'applicazione su un server Web compatibile con Jakarta Servlet.
* Accedi alla pagina di login e sperimenta l'esperienza utente AWESOME!

**Nota Importante**:
Questo è solo l'inizio!
Puoi espandere l'applicazione aggiungendo nuove funzionalità, migliorando l'interfaccia utente o rendendola ancora più sicura.
Al lettore viene quindi lasciata la possibilità di prelevare le informazioni da un DB ed implementare anche le funzioni di registrazione, modifica e cancellazione di utenti.
*Fai le tue modifiche e fai brillare questa applicazione come mai prima d'ora*! 💎

### Grazie per Essere Qui! 🙌

Se hai domande, suggerimenti o vorresti contribuire, sentiti libero di farlo.
Abbiamo una fantastica community che ti aspetta! 🚀

<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)