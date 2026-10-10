package model;
public class Person {
	private String firstname, lastname;
	private boolean isMale;
	private int age;
	public Person(String firstname, String lastname, boolean isMale, int age) {
		this.firstname = firstname != null && !firstname.isBlank() ? firstname.strip() : "Gennaro";
		this.lastname = lastname != null && !lastname.isBlank() ? lastname.strip() : "Esposito";
		this.isMale = isMale;
		this.age = age >= 0 ? age : 16;
	}
	public Person(Person p) {
		this(
			p != null ? p.firstname : "Gennaro",
			p != null ? p.lastname : "Esposito",
			p != null && p.isMale,
			p != null ? p.age : 16
		);
	}
	public Person() {
		this("Gennaro", "Esposito", true, 16);
	}
	public String getFirstname() {
		return firstname;
	}
	public String getLastname() {
		return lastname;
	}
	public boolean isMale() {
		return isMale;
	}
	public int getAge() {
		return age;
	}
	public void setFirstname(String firstname) {
		if(firstname != null && !firstname.isBlank())
			this.firstname = firstname.strip();
	}
	public void setLastname(String lastname) {
		if(lastname != null && !lastname.isBlank())
			this.lastname = lastname.strip();
	}
	public void setMale(boolean isMale) {
		this.isMale = isMale;
	}
	public void setAge(int age) {
		if(age >= 0)
			this.age = age;
	}
	public String getGender() {
		return isMale ? "m" : "f";
	}
	public boolean isAdult() {
		return age >= 18;
	}
	public String getFullname() {
		return "%s %s".formatted(firstname, lastname);
	}
	public String getHonorific() {
		return switch((isMale ? 2 : 0) | (isAdult() ? 1 : 0)) {
			case 0 -> "la sig.na";
			case 1 -> "la sig.ra";
			case 2 -> "il sig.ino";
			case 3 -> "il sig.";
			default -> "";
		};
	}
	@Override
	public String toString() {
		return "Sono %s %s, ed ho %d anni.".formatted(
			getHonorific(), getFullname(), age
		);
	}
	@Override
	public boolean equals(Object o) {
		return this == o || (
			o != null && (o instanceof Person p)
				? toString().equals(p.toString())
				: false
		);
	}
}
