package test;
import model.Creature;
public class Main {
	public static void main(String[] args) {
		Creature
			warewolf = new Creature("Warewolf"),
			vampire = new Creature("Vampire");
		int i = 0;
		while(warewolf.isAlive() && vampire.isAlive()) {
			System.out.printf(
				"""
				%d. FIGHT
				%s	🆚	%s
				""",
				i + 1,
				warewolf, vampire
			);
			System.out.printf(
				"""
				%s
				%s	-	%s
				""",
				warewolf.clash(vampire) ? "💥" : "❤️‍🩹",
				warewolf, vampire
			);
			i++;
		}
	}
}
