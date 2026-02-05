<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>SuperHeroes List (pure PHP)</title>
	<link type="image/png" rel="icon" href="https://em-content.zobj.net/source/facebook/158/superhero_emoji-modifier-fitzpatrick-type-1-2_1f9b8-1f3fb_1f3fb.png" />
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous" />
</head>
<body>
<table class="table table-primary table-striped">
	<thead>
		<tr>
			<th scope="col">id</th>
			<th scope="col">Super Hero</th>
			<th scope="col">isHuman</th>
			<th scope="col">firstname</th>
			<th scope="col">lastname</th>
		</tr>
	</thead>
	<tbody>
<?php
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
	foreach($heroes as $hero) {
		$human = $hero['isHuman'] ? '🧑' : '👽';
		echo "
			<tr>
				<th>{$hero['id']}</th>
				<td><i>{$hero['supername']}</i></td>
				<td>{$human}</td>
				<td>{$hero['firstname']}</td>
				<td>{$hero['lastname']}</td>
			</tr>
		";
	}
} catch (PDOException $e) {
	echo "<tr><td colspan='5'><i>{$e->getMessage()}</i></td></tr>";
}
?>
	</tbody>
</table>
</body>
</html>