package controller;

import java.io.IOException;
import java.util.ArrayList;

import com.google.gson.Gson;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
@SuppressWarnings("serial")
@WebServlet(urlPatterns = {"/api/*"})
public class TestWebAPI extends HttpServlet {
	ArrayList<String> itemsList;
	public TestWebAPI() {
		itemsList = new ArrayList<>();
	}
	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse res)
			throws ServletException, IOException {
		res.setContentType("application/json");
		res.setCharacterEncoding("UTF-8");
		String item =
			req.getPathInfo() != null &&
			req.getPathInfo().split("/").length > 1
				? req.getPathInfo().split("/")[1].strip().toLowerCase()
				: "";
		if(!item.isBlank() && !itemsList.contains(item) && itemsList.add(item)) {
			res.getWriter().printf("""
			{
				"message": "add '%s' to list!..",
				"success": true
			}
			""", item);
			return;
		}
		res.getWriter().printf("""
		{
			"message": "maybe '%s' is already in your list..',
			"success": false
		}
		""", item);
	}
	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse res)
			throws ServletException, IOException {
		res.setContentType("application/json");
		res.setCharacterEncoding("UTF-8");
		if(req.getPathInfo() == null || req.getPathInfo().equals("/") && !itemsList.isEmpty()) {
			itemsList.sort(null);
			res.getWriter().print(new Gson().toJson(itemsList));
			return;
		}
		res.getWriter().print("[]");
	}
	@Override
	protected void doPut(HttpServletRequest req, HttpServletResponse res)
			throws ServletException, IOException {
		res.setContentType("application/json");
		res.setCharacterEncoding("UTF-8");
		int id = -1;
		String item = "";
		if(req.getPathInfo() != null && req.getPathInfo().split("/").length > 2) {
			id = Integer.parseInt(req.getPathInfo().split("/")[1].strip());
			item = req.getPathInfo().split("/")[2].strip().toLowerCase();
		}
		if(id > -1 && !item.isBlank() && !itemsList.contains(item)) {
			res.getWriter().printf("""
			{
				"method": "update '%s', change to '%s'..",
				"success": true
			}
			""", itemsList.get(id), item);
			itemsList.set(id, item);
			return;
		}
		res.getWriter().printf("""
		{
			"method": "maybe '%s' is already in your list or maybe %d is not a valid index..",
			"success": false
		}
		""", item, id);
	}
	@Override
	protected void doDelete(HttpServletRequest req, HttpServletResponse res)
			throws ServletException, IOException {
		res.setContentType("application/json");
		res.setCharacterEncoding("UTF-8");
		int id =
			req.getPathInfo() != null &&
			req.getPathInfo().split("/").length > 1 &&
			Integer.parseInt(req.getPathInfo().split("/")[1].strip()) > -1
				? Integer.parseInt(req.getPathInfo().split("/")[1].strip())
				: -1;
		if (id > -1 && id < itemsList.size()) {
			String item = itemsList.remove(id);
			res.getWriter().printf("""
			{
				"message": "'%s' was removed..",
				"success": true
			}
			""", item);
			return;
		}
		res.getWriter().printf("""
		{
			"message": "maybe '%d' is not a valid index..",
			"success": false
		}
		""",id);
	}
}