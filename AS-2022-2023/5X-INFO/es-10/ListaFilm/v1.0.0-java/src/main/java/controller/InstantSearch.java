package controller;
import model.FilmDAO;
import java.io.IOException;
import com.google.gson.Gson;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
@SuppressWarnings("serial")
@WebServlet(urlPatterns = { "/api/*" })
public class InstantSearch extends HttpServlet {
	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse res)
		throws ServletException, IOException
	{
		res.setContentType("application/json");
		res.setCharacterEncoding("UTF-8");
		String title = req.getPathInfo() != null && req.getPathInfo().split("/").length > 1
			? req.getPathInfo().split("/")[1].strip().toLowerCase()
			: "";
		res.getWriter().print(new Gson().toJson(FilmDAO.getFilmByTitle(title)));
	}
}
