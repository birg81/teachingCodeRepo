-- Prima di creare il DB cancelliamo la versione veccchia
DROP DATABASE IF EXISTS UnivStud5F;
CREATE DATABASE IF NOT EXISTS UnivStud5F;
-- Indichiamo di usare il DB appena creato
USE UnivStud5F;

-- Studenti
DROP TABLE IF EXISTS Students;
CREATE TABLE IF NOT EXISTS Students(
	id INT PRIMARY KEY AUTO_INCREMENT,
	firstname VARCHAR(24) NOT NULL,
	lastname VARCHAR(24) NOT NULL,
	cf CHAR(16) UNIQUE NOT NULL,
	birthday DATE NOT NULL,
	-- questa è la matricola
	serialnumber VARCHAR (10) NOT NULL,
	gender CHAR(1) NOT NULL DEFAULT 'm'
);

-- Studenti (Popolamento)
INSERT INTO Students(firstname, lastname, gender, cf, birthday, serialnumber) VALUES
	('Alessio',	'Liguori',	'm',	'LGILSS99B27H999Z',	'1999-02-27',	'XF86944810'),
	('Agata',	'Capone',	'f',	'CPNGTA02H69Y102X',	'2002-06-29',	'QH47754832'),
	('Bernardo',	'Monaldo',	'm',	'MNLBRD00R12X098X',	'2000-10-12',	'WL66820854'),
	('Lorella',	'Pinto',	'f',	'PNTLRL09D55W456X',	'2009-04-15',	'PA48512092'),
	('Marco',	'Messigno',	'm',	'MSSMRC98P12A123X',	'1998-09-12',	'WL55483921');


-- Materie
DROP TABLE IF EXISTS Subjects;
CREATE TABLE IF NOT EXISTS Subjects (
	id INT PRIMARY KEY AUTO_INCREMENT,
	courseName VARCHAR(32) NOT NULL,
	code CHAR(12) NOT NULL
);

-- Popolamento Materie
INSERT INTO Subjects(courseName, code) VALUES
	('Informatica',	'ING-INF/05'),
	('Analisi I',	'MAT/05'),
	('Analisi II',	'MAT/05'),
	('Basi di dati',	'ING-INF/05'),
	('Reti di calcolatori',	'ING-INF/05'),
	('Programmazione ad oggetti',	'ING-INF/05');


-- Corsi (corsi intesi come diverse lezioni)
DROP TABLE IF EXISTS Lessons;
CREATE TABLE IF NOT EXISTS Lessons (
	id INT PRIMARY KEY AUTO_INCREMENT,
	dt DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	fk_subject INT NOT NULL,
	FOREIGN KEY (fk_subject) REFERENCES Subjects(id)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);


-- Esami
-- grade [ovvero voto]: (17: bocciatura, ... 31: lode)
DROP TABLE IF EXISTS Exams;
CREATE TABLE IF NOT EXISTS Exams (
	id INT PRIMARY KEY AUTO_INCREMENT,
	dt DATE NOT NULL DEFAULT (CURRENT_DATE),
	grade INT NOT NULL CHECK(grade >=17 AND grade <= 31),
	fk_stud INT NOT NULL,
	fk_subject INT NOT NULL,
	FOREIGN KEY (fk_stud) REFERENCES Students(id)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	FOREIGN KEY (fk_subject) REFERENCES Subjects(id)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);

-- Esami
INSERT INTO Exams(fk_stud, fk_subject, grade) VALUES
	(3,	2,	18),
	(1,	1,	20),
	(2,	3,	21),
	(1,	2,	17),
	(4,	4,	23);



-- Q: Selezionare mtr, nome, cognome, voto, materia degli studenti che hanno sostenuto esami
SELECT
	s.serialnumber AS mtr,
	s.firstname AS nome,
	s.lastname AS cognome,
	e.grade AS voto,
	m.courseName AS materia,
	e.dt AS dt_Esame
FROM
	Students AS s,
	Exams AS e,
	Subjects AS m
WHERE
	s.id = e.fk_stud AND
	e.fk_subject = m.id;


-- Q: alternativa AVANZATA query precedente
SELECT
	s.serialnumber AS mtr,
	s.firstname AS nome,
	s.lastname AS cognome,
	e.grade AS voto,
	m.courseName AS materia,
	e.dt AS dt_Esame
FROM
	(Students AS s) INNER JOIN (Exams AS e)
		ON s.id = e.fk_stud
	INNER JOIN (Subjects AS m)
		ON e.fk_subject = m.id
ORDER BY
	s.lastname ASC,
	s.firstname ASC,
	s.serialnumber ASC;