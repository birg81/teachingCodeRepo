-- Creazione Database
DROP DATABASE IF EXISTS SuperHeroes;
CREATE DATABASE IF NOT EXISTS SuperHeroes;
USE SuperHeroes;

-- Creazione Tabella
CREATE TABLE HeroesList (
	id INT AUTO_INCREMENT PRIMARY KEY,
	firstname VARCHAR(48) NOT NULL,
	lastname VARCHAR(48) NOT NULL,
	isHuman BOOLEAN NOT NULL,
	supername VARCHAR(48) NOT NULL UNIQUE
);

-- Popolamento Tabella (Marvel + DC)
INSERT INTO HeroesList (firstname, lastname, isHuman, supername) VALUES
-- Marvel
('Peter', 'Parker', TRUE, 'Spider-Man'),
('Tony', 'Stark', TRUE, 'Iron Man'),
('Steve', 'Rogers', TRUE, 'Captain America'),
('Bruce', 'Banner', TRUE, 'Hulk'),
('Thor', 'Odinson', FALSE, 'Thor'),
('Natasha', 'Romanoff', TRUE, 'Black Widow'),
('Clint', 'Barton', TRUE, 'Hawkeye'),
('Wanda', 'Maximoff', TRUE, 'Scarlet Witch'),
('Vision', 'Synthozoid', FALSE, 'Vision'),
('Stephen', 'Strange', TRUE, 'Doctor Strange'),
('TChalla', 'Udaku', TRUE, 'Black Panther'),
('Scott', 'Lang', TRUE, 'Ant-Man'),
('Carol', 'Danvers', TRUE, 'Captain Marvel'),
('Logan', 'Howlett', TRUE, 'Wolverine'),
('Jean', 'Grey', TRUE, 'Phoenix'),
-- DC
('Bruce', 'Wayne', TRUE, 'Batman'),
('Clark', 'Kent', FALSE, 'Superman'),
('Diana', 'Prince', FALSE, 'Wonder Woman'),
('Barry', 'Allen', TRUE, 'Flash'),
('Hal', 'Jordan', TRUE, 'Green Lantern'),
('Arthur', 'Curry', FALSE, 'Aquaman'),
('Victor', 'Stone', TRUE, 'Cyborg'),
('Oliver', 'Queen', TRUE, 'Green Arrow'),
('Billy', 'Batson', TRUE, 'Shazam'),
('Kara', 'Zor-El', FALSE, 'Supergirl'),
('Lex', 'Luthor', TRUE, 'Lex Luthor'),
('Selina', 'Kyle', TRUE, 'Catwoman'),
('Harleen', 'Quinzel', TRUE, 'Harley Quinn'),
('Slade', 'Wilson', TRUE, 'Deathstroke'),
('Pamela', 'Isley', TRUE, 'Poison Ivy'),
-- Master of the Universe
('Adam', 'of Eternia', TRUE, 'He-Man'),
('Skeletor', 'Unknown', FALSE, 'Skeletor'),
('Teela', 'Na', TRUE, 'Teela'),
('Duncan', 'Man-At-Arms', TRUE, 'Man-At-Arms'),
('Orko', 'Unknown', FALSE, 'Orko'),
('Evil', 'Lyn', TRUE, 'Evil-Lyn'),
('Keldor', 'of Eternia', FALSE, 'Keldor'),
('Hordak', 'Unknown', FALSE, 'Hordak'),
('Beast', 'Man', FALSE, 'Beast Man'),
('Trap', 'Jaw', FALSE, 'Trap Jaw');