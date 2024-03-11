package pkg.repository;
import pkg.entity.Product;
import org.springframework.data.jpa.repository.JpaRepository;
public interface ProductRepo extends JpaRepository<Product, Integer> { }