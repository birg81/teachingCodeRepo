package model;
public class Creature {
	private String name;
	private int healthPoints;
	private int attackPower;
	public Creature(String name) {
		this.name = name != null && !name.isBlank() ? name.strip() : "(creature)";
		this.healthPoints = 100;
		this.attackPower = 10;
	}
	public Creature(Creature o) {
		this(o.name);
		healthPoints = o.healthPoints;
		attackPower = o.attackPower;
	}
	public Creature() {
		this("");
	}
	public String getName() {
		return name;
	}
	public int getHealthPoints() {
		return healthPoints;
	}
	public int getAttackPower() {
		return attackPower;
	}
	public void setName(String name) {
		if(name != null && !name.isBlank())
			this.name = name.strip();
	}
	public boolean isAlive() {
		return this.healthPoints > 0;
	}
	public void healToFull() {
		healthPoints = 100;
	}
	@Override
	public String toString() {
		return "🧌['%s' >> %s %3d٪ | ⚔️ %d]".formatted(
			name, isAlive() ? "💓" : "☠️", healthPoints, attackPower
		);
	}
	public boolean clash(Creature o) {
		if (o == null || this == o || !isAlive() || !o.isAlive())
			return false;

		int damage = (this.attackPower - o.attackPower) + ((int) (11 * Math.random()) -5);

		if (damage > 0)
			o.healthPoints -= damage;
		else if (damage < 0)
			healthPoints += damage;
		else {
			healthPoints -= 2;
			o.healthPoints -= 2;
		}
		if(!isAlive())
			o.attackPower += 5;
		if(!o.isAlive())
			attackPower += 5;

		return true;
	}
}