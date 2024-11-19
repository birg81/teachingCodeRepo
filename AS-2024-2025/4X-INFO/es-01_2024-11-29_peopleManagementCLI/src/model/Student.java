package model;
public class Student extends Person {
	private String classroom;
	public Student(String firstname, String lastname, int age, String classroom) {
		super(firstname, lastname, age);
		this.classroom = !classroom.isBlank() ? classroom.strip() : "(classroom)";
	}
	public String getClassroom() {
		return classroom;
	}
	public void setClassroom(String classroom) {
		if(!classroom.isBlank())
			this.classroom = classroom.strip();
	}
	@Override
	public String toString() {
		return "Hi! I'm %s %s (%d). I’m in the %s grade".formatted(
			lastname, firstname, age,
			classroom
		);
	}
}