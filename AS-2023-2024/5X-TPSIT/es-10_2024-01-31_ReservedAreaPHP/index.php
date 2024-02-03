<?php session_start();
if(isset($_SESSION['currentUser']['username']) && !empty(trim($_SESSION['currentUser']['username']))) {
	header('location: ./welcome.php');
	die;
} ?><!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<link rel="icon" type="image/png" href="https://em-content.zobj.net/source/google/387/locked-with-key_1f510.png"/>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap/dist/css/bootstrap.min.css" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous"/>
<title>login Test</title>
</head>
<body>
<div class="container mt-5">
<form method="post" action="./login.php" class="col-md-4 offset-md-4">
	<input type="text" name="username" class="form-control" placeholder="username" required>
	<input type="password" name="secret" class="form-control" placeholder="secret" required>
	<input type="submit" value="Login" class="btn btn-primary btn-block" />
</form>
</div>
</body>
</html>