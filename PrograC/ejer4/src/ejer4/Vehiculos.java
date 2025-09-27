package ejer4;

public abstract class Vehiculos {
	double costodiario=500;
	int cantplazas;
	Vehiculos(int cantplazas)
	{
		this.cantplazas=cantplazas;
	}
		
	public abstract double costototal(int dias);
		
	
	
	
}
