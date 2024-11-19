package model;
public class Person {
	protected String firstname;
	protected String lastname;
	protected int age;
	public Person(String firstname, String lastname, int age) {
		this.firstname = !firstname.isBlank() ? firstname.strip() : "(firstname)";
		this.lastname = !lastname.isBlank() ? lastname.strip() : "(lastname)";
		this.age = age > 13 && age < 120 ? age : 18;
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
		if(!firstname.isBlank())
			this.firstname = firstname.strip();
	}
	public void setLastname(String lastname) {
		if(!lastname.isBlank())
			this.lastname = lastname.strip();
	}
	public void setAge(int age) {
		if(age > 13 && age < 120)
			this.age = age;
	}
	@Override
	public String toString() {
		return "Hi! I'm %s %s. I'm %d!".formatted(firstname, lastname, age);
	}
}