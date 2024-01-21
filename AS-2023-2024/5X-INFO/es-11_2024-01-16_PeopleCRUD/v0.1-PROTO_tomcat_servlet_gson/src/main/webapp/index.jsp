<%@	page
	language="java"
	pageEncoding="utf-8"
	contentType="text/html; charset=utf-8"
%><!doctype html>
<html lang="it">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<link rel="icon" type="image/png" href="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Google_Contacts_icon_%282022%29.svg/203px-Google_Contacts_icon_%282022%29.svg.png">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap/dist/css/bootstrap.min.css" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous" />
<title>People List</title>
</head>
<body>
<script src="./src/crud.js"></script>
<table class="table table-striped">
<thead class="table-dark">
<tr>
	<th class="table-dark">id</th>
	<th class="table-dark">FirstName</th>
	<th class="table-dark">Lastname</th>
	<th class="table-dark">⚙️</th>
</tr>
<tr>
	<th><input type="number" placeholder="id" id="id_0" class="form-control" /></th>
	<th><input type="text" placeholder="firstname" id="firstname_0" class="form-control" /></th>
	<th><input type="text" placeholder="lastname" id="lastname_0" class="form-control" /></th>
	<th><button class="btn btn-outline-primary" onclick="addPerson()">✔️</button></th>
</tr>
<tr>
	<th colspan="4">
	<input type="search" placeholder="match" id="searchbox" class="form-control" onkeyup="updatePageData(this.value)"/>
	</th>
</tr>
</thead>
<tbody id="people">
</tbody>
</table>
<nav class="navbar fixed-bottom navbar-dark bg-dark">
	<button class="btn btn-dark w-100" onclick="updatePageData()">🔄 Ricarica Pagina</button>
</nav>
</body>
</html>