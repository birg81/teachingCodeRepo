<%@page language="java" pageEncoding="utf-8" contentType="text/html; charset=utf-8"%>
<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8" />
<title>Fake Login</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous" />
<link rel="icon" type="image/png" href="https://em-content.zobj.net/source/google/350/grinning-cat-with-smiling-eyes_1f638.png" />
</head>
<body>
	<form method="get" action="./authentication.jsp">
		<div class="input-group mb-3">
			<input type="text" class="form-control" name="username" aria-placeholder="username" required />
			<input type="password" class="form-control" name="password" aria-placeholder="password" required />
			<input type="submit" class="btn btn-primary" />
		</div>
	</form>
</body>
</html>