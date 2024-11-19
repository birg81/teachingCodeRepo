package model;
public class Teacher extends Person {
	private String subject;
	public Teacher(String firstname, String lastname, int age, String subject) {
		super(firstname, lastname, age);
		this.subject = !subject.isBlank() ? subject.strip(): "(subject)";
	}
	public String getSubject() {
		return subject;
	}
	public void setSubject(String subject) {
		if(!subject.isBlank())
			this.subject = subject.strip();
	}
	@Override
	public String toString() {
		return "I'm mr. %s %s (%d). I teach %s".formatted(
			lastname, firstname, age,
			subject
		);
	}
}