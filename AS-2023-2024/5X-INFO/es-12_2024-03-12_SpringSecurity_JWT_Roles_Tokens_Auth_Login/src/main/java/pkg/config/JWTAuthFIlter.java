package pkg.config;
import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import pkg.service.JWTUtils;
import pkg.service.OurUserDetailsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.context.SecurityContext;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.web.authentication.WebAuthenticationDetailsSource;
import org.springframework.stereotype.Component;
import org.springframework.web.filter.OncePerRequestFilter;
import java.io.IOException;
@Component
public class JWTAuthFIlter extends OncePerRequestFilter {
	@Autowired
	private JWTUtils jwtUtils;
	@Autowired
	private OurUserDetailsService ourUserDetailsService;
	@Override
	protected void doFilterInternal(HttpServletRequest req, HttpServletResponse res, FilterChain filterChain) throws ServletException, IOException {
		final String authHeader = req.getHeader("Authorization");
		if (authHeader == null || authHeader.isBlank()) {
			filterChain.doFilter(req, res);
			return;
		}
		final String jwtToken = authHeader.substring(7);
		final String userEmail = jwtUtils.extractUsername(jwtToken);
		if (userEmail != null && SecurityContextHolder.getContext().getAuthentication() == null) {
			UserDetails userDetails = ourUserDetailsService.loadUserByUsername(userEmail);
			if (jwtUtils.isTokenValid(jwtToken, userDetails)) {
				SecurityContext securityContext = SecurityContextHolder.createEmptyContext();
				UsernamePasswordAuthenticationToken token = new UsernamePasswordAuthenticationToken(
					userDetails, null, userDetails.getAuthorities()
				);
				token.setDetails(new WebAuthenticationDetailsSource().buildDetails(req));
				securityContext.setAuthentication(token);
				SecurityContextHolder.setContext(securityContext);
			}
		}
		filterChain.doFilter(req, res);
	}
}