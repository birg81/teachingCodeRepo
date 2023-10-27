package model;
public class Student extends Person {
	private String classroom;
	public Student(String firstname, String lastname, int age, String classroom) {
		super(firstname, lastname, age);
		this.classroom = classroom != null && classroom.strip().length() == 2 ? classroom.strip() : "6Z";
	}
	public String getClassroom() {
		return classroom;
	}
	public void setClassroom(String classroom) {
		if(!classroom.isBlank() && classroom.strip().length() == 2)
			this.classroom = classroom.strip();
	}
	@Override
	public String toString() {
		return "%s\nI'm in the %s class!"
			.formatted(
				super.toString(), classroom
			);
	}
}