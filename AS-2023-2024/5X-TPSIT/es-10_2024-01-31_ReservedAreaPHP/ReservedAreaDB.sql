DROP DATABASE IF EXISTS ReservedAreaDB;
CREATE DATABASE IF NOT EXISTS ReservedAreaDB;
USE ReservedAreaDB;

DROP TABLE IF EXISTS Users;
CREATE TABLE IF NOT EXISTS Users (
	id INT AUTO_INCREMENT PRIMARY KEY,
	username VARCHAR(48) NOT NULL UNIQUE,
	secret VARCHAR(48) NOT NULL
);

-- Esempio di inserimento di un utente di test
INSERT INTO Users(username, secret) VALUES
	('admin', 'admin'),
	('homer', 'hjays'),
	('peter', 'megatron'),
	('stan', 'americamylove'),
	('telespalla', 'diebartdie');