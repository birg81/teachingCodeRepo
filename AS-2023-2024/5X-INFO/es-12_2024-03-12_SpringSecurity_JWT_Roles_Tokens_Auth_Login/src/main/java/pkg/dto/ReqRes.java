package pkg.dto;
import lombok.Data;
import java.util.List;
import pkg.entity.Product;
import pkg.entity.OurUsers;
// import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
@Data
@JsonIgnoreProperties(ignoreUnknown = true)
@JsonInclude(JsonInclude.Include.NON_NULL)
public class ReqRes {
	private int statusCode;
	private String error;
	private String message;
	private String token;
	private String refreshToken;
	private String expirationTime;
	private String name;
	private String email;
	private String role;
	private String password;
	private List<Product> products;
	private OurUsers ourUsers;
}