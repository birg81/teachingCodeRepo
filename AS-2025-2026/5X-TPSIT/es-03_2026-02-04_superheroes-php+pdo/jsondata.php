<?php
header('Content-Type: application/json; charset=utf-8');
$q = "
	SELECT
		id,
		firstname, lastname,
		isHuman,
		supername
	FROM
		HeroesList
	ORDER BY
		supername ASC,
		lastname ASC,
		firstname ASC;
";

try {
	$con = new PDO(
		'mysql:host=localhost:3306;dbname=SuperHeroes',
		'root',
		''
	);
	$rs = $con->query($q);
	$heroes = $rs->fetchAll(PDO::FETCH_ASSOC);

	echo json_encode(
		$heroes,
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE
	);
} catch (PDOException $e) {
	http_response_code(500);
	echo json_encode([
		'message' => $e->getMessage()
	]);
}