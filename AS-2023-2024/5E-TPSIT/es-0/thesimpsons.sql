-- Creazione del DB con concellazione della versione vecchia
DROP DATABASE IF EXISTS TheSimpsons;
CREATE DATABASE IF NOT EXISTS TheSimpsons;
USE TheSimpsons;


-- Creazione Tabella con cancellazione della versione vecchia
DROP TABLE IF EXISTS CharactersList;
CREATE TABLE IF NOT EXISTS CharactersList(
	id	INT	PRIMARY KEY	AUTO_INCREMENT,
	firstname	VARCHAR(32)	NOT NULL,
	lastname	VARCHAR(32)	NOT NULL,
	gender CHAR(1)	DEFUALT 'm' NOT NULL,
	UNIQUE (firstname, lastname)
);


-- Popolamento Tabella
INSERT INTO CharactersList(firstname, lastname, gender) VALUES
	('Homer',	'Simpson',	'm'),
	('Marge',	'Bouvier',	'f'),
	('Bart',	'Simpson',	'm'),
	('Lisa',	'Simpson',	'f'),
	('Maggie',	'Simpson',	'f'),
	('Ned',	'Flanders',	'm'),
	('Maude',	'Flanders',	'f'),
	('Chief',	'Wiggum',	'm'),
	('Ralph',	'Wiggum',	'm'),
	('Waylon',	'Smithers',	'm'),
	('Montgomery',	'Burns',	'm'),
	('Edna',	'Krabappel',	'f'),
	('Patty',	'Bouvier',	'f'),
	('Selma',	'Bouvier',	'f'),
	('Kent',	'Brockman',	'm');
