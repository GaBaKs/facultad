package barcos;

public class Barco implements Cloneable{
	String Nombre;
	double Velocidad;
	Armamentos Armamento;
	
	
	public Barco(String nombre, double velocidad, Armamentos armamento) {
		super();
		this.Nombre = nombre;
		Velocidad = velocidad;
		Armamento = armamento;
	}


	@Override
		public Object clone() throws CloneNotSupportedException{
		
			Barco barcoclonado=null;
			barcoclonado=(Barco)super.clone();
			barcoclonado.Armamento=(Armamentos) Armamento.clone();
			return barcoclonado;
			
	}


	@Override
	public String toString() {
		return "Barco [Nombre=" + Nombre + ", Velocidad=" + Velocidad + ", Armamento=" + Armamento + "]";
	}
	
	
}
