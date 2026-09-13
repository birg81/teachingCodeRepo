package pkg.repository;
import org.springframework.data.jpa.repository.JpaRepository;
import pkg.entity.Person;
public interface PersonRepository extends JpaRepository<Person, Integer> {
}