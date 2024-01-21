package pkg.router;
import java.util.List;
import pkg.entity.Person;
import pkg.repository.PersonRepository;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/api/person")
public class PersonRouter {
	@Autowired
	private PersonRepository people;
	@PostMapping			// ./ JSON Person in the body
	public ResponseEntity<String> createPerson(@RequestBody Person person) {
		if (!people.existsById(person.getId())) {
			people.save(person);
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
	public List<Person> getPeople() {
		return people.findAll();
	}
	@GetMapping("/{id}")	// ./5
	public ResponseEntity<Person> getPerson(@PathVariable int id) {
		return people.findById(id)
			.map(p -> new ResponseEntity<>(p, HttpStatus.OK))
			.orElse(new ResponseEntity<>(HttpStatus.NOT_FOUND));
	}
	@GetMapping("/")		// ./?id=7
	public ResponseEntity<Person> getPersonByQueryURL(@RequestParam int id) {
		return getPerson(id);
	}
	@PutMapping("/{id}")	// ./11
	public ResponseEntity<String> modifyPerson(@PathVariable int id, @RequestBody Person person) {
		if (people.existsById(id)) {
			person.setId(id);
			people.save(person);
			return new ResponseEntity<>(
				"Person with ID %d updated successfully".formatted(id),
				HttpStatus.OK
			);
		}
		return new ResponseEntity<>(
			"Unable to update Person with ID %d. Person not found.".formatted(id),
			HttpStatus.NOT_FOUND
		);
	}
	@DeleteMapping("/{id}")	// ./3
	public ResponseEntity<String> removePerson(@PathVariable int id) {
		if (people.existsById(id)) {
			people.deleteById(id);
			return new ResponseEntity<>("Success! Correct remove Person ID %d!".formatted(id), HttpStatus.OK);
		}
		return new ResponseEntity<>("Error! Unable remove Person ID %d".formatted(id), HttpStatus.NOT_FOUND);
	}
}