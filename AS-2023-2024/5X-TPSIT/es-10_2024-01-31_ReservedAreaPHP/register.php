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
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous"/>
<title>register</title>
</head>
<body>
<div class="container mt-5">
<form method="post" action="./signup.php" class="col-md-4 offset-md-4">
	<input type="text" name="username" class="form-control" placeholder="username" required />
	<input type="password" name="secret" class="form-control" placeholder="secret" required />
	<input type="submit" value="Register" class="btn btn-primary btn-block" />
	<a href="./" class="btn btn-success btn-block">Home</a>
</form>
</div>
</body>
</html>