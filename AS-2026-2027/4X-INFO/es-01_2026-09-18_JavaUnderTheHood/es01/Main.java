package es01;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		System.out.print("Enter your name: ");
		String nome = scan.nextLine().strip();

		System.out.print("How many times do you want to repeat the loop? ");
		int n = scan.nextInt();

		for(int i = 0; i < n; i++) {
			System.out.printf("%02d. %s\n", i + 1, nome);
		}
		System.out.println("Thanks for using our software....");
	}
}
