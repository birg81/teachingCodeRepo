-- Test Advance query
SELECT
	p0.lastname AS cognome,
	p0.firstname AS nome,
	IF(p0.gender < 2 , "♂️", "♀") AS `⚥`,
	p0.birthday AS bDay,
	cb.name AS cityBorn,
	cl.name AS cityLive,
	cj.name AS cityJob
FROM
-- city born
	(people AS p0)
		JOIN
	(cities AS cb)
		ON
			bornplace = cb.id,
-- city live
	(people AS pl)
		JOIN
	(place2live AS l)
		ON
			l.people = pl.id
	JOIN
		(cities AS cl)
		ON
			l.place = cl.id,
-- city job
	(people AS pj)
		JOIN
	(place2job AS j)
		ON
			j.people = pj.id
	JOIN
		(cities AS cj)
		ON
			j.place = cj.id
WHERE
	pl.id = p0.id AND
	pj.id = p0.id
ORDER BY
	cognome ASC;
