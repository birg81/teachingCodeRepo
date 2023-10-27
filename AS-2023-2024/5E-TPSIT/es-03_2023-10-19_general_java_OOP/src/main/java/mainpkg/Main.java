package mainpkg;
import model.Person;
import model.Student;
import java.util.ArrayList;
public class Main {
	public static void main(String[] args) {
		// Object List
		ArrayList<Object> people = new ArrayList<>();
		// add Person and Student - Polymorphism Approach
		people.add(new Person("Antonio", "Cuomo", 24));
		people.add(new Student("Beatrice", "Di Maio", 17, "5E"));
		// add String, double (Double), int (Integer), boolean (Boolean) and char (Character) for testing
		people.add("Napoli, Campania - Italia");
		people.add(3.1415926);
		people.add(13);
		people.add(true);
		people.add('X');
		// foreach loop for printing test
		for(Object p: people)
			System.out.println(p);
	}
}