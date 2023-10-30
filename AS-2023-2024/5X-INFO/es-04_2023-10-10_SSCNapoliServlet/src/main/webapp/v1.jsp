<%@ page
language="java"
import="model.Soccer, java.util.ArrayList"
pageEncoding="UTF-8"
contentType="text/html; charset=UTF-8"
%><!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>SSC Napoli - v.1</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<link rel="icon" type="image/png" href="https://em-content.zobj.net/source/google/110/stadium_1f3df.png"/>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous"/>
</head>
<body>
<div class="card">
	<div class="card-body">
	This is the lineup of SSC Napoli for their first Serie A championship win in the 1986-1987 season.
	</div>
</div>
<table class="table table-sm">
<thead>
	<tr>
		<th>#N</th><th>Firstname</th><th>Lastname</th><th>Country</th><th>Role</th>
	</tr>
</thead>
<tbody><% for(Soccer p: (ArrayList<Soccer>) request.getAttribute("players")) { %>
<tr>
	<th><%= p.getN() %></th>
	<td><%= p.getFirstname() %></td>
	<td><%= p.getLastname() %></td>
	<td><%= p.getCountry() %></td>
	<td><%= p.getRole() %></td>
</tr><% } %></tbody>
</table>
</tr>
</body>
</html>