<%@	page
	language="java"
	pageEncoding="utf-8"
	contentType="text/html; charset=utf-8"
%><%
if(session.getAttribute("currentUser") != null)
	response.sendRedirect("welcome.jsp");
%><!doctype html>
<html lang="it">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" />
<link rel="icon" type="image/png" href="https://em-content.zobj.net/source/toss-face/381/bust-in-silhouette_1f464.png"/>
<title>Login</title>
</head>
<body>
<div class="container mt-5">
	<div class="row justify-content-center">
		<div class="col-md-6">
			<div class="card">
				<div class="card-header bg-primary text-white">
					<h4 class="mb-0">Login</h4>
				</div>
				<div class="card-body">
					<form method="post" action="./signIn">
						<div class="form-group">
							<label for="inputEmail">Email</label>
							<input type="email" class="form-control" name="email" placeholder="Email" required>
						</div>
						<div class="form-group">
							<label for="inputPassword">Password</label>
							<input type="password" class="form-control" name="passwd" placeholder="Password" required>
						</div>
						<button type="submit" class="btn btn-success">Sign in</button>
						<a href="./register.jsp" class="btn btn-primary">Sign up</a>
					</form>
				</div>
			</div>
		</div>
	</div>
</div>
</body>
</html>