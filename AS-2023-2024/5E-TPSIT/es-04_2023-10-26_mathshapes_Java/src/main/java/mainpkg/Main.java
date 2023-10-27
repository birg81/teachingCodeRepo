package mainpkg;
import model.Shape;
import model.Polygon;
import shapes.Square;
import shapes.Rectangle;
import shapes.RegularShape;
import shapes3D.Prism;
public class Main {
	public static void main(String[] args) {
		System.out.println("\n******** SHAPE 2D ********");
		Shape[] shapes = {
			new Rectangle(10, 5),
			new Square(7.3),
			new RegularShape(10, Polygon.TRIANGLE),
			new RegularShape(10, 4),
			new RegularShape(10, 5),
			new RegularShape(10, 6),
			new RegularShape(10, 7),
			new RegularShape(10, 8),
			new RegularShape(10, 9),
			new RegularShape(10, 10),
			new RegularShape(10, 11),
			new RegularShape(10, 12),
			new RegularShape(10, 13),
		};
		for(Shape shape: shapes)
			System.out.println(shape);
		System.out.println("\n******** SHAPE 3D ********");
		Prism[] parallepieds = {
			new Prism(2, 10, 3),
			new Prism(2, 10, 4),
			new Prism(2, 10, 5),
			new Prism(2, 10, 6),
			new Prism(2, 10, 7),
			new Prism(2, 10, 8),
			new Prism(2, 10, 9),
			new Prism(2, 10, 10),
			new Prism(2, 10, 11),
			new Prism(2, 10, 12)
		};
		for(Prism p: parallepieds)
			System.out.println(p);
	}
}