package shapes3D;
import model.Polygon;
import model.Shape3D;
import shapes.RegularShape;
public class Prism extends RegularShape implements Shape3D {
	private double w;
	public Prism(double w, double l, int N) {
		super(l, N);
		this.w = w;
	}
	public double getW() {
		return w;
	}
	public void setW(double w) {
		if(w >= 0)
			this.w = w;
	}
	@Override
	public double volume() {
		return super.area() * w;
	}
	@Override
	public double totSurfaceArea() {
		return 2 * super.area() + super.perimeter() * w;
	}
	@Override
	public String toString() {
		return """
		%s PRISM:
		N:	%d
		l:	%.2f cm
		p:	%.2f cm
		B:	%.2f cm^2
		St:	%.2f cm^2
		V:	%.2f cm^3
		""".formatted(
		N <= Polygon.values().length - 3
				? Polygon.values()[N -3]
				: "MULTI-SIDES",
			N, l,
			perimeter(),
			area(),
			totSurfaceArea(),
			volume()
		).strip();
	}
}