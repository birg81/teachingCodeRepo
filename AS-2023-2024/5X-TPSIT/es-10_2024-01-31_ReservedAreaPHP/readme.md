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

# Awesome PHP-MySQL WebApp! 🚀

This repository houses a WebApp built on **PHP** and **MySQL** that manages user authentication through an interactive login page. But hold on, it's not just an ordinary login application; it's **AWESOME**! 😎

## What Will You Find Here? 📁

- 😎 **Dynamic Web Pages**
	* The [`index.php`](./index.php) page welcomes users, allowing them to access the reserved area.
	* The [`welcome.php`](./welcome.jsp) page displays a warm welcome to the user's reserved space.
- 🎨 **PHP Controllers**:
	* The [`login.php`](./login.php) page manages the user authentication process.
	* The [`logout.php`](./logout.php) page handles user logout and destroys data stored in sessions.
- 🧑‍💻 **Database**: A purposefully crafted database [`ReservedAreaDB.sql`](./ReservedAreaDB.sql) that can be easily imported into your trusted MySQL/MariaDB DBMS. This DB contains the definition of the `Users` table, storing `username` and `password` of registered users.

## How Does It Work? 🚦

1. 🚀 **User Initialization**: In the [`Users`](./ReservedAreaDB.sql) table, authentic users are created to test the application.

2. 📤 **Parameter Reception**: When you make a login request from the [`index.php`](./index.php) page, send the `username` and `secret` parameters via POST to the [`login.php`](./login.php) page. The received data, inside the associative array `$_REQUEST`, will be sanitized using `trim()` and `mysqli::real_escape_string()`. This ensures that a query can extract only the selected user from the table.

3. 🔍 **Credential Verification**: The credentials are compared with those of stored users. If there's a match, the user is authenticated, and the session is set with the user's `username` and `id`.

4. 🚪 **Secure Redirection**: If someone attempts to access the [`welcome`](./welcome.php) page directly via a GET request, they'll be automatically redirected to the [`logout`](./logout.php) page.

## How Can I Get Started? 🚀

* Ensure you have a properly configured development environment.
* Download the repository.
* Run the application on a PHP and MySQL compatible web server.
* Access the login page and experience the AWESOME user journey!

**Important Note**:
This is just the beginning! You can expand the application by adding new features, enhancing the user interface, or making it even more secure. The reader is then empowered to implement user registration, modification, and deletion functions.
*Make your changes and make this application shine brighter than ever*! 💎

### Thank You for Being Here! 🙌

If you have questions, suggestions, or would like to contribute, feel free to do so.
We have an awesome community waiting for you! 🚀

<hr/>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a> 🤍 <a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>
# Reserved Area! 🚀

Questo repository contiene una WebApp basata su **PHP** e **MySQL** che gestisce l'autenticazione degli utenti tramite una pagina di login interattiva.
Ma aspetta, non è solo un'applicazione di login ordinaria, è **AWESOME**! 😎

## Cosa troverai qui? 📁

- 😎 **Pagine web Dinamiche**
	* La pagine [`index.php`](./index.php) accoglie gli utenti permettendo loro di accedere all'area riservata
	* La pagina [`welcome.php`](./welcome.jsp) mostra un benvenuto nell'area riservata agli utenti
- 🎨 **Controller Java Servlet**:
	* pagina [`login.java`](./login.php) gestisce il processo di autenticazione degli utenti.
	* La classe [`logout.php`](./logout.php) gestisce il logout degli utenti e distrugge i dati contenuti nelle sessioni
- 🧑‍💻 **Base di Dati**: Un database creato ad arte [`ReservedAreaDB.sql`](./ReservedAreaDB.sql) che può tranquillamente essere importato nel tuo DBMS di fiducia di tipo MySQL/MariaDB; questo DB contiene la definizione della tabella `Users` che contiene `username` e `password` dei diversi utenti registrati.

## Come Funziona? 🚦

1. 🚀 **Inizializzazione Utenti**: Nella tabella [`Users`](./ReservedAreaDB.sql), vengono creati degli utenti autentici per testare l'applicazione.

2. 📤 **Ricezione dei Parametri**: Quando effettui una richiesta di login dalla pagina [`index.php`](./index.php), spedisci i parametri `username` e `secret` tramite il medoto POST alla pagina [`login.java`](./login.php), i dati ricevuti all'interno dell'array associativo `$_REQUEST`, verranno ripuliti attraverso i metodi `trim()` e `mysqli::real_escape_string()`, in modo che attraverso una query sarà possibile estrarre solo l'utente selezionato dalla tabella

3. 🔍 **Verifica delle Credenziali**: Le credenziali vengono confrontate con quelle degli utenti memorizzati.
Se c'è una corrispondenza, l'utente viene autenticato e la sessione viene impostata settandola col `username` e `id` dell'utente selezionato.
4. 🚪 **Redirezione Sicura**: Nel caso in cui qualcuno tenti di accedere alla pagina di [`welcome`](./welcome.php) direttamente tramite una richiesta GET, verrà rediretto automaticamente verso la pagina di [`logout`](./logout.php).

## Come Posso Iniziare? 🚀

* Assicurati di avere un ambiente di sviluppo configurato correttamente.
* Scarica il repository.
* Esegui l'applicazione su un server Web compatibile con PHP e MySQL.
* Accedi alla pagina di login e sperimenta l'esperienza utente AWESOME!

**Nota Importante**:
Questo è solo l'inizio!
Puoi espandere l'applicazione aggiungendo nuove funzionalità, migliorando l'interfaccia utente o rendendola ancora più sicura.
Al lettore viene quindi lasciata la possibilità di implementare anche le funzioni di registrazione, modifica e cancellazione di utenti.
*Fai le tue modifiche e fai brillare questa applicazione come mai prima d'ora*! 💎

### Grazie per Essere Qui! 🙌

Se hai domande, suggerimenti o vorresti contribuire, sentiti libero di farlo.
Abbiamo una fantastica community che ti aspetta! 🚀

<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)