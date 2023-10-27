package shapes;
import model.Shape;
public class Square implements Shape {
	protected double l;
	public Square() {
		this(1);
	}
	public Square(double l) {
		this.l = l >= 0 ? l : 0;
	}
	public double getL() {
		return l;
	}
	public void setL(double l) {
		if(l >= 0)
			this.l = l;
	}
	@Override
	public double area() {
		return l * l;
	}
	@Override
	public double perimeter() {
		return l * 4;
	}
	@Override
	public String toString() {
		return """
		SQUARE SHAPE:
		* l:	%.2f cm
		* p:	%.2f cm
		* A:	%.2f cm^2
		""".formatted(l, perimeter(), area()).strip();
	}
}