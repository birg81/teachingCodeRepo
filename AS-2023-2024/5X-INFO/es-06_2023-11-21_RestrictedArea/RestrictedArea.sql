DROP DATABASE IF EXISTS RestrictedAreaDB;
CREATE DATABASE IF NOT EXISTS RestrictedAreaDB;
USE RestrictedAreaDB;

DROP TABLE IF EXISTS UsersList;
CREATE TABLE IF NOT EXISTS UsersList (
	id	INT	PRIMARY KEY	AUTO_INCREMENT,
	email	VARCHAR(32)	NOT NULL,
	UNIQUE KEY(email),
	passwd	VARCHAR(32)	NOT NULL,
	firstname	VARCHAR(32)	NOT NULL,
	lastname	VARCHAR(32)	NOT NULL,
	UNIQUE KEY(firstname, lastname)
);

INSERT INTO UsersList(email, passwd,	firstname, lastname) VALUES
	('root@root.com', 'root',	'System', 'Administrator');