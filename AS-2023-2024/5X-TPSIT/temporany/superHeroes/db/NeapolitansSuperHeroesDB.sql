DROP DATABASE IF EXISTS NeapolitansSuperHeroesDB;
CREATE DATABASE IF NOT EXISTS NeapolitansSuperHeroesDB;
USE NeapolitansSuperHeroesDB;



-- Update della tabella SuperHeroes
DROP TABLE IF EXISTS SuperHeroes;
CREATE TABLE IF NOT EXISTS SuperHeroes (
	id INT PRIMARY KEY AUTO_INCREMENT,
	firstname VARCHAR(50) NOT NULL,
	lastname VARCHAR(50) NOT NULL,
	supername VARCHAR(50) UNIQUE NOT NULL
);

-- Popolamento della tabella SuperHeroes
INSERT INTO SuperHeroes (firstname, lastname, supername) VALUES
	('Antonio', 'Esposito', 'PizzaPuncher'),
	('Giovanna', 'Ricciardi', 'VesuviusVortex'),
	('Luigi', 'De Luca', 'PastaMaster'),
	('Carmela', 'Ferrara', 'TarantellaTwister'),
	('Raffaele', 'Sorrentino', 'GelatoGlider'),
	('Teresa', 'Amato', 'MozzarellaMystique'),
	('Mario', 'Gallo', 'SfogliatellaSpectre');



-- Update della tabella SuperPowers
DROP TABLE IF EXISTS SuperPowers;
CREATE TABLE IF NOT EXISTS SuperPowers (
	id INT PRIMARY KEY AUTO_INCREMENT,
	power VARCHAR(50) UNIQUE NOT NULL,
	description VARCHAR(255) NOT NULL
);

-- Popolamento della tabella SuperPowers
INSERT INTO SuperPowers (power, description) VALUES
	('Manipolazione della Pizza', 'Controllo degli ingredienti e delle forme della pizza'),
	('Esplosione di Energia Vulcanica', 'Scatena un&rsquo;energia potente dal Vesuvio'),
	('Trasformazione della Pasta', 'Può trasformare oggetti in pasta'),
	('Teletrasporto con Tarantella', 'Si sposta istantaneamente con la danza della tarantella'),
	('Generazione di Gelato', 'Crea e controlla costrutti di gelato'),
	('Telecinesi della Mozzarella', 'Muove oggetti con il potere della mozzarella'),
	('Invisibilità con Sfogliatella', 'Può diventare invisibile con il potere della sfogliatella'),
	('Proiezione di Pomodoro', 'Proietta illusioni usando il potere del pomodoro'),
	('Rimbalzo con il Baba', 'Rimbalza su superfici con il potere del baba'),
	('Fulmini al Limone', 'Genera fulmini con l&rsquo;essenza dei limoni'),
	('Protezione del Provolone', 'Crea barriere protettive con il provolone'),
	('Contorsione del Calzone', 'Piega e torce la realtà con il potere del calzone'),
	('Guarigione con l&rsquo;Olio d&rsquo;Oliva', 'Cura le ferite usando la magia dell&rsquo;olio d&rsquo;oliva'),
	('Riflessione della Ricotta', 'Riflette gli attacchi con il potere della ricotta'),
	('Clonazione del Cannolo', 'Crea duplicati con l&rsquo;essenza del cannolo'),
	('Allungamento degli Spaghetti', 'Estende e manipola oggetti con gli spaghetti'),
	('Fase del Panzerotto', 'Può attraversare oggetti solidi come un panzerotto'),
	('Manipolazione Temporale del Tiramisù', 'Controlla il tempo con la dolcezza del tiramisù'),
	('Telepatia dei Biscotti', 'Comunica con gli altri usando il potere dei biscotti'),
	('Portali delle Pizzelle', 'Apre portali verso diverse posizioni con le pizzelle');



-- Update della tabella che associa supereroi a superpoteri
DROP TABLE IF EXISTS SuperHeroPowers;
CREATE TABLE IF NOT EXISTS SuperHeroPowers (
	fk_superhero INT NOT NULL,
	fk_power INT NOT NULL,
	PRIMARY KEY (fk_superhero, fk_power),
	FOREIGN KEY (fk_superhero) REFERENCES SuperHeroes(id)
		ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (fk_power) REFERENCES SuperPowers(id)
		ON DELETE CASCADE ON UPDATE CASCADE
);

-- Popolamento della tabella SuperHeroPowers
INSERT INTO SuperHeroPowers (fk_superhero, fk_power) VALUES
	(1, 1),
	(1, 7),
	(2, 2),
	(2, 10),
	(3, 3),
	(3, 18),
	(4, 4),
	(4, 15),
	(5, 5),
	(5, 13),
	(6, 6),
	(6, 17),
	(7, 7),
	(7, 19),
	(1, 14),
	(2, 9),
	(3, 12),
	(4, 16),
	(5, 11),
	(6, 8),
	(7, 20);