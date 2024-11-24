[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

<a name="TOP"></a>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a>
🤍
<a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇬🇧](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png) <a name="EN"></A>
# Guide to Socket Communication in Python 🚀

Welcome to this captivating journey into the world of sockets and server-client connections in Python! 🐍
We will explore what a socket is, how it works, ports and their value ranges, as well as the phases involved in creating a *client-server* connection.

## What is a Socket? 🧩

**Socket** is a magical word in the realm of communication.
Imagine a socket as a magical window through which you can talk to another computer on a network.
Sockets allow you to send and receive data between two devices, enabling communication between them.

### Socket Definition

A **socket** is a bidirectional communication point between two computers on a network.
It's a virtual channel through which data can flow from the sender (client) to the receiver (server).

## What's the Purpose of a Socket? 📡

Sockets are fundamental for network communications, enabling different computers to exchange data.
They are used in applications like chat, online games, file sharing, and much more.
In essence, sockets make the magic of device interconnection possible.

They are used for:

- **Communication**: Sockets allow two computers to exchange information, both on a local network and over the internet.
- **Data Transmission**: You can send text, images, videos, or any type of data between computers using sockets.
- **Distributed Applications**: Sockets are crucial for creating distributed applications like chat systems, online games, and more.

## How a Socket Works in an Example 🍺

Imagine that devices come to life and turn into adventurous patrons at a bar! The *bartender* (the **Server**) is ready to fulfill the strangest requests from customers (**Clients**).

- 🍸 The *Bartender* stands behind the bar (**Host**) like a sentinel, keeping a watchful eye on a specific area (**Port**), ready to take customer orders with a perpetual smile.

- 🚶 Curious *Customers* must discover not only the name of the bar (**Host**) but also where to find the Bartender, namely the cash register (**Port**).
This is the ticket to the enchanted world of the bar.

- 🌍 Each *customer* arrives from a different corner of the world, with their own **Host** and **Port**.
They are like travelers from distant lands.

- 🕰️ The *Bartender* is truly skilled: he can serve one order at a time, but he does it with such dexterity that it seems as if he is everywhere at once.

- 🍹 Every *order* (**Request**) delivered to the *Bartender* is carefully processed, and the *Bartender* responds with the desired order (**Response**).

- 🚪 When a *customer* is satisfied, they leave the bar with a smile, *closing the connection* like a departing guest.

- 🕰️ At the end of the night, when all requests have been fulfilled and the hour is late, the bar closes, and so the **Server** *closes the connection*.

## Ports and Their Value Ranges 🚪

*Ports* are 16-bit integer numbers that identify a specific application on a computer, so the value of a port ranges from 0 to 65535 (i.e., $2^{16}-1$).

Ports are divided as follows:

- Lower numbers (0-1023) are reserved for well-known services (e.g., HTTP on port 80 and HTTPS on port 443).
- Ports from 1024 to 49151 are often used for custom applications.
- Ports from 49152 to 65535 are for temporary or private purposes.

## Writing a Server in a Programming Language 🖥️

We can create sockets in any language; we could even mix two languages, using one for the client and another for the server.
ut in this context, let's understand how to do it in Python!

## Creating a Server Socket in Python 🐍

Creating a server socket in Python is an exciting process in 5 simple steps 🤝:

1. **Import the socket module** 📦:
```python
import socket
```

2. **Create a socket object** 📱: This defines the type of socket and the protocol:
```python
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
the variable `ss` represents the **server socket**.

3. **Bind the socket to the address and port**: Use
```python
ss.bind((HOST, PORT))
```
to specify the address and port on which the server will listen.

4. **Listen for incoming connections**: Use:
```python
ss.listen(number)
```
to establish the *number* of maximum waiting connections.

5. **Accept incoming connections**: Use
```python
con, addr = ss.accept()
```
to accept incoming connections and start communication, where `con` represents the connection with the **client**, and `addr` represents the remote **HOST** and **PORT** of the **client** from which the request originates.

## Creating a Client Socket in Python 📱

Creating a client socket in Python is equally thrilling and engaging!
Here's how to do it:

1. **Import the socket module**: First, import the `socket` module, as before.

2. **Create a socket object**: Create a socket object using
```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
In this case, `s` represents the *client socket*.

3. **Connect to the server**: Use
```python
s.connect((HOST, PORT))
```
to connect to the server socket.

4. **Communicate with the server**: Now, you are ready to send and receive data from the server using
```python
s.send()  # send messages
s.recv()  # receive messages
```

## Great Job! 👏

Now, you have a solid understanding of what a socket is, how it works, ports, and how to establish a client-server connection in Python. You're ready to start creating fascinating and engaging network applications! 🌐🎉

Happy coding! 🚀🐍👩‍💻


<hr/>

<a href="#IT"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png" /></a> 🤍 <a href="#EN"><img style="height:25px" src="https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-united-kingdom_1f1ec-1f1e7.png" /></a>

<hr />


![🇮🇹](https://em-content.zobj.net/thumbs/60/whatsapp/352/flag-italy_1f1ee-1f1f9.png) <a name="IT"></A>
# Guida alla Comunicazione Socket in Python 🚀

Benvenuti a questa affascinante avventura nel mondo dei socket e delle connessioni server-client in Python! 🐍
Scopriremo cos'è un socket, come funziona, le porte e i loro intervalli di valori, nonché le fasi coinvolte nella creazione di una connessione client-server.

## Cos'è un Socket? 🧩

**Socket** è una parola magica nel mondo della comunicazione.
Immagina un socket come una finestra magica attraverso cui puoi parlare con un altro computer su una rete.
I socket ti permettono di inviare e ricevere dati tra due dispositivi, permettendo la comunicazione tra di essi.

### Definizione di Socket

Un **socket** è un punto di comunicazione bidirezionale tra due computer su una rete.
È un canale virtuale attraverso il quale i dati possono fluire tra il mittente (client) e il destinatario (server).

## A Cosa Serve un Socket? 📡

I socket sono fondamentali per le comunicazioni su reti, consentendo a computer diversi di scambiare dati.
Sono utilizzati in applicazioni come chat, giochi online, condivisione di file e molto altro.
In sostanza, i socket rendono possibile la magia dell'interconnessione tra dispositivi.

Sono utilizzati per:

- **Comunicazione**: I socket consentono a due computer di scambiare informazioni tra loro, sia su una rete locale che su Internet.
- **Trasmissione di Dati**: Puoi inviare testo, immagini, video o qualsiasi tipo di dati tra i computer utilizzando i socket.
- **Applicazioni Distribuite**: I socket sono fondamentali per la creazione di applicazioni distribuite come chat, giochi online e molto altro.

## Come funziona un socket in un esempio 🍺

Immagina che i dispositivi prendono vita e si trasformano in avventurosi frequentatori di un bar!
Il *barman* (il **Server**) è pronto a soddisfare le richieste più strane dei clienti (**Client**).

- 🍸 Il *Barman* attende al bancone del suo bar (**Host**) come una sentinella, tenendo un occhio attento su una zona ben specifica (**Port**), pronto ad accogliere le ordinazioni dei clienti con un perenne sorriso.

- 🚶 I *Clienti* Curiosi devono scoprire non solo il nome del bar (*Host*), ma anche il luogo in cui il Barman dimora, ovvero la cassa (*Port*).
Questo è il biglietto d'accesso al mondo incantato del bar.

- 🌍 Ogni *cliente* arriva da un angolo diverso del mondo, con il proprio **Host** e **Port**.
Sono come viaggiatori provenienti da terre lontane.

- 🕰️ Il *Barman* è davvero bravo: può servire una comanda alla volta, ma lo fa con tale destrezza che sembra essere ovunque contemporaneamente.

- 🍹 Ogni *comanda* (**Request**) consegnata al *Barman* viene elaborata con cura, e il *Barman* risponde con l'ordine desiderato (**Response**).

- 🚪 Quando un *cliente* è soddisfatto, lascia il bar con un sorriso, *chiudendo la connessione* come un ospite che parte.

- 🕰️ Alla fine della notte, quando tutte le richieste sono state soddisfatte e l'ora è tarda, il bar chiude i battenti, e così il **Server** *chiude la connessione*.

## Porte e i Loro Intervalli di Valori 🚪

Le *porte* (**ports**) sono numeri interi espressi su 16 bit che identificano un'applicazione specifica su un computer, quindi il valore di una porta è compreso tra 0 a 65535 (ovvero $2^{16}-1$).

Le porte sono così suddivise:

- I numeri inferiori (0-1023) sono riservate per servizi noti (come HTTP sulla porta 80 e HTTPS sulla porta 443).
- Le porte tra 1024 e 49151 sono spesso utilizzate per applicazioni personalizzate
- Mentre quelle tra 49152 e 65535 sono per scopi temporanei o privati.

## Scrivere un Server in un linguaggio di programmazione 🖥️

Possiamo creare socket in qualsiasi linguaggio, potremmo addirittura mischiare due linguaggi usandone uno per il client e l'altro per il server, ma in questo contesto comprenderemo come farlo in Python!

## Creare un Server Socket in Python 🐍

Creare un server socket in Python è un processo affascinante in 5 semplici fasi 🤝:

1. **Importare il modulo socket** 📦:
```python
import socket
```

2. **Creare un oggetto socket** 📱: Questo definisce il tipo di socket e il protocollo:
```python
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
la variabile `ss` rappresenta il **server socket**.


3. **Legare il socket all'indirizzo e alla porta**: Usa
```python
ss.bind((HOST, PORT))
```
per specificare l'indirizzo e la porta su cui il server ascolterà.

4. **Ascoltare le connessioni in arrivo**: Utilizza:
```python
ss.listen(number)
```
per stabilire il *numero* massimo di connessioni in attesa.

5. **Accettare connessioni in arrivo**: Utilizza
```python
con, addr = ss.accept()
```
per accettare le connessioni in arrivo e iniziare la comunicazione, in tal caso `con` rappresenta la connessione con il **client** e `addr` rappresenta l'indirizzo **HOST** e la **PORT** remota del **client** dal quale proviene la richiesta.

## Creare un Client Socket in Python 📱

Creare un client socket in Python è altrettanto emozionante e coinvolgente!
Ecco come farlo:


1. **Importare il modulo socket**: Come prima cosa, importa il modulo `socket`.
2. **Creare un oggetto socket**: Crea un oggetto socket utilizzando
```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
In questo caso `s` rappresenta il *client socket*.

3. **Connettersi al server**: Utilizza
```python
s.connect((HOST, PORT))
```
per connetterti al server socket.
4. **Comunicare con il server**: Adesso sei pronto per inviare e ricevere dati dal server utilizzando
```python
s.send()	# invia i messaggi
s.recv()	# riceve i messaggi
```

## Ottimo Lavoro! 👏

Ora hai una solida comprensione di cosa sia un socket, come funziona, le porte e come instaurare una connessione client-server in Python.
Sei pronto per iniziare a creare applicazioni di rete affascinanti e coinvolgenti! 🌐🎉


Buon coding! 🚀🐍👩‍💻

<a href="#TOP">&utrif; top &utrif;</a>

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/biagio-rosario-greco-77145774/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/birg_81)
