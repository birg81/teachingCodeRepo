<%@page
	language="java"
	pageEncoding="UTF-8"
	contentType="text/html; charset=UTF-8"
	import="java.util.ArrayList,model.LastnameCounter"
%><!doctype html><%
ArrayList<LastnameCounter> surnames =
	request.getAttribute("surnamesList") != null
		? (ArrayList<LastnameCounter>) request.getAttribute("surnamesList")
		: new ArrayList<LastnameCounter>();
%>
<html lang="en">
<head>
<meta charset="utf-8"/>
<title>Lastname Counter</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<link rel="icon" type="image/png" href="https://em-content.zobj.net/source/google/387/busts-in-silhouette_1f465.png" />
<link href="https://cdn.jsdelivr.net/npm/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
</head>
<body>
<table class="table">
	<thead>
		<tr>
			<th scope="col">#</th>
			<th scope="col">surname</th>
			<th scope="col">N</th>
		</tr>
	</thead>
	<tbody class="table-group-divider">
		<%
		if(surnames != null && surnames.size() > 0) {
			int i = 0;
			for(LastnameCounter surname: surnames) { %>
		<tr>
			<th scope="row"><%= ++i %>.</th>
			<td style="text-transform: capitalize;"><%= surname.getLastname() %></td>
			<td><%= surname.getN() %></td>
		</tr>
		<% }
		} else { %>
		<tr>
			<td colspan="3">Sorry your list is empty 💔</td>
		</tr>
		<% } %>
	</tbody>
</table>
</body>
</html>