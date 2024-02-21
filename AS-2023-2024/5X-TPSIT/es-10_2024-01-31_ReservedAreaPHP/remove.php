<?php
$con = @new mysqli('localhost:3306', 'root', '', 'ReservedAreaDB') or die("Errore: $conn->connect_error");
if(
	isset($_REQUEST['id']) &&
	!empty(trim($con->real_escape_string($_REQUEST['id'])))
) {
	$id = trim($con->real_escape_string($_REQUEST['id'])) + 0;
	$con->query(trim("DELETE FROM Users WHERE id=$id;"));
	if ($con->errno === 0 && $rs->affected_rows > 0) {
		$con->close();
	}
}
header('location: ./logout.php');
die;