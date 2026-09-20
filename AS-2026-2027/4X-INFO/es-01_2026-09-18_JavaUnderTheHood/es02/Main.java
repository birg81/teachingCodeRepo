package es02;

public class Main {
	public static void main(String[] args) {
		if(args.length > 0) {
			System.out.printf("Sono stati passati %d argomenti...\n", args.length);
			for(String arg: args) {
				System.out.println(arg);
			}
		} else {
			System.err.print(
				"""
				ERRORE:
				Non sono stati passati parametri dalla linea di comando!!!...
				"""
			);
		}
	}
}
