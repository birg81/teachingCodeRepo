<%@page language="java" pageEncoding="utf-8" contentType="text/html; charset=utf-8"%>
<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,shrink-to-fit=no,user-scalable=yes,initial-scale=1.0,maximum-scale=4.0,minimum-scale=0.5" />
<link type="image/png" rel="icon" href="https://em-content.zobj.net/source/twitter/376/cat-face_1f431.png" />
<title>Web Page</title>
</head>
<body>
<% for(int i = 0; i < 10; i++) { %>
<p>Forza Napoli! (<%= i %>)</p>
<% } %>
</body>
</html>