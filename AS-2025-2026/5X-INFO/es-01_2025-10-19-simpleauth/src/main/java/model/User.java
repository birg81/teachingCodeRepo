package model;

public class User {
	private int id;
	private String firstname, lastname, email, password;

	public User(int id, String firstname, String lastname, String email, String password) {
		this.id = id > 0 ? id : 0;
		this.firstname = firstname != null && !firstname.isBlank() ? firstname.strip() : "(firstname)";
		this.lastname = lastname != null && !lastname.isBlank() ? lastname.strip() : "(lastname)";
		this.email = email != null && !email.isBlank() ? email.strip() : "(email)";
		this.password = password != null && !password.isBlank() ? password.strip() : "(password)";
	}

	// Getters
	public int getId() {
		return id;
	}
	public String getFirstname() {
		return firstname;
	}
	public String getLastname() {
		return lastname;
	}
	public String getEmail() {
		return email;
	}
	public String getPassword() {
		return password;
	}

	// Setters (con controllo: non modificano se input non valido)
	public void setFirstname(String firstname) {
		if (firstname != null && !firstname.isBlank())
			this.firstname = firstname.strip();
	}
	public void setLastname(String lastname) {
		if (lastname != null && !lastname.isBlank())
			this.lastname = lastname.strip();
	}
	public void setEmail(String email) {
		if (email != null && !email.isBlank())
			this.email = email.strip();
	}
	public void setPassword(String password) {
		if (password != null && !password.isBlank())
			this.password = password.strip();
	}
	public String toString() {
		return "%s %s (<em>%s</em>)".formatted(firstname, lastname, email);
	}
}