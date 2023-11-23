package model;

public class WaterPet extends Animal{
	private boolean isSeaWater;
	public WaterPet(String name, int dimension, boolean isSeaWater) {
		super(name, dimension);
		this.isSeaWater = isSeaWater;
	}
	public boolean isSeaWater() {
		return isSeaWater;
	}
	public void setSeaWater(boolean isSeaWater) {
		this.isSeaWater = isSeaWater;
	}
	@Override
	public String toString() {
		return "I'm %s, I love swim in %s water and I'm %d cm."
			.formatted(name, isSeaWater ? "sea": "fresh", dimension);
	}
	// custom method for saving on text file
	@Override
	public String toCSVfile() {
		return "W,%s,%d,%c".formatted(name, dimension, isSeaWater ? 'S': 'F');
	}
}