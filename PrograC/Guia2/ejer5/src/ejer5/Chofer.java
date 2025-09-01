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
		this.colectivo=null;
	}
	
	
	@Override
	public String toString()
	{
	  if (this.colectivo!=null)
		  return "nombre: "+ nombre + " domicilio: " + domicilio + " categoria: " + categoria + colectivo;
	  else
		  return "nombre: "+ nombre + " domicilio: " + domicilio + " categoria: " + categoria + " No tiene un colectivo asignado";
	}
	
}
