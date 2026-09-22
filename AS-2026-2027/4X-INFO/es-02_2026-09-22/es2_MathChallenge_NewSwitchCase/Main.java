package es2MathchallengeNewSwitchCase;
import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String[] operations = { "ADD", "SUB", "MUL", "DIV" };
		int op1 = (int) (Math.random() * 100);
		int op2 = (int) (Math.random() * 100);
		String op = operations[(int) (Math.random() * operations.length)];
		int ris;
		int ans = switch (op) {
			case "ADD" -> {
				System.out.printf("%d + %d ? ", op1, op2);
				yield op1 + op2;
			}
			case "SUB" -> {
				System.out.printf("%d - %d ? ", op1, op2);
				yield op1 - op2;
			}
			case "MUL" -> {
				System.out.printf("%d x %d ? ", op1, op2);
				yield op1 * op2;
			}
			case "DIV" -> {
				System.out.printf("%d : %d ? ", op1, op2);
				yield op1 / op2;
			}
			default -> {
				yield 0;
			}
		};
		ris = scan.nextInt();
		scan.close();
		System.out.println(ris == ans ? "Complimenti!" : "Risposta Errata!");
	}
}
