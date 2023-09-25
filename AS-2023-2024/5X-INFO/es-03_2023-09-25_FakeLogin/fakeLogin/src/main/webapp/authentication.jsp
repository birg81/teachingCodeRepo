<%@page import="model.User, java.util.Arrays, java.util.ArrayList"%>
<%@page language="java" pageEncoding="utf-8" contentType="text/html; charset=utf-8"%>
<%
// lista di utenti riconosciuti
ArrayList<User> userslist = new ArrayList<>(Arrays.asList(
	new User("admin", "admin"),
	new User("root", "root"),
	new User("sa", "sa"),
	new User("user", "1234")
));
// ricevo username e password se sono stati spediti altrimenti li pongo stringa nulla
String username = request.getParameter("username") != null ? request.getParameter("username").strip() : "";
String password = request.getParameter("password") != null ? request.getParameter("password").strip() : "";
// indica se le credenziali ricevute corrispondono ad un utente valido
boolean findUser = false;
// se le credenziali sono valide inizio la ricerca
if(!username.isBlank() && !password.isBlank())
	// cerco il mio utente nella lista di utenti
	for(User u: userslist)
		// se trovo l'utente interrompo la ricerca e pongo il flag findUser a true
		if(u.checkUser(username, password)){
			findUser = true;
			break;
		}
// alternativa alla precedenti righe di codice a partire dalla dichiarazione di findUser
/*
boolean findUser =
	userslist
		.stream()
		.anyMatch(u -> !username.isBlank() && !password.isBlank() && u.checkUser(username, password));
*/
// se al termine della ricerca, non trovo l'utente torno al logine
if(!findUser)
	response.sendRedirect("./");
%>
<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8" />
<title>welcome back <%= username %></title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous" />
<link rel="icon" type="image/png" href="https://em-content.zobj.net/source/google/350/weary-cat_1f640.png" />
</head>
<body>
	<p>Welcome back</p>
	<h1><%= username %></h1>
</body>
</html>