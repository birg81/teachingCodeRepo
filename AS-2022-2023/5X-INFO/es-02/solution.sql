USE personlist5x;


-- Q1:
SELECT
	p.lastname AS Cognome,
	p.firstname AS Nome,
	IF (p.gender > 1, "F ♀", "M ♂") AS Sesso,
	p.birthday AS `B.day`
FROM
	people AS p
ORDER BY
	p.lastname ASC,
	p.firstname ASC,
	p.birthday DESC;


-- Q2
SELECT
	p.lastname AS Cognome,
	p.firstname AS Nome,
	IF (p.gender > 1, "F ♀", "M ♂") AS Sesso,
	p.birthday AS `B.day`
FROM
	people AS p
WHERE
	p.gender = 2 AND
	p.birthday < '2000-01-01'
ORDER BY
	p.birthday DESC;


-- Q3:
SELECT
	p.lastname AS Cognome,
	p.firstname AS Nome,
	IF (p.gender > 1, "F ♀", "M ♂") AS Sesso,
	p.weight AS peso,
	p.height AS altezzaFROM
FROM
	people AS p
WHERE
	p.gender = 1
ORDER BY
	p.height DESC
LIMIT 10;


-- Q4:
SELECT
	p.lastname AS Cognome,
	p.firstname AS Nome,
	IF (p.gender > 1, "F ♀", "M ♂") AS Sesso,
	p.weight AS peso,
	p.height AS h
FROM
	people AS p
WHERE
	p.gender = 2
ORDER BY
	p.weight ASC
LIMIT 5;


-- Q5:
SELECT
	p.lastname AS Cognome,
	p.firstname AS Nome,
	IF (p.gender > 1, "F ♀", "M ♂") AS Sesso,
	p.weight AS peso,
	p.height AS altezza,
	10000 * weight/(height*height) AS IMC
FROM
	people AS p
ORDER BY
	IMC ASC;


-- Q6:
SELECT
	p.lastname AS Cognome,
	p.firstname AS Nome,
	p.birthday AS `B-Day`,
	IF (p.gender > 1, "F ♀", "M ♂") AS Sesso,
	p.weight AS peso,
	p.height AS altezza,
	10000 * weight/(height*height) AS IMC
FROM
	people AS p
WHERE
	10000 * weight / (height*height) BETWEEN 18.5 AND 25
ORDER BY
	IMC DESC;


-- Q7:
SELECT
	p.lastname AS Cognome,
	p.firstname AS Nome,
	IF (p.gender > 1, "F ♀", "M ♂") AS Sesso,
	p.mobile AS `cel.`
FROM
	people AS p
WHERE
	p.mobile NOT LIKE '%2%' AND
	p.mobile NOT LIKE '%4%'
ORDER BY
	p.lastname DESC,
	p.firstname ASC;


-- Q8:
SELECT
	p.lastname AS Cognome,
	p.firstname AS Nome,
	IF (p.gender > 1, "F ♀", "M ♂") AS Sesso,
	p.height AS h
FROM
	people AS p
WHERE
	p.gender = 1 AND
	p.height BETWEEN 165 AND 171
ORDER BY
	p.height DESC;


-- Q9:
SELECT
	p.lastname AS Cognome,
	p.firstname AS Nome,
	IF (p.gender > 1, "F ♀", "M ♂") AS Sesso,
	p.code AS `Cod. Fis.`
FROM
	people AS p
WHERE
	p.code LIKE '%L' AND
	p.gender = 2
ORDER BY
	p.code;


-- Q10:
SELECT
	p.lastname AS Cognome,
	p.firstname AS Nome,
	IF (p.gender > 1, "F ♀", "M ♂") AS Sesso,
	p.code AS `Cod. Fis.`
FROM
	people AS p
WHERE
	p.firstname NOT LIKE '%O%' AND
	p.lastname NOT LIKE '%O%' AND
	p.gender = 1
ORDER BY
	p.lastname ASC,
	p.firstname DESC;
