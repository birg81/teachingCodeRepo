package model;
public class User {
	private String username, password;
	public User(String username, String password) {
		this.username = username != null && !username.isBlank() ? username.trim() : "(username)";
		this.password = password != null && !password.isBlank() ? password.trim() : "(password)";
	}
	public void setUsername(String username) {
		if(username != null && !username.isBlank())
			this.username = username.trim();
	}
	public void setPassword(String password) {
		if(password != null && !password.isBlank())
			this.password = password.trim();
	}
	public String getUsername() {
		return username;
	}
	public boolean checkUser(String username, String password) {
		return
			username != null &&
			password != null &&
			!username.isBlank() &&
			!password.isBlank() &&
			this.username.equals(username.trim()) &&
			this.password.equals(password.trim());
	}
}