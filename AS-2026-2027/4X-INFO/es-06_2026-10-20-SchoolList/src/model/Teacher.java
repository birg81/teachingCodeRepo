package model;
public class Teacher extends Person {
	private String subject;
	public Teacher(String firstname, String lastname, boolean isMale, int age, String subject) {
		super(firstname, lastname, isMale, age);
		this.subject = subject != null && !subject.isBlank() ? subject.strip() : "astro medicina";
	}
	public void setSubject(String subject) {
		if(subject != null && !subject.isBlank())
			this.subject = subject.strip();
	}
	public String getSubject() {
		return subject;
	}
	@Override
	public String toString() {
		String prename = switch((isMale ? 2 : 0) | (isAdult() ? 1 : 0)) {
			case 0 -> "la tirocinante";
			case 1 -> "la prof.ssa";
			case 2 -> "il tirocinante";
			case 3 -> "il prof.";
			default -> "";
		};
		return "Sono %s %s %s (%d anni), docente di %s".formatted(
			prename, lastname, firstname, age, subject
		);
	}
}
