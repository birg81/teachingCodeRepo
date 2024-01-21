package pkg.router;
import pkg.entity.Person;
import java.util.ArrayList;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/api/person")
public class PersonRouter {
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
	@PostMapping			// ./ JSON Person in the body
	public ResponseEntity<String> createPerson(@RequestBody Person person) {
		if(person.getId() > 0 && !people.stream().anyMatch(p -> p.getId() == person.getId())) {
			people.add(person);
			return new ResponseEntity<>(
				"Success! Person '%s' has been added to the list!".formatted(person.toString()),
				HttpStatus.OK
			);
		}
		return new ResponseEntity<>(
			"Unable to add Person '%s'! Same ID already exists!".formatted(person.toString()),
			HttpStatus.BAD_REQUEST
		);
	}
	@GetMapping				// ./
	public ArrayList<Person> getPeople() {
		// people.sort((p1, p2) -> Integer.compare(p1.getId(), p2.getId()));
		return people;
	}
	@GetMapping("/{id}")	// ./5
	public Person getPerson(@PathVariable int id) {
		return people.stream().filter(p -> p.getId() == id).findFirst().orElse(null);
	}
	@GetMapping("/")		// ./?id=7
	public Person getPersonByQueryURL(@RequestParam int id) {
		return getPerson(id);
	}
	@PutMapping("/{id}")	// ./11
	public ResponseEntity<String> modifyPerson(@PathVariable int id, @RequestBody Person person) {
		return
			people.stream().anyMatch(p -> p.getId() == id) &&
			person.getId() == id &&
			people.removeIf(p -> p.getId() == id) &&
			people.add(person)
				? new ResponseEntity<>(
					"Person with ID %d updated successfully".formatted(id),
					HttpStatus.OK
				)
				: new ResponseEntity<>(
					"Unable to update Person with ID %d. Person not found.".formatted(id),
					HttpStatus.NOT_FOUND
				);
	}
	@DeleteMapping("/{id}")	// ./3
	public ResponseEntity<String> removePerson(@PathVariable int id) {
		return people.removeIf(p -> p.getId() == id)
			? new ResponseEntity<>("Success! Correct remove Person ID %d!".formatted(id), HttpStatus.OK)
			: new ResponseEntity<>("Error! Unable remove Person id %d".formatted(id), HttpStatus.NOT_FOUND);
	}
}