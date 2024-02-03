<!doctype html>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"
%><%
int count = session.getAttribute("count") != null ? (Integer) session.getAttribute("count") : 0;
session.setAttribute("count", ++count);
%><html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<link rel="icon" type="image/png" href="https://em-content.zobj.net/source/sony/336/dizzy_1f4ab.png"/>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap/dist/css/bootstrap.min.css" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous"/>
<title>Counting</title>
</head>
<body class="text-center">
<div class="container mt-5">
<div class="row">
	<div class="col">
		<div class="alert alert-primary" role="alert"><h1><%= count %></h1></div>
	</div>
</div>
<div class="row mt-3">
<div class="col">
	<div class="alert alert-info" role="alert" title="Session ID"><%= session.getId() %></div>
</div>
</div>
<div class="row mt-3">
	<div class="col-6">
		<a href="./reset" title="Reset Counting" class="btn btn-danger btn-block" role="button">🗑️</a>
	</div>
	<div class="col-6">
		<a href="./" title="Reload Page" class="btn btn-success btn-block" role="button">😵</a>
	</div>
</div>
</div>
</body>
</html>