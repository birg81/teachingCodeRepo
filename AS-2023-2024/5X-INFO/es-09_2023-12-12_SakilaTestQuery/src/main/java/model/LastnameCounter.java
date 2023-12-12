package model;
public class LastnameCounter {
	private String lastname;
	private int n;
	public LastnameCounter(String lastname, int n) {
		this.lastname = lastname;
		this.n = n;
	}
	public String getLastname() {
		return lastname;
	}
	public int getN() {
		return n;
	}
	public void setLastname(String lastname) {
		this.lastname = lastname;
	}
	public void setN(int n) {
		this.n = n;
	}
}