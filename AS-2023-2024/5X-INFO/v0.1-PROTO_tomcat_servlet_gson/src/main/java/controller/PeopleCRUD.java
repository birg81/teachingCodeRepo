package controller;
import model.Person;
import java.util.List;
import java.util.Arrays;
import java.io.IOException;
import java.util.ArrayList;
import com.google.gson.Gson;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
@WebServlet(urlPatterns = {"/api/v1.0/people.json"})
public class PeopleCRUD extends HttpServlet {
	private static List<Person> people = new ArrayList<>(Arrays.asList(
		new Person(0, "Ciro", "Raimo", 37),
		new Person(1, "Gennaro", "Esposito", 40),
		new Person(2, "Antonio", "Russo", 23),
		new Person(3, "Carmela", "Ferraiuolo", 41),
		new Person(4, "Salvatore", "De Luca", 37),
		new Person(5, "Lucia", "Cuomo", 19),
		new Person(6, "Raffaele", "Attianese", 32),
		new Person(7, "Maria", "Ricciardi", 24),
		new Person(8, "Pasquale", "De Rosa", 17),
		new Person(9, "Anna", "Langella", 21)
	));
	private static ArrayList<Person> find(int id) {
		return new ArrayList<Person>(people.stream().filter(p -> p.getId() == id).toList());
	}
	public PeopleCRUD() {
		people.sort((p1, p2) -> p1.getLastname().compareTo(p2.getLastname()));
	}
	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException {
		res.setContentType("application/json");
		res.setCharacterEncoding("UTF-8");
		Person p = new Gson().fromJson(req.getReader(), Person.class);
		if (p != null) {
			people.add(p);
			people.sort((p1, p2) -> p1.getLastname().compareTo(p2.getLastname()));
			res.getWriter().print(new Gson().toJson(p));
		} else {
			res.setStatus(HttpServletResponse.SC_NOT_FOUND);
			res.getWriter().print("Oggetto non inviato o non valido!");
		}
	}
	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException {
		res.setContentType("application/json");
		res.setCharacterEncoding("UTF-8");
		if(req.getParameter("q") != null && !req.getParameter("q").isBlank()) {
			final List<Person> pList = people.stream().filter(
				p ->
					p.toString().toLowerCase().contains(req.getParameter("q").trim().toLowerCase())
			).toList();
			res.getWriter().print(new Gson().toJson(pList));
		} else {
			res.getWriter().print(new Gson().toJson(people));
		}
	}
	@Override
	protected void doPut(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException {
		Person person = null;
		person = new Gson().fromJson(req.getReader(), Person.class);
		if(person != null && req.getParameter("id") != null) {
			int id = Integer.parseInt(req.getParameter("id"));
			for(Person p: people) {
				if(p.getId() == id) {
					p.setFirstname(person.getFirstname());
					p.setLastname(person.getLastname());
					p.setAge(person.getAge());
				}
			}
			res.setContentType("application/json");
			res.setCharacterEncoding("UTF-8");
			person.setId(id);
			res.getWriter().print(new Gson().toJson(person));
		} else {
			res.setStatus(HttpServletResponse.SC_NOT_FOUND);
			res.getWriter().print("Indice non valido o oggetto non inviato!");
		}
	}
	@Override
	protected void doDelete(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException {
		res.setContentType("application/json");
		res.setCharacterEncoding("UTF-8");
		Person p =
			req.getParameter("id") != null &&
			find(Integer.parseInt(req.getParameter("id"))).size() > 0
				? find(Integer.parseInt(req.getParameter("id"))).get(0)
				: null;
		if(p != null){
			people.remove(p);
			res.getWriter().print(new Gson().toJson(p));
		} else {
			res.setStatus(HttpServletResponse.SC_NOT_FOUND);
			res.getWriter().print("Indice non valido!");
		}
	}
}