package shapes;
import model.Shape;
import model.Polygon;
public class RegularShape implements Shape {
	protected final int N;
	protected double l;
	public RegularShape(double l, int N) {
		this.l = l > 0 ? l : 1;
		this.N = N >= 3 ? N : 3 + Polygon.SQUARE.ordinal();
	}
	public RegularShape(double l, Polygon polygonKind) {
		this(l, 3 + polygonKind.ordinal());
	}
	public RegularShape(double l) {
		this(l, Polygon.SQUARE);
	}
	public RegularShape() {
		this(1);
	}
	public int getN() {
		return N;
	}
	public double getL() {
		return l;
	}
	public void setL(double l) {
		if(l > 0)
			this.l = l;
	}
	@Override
	public double area() {
		return .25 * l * l * N / Math.tan(Math.PI / N);
	}
	@Override
	public double perimeter() {
		return N * l;
	}
	@Override
	public String toString() {
		return """
		%s SHAPE:
		* N:	%d
		* l:	%.2f cm
		* p:	%.2f cm
		* A:	%.2f cm^2
		""".formatted(
			N <= Polygon.values().length - 3
				? Polygon.values()[N -3]
				: "MULTI-SIDES",
			N, l,
			perimeter(),
			area()
		).strip();
	}
}