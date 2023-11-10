package test;
public class Test {
	public static void main(String[] args) {
		model.PersonDAO.getAllCharacters().forEach(System.out::println);
	}
}