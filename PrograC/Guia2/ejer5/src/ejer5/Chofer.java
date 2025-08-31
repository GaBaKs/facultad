package ejer5;

public class Chofer {
	Categoria categoria;
	Domicilio domicilio;
	String nombre;
	Colectivo colectivo;
	
	
	void desvincula()
	{
		this.colectivo=null;
	}
	
	
	Chofer(Categoria categoria,Domicilio domicilio,String nombre, Colectivo colectivo)
	{
		this.categoria=categoria;
		this.domicilio=domicilio;
		this.nombre=nombre;
		this.colectivo=colectivo;
	}
	
	Chofer(Categoria categoria,Domicilio domicilio,String nombre)
	{
		this.categoria=categoria;
		this.domicilio=domicilio;
		this.nombre=nombre;
	}
	
	
}
