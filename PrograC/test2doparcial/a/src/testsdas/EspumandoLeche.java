package testsdas;

public class EspumandoLeche implements Istate{

	Cafetera a
	public EspumandoLeche(Cafetera cafetera) {
		this.a=cafetera;
	}
	@Override
	public void preparoCafe() {
		a.setEstado(new PreparandoCafe(a));
		System.out.println("preparando cafe");
		
	}
	@Override
	public void espumoLeche() {
		// TODO Auto-generated method stub
		
	}
	@Override
	public void Disponible() {
		// TODO Auto-generated method stub
		
	}
	
	
}
