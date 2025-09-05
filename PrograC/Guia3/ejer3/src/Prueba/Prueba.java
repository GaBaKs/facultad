package Prueba;

import ejer3.*;

public class Prueba {

	public static void main(String[] args) {
		CuentaBanco c1= new CajaAhorro("martin",2);
		System.out.println("C1");
		c1.depositar(1000);
		c1.extraer(500);
		
		CuentaBanco c2= new CuentaUniversitaria("Gabriel");
		System.out.println("C2");
		c2.depositar(1000);
		c2.extraer(1000);
		
		CuentaBanco c3 = new CuentaCorriente("Matias",1000);
		System.out.println("C3");
		c3.depositar(1000);
		c3.extraer(2000);
		
		System.out.println(c1);
		System.out.println(c2);
		System.out.println(c3);
	}

}
