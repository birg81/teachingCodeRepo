package controller;
import java.io.IOException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
@WebServlet(urlPatterns = {"/index.html", "/index.jsp"})
public class ServletV0 extends HttpServlet {
	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException {
		res.getWriter().print(
		"""
		<!DOCTYPE html>
		<html lang="en">
		<head>
		<meta charset="utf-8" />
		<title>intro Servlet</title>
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<link rel="icon" type="image/png" href="https://em-content.zobj.net/source/google/110/smiling-cat-face-with-open-mouth_1f63a.png"/>
		<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous"/>
		</head>
		<body>
		<div class="container">
		<h1 class="mt-5">Welcome to this page</h1>
		<p class="mt-3"><b>Be very cautious</b>, for nothing is as it appears! 😲✨🔮</p>
		<p class="mt-4">Now, please select your favorite <b>version</b>:</p>
		<ul class="list-group">
		<li class="list-group-item"><b>Version 0:</b> This current page is actually <b>only</b> a servlet that returns an HTML page.</li>
		<li class="list-group-item"><b><a href="./v1.html">Version 1</a></b>: This is not an HTML page but a Servlet to get an ArrayList&lt;Player&gt; to a JSP page.</li>
		<li class="list-group-item"><b><a href="./v2.html">Version 2</a></b>: This, on the other hand, is an HTML page that receives JSON data from a Servlet through a JavaScript fetch operation and displays it on the page.</li>
		</ul>
		</div>
		</body>
		</html>
		"""
		);
	}
}