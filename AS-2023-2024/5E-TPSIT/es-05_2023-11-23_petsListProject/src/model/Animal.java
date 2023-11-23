package model;

public class Animal {
	protected String name;
	protected int dimension;
	public Animal(String name, int dimension) {
		this.name = name!=null && !name.isBlank() ? name.strip() : "(animal)";
		this.dimension = dimension > 0 ? dimension : 0;
	}
	public String getName() {
		return name;
	}
	public int getDimension() {
		return dimension;
	}
	public void setName(String name) {
		if(name != null && !name.isBlank())
			this.name = name.strip();
	}
	public void setDimension(int dimension) {
		if(dimension > 0)
			this.dimension = dimension;
	}
	@Override
	public String toString() {
		return "Hi! I'm %s and I'm %d kg.".formatted(name, dimension);
	}
	// custom method for saving on text file
	public String toCSVfile() {
		return "A,%s,%d,*".formatted(name, dimension);
	}
}