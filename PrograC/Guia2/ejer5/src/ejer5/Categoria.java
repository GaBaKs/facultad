package ejer5;

public class Categoria {
	String nombrecategoria;
	double sueldo;
	
	
	Categoria(String nombrecategoria,int sueldo)
	{
		this.nombrecategoria=nombrecategoria;
		this.sueldo=sueldo;
	}
	
	void sueldosup(double sueldo)
	{
		if (sueldo>this.sueldo)
			System.out.print(" "+ nombrecategoria);
	}
}
