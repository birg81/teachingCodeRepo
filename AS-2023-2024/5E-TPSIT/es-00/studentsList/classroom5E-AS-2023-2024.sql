-- Creazione del DB con concellazione della versione vecchia
DROP DATABASE IF EXISTS Students;
CREATE DATABASE IF NOT EXISTS Students;
USE Students;


-- Creazione Tabella con cancellazione della versione vecchia
DROP TABLE IF EXISTS StudentsList;
CREATE TABLE IF NOT EXISTS StudentsList(
	id INT PRIMARY KEY AUTO_INCREMENT,
	firstname VARCHAR(32) NOT NULL,
	lastname VARCHAR(32) NOT NULL,
	gender CHAR(1)	DEFUALT 'm' NOT NULL,
	UNIQUE (firstname, lastname)
);


-- Popolamento Tabella
INSERT INTO StudentsList(firstname, lastname, gender) VALUES
	('Gennaro',	'Cannavale',	'm'),
	('Salvatore',	'Caprio',	'm'),
	('Francesco Paolo',	'Carrano',	'm'),
	('Raffaele',	'Cioffi',	'm'),
	('Graziano',	'Coscarelli',	'm'),
	('Andrea',	'Cuomo',	'm'),
	('Luigi',	'D\'Esposito',	'm'),
	('Giovanni',	'Di Somma',	'm'),
	('Giovanni',	'Donnarumma',	'm'),
	('Simone',	'Esposito',	'm'),
	('Giuseppe',	'Ferraro',	'm'),
	('Giuseppe',	'Langellotti',	'm'),
	('Giuseppe',	'Lopindo',	'm'),
	('Giuseppe',	'Martino',	'm'),
	('Francesco Pio',	'Ruggiero',	'm'),
	('Adriano',	'Russo',	'm'),
	('Vincenzo',	'Tramparulo',	'm'),
	('Giovanni',	'Verde',	'm');