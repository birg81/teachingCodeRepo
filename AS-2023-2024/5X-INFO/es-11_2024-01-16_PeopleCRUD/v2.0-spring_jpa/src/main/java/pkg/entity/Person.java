package pkg.entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import org.hibernate.annotations.Check;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
@Entity
@Table(name = "People")
@Check(constraints = "age > 0")
public class Person {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Integer id;
	@Column(length = 48, nullable = false)
	private String firstname;
	@Column(length = 48, nullable = false)
	private String lastname;
	@Column(nullable = false)
	private int age;
	public Person(int id, String firstname, String lastname, int age) {
		this.id = id > 0 ? id : 0;
		this.firstname = firstname != null && !firstname.isBlank() ? firstname.strip() : "(firstname)";
		this.lastname = lastname != null && !lastname.isBlank() ? lastname.strip() : "(lastname)";
		this.age = age > 0 ? age : 0;
	}
	public Person() {
		this(-1, null, null, 0);
	}
	public int getId() {
		return id;
	}
	public String getFirstname() {
		return firstname;
	}
	public String getLastname() {
		return lastname;
	}
	public int getAge() {
		return age;
	}
	public void setId(int id) {
		if(id > 0)
			this.id = id;
	}
	public void setFirstname(String firstname) {
		if(firstname != null && !firstname.isBlank())
			this.firstname = firstname.strip();
	}
	public void setLastname(String lastname) {
		if(lastname != null && !lastname.isBlank())
			this.lastname = lastname.strip();
	}
	public void setAge(int age) {
		if(age > 0)
			this.age = age;
	}
	@Override
	public String toString() {
		return "(%d) %s %s, %d years old".formatted(id, firstname, lastname, age);
	}
}