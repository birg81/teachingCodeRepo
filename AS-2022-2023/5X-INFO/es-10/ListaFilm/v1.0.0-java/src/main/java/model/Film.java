package model;
public class Film {
	private int film_id;
	private String title, description;
	private int length;
	public Film(int film_id, String title, String description, int length) {
		this.film_id = film_id;
		this.title = title;
		this.description = description;
		this.length = length;
	}
	public int getFilm_id() {
		return film_id;
	}
	public String getTitle() {
		return title;
	}
	public String getDescription() {
		return description;
	}
	public int getLength() {
		return length;
	}
	public void setTitle(String title) {
		if (title != null && !title.isBlank())
			this.title = title.strip();
	}
	public void setDescription(String description) {
		if (description != null && !description.isBlank())
			this.description = description.strip();
	}
	public void setLength(int length) {
		if (length > 0)
			this.length = length;
	}
}