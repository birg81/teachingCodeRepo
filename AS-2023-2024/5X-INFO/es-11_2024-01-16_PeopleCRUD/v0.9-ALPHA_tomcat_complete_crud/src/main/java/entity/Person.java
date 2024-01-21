package entity;
public class Person {
	private int id;
	private String firstname, lastname;
	private int age;
	public Person(int id, String firstname, String lastname, int age) {
		this.id = id > 0 ? id : 0;
		this.firstname = firstname != null && !firstname.isBlank() ? firstname.strip() : "(firstname)";
		this.lastname = lastname != null && !lastname.isBlank() ? lastname.strip() : "(lastname)";
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