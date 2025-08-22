package ejer4;

public class main {

	public static void main(String[] args) {
		Rectangulo rec1 = new Rectangulo();
		Rectangulo rec2 = new Rectangulo(10,10);
		Rectangulo rec3 = new Rectangulo(0,0,10,10);
		
		System.out.println("el perimetro del rectangulo es de " + rec1.perimetro());
		System.out.println("el perimetro del rectangulo es de " + rec2.perimetro());
		System.out.println("el perimetro del rectangulo es de " + rec3.perimetro());

	}

}
