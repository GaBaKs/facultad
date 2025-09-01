package ejer5;

public class Colectivo {
	static int cont=100;
	String modelo;
	int numerointerno;
	
	
	Colectivo(String modelo)
	{
		this.modelo=modelo;
		cont+=1;
		this.numerointerno=cont;
	}
	
	@Override
		public String toString()
		{
			return "Modelo colectivo: "+ modelo +" numero interno: " + numerointerno;
		}
	
}
