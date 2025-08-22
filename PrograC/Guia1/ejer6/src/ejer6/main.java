package ejer6;

public class main {

	public static void main(String[] args) {
		Socio soc1 = new Socio(66);
		Socio soc2 = new Socio(16);
		Socio soc3 = new Socio(65);
		Socio soc4 = new Socio(20);
		
		System.out.println("el precio que paga el socio 1 es de" + soc1.calcularCuota());
		System.out.println("el precio que paga el socio 2 es de" + soc2.calcularCuota());
		System.out.println("el precio que paga el socio 3 es de" + soc3.calcularCuota());
		System.out.println("el precio que paga el socio 4 es de" + soc4.calcularCuota());
		
		
		
	}

}
