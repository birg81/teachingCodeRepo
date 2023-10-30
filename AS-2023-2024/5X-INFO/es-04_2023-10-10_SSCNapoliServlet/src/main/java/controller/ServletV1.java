package controller;
import java.io.IOException;
import java.util.ArrayList;

import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import model.Soccer;
@WebServlet(urlPatterns = {"/v1.html"})
public class ServletV1 extends HttpServlet {
	ArrayList<Soccer> players = new ArrayList<>();
	public ServletV1() {
		players.add(new Soccer(1,	"IT",	'P',	"Claudio",	"Garella"));
		players.add(new Soccer(11,	"IT",	'D',	"Andrea",	"Carnevale"));
		players.add(new Soccer(7,	"BR",	'D',	"Alemao",	"Francisco"));
		players.add(new Soccer(3,	"IT",	'D',	"Ciro",	"Ferrara"));
		players.add(new Soccer(2,	"IT",	'D',	"Giuseppe",	"Bruscolotti"));
		players.add(new Soccer(4,	"IT",	'C',	"Salvatore",	"Bagni"));
		players.add(new Soccer(10,	"AR",	'C',	"Diego Armando",	"Maradona"));
		players.add(new Soccer(5,	"IT",	'C',	"Raffaele",	"Di Fusco"));
		players.add(new Soccer(6,	"IT",	'A',	"Giuseppe",	"Volpecina"));
		players.add(new Soccer(9,	"IT",	'A',	"Bruno",	"Giordano"));
		players.add(new Soccer(8,	"IT",	'C',	"Fernando",	"De Napoli"));
	}
	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException {
		req.setAttribute("players", players);
		req.getRequestDispatcher("/v1.jsp")
			.forward(req, res);
	}
}