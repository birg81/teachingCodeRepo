<?php
session_start();
$con = @new mysqli('localhost:3306', 'root', '', 'ReservedAreaDB') or die("Errore: $conn->connect_error");
if(
	$_SERVER['REQUEST_METHOD'] === 'POST' &&
	isset($_REQUEST['username']) &&
	isset($_REQUEST['secret']) &&
	!empty(trim($con->real_escape_string($_REQUEST['username']))) &&
	!empty(trim($con->real_escape_string($_REQUEST['secret'])))
) {
	$username = trim($con->real_escape_string($_REQUEST['username']));
	$secret = trim($con->real_escape_string($_REQUEST['secret']));
	$rs = $con->query(trim("SELECT id, username FROM Users WHERE username = '{$username}' AND secret = '$secret';"));
	if ($con->errno === 0 && $rs->num_rows > 0) {
		$_SESSION['currentUser'] = $rs->fetch_assoc();
		$con->close();
		header('location: ./welcome.php');
		die;
	}
}
header('location: ./logout.php');
die;