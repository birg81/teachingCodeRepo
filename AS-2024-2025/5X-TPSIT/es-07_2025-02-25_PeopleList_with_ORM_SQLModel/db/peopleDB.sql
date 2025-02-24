DROP DATABASE IF EXISTS PeopleDB;
CREATE DATABASE IF NOT EXISTS PeopleDB;
-- TRUNCATE TABLE People;
/*
USE PeopleDB;

CREATE TABLE People (
	id INT PRIMARY KEY AUTO_INCREMENT,
	firstname VARCHAR(50) NOT NULL,
	lastname VARCHAR(50) NOT NULL,
	age INT NOT NULL DEFAULT 18,
	CHECK(age > 0)
);

INSERT INTO People (age, lastname, firstname) VALUES
	(17, 'Di Martino', 'Catello'),
	(25, 'Esposito', 'Antonio'),
	(30, 'Ferraro', 'Giuseppe'),
	(22, 'De Rosa', 'Annunziata'),
	(28, 'De Luca', 'Francesco'),
	(35, 'Bianchi', 'Giovanni'),
	(40, 'Mancuso', 'Carmela'),
	(27, 'Gallo', 'Salvatore'),
	(24, 'Martino', 'Vincenzo'),
	(21, 'Della Rocca', 'Lucia'),
	(33, 'Coppola', 'Gennaro'),
	(29, 'Miele', 'Raffaele'),
	(31, 'Pugliese', 'Patrizia'),
	(26, 'Beneduce', 'Rosaria'),
	(38, 'Fusco', 'Pietro'),
	(32, 'Alfano', 'Caterina');
*/