<%@	page
	language="java"
	pageEncoding="utf-8"
	contentType="text/html; charset=utf-8"
%><%@ page import="java.util.ArrayList" %><!doctype html>
<html lang="it">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>ShoppingList</title>
<link rel="icon" style="image/png" href="https://em-content.zobj.net/source/google/56/shopping-trolley_1f6d2.png" />
<link rel="stylesheet" crossorigin="anonymous" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" />
</head>
<body>
<script src="./src/modifyItem.js"></script>
<nav class="navbar bg-light">
<div class="container-fluid row g-3">
<form method="get" action="./create" class="d-flex" role="search">
	<input type="search" name="item" placeholder="inserisci prodotto" class="form-control" aria-label="Search" />
	<input type="submit" value="&#x1f6d2;" class="btn btn-outline-success" />
</form>
</div>
</nav>
<%
ArrayList<String> itemsList = (ArrayList<String>) session.getAttribute("itemsList");
if(itemsList == null)
	itemsList = new ArrayList<String>();
%><ul class="list-group"><% for(int i = 0; i < itemsList.size(); i++) { %>
<li class="list-group-item">
	<div class="btn-group" role="group">
		<a class="btn btn-outline-danger" href="./delete?id=<%= i %>">&#x274c;</a>
		<a class="btn btn-outline-warning" href="javascript:modifyItem(<%= i %>, '<%= itemsList.get(i) %>')">&#x270d;</a>
	</div>
	<b><%= itemsList.get(i) %></b>
</li>
<% } %></ul>
<nav class="navbar fixed-bottom navbar-light bg-light">
	<a class="btn btn-primary w-100" href="./">🔄 Ricarica Pagina</a>
</nav>
</body>
</html>