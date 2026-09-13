package model;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
public class FilmDAO {
	private static Connection con;
	private static ResultSet rs;
	private static final String qGeneral = "SELECT * FROM Film";
	public static ArrayList<Film> getFilmByTitle(String title) {
		ArrayList<Film> movies = new ArrayList<>();
		String q = qGeneral;
		if (title != null && !title.isBlank())
			q += " WHERE title LIKE '%" + title.strip().toLowerCase() + "%'";
		q += " ORDER BY title ASC;";
		try {
			con = DriverManager.getConnection("jdbc:mysql://localhost:3306/sakila", "root", "");
			rs = con.createStatement().executeQuery(q);
			while (rs.next())
				movies.add(
					new Film(
						rs.getInt("film_id"),
						rs.getString("title").toLowerCase(),
						rs.getString("description").toLowerCase(),
						rs.getInt("length")
					)
				);
			rs.close();
			con.close();
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return movies;
	}
}