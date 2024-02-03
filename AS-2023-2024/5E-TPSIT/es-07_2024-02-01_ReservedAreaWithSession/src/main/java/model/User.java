package model;
public class User {
	private String username, secret;
	public User(String username, String secret) {
		this.username = username != null && !username.isBlank() ? username.strip() : "";
		this.secret = secret != null && !secret.isBlank() ? secret.strip() : "";
	}
	public String getUsername() {
		return username;
	}
	public String getSecret() {
		return secret;
	}
	public void setUsername(String username) {
		if(username != null && !username.isBlank())
			this.username = username.strip();
	}
	public void setSecret(String secret) {
		if(secret != null && !secret.isBlank())
			this.secret = secret.strip();
	}
	@Override
	public boolean equals(Object o) {
		// il metodo equals permette di confrontare le variabili di istanza del mio oggetto con un altro oggetto
		User u = (User) o;
		return username.equals(u.username) && secret.equals(u.secret);
	}
	@Override
	public String toString() {
		return "%s [%s]".formatted(username, secret.hashCode());
	}
}