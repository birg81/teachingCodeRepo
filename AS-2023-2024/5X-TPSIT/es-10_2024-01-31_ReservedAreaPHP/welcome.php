<?php session_start();
if(!isset($_SESSION['currentUser']['username']) || empty(trim($_SESSION['currentUser']['username']))) {
	header('location: ./logout.php');
	die;
} ?><!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<link rel="icon" type="image/png" href="https://em-content.zobj.net/source/google/387/locked-with-key_1f510.png"/>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap/dist/css/bootstrap.min.css" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous"/>
<title>login <?= $_SESSION['currentUser']['username'] ?></title>
</head>
<body>
Welcome <b><?= $_SESSION['currentUser']['username'] ?></b> (<i><?= $_SESSION['currentUser']['id'] ?></i>)
<div><a href="./logout.php" class="btn btn-primary btn-block">logout</a></div>
</form>
</body>
</html>