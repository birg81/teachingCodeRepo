/*
Guess the Number
*/

import java.util.Random;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		// Initialize Scanner for user input and Random for number generation
		Scanner scan = new Scanner(System.in);
		Random random = new Random();

		// Generate a random target number between 0 and 9 (inclusive)
		int targetNumber = random.nextInt(10);

		// Define maximum allowed attempts
		int maxAttempts = 3;
		boolean hasGuessedCorrectly = false;

		// multiline-string
		System.out.println(
			"""
			Welcome to the Number Guessing Game!
			I have chosen a number between 0 and 9.
			You have 3 attempts to guess it!
			"""
		);

		// Game loop for a maximum of 3 attempts
		for (int attempt = 1; attempt <= maxAttempts && !hasGuessedCorrectly; attempt++) {
			System.out.printf("Attempt %d - Enter your guess: ", attempt);
			int userGuess = scan.nextInt();

			// Check if the guess is correct
			if (userGuess == targetNumber) {
				System.out.printf("Congratulations! You guessed the correct number! [%d]\n", userGuess);
				hasGuessedCorrectly = true;		// Exit the loop early if the user wins
			} else if (attempt < maxAttempts) {
				// Provide hints only if attempts remain
				System.out.println(
					userGuess > targetNumber
						? "Your guess is too high. Try a lower number."
						: "Your guess is too low. Try a higher number."
				);
			}
		}

		// Output message if the user fails after all attempts
		if (!hasGuessedCorrectly)
			System.out.printf("Sorry, you did not guess the number. The number I was thinking of was %d.\n", targetNumber);

		// Close scanner resource
		scan.close();
	}
}