package model;
public class Student extends Person {
	private String classroom;
	public Student(String firstname, String lastname, boolean isMale, int age, String classroom) {
		super(firstname, lastname, isMale, age);
		this.classroom = classroom != null && !classroom.isBlank() ? classroom.strip() : "6Z";
	}
	public String getClassroom() {
		return classroom;
	}
	public void setClassroom(String classroom) {
		if(classroom != null && !classroom.isBlank())
			this.classroom = classroom.strip();
	}
	@Override
	public String toString() {
		String studGender = !isMale ? "ssa" : "";
		String studKind = isAdult() ? " del corso universitario" : "";
		return "Ciao, sono %s %s, ho %d anni; sono studente%s%s di %s".formatted(
			lastname, firstname, age, studGender, studKind, classroom
		);
	}
}
