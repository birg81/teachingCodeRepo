package pkg.entity;
public class Person {
	private int id;
	private String firstname;
	private String lastname;
	private int age;
	public Person() {
		this(0, null, null, 0);
	}
	public Person(int id, String firstname, String lastname, int age) {
		this.id = id > -1 ? id : 0;
		this.firstname = firstname != null && !firstname.isBlank()
			? firstname.strip()
			: "(no firstname)";
		this.lastname = lastname != null && !lastname.isBlank()
			? lastname.strip()
			: "(no lastname)";
		this.age = age > 0 ? age : 0;
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
	public void setFirstname(String firstname) {
		if (firstname != null && !firstname.isBlank())
			this.firstname = firstname.strip();
	}
	public void setLastname(String lastname) {
		if (lastname != null && !lastname.isBlank())
			this.lastname = lastname.strip();
	}
	public void setAge(int age) {
		if (age > 0)
			this.age = age;
	}
	public Person setPerson(Person p) {
		if (p != null) {
			setFirstname(p.firstname);
			setLastname(p.lastname);
			setAge(p.age);
			return this;
		}
		return null;
	}
	@Override
	public String toString() {
		return "%d. Hi! I'm %s %s. I'm %d".formatted(id, firstname, lastname, age);
	}
}