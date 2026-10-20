package test;
import model.*;
public class Main {
	public static void main(String[] args) {
		Person[] people = {
			new Person(),
			new Student("Antonio", "Alfano", true, 17, "4X"),
			new Teacher("Barbara", "Barretta", false, 29, "Computer Science")
		};
		for(Person p: people)
			System.out.println(p);
	}
}
