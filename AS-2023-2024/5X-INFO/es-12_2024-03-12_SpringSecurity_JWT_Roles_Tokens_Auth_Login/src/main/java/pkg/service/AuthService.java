package pkg.service;
import pkg.dto.ReqRes;
import pkg.entity.OurUsers;
import pkg.repository.OurUserRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import java.util.HashMap;
@Service
public class AuthService {
	@Autowired
	private OurUserRepo ourUserRepo;
	@Autowired
	private JWTUtils jwtUtils;
	@Autowired
	private PasswordEncoder passwordEncoder;
	@Autowired
	private AuthenticationManager authenticationManager;
	public ReqRes signUp(ReqRes registrationRequest) {
		ReqRes resp = new ReqRes();
		try {
			OurUsers ourUsers = new OurUsers();
			ourUsers.setEmail(registrationRequest.getEmail());
			ourUsers.setPassword(passwordEncoder.encode(registrationRequest.getPassword()));
			ourUsers.setRole(registrationRequest.getRole());
			OurUsers ourUserResult = ourUserRepo.save(ourUsers);
			if (ourUserResult != null && ourUserResult.getId() > 0) {
				resp.setOurUsers(ourUserResult);
				resp.setMessage("User Saved Successfully");
				resp.setStatusCode(200);
			}
		} catch (Exception e) {
			resp.setStatusCode(500);
			resp.setError(e.getMessage());
		}
		return resp;
	}
	public ReqRes signIn(ReqRes signinRequest){
		ReqRes res = new ReqRes();
		try {
			authenticationManager.authenticate(new UsernamePasswordAuthenticationToken(signinRequest.getEmail(),signinRequest.getPassword()));
			var user = ourUserRepo.findByEmail(signinRequest.getEmail()).orElseThrow();
			System.out.printf("USER IS: %s\n", user);
			var jwt = jwtUtils.generateToken(user);
			var refreshToken = jwtUtils.generateRefreshToken(new HashMap<>(), user);
			res.setStatusCode(200);
			res.setToken(jwt);
			res.setRefreshToken(refreshToken);
			res.setExpirationTime("24Hr");
			res.setMessage("Successfully Signed In");
		} catch (Exception e) {
			res.setStatusCode(500);
			res.setError(e.getMessage());
		}
		return res;
	}
	public ReqRes refreshToken(ReqRes refreshTokenReqiest){
		ReqRes res = new ReqRes();
		String ourEmail = jwtUtils.extractUsername(refreshTokenReqiest.getToken());
		OurUsers users = ourUserRepo.findByEmail(ourEmail).orElseThrow();
		if (jwtUtils.isTokenValid(refreshTokenReqiest.getToken(), users)) {
			var jwt = jwtUtils.generateToken(users);
			res.setStatusCode(200);
			res.setToken(jwt);
			res.setRefreshToken(refreshTokenReqiest.getToken());
			res.setExpirationTime("24Hr");
			res.setMessage("Successfully Refreshed Token");
		}
		res.setStatusCode(500);
		return res;
	}
}
