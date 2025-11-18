package testsdas;

public class Disponible implements Istate{

	Cafetera a;
	
	public Disponible(Cafetera a) {
		a.setEstado(this);
	}
	
	
	
	
}
