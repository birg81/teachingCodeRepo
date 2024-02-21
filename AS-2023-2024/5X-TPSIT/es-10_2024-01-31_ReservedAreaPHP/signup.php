<?php

$con = @new mysqli('localhost:3306', 'root', '', 'ReservedAreaDB') or die("Errore: $conn->connect_error");
if(
	isset($_REQUEST['username']) &&
	isset($_REQUEST['secret']) &&
	!empty(trim($con->real_escape_string($_REQUEST['username']))) &&
	!empty(trim($con->real_escape_string($_REQUEST['secret'])))
) {
	$username = trim($con->real_escape_string($_REQUEST['username']));
	$secret = trim($con->real_escape_string($_REQUEST['secret']));
	$con->query(trim("INSERT INTO Users(username, secret) VALUES ('$username', '$secret');"));
	if ($con->errno === 0 && $con->affected_rows > 0) {
		$con->close();
	}
}
header('location: ./logout.php');
die;