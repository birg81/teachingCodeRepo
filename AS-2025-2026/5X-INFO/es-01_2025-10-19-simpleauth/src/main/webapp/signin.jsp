<%@page import="model.User,controller.UsersManager" %>
<%
String email = request.getParameter("email") != null ? request.getParameter("email").strip() : "";
String password = request.getParameter("password") != null ? request.getParameter("password").strip() : "";

User u = UsersManager.checkUser(email,password);
%><!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Login Response</title>
</head>
<body>
<% if(u != null) {%>
<h1>Salve, <%= u.toString() %></h1>
<% } else { %>
<p>Spiacente ma non esiste un utente con credenziali <strong><%= email %></strong> e <em><%= password %></em></p>
<% } %>
</body>
</html>