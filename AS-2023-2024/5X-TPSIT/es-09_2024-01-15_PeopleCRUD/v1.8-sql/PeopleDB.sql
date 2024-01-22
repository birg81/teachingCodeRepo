CREATE TABLE People(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	firstname VARCHAR(48) NOT NULL,
	lastname VARCHAR(48) NOT NULL,
	age INTEGER NOT NULL
);

INSERT INTO People (firstname, lastname, age) VALUES
	('Homer', 'Simpson', 39),
	('Marge', 'Simpson', 36),
	('Bart', 'Simpson', 10),
	('Lisa', 'Simpson', 8),
	('Maggie', 'Simpson', 1),
	('Milhouse', 'Van Houten', 10),
	('Maude', 'Flanders', 40),
	('Agnes', 'Skinner', 70);