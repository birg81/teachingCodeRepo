package shapes;
import model.Shape;
public class Rectangle implements Shape {
	protected double b, h;
	public Rectangle(double b, double h) {
		this.b = b >= 0 ? b : 0;
		this.h = h >= 0 ? h : 0;
	}
	public Rectangle(double l) {
		this(l, l);
	}
	public Rectangle() {
		this(1);
	}
	public double getB() {
		return b;
	}
	public double getH() {
		return h;
	}
	public void setB(double b) {
		if(b >= 0)
			this.b = b;
	}
	public void setH(double h) {
		if(h >= 0)
			this.h = h;
	}
	@Override
	public double area() {
		return b * h;
	}
	@Override
	public double perimeter() {
		return 2 * (b + h);
	}
	@Override
	public String toString() {
		return """
		RECTANGLE SHAPE:
		* b:	%.2f cm
		* h:	%.2f cm
		* p:	%.2f cm
		* A:	%.2f cm^2
		""".formatted(b, h, perimeter(), area()).strip();
	}
}