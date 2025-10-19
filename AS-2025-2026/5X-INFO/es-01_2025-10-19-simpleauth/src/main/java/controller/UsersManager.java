package controller;

import model.User;
import java.util.List;
import java.util.ArrayList;

public class UsersManager {
	private static List<User> users = new ArrayList<>(List.of(
		new User(0, "Admin", "User", "admin@email.com", "admin"),
		new User(1, "Gennaro", "Esposito", "gennaro.esposito@email.it", "genn@123"),
		new User(2, "Ciro", "Di Maio", "ciro.dimaio@email.it", "ciro456"),
		new User(3, "Concetta", "Russo", "concetta.russo@email.it", "concetta789"),
		new User(4, "Pasquale", "Palmieri", "pasquale.palmieri@email.it", "pass123"),
		new User(5, "Assunta", "De Luca", "assunta.deluca@email.it", "assu2021"),
		new User(6, "Salvatore", "Fiore", "salvatore.fiore@email.it", "salva321"),
		new User(7, "Carmela", "Monti", "carmela.monti@email.it", "monti2022"),
		new User(8, "Antonio", "Vitale", "antonio.vitale@email.it", "tony456"),
		new User(9, "Rosaria", "Bianchi", "rosaria.bianchi@email.it", "rosy789"),
		new User(10, "Luigi", "Cuomo", "luigi.cuomo@email.it", "cuomo2023")
	));
	public static List<User> getAllUsers() {
		return users;
	}
	public static User getUser(int id) {
		return id >= 0 && id < users.size() ? users.get(id) : null;
	}
	public static User checkUser(String email, String password) {
		for(User u : users)
			if(email.equals(u.getEmail()))
				return password.equals(u.getPassword()) ? u : null;
		return null;
	}
}