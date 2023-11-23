package test;

import model.Animal;
import model.LandPet;
import model.WaterPet;
import java.util.Scanner;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.BufferedWriter;

public class Main {
	public static void main(String[] args) {
		final String FILENAME = "petslist.csv";
		// Create pets list
		ArrayList<Animal> pets = new ArrayList<>();

		// read from csv your pets data
		try(BufferedReader inputFile = new BufferedReader(new FileReader(FILENAME))) {
			// pets data file line
			String line;
			// In your file, the first line means fields name. you don't load on pets variabile this data line
			boolean firstLine = true;
			while ((line = inputFile.readLine()) != null) {
				if(!firstLine) {
					// split your fields and use it
					final String[] fields = line.split(",");
					final String animalType = fields[0];
					final String animalName = fields[1];
					final int animalDimension = Integer.parseInt(fields[2]);
					final String other = fields[3].strip();
					// add specific animal kind
					pets.add(
						switch(animalType) {
							case "L" ->	new LandPet(animalName, animalDimension, other);
							case "W" ->	new WaterPet(animalName, animalDimension, "S".equals(other));
							default ->	new Animal(animalName, animalDimension);
						}
					);
				} else
					firstLine = false;
			}
		} catch (IOException e) {
			System.err.println("ATTENTION: The file containing the list of animals was not found!");
		}

		// for input your data
		Scanner input = new Scanner(System.in);

		// Choice if continue or not your animal CLI request
		boolean goAgain = true;

		// insert your Animals' List
		while(goAgain) {
			// request animal name
			System.out.print("\n* Insert animal name: ");
			String name = input.next();

			// request animal dimension
			System.out.print("* Insert animal dimension: ");
			int dimension = input.nextInt();

			// request animal type
			System.out.print("""
				* Insert animal type:
				[L].		LandPet
				[W].		WaterPet
				[(other)].	General Animal type
				>_:
				""".strip());
			switch (input.next().strip().toUpperCase()) {
				case "L" -> {
					// request animal sound
					System.out.print("* Insert Animal Sound: ");
					String sound = input.next();
					// add landpet
					pets.add(new LandPet(name, dimension, sound));
				}
				case "W" -> {
					// request if swim in fresh o sea water
					System.out.print("* Is seawater?: [y/n] ");
					boolean isSeaWater = "Y".equalsIgnoreCase(input.next());
					// ad waterpet
					pets.add(new WaterPet(name, dimension, isSeaWater));
				}
				// add general pet
				default -> pets.add(new Animal(name, dimension));
			}

			System.out.print("(do you want to finish?) [y/N] >_: ");
			goAgain = !"Y".equalsIgnoreCase(input.next());
		}
		// close your input channel
		input.close();

		// write your pets on csv file
		try (BufferedWriter outputFile = new BufferedWriter(new FileWriter( FILENAME))) {
			outputFile.write("type,name,dimension,other\n");
			for(Animal a: pets) {
				outputFile.write(a.toCSVfile());
				outputFile.write("\n");
			}
		} catch (IOException e) {
			e.printStackTrace();
		}

		// print your pets
		System.out.println("\n\n");
		for(Animal a: pets)
			System.out.println(a);
	}
}