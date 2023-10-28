package controller;
import model.Soccer;
import java.io.IOException;
import java.util.ArrayList;
import com.google.gson.Gson;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
@WebServlet(urlPatterns = {"/api/soccer"})
public class Routing extends HttpServlet {
	ArrayList<Soccer> players = new ArrayList<>();
	public Routing() {
		players.add(new Soccer(1,	"IT",	'P',	"Alex",	"Meret"));
		players.add(new Soccer(3,	"BR",	'D',	"Natan Berardo",	"de Souza"));
		players.add(new Soccer(4,	"DE",	'C',	"Diego",	"Demme"));
		players.add(new Soccer(5,	"BR",	'D',	"Juan",	"Jesus"));
		players.add(new Soccer(6,	"PT",	'D',	"Mário",	"Rui"));
		players.add(new Soccer(7,	"MK",	'C',	"Eljif",	"Elmas"));
		players.add(new Soccer(9,	"NG",	'A',	"Victor",	"Osimhen"));
		players.add(new Soccer(13,	"KS",	'D',	"Amir",	"Rrahmani"));
		players.add(new Soccer(14,	"IT",	'P',	"Nikita",	"Contini"));
		players.add(new Soccer(16,	"PL",	'P',	"Hubert",	"Idasiak"));
		players.add(new Soccer(17,	"UY",	'D',	"Mathías",	"Olivera"));
		players.add(new Soccer(18,	"AR",	'A',	"Giovanni",	"Simeone"));
		players.add(new Soccer(20,	"PL",	'C',	"Piotr",	"Zieliński"));
		players.add(new Soccer(21,	"IT",	'A',	"Matteo",	"Politano"));
		players.add(new Soccer(22,	"IT",	'D',	"Giovanni",	"Di Lorenzo"));
		players.add(new Soccer(23,	"IT",	'A',	"Alessio",	"Zerbin"));
		players.add(new Soccer(24,	"SE",	'C',	"Jens",	"Cajuste"));
		players.add(new Soccer(29,	"DK",	'C',	"Jesper",	"Lindstrøm"));
		players.add(new Soccer(55,	"NO",	'D',	"Leo Skiri",	"Østigård"));
		players.add(new Soccer(59,	"IT",	'D',	"Alessandro",	"Zanoli"));
		players.add(new Soccer(68,	"SK",	'C',	"Stanislav",	"Lobotka"));
		players.add(new Soccer(70,	"IT",	'C',	"Gianluca",	"Gaetano"));
		players.add(new Soccer(77,	"GE",	'A',	"Khvicha",	"Kvaratskhelia"));
		players.add(new Soccer(81,	"IT",	'A',	"Giacomo",	"Raspadori"));
		players.add(new Soccer(95,	"IT",	'P',	"Pierluigi",	"Gollini"));
		players.add(new Soccer(99,	"CM",	'C',	"André Zambo",	"Anguissa"));
	}
	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException {
		res.setContentType("application/json");
		res.setCharacterEncoding("UTF-8");
		res.getWriter().append(new Gson().toJson(players));
	}
}