package controller;
import model.*;
import java.util.List;
import java.util.Scanner;
import java.util.ArrayList;
public class Main {
	public static void print(List<Person> plist) {
		if(plist.size() == 0) {
			System.out.println("(empty list)");
			return;
		}
		int i = 0;
		for(Person p : plist)
			System.out.println("%02d >>\t%s".formatted(i++, p));
	}
	public static void main(String[] args) {
		List<Person> people = new ArrayList<>();
		people.add(new Teacher("Biagio Rosario", "Greco", 43, "Informatica"));
		int choice;
		Scanner input = new Scanner(System.in);
		do {
			System.out.print("""
				1. view people list
				2. find people
				3. add new person
				4. remove person

				0. exit

				(choice) >_:
				""".strip()
			);
			choice = input.nextInt();
			switch(choice) {
				case 1-> {
					System.out.println("*** View People List ***");
					print(people);
				}
				case 3 -> {
					System.out.println("*** Add People ***");
					System.out.print("\nInsert firstname: ");
					String firstname = input.next();
					System.out.print("\nInsert lastname: ");
					String lastname = input.next();
					System.out.println("\nInsert age: ");
					int age = input.nextInt();
					System.out.println("\nInsert role [p]erson, [s]tudent, [t]eacher: ");
					String kind = input.next().toLowerCase().substring(0, 1);
					switch(kind) {
						case "p" -> {
							people.add(new Person(firstname, lastname, age));
						}
						case "s" -> {
							System.out.println("\nInsert classroom: ");
							String classroom = input.next();
							people.add(new Student(firstname, lastname, age, classroom));
						}
						case "t" -> {
							System.out.println("\nInsert subject: ");
							String subject = input.next();
							people.add(new Teacher(firstname, lastname, age, subject));
						}
						default -> {
							System.err.println("*** Errore: SCELTA NON VALIDA ***");
						}
					}
				}
				case 4 -> {
					System.out.println("*** REMOVE ***");
					System.out.println("\nInsert id: ");
					int id = input.nextInt();
					people.remove(id);
				}
				case 0 -> {
					System.out.println("*** EXIT***");
				}
				default -> {
					System.out.println("*** SCELTA NON VALIDA ***");
				}
			}
		} while (choice != 0);
		input.close();
		System.out.println("\nThanks for using our management software...");
	}
}