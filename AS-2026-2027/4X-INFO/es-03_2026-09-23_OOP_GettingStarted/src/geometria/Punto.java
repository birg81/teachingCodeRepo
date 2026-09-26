package geometria;
public class Punto {
	private double x, y;
	public Punto(final double x, final double y) {
		this.x = x;
		this.y = y;
	}
	public Punto(final double t) {
		this(t, t);
	}
	public Punto() {
		this(0.);
	}
	public Punto(final Punto p) {
		this(p != null ? p.x : 0, p != null ? p.y : 0);
	}
	public final double getX() {
		return x;
	}
	public final double getY() {
		return y;
	}
	public final void setX(final double x) {
		this.x = x;
	}
	public final void setY(final double y) {
		this.y = y;
	}
	@Override
	public String toString() {
		return "(%.2f, %.2f)".formatted(x, y);
	}
	public double dist(final Punto p) {
		return Math.sqrt((x - p.x) * (x - p.x) + (y - p.y) * (y - p.y));
	}
	public double module() {
		return dist(new Punto());
	}
	public Punto scale(final double k) {
		return new Punto(k * x, k * y);
	}
	public void info() {
		System.out.printf("%s;\n", this);
	}
}