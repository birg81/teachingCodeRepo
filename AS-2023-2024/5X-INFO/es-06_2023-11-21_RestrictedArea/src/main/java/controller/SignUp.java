package controller;
import model.User;
import model.UserDAO;
import java.io.IOException;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
@WebServlet(urlPatterns = {"/signUp"})
public class SignUp extends HttpServlet {
	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException {
		final String
			email = !req.getParameter("email").isBlank() ? req.getParameter("email").strip() : "(email)",
			passwd = !req.getParameter("passwd").isBlank() ? req.getParameter("passwd").strip() : "(password)",
			firstname = !req.getParameter("firstname").isBlank() ? req.getParameter("firstname").strip() : "(firstname)",
			lastname = !req.getParameter("lastname").isBlank() ? req.getParameter("lastname").strip() : "(lastname)";
			res.sendRedirect(
				UserDAO.addUser(new User(-1, email, passwd, firstname, lastname))
					? "login.jsp"
					: "register.jsp"
			);
	}
}