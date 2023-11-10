package model;
import java.sql.ResultSet;
import java.sql.Connection;
import java.util.ArrayList;
import java.sql.DriverManager;
public class PersonDAO {
	private static Connection con;
	private static ResultSet rs;
	private static final String JDBC_DRIVER =
		"com.mysql.cj.jdbc.Driver";		// MySQL DBMS
		// "org.sqlite.JDBC";			// SQLite DBMS
		// "org.h2.Driver";				// H2 DBMS
	private static final String CONNECTION_STR =
		"jdbc:mysql://localhost:3306/theSimpsonsDB?user=root&password=";	// MySQL DBMS
		// "jdbc:sqlite:./theSimpsonsDB.db";								// SQLite DBMS
		// "jdbc:h2:./theSimpsonsDB?user=sa&password=sa"					// H2 DBMS
	private static final String q = "SELECT * FROM CharactersList;";
	public static ArrayList<Person> getAllCharacters() {
		ArrayList<Person> characters = new ArrayList<>();
		try {
			Class.forName(JDBC_DRIVER);
			con = DriverManager.getConnection(CONNECTION_STR);
			rs = con.createStatement().executeQuery(q);
			while(rs.next())
				characters.add(new Person(
					rs.getInt("id"),
					rs.getString("firstname"),
					rs.getString("lastname"),
					rs.getString("gender")
				));
			rs.close();
			con.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
		return characters;
	}
}