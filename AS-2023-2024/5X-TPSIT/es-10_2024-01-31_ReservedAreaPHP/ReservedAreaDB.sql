DROP DATABASE IF EXISTS ReservedAreaDB;
CREATE DATABASE IF NOT EXISTS ReservedAreaDB;
USE ReservedAreaDB;

DROP TABLE IF EXISTS Users;
CREATE TABLE IF NOT EXISTS Users (
	id INT AUTO_INCREMENT PRIMARY KEY,
	username VARCHAR(48) NOT NULL UNIQUE,
	password VARCHAR(48) NOT NULL
);

-- Esempio di inserimento di un utente di test
INSERT INTO Users(username, password) VALUES
	('admin', 'admin'),
	('scugnizz', 'N@P0l1T@n0!'),
	('mandolin@', 'P@r0l@N@p0l1Tan@'),
	('pizzal0ver', 'V3R@p0m0'),
	('sfogliat3lla', 'Nap0l3t@n@_C@nn0l@'),
	('vesuviovibes', 'Sp1rit0_di_V3suv1o');