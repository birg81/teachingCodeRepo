package controller;
import model.User;
import java.io.IOException;
import java.util.ArrayList;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
@WebServlet(urlPatterns = { "/login" })
public class Login extends HttpServlet {
	// lista utenti
	private ArrayList<User> users = new ArrayList<>();
	public Login() {
		// setto degli utenti fittizi
		users.add(new User("admin", "admin"));
		users.add(new User("birg81", "123456"));
		users.add(new User("peppe", "pallino"));
		users.add(new User("raffaele", "cioffigo"));
	}
	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException {
		// invalido la vecchia sessione
		req.getSession().invalidate();
		// prelevo i parametri e li metto in un oggetto User che eventualmente li ripulirà!
		User user = new User(req.getParameter("username"), req.getParameter("secret"));
		// controllo che nella lista esista un utente con le credenziali assegnate e che le credenziali siano corrette
		if(users.stream().anyMatch(u -> u.equals(user))) {
			// scrivo nella sessione il nome dell'utente corrente
			req.getSession().setAttribute("currentUser", user);
			// salto nella pagina di benvenuto
			res.sendRedirect("./welcome.jsp");
		} else
			// passo il controllo alla servlet per il logout
			req.getRequestDispatcher("./logout")
				.forward(req, res);
	}
	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException {
		// serve a prevenire i casi in cui mi dirigo sulla rotta in cui gira la servlet
		res.sendRedirect("./logout");
	}
}