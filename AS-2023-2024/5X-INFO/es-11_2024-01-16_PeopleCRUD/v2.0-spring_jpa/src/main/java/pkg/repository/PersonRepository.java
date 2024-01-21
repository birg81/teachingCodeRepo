package pkg.repository;
import pkg.entity.Person;
import org.springframework.data.jpa.repository.JpaRepository;
public interface PersonRepository extends JpaRepository<Person, Integer> { }