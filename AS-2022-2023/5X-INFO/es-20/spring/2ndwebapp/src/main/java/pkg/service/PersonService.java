package pkg.service;
import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import pkg.entity.Person;
import pkg.repository.PersonRepository;
@Service
public class PersonService {
	@Autowired
	private PersonRepository people;
	public Person savePerson(Person p) {
		return people.save(p);
	}
	public List<Person> savePeople(List<Person> plist) {
		return people.saveAll(plist);
	}
	public List<Person> getPeople() {
		return people.findAll();
	}
	public Person getPersonById(int id) {
		return people.findById(id).orElse(null);
	}
	public Person updatePerson(int id, Person someone) {
		Person p = getPersonById(id);
		if (p == null)
			return null;
		p.setPerson(someone);
		return people.save(p);
	}
	public Person removePerson(int id) {
		Person p = getPersonById(id);
		if (p == null)
			return null;
		people.delete(p);
		return p;
	}
}