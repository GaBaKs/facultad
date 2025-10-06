package barcos;

import barcos.Armamentos.Posiciones;

public class Armamento_canon extends Armamentos{
	int Cargador;
	Posiciones posicion;
	
	
	
	
	public Armamento_canon(Float alcance, int cargador, Posiciones posicion) {
		super(alcance);
		Cargador = cargador;
		this.posicion = posicion;
	}




	@Override
	public Object clone() throws CloneNotSupportedException{
		if (posicion==Posiciones.BABOR || posicion==Posiciones.ESTRIBOR) {
			Armamentos armamentocanonclon=null;
			armamentocanonclon=(Armamento_Misil)super.clone();
			return armamentocanonclon;
		}
		else
			throw new CloneNotSupportedException();
	}	

}
