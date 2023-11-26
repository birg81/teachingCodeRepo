package controller;
import model.User;
import model.UserDAO;

import java.io.IOException;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
@WebServlet(urlPatterns = { "/signIn" })
public class SignIn extends HttpServlet{
	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException {
		final String
			email = req.getParameter("email") != null & !req.getParameter("email").isBlank()
				? req.getParameter("email").strip()
				: "(email)",
			passwd = req.getParameter("passwd") != null && !req.getParameter("passwd").isBlank()
				? req.getParameter("passwd").strip()
				: "(password)";
		User u = UserDAO.getUserByAuth(email, passwd);
		if(u != null)
			req.getSession().setAttribute("currentUser", u);
		res.sendRedirect("./");
	}
}