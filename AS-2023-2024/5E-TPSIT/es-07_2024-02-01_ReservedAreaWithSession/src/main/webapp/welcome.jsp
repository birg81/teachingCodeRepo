<%@page language="java" import="model.User" pageEncoding="UTF-8" contentType="text/html; charset=UTF-8"
%><%
User user = (User) session.getAttribute("currentUser") != null ? (User) session.getAttribute("currentUser") : new User("", "");
if("".equals(user.getUsername()))
	response.sendRedirect("./logout");
%><!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<link rel="icon" type="image/png" href="https://em-content.zobj.net/source/google/387/locked-with-key_1f510.png"/>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap/dist/css/bootstrap.min.css" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous"/>
<title><%= user.getUsername() %> 🔑</title>
</head>
<body>
Welcome <b><%= user %></b>
<div><a href="./logout" class="btn btn-primary btn-block">logout</a></div>
</form>
</body>
</html>