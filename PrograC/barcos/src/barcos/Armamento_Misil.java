package barcos;


public class Armamento_Misil extends Armamentos{
	double Potencia_explosivo;
	boolean ILS;
	Posiciones posicion;
	
	
	
	
	public Armamento_Misil(Float Alcance,double potencia_explosivo, boolean iLS, Posiciones posicion) {
		super(Alcance);
		Potencia_explosivo = potencia_explosivo;
		ILS = iLS;
		this.posicion = posicion;
	}




	public Armamento_Misil(float Alcance,double potencia_explosivo, boolean iLS, Posiciones posicion) {
		super(Alcance);
		Potencia_explosivo = potencia_explosivo;
		ILS = iLS;
		this.posicion = posicion;
	}




	@Override
	public Object clone() throws CloneNotSupportedException{
		if (posicion==Posiciones.BABOR || posicion==Posiciones.ESTRIBOR) {
			Armamentos armamentomisilclon=null;
			armamentomisilclon=(Armamento_Misil)super.clone();
			return armamentomisilclon;
		}
		else
			throw new CloneNotSupportedException();
		
	}
}
