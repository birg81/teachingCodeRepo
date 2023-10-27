package model;
public class Person {
	private String firstname;
	private String lastname;
	private int age;
	public Person(String firstname, String lastname, int age) {
		this.firstname = firstname != null && !firstname.isBlank() ? firstname.strip() : "(firstname)";
		this.lastname = lastname != null && !lastname.isBlank() ? lastname.strip() : "(lastname)";
		this.age = age > 0 ? age : 0;
	}
	//waterfall constructor
	public Person() {
		this(null, null, -1);
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
		if(age > 0)
			this.age = age;
	}
	@Override
	public String toString() {
		return "Hi! I'm %s %s. I'm %d..".formatted(firstname, lastname, age);
	}
}