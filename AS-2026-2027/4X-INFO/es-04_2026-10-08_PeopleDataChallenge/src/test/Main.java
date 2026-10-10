package test;
import model.Person;
public class Main {
	public static void main(String[] args) {
		Person gennaro = new Person();											// Default (Maschio Minorenne)
		Person tony = new Person("Antony Edward", "Stark", true, 53);			// Completo (Maschio Maggiorenne)
		Person jennifer = new Person("Jennifer Susan", "Walters", false, 17);	// Completo (Femmina Minorenne)
		Person wanda = new Person("Wanda", "Maximoff", false, 32);				// Completo (Femmina Maggiorenne)
		Person tonyClone = new Person(tony);									// Copia
		Person anonymous = new Person("   ", null, true, -5);					// Fallback/Edge Case
		System.out.printf(
			"""
			--- 1. Test Titoli e Appellativi (toString) ---
			%s
			%s
			%s
			%s

			--- 2. Test Metodi e Costruttore di Copia ---
			Nome completo clone	:	%s
			Sesso clone			:	%s
			È maggiorenne?		:	%b
			Originale == Clone?	:	%b

			--- 3. Test Inizializzazione con Dati Errati/Null ---
			%s
			""",
			gennaro, tony, jennifer, wanda,
			tonyClone.getFullname(),
			tonyClone.getGender(),
			tonyClone.isAdult(),
			tony.equals(tonyClone),
			anonymous
		);
	}
}