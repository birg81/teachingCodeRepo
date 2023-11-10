<%@page
	language="java"
	pageEncoding="UTF-8"
	contentType="text/html; charset=UTF-8"
	import="model.Person,java.util.ArrayList"
%><!DOCTYPE html>
<%
ArrayList<Person> characters;
String type;
if(request.getAttribute("characters") != null) {
	characters = (ArrayList<Person>) request.getAttribute("characters");
	type = "warning";
} else {
	characters = (ArrayList<Person>) model.PersonDAO.getAllCharacters();
	type = "danger";
}
%><html lang="it">
<head>
<meta charset="UTF-8" />
<title>The Simpson's</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<link rel="icon" type="image/png" href="https://d1nxzqpcg2bym0.cloudfront.net/google_play/artdevepro.homersimpson.wallpapers/b2a80be6-2486-11e8-8e97-2bae706b6a4f/32x32" />
<link rel="stylesheet" crossorigin="anonymous" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" />
</head>
<body>
<nav aria-label="breadcrumb">
	<ol class="breadcrumb">
		<li class="breadcrumb-item"><a href="./">Dispatcher</a></li>
		<li class="breadcrumb-item"><a href="./characters.v1.jsp">JSP</a></li>
		<li class="breadcrumb-item"><a href="./characters.v2.html">HTML + JSON</a></li>
		<li class="breadcrumb-item"><a href="./api/v2/characters.json">Native JSON</a></li>
	</ol>
</nav>
<table class="table table-<%= type %> table-striped table-hover">
	<thead class="table-dark">
		<tr>
			<th>#</th><th>firstname</th><th>lastname</th><th>gender</th>
		</tr>
	</thead>
	<tbody><%
	if(characters != null && characters.size() > 0) {
		for(Person p: characters) {
	%>
		<tr>
			<th><%= p.getId() %></th>
			<td><%= p.getFirstname() %></td>
			<td><%= p.getLastname() %></td>
			<td><%= p.getGender() %></td>
		</tr><%
		}
	} else { %>
		<tr>
			<td colspan="4">
				<h1>I'm sorry 😞💔</h1>
				<h2>but I can't load the characters 🤷🏻‍♂️ you were looking for&hellip;</h2>
			</td>
		</tr>
	<% } %></tbody>
</table>
</body>
</html>