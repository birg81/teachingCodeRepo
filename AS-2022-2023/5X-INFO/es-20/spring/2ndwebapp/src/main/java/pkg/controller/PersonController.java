package pkg.controller;
import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import pkg.entity.Person;
import pkg.service.PersonService;
@RestController
@RequestMapping("/api/people")
public class PersonController {
	@Autowired
	private PersonService people;
	@PostMapping
	public Person addPerson(@RequestBody Person p) {
		return people.savePerson(p);
	}
	@PostMapping("/any/")
	public List<Person> addPeople(@RequestBody List<Person> plist) {
		return people.savePeople(plist);
	}
	@GetMapping
	public List<Person> getPeople() {
		return people.getPeople();
	}
	@GetMapping("/{id}")
	public Person getPerson(@PathVariable int id) {
		return people.getPersonById(id);
	}
	@GetMapping("/") // GET: /?id=12
	public Person getPersonFromURL(@RequestParam int id) {
		return getPerson(id);
	}
	@PutMapping("/{id}")
	public Person updatePerson(@PathVariable int id, @RequestBody Person p) {
		return people.updatePerson(id, p);
	}
	@DeleteMapping("/{id}")
	public Person removePerson(@PathVariable int id) {
		return people.removePerson(id);
	}
}