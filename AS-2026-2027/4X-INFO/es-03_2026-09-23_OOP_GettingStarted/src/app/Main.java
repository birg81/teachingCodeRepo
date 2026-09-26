package app;
import geometria.Punto;
public class Main {
	public static void main(String[] args) {
		Punto p = new Punto(3, 4);
		Punto q = new Punto(5, 12);
		Punto o = new Punto();
		System.out.printf(
			"""
			P%s module: %.2f
			Q%s module: %.2f
			O%s module: %.2f
			d(P,Q): %.2f
			scale 3P = %s
			""",
				p, p.module(),
				q, q.module(),
				o, o.module(),
				p.dist(q),
				p.scale(3)
		);
	}
}
