package ejer3guia2;

public class main {

	public static void main(String[] args) {
		CuentaBancaria c1 = new CuentaBancaria("Martin");
		
		c1.depositar(1000);
		c1.depositar(-1000);
		boolean x= c1.extraer(500);
		if (x)
			System.out.print("se pudo extraer correctamente");
		else
			System.out.print("sos tonto flaco?");
	}

}
