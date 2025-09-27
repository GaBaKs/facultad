package ejer4;


public class Combis extends Vehiculos {

	Combis(int cantplazas)
	{
		super(cantplazas);
		
	}
	
	public double costototal(int dias)
	{
		return costodiario*dias*1.02*cantplazas;
	}
}
