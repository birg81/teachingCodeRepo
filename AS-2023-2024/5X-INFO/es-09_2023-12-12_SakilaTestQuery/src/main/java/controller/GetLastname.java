package controller;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.io.IOException;
import java.sql.Connection;
import model.LastnameCounter;
import java.sql.DriverManager;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
@WebServlet(urlPatterns = {"/index.html"})
public class GetLastname extends HttpServlet {
	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException {
		final String
			DBNAME = "sakila",
			USER = "root",
			PASSWORD = "",
			CONNECT_STR = "jdbc:mysql://localhost:3306/%s".formatted(DBNAME),
			q = """
				SELECT
					last_name AS lastname,
					COUNT(*) AS N
				FROM actor
				GROUP BY
					last_name
				HAVING N > 1
				ORDER BY
					N DESC,
					last_name ASC;
				""".strip();
		ArrayList<LastnameCounter> surnamesList = new ArrayList<>();
		try {
			Class.forName("com.mysql.cj.jdbc.Driver");
			Connection con = DriverManager.getConnection(CONNECT_STR, USER, PASSWORD);
			ResultSet rs = con.prepareStatement(q).executeQuery();
			while(rs.next())
				surnamesList.add(
					new LastnameCounter(
						rs.getString("lastname").toLowerCase(),
						rs.getInt("N")
					)
				);
			rs.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
		req.setAttribute("surnamesList", surnamesList);
		req.getRequestDispatcher("surnamesList.jsp")
			.forward(req, res);
	}
}