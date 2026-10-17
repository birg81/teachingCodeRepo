-- eliminazione vecchia versione del db
DROP DATABASE IF EXISTS BuddyListDB;
-- crea il db (se non esiste già un'altra versione)
CREATE DATABASE IF NOT EXISTS BuddyListDB;
-- usiamo il db creato
USE BuddyListDB;

-- elimino tabella vecchia e creo una tabella nuova
DROP TABLE IF EXISTS UsersList;
CREATE TABLE IF NOT EXISTS UsersList(
	id INT PRIMARY KEY AUTO_INCREMENT,
	-- chiave candidata: non possono esserci 2 o più email uguali!
	email VARCHAR(48) NOT NULL UNIQUE KEY,
	passwd VARCHAR(48) NOT NULL
);

-- tabella dello storico dei login
CREATE TABLE LoginHistory (
	-- chiave esterna
	user_fk INT NOT NULL,
	-- istante di tempo (data e ora precisa) del momento in cui l'utente si è loggato
	login_at DATETIME DEFAULT CURRENT_TIMESTAMP,

	-- una chiave primaria può anche essere ottenuta con una chiave esterna
	PRIMARY KEY (user_fk, login_at),
	-- definizione della chiave esterna
	FOREIGN KEY (user_fk) REFERENCES Users(id)

	-- modo alternativo per definire la chiave esterna
	-- user_fk INT REFERENCES UsersList(id)
);

-- popolamento tabella utenti
INSERT INTO UsersList (email, passwd) VALUES
	('amministratore@buddylist.it', 'Admin001!'),
	('gennaro.esposito@example.com', 'Gennaro123!'),
	('salvatore.sorrentino@example.com', 'Salvatore456!'),
	('carmela.de.luca@example.com', 'Carmela789!'),
	('pasquale.martucci@example.com', 'Pasquale777!'),
	('concetta.ferraiolo@example.com', 'Concetta321!'),
	('enzo.pellegrino@example.com', 'Enzo654!'),
	('luigi.marciano@example.com', 'Luigi987!'),
	('assunta.ricciardi@example.com', 'Assunta2025!'),
	('ciro.damico@example.com', 'Ciro159!'),
	('rosaria.ferrara@example.com', 'Rosaria753!');

-- popolamento tabella accessi
INSERT INTO LoginHistory(user_fk, login_at) VALUES
	(2, NOW() - INTERVAL 1 DAY),		-- Accesso un giorno fa
	(3, NOW() - INTERVAL 1 WEEK),		-- Accesso una settimana fa
	(4, NOW() - INTERVAL 1 MONTH),		-- Accesso un mese fa
	(5, NOW() - INTERVAL 1 YEAR),		-- Accesso un anno fa
-- Accesso 1 anno, 2 mesi e 4 giorni fa
	(1, NOW() -  INTERVAL 1 YEAR - INTERVAL 2 MONTH - INTERVAL 4 DAY);

-- popolamento tabella accessi: gli utenti che si loggano adesso: login_at = NOW() di default
INSERT INTO LoginHistory (user_fk) VALUES
	(1),
	(4),
	(6);
