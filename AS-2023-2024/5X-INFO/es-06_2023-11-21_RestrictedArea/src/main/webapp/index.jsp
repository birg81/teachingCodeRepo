<%
response.sendRedirect(
	"%s.jsp".formatted(
		session.getAttribute("currentUser") == null
			? "login"
			: "welcome"
	)
);
%>