package model;
public class Soccer {
	private int n;
	private String country;
	private char role;
	private String firstname, lastname;
	public Soccer(int n, String country, char role, String firstname, String lastname) {
		this.n = n > 0 ? n : 0;
		this.country = country != null && !country.isBlank() && country.strip().length() == 2 ? country.strip() : "**";
		this.role = switch(role) {
			case 'A', 'C', 'D', 'P' -> role;
			default -> '*';
		};
		this.firstname = firstname != null && !firstname.isBlank() ? firstname.strip() : "(firstname)";
		this.lastname = lastname != null && !lastname.isBlank() ? lastname.strip() : "(lastname)";
	}
	public Soccer() {
		this(-1, "",  ' ', "", "");
	}
	public int getN() {
		return n;
	}
	public String getCountry() {
		return country;
	}
	public char getRole() {
		return role;
	}
	public String getFirstname() {
		return firstname;
	}
	public String getLastname() {
		return lastname;
	}
	public void setN(int n) {
		if(n > 0)
			this.n = n;
	}
	public void setCountry(String country) {
		if(country != null && !country.isBlank() && country.strip().length() == 2)
			this.country = country.strip();
	}
	public void setRole(char role) {
		if(role == 'A' || role == 'C' || role == 'D' || role == 'P')
			this.role = role;
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
		return
			"%-15s %-15s\t#%d\t#%c\t[%s]".formatted(
				firstname,	lastname,
				n,	role,	country
			);
	}
}