<%@	page
	language="java"
	pageEncoding="utf-8"
	contentType="text/html; charset=utf-8"
%><%@ page import="model.User" %><%
User currentUser = (User) session.getAttribute("currentUser");
if(currentUser == null)
	response.sendRedirect("login.jsp");
%><!doctype html>
<html lang="it">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" />
<link rel="icon" type="image/png" href="https://em-content.zobj.net/source/toss-face/381/bust-in-silhouette_1f464.png"/>
<title>Welcome <%= currentUser.getEmail() %></title>
</head>
<body>
<h5><%= session.getId() %></h5>
<h1><%= currentUser.toString() %></h1>
<a href="./signOut" class="btn btn-danger">Sign Out</a>
</body>
</html>