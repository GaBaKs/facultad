package ejer4;



public class Autos extends Vehiculos {

	public Autos(int cantplazas) {
		super(cantplazas);
		
		
	}
	
	public double costototal(int dias) {
		return dias*costodiario*1.015*cantplazas;
	}
	
	
	
}
