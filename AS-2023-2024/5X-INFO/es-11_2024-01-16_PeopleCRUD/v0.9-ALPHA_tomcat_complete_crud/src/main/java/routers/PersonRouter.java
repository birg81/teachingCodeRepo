package routers;
import entity.Person;
import java.io.IOException;
import java.util.ArrayList;
import com.google.gson.Gson;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
@WebServlet(urlPatterns = {"/api/person/*"})
public class PersonRouter extends HttpServlet {
	private ArrayList<Person> people = new ArrayList<>();
	public PersonRouter() {
		people.add(new Person(1, "Gennaro", "Esposito", 30));
		people.add(new Person(2, "Antonio", "Russo", 25));
		people.add(new Person(3, "Maria", "Ferraro", 28));
		people.add(new Person(4, "Carmela", "De Luca", 35));
		people.add(new Person(5, "Pasquale", "Coppola", 40));
		people.add(new Person(6, "Rosa", "Romano", 22));
		people.add(new Person(7, "Salvatore", "Di Martino", 32));
	}
	private int getId(HttpServletRequest req) {
		return req.getPathInfo().split("/").length > 0
			? Integer.parseInt(req.getPathInfo().split("/")[1])
			: -1;
	}
	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException {
		res.setCharacterEncoding("UTF-8");
		res.setContentType("text/plain");
		final Person person = new Gson().fromJson(req.getReader(), Person.class);
		if(person.getId() > 0 && !people.stream().anyMatch(p -> p.getId() == person.getId())) {
			people.add(person);
			res.setStatus(HttpServletResponse.SC_OK);
			res.getWriter().printf("Success! Person '%s' has been added to the list!", person.toString());
		} else {
			res.setStatus(HttpServletResponse.SC_BAD_REQUEST);
			res.getWriter().printf("Unable to add Person '%s'! Same ID already exists!", person.toString());
		}
	}
	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException {
		res.setCharacterEncoding("UTF-8");
		res.setContentType("application/json");
		final int id = getId(req);
		final Person person = people.stream().filter(p -> p.getId() == id).findFirst().orElse(null);
		res.getWriter().print(new Gson().toJson(id == -1 ? people : id > 0 && person != null ? person : new ArrayList<>()));
	}
	@Override
	protected void doPut(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException {
		res.setCharacterEncoding("UTF-8");
		res.setContentType("text/plain");
		final int id = getId(req);
		final Person person = new Gson().fromJson(req.getReader(), Person.class);
		if(id > 0 && person != null && person.getId() == id && people.removeIf(p -> p.getId() == id)) {
			people.add(person);
			res.setStatus(HttpServletResponse.SC_OK);
			res.getWriter().printf("Person with ID %d updated successfully", id);
		} else {
			res.setStatus(HttpServletResponse.SC_BAD_REQUEST);
			res.getWriter().printf("Unable to update Person with ID %d. Person not found.", id);
		}
	}
	@Override
	protected void doDelete(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException {
		res.setCharacterEncoding("UTF-8");
		res.setContentType("text/plain");
		final int id = getId(req);
		if(people.removeIf(p -> p.getId() == id)) {
			res.setStatus(HttpServletResponse.SC_OK);
			res.getWriter().printf("Success! Correct remove Person ID %d!", id);
		} else {
			res.setStatus(HttpServletResponse.SC_BAD_REQUEST);
			res.getWriter().printf("Error! Unable remove Person id %d", id);
		}
	}
}