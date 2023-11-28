package controller;
import java.io.IOException;
import java.util.ArrayList;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
@WebServlet("/delete")
public class Delete extends HttpServlet {
	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException {
		final ArrayList<String> itemsList = req.getSession().getAttribute("itemsList") != null
			? (ArrayList<String>) req.getSession().getAttribute("itemsList")
			: new ArrayList<String>();
		int id = req.getParameter("id") != null ? Integer.parseInt(req.getParameter("id")) : -1;
		if(id > -1 && id < itemsList.size())
			itemsList.remove(id);
		req.getSession().setAttribute("itemsList", itemsList);
		res.sendRedirect("./");
	}
}