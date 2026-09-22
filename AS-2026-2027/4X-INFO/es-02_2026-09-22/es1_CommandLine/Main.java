package es1CommandLine;
public class Main {
	public static void main(String[] args) {
		if(args.length < 2 || !args[1].matches("\\d+")) {
			System.err.println("Numero di argomenti inadeguato!");
			return;
		}
		final String toPrint = args[0];
		final int n = Integer.parseInt(args[1]);
		for (int i = 0; i < n; i++)
			System.out.printf("%d) %s\n", i + 1, toPrint);
	}
}
