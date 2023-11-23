package model;

public class LandPet extends Animal {
	private String animalSound;
	public LandPet(String name, int dimension, String animalSound) {
		super(name, dimension);
		this.animalSound = animalSound != null && !animalSound.isBlank() ? animalSound.strip() : "(mute)";
	}
	public String getAnimalSound() {
		return animalSound;
	}
	public void setAnimalSound(String animalSound) {
		if(!animalSound.isBlank())
			this.animalSound = animalSound.strip();
	}
	@Override
	public String toString() {
		return "I'm %s and I say %s. I'm %d kg.".formatted(name, animalSound, dimension);
	}
	// custom method for saving on text file
	@Override
	public String toCSVfile() {
		return "L,%s,%d,%s".formatted(name, dimension, animalSound);
	}
}