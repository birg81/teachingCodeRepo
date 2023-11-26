package model;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
public class UserDAO {
	private static final String
		USER = "root", SECRET = "",
		CON_STR = "jdbc:mysql://localhost:3306/restrictedareadb";
	public static User getUserByAuth(String email, String passwd) {
		final String q = "SELECT * FROM UsersList WHERE email=? AND passwd=?;";
		User u = null;
		try {
			Class.forName("com.mysql.cj.jdbc.Driver");
			Connection con = DriverManager.getConnection(CON_STR, USER, SECRET);
			PreparedStatement st = con.prepareStatement(q);
			st.setString(1, email);
			st.setString(2, passwd);
			ResultSet rs = st.executeQuery();
			if(rs.next()) {
				u = new User(
					rs.getInt("id"),
					rs.getString("email"),
					rs.getString("passwd"),
					rs.getString("firstname"),
					rs.getString("lastname")
				);
			}
			st.close();
			rs.close();
			con.close();
			return u;
		} catch (SQLException | ClassNotFoundException e) {
			e.printStackTrace();
		}
		return u;
	}
	public static boolean addUser(User u) {
		int res = 0;
		final String q = "INSERT INTO UsersList(email, passwd, firstname, lastname) VALUE(?,?,?,?);";
		try {
			Class.forName("com.mysql.cj.jdbc.Driver");
			Connection con = DriverManager.getConnection(CON_STR, USER, SECRET);
			PreparedStatement st = con.prepareStatement(q);
			st.setString(1, u.getEmail());
			st.setString(2, u.getPasswd());
			st.setString(3, u.getFirstname());
			st.setString(4, u.getLastname());
			res = st.executeUpdate();
			st.close();
			con.close();
			return res > 0;
		} catch (SQLException | ClassNotFoundException e) {
			e.printStackTrace();
		}
		return res > 0;
	}
}
