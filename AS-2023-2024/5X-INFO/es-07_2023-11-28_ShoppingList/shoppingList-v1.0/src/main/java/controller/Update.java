package controller;
import java.io.IOException;
import java.util.ArrayList;
import java.util.stream.Collectors;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
@WebServlet("/update")
public class Update extends HttpServlet {
	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException {
		final ArrayList<String> itemsList = req.getSession().getAttribute("itemsList") != null
			? (ArrayList<String>) req.getSession().getAttribute("itemsList")
			: new ArrayList<String>();
		int id = req.getParameter("id") != null ? Integer.parseInt(req.getParameter("id")) : -1;
		String item = req.getParameter("item") != null ? req.getParameter("item").strip().toLowerCase() : "";
		if(id > -1 && id < itemsList.size() && !item.isBlank() && !itemsList.contains(item))
			itemsList.set(id, item);
		req.getSession().setAttribute("itemsList", itemsList.stream().sorted().collect(Collectors.toList()));
		res.sendRedirect("./");
	}
}