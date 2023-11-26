package model;
public class User {
	private int id;
	private String email, passwd, firstname, lastname;
	public User(int id, String email, String passwd, String firstname, String lastname) {
		this.id = id > 0 ? id : 0;
		this.email = email != null && !email.isBlank() ? email.strip() : "(email)";
		this.passwd = !passwd.isBlank() ? passwd.strip() : "(passwd)";
		this.firstname = firstname;
		this.lastname = lastname;
	}
	public int getId() {
		return id;
	}
	public String getEmail() {
		return email;
	}
	public String getPasswd() {
		return passwd;
	}
	public String getFirstname() {
		return firstname;
	}
	public String getLastname() {
		return lastname;
	}
	public void setId(int id) {
		if(id > 0)
			this.id = id;
	}
	public void setEmail(String email) {
		if(email != null && !email.isBlank())
			this.email = email.strip();
	}
	public void setPasswd(String passwd) {
		if(passwd != null && !passwd.isBlank())
			this.passwd = passwd.strip();
	}
	public void setFirstname(String firstname) {
		if(firstname != null && !firstname.isBlank())
			this.firstname = firstname.strip();
	}
	public void setLastname(String lastname) {
		if(lastname != null && !lastname.isBlank())
			this.lastname = lastname.strip();
	}
	@Override
	public String toString() {
		return "Hi! I'm %s %s [%d] (%s) {%s}"
			.formatted(
				firstname, lastname,
				id, email, passwd
			);
	}
}