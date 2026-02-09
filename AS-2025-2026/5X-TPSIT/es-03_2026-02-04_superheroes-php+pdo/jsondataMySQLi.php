<?php
header('Content-Type: application/json; charset=utf-8');

$filterTxt = (isset($_REQUEST['filterTxt']) && !empty(trim($_REQUEST['filterTxt'])))
	? trim($_REQUEST['filterTxt'])
	: '';

$q = "
	SELECT
		id,
		firstname,
		lastname,
		isHuman,
		supername
	FROM
		HeroesList
	WHERE
		firstname LIKE '%$filterTxt%' OR
		lastname LIKE '%$filterTxt%' OR
		supername LIKE '%$filterTxt%'
	ORDER BY
		supername ASC,
		lastname ASC,
		firstname ASC
	";

try {
	$con = new mysqli('localhost:3306', 'root', '',
		'SuperHeroes'
	);

	if ($con->connect_errno > 0)
		throw new Exception($con->connect_error);

	$rs = $con->query($q);
	$heroes = $rs->fetch_all(MYSQLI_ASSOC);

	echo json_encode(
		$heroes,
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE
	);

	$con->close();
} catch (Throwable $e) {
	http_response_code(500);
	echo json_encode([
		'message' => $e->getMessage()
	]);
}