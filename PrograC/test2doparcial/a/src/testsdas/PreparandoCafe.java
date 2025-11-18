package testsdas;

public class PreparandoCafe implements Istate{
	
	Cafetera a;
	
	public PreparandoCafe(Cafetera cafetera) {
		a=cafetera;
	}
	
	
	public void preparoCafe() {
		System.out.println("ya estoy preparando cafe");
	}
	
	public void espumoLeche() {
		a.setEstado(new EspumandoLeche(a));
		System.out.println("Espumando leche");
	}
	
	public void CargoAgua() {
		//error xq esta preparando cafe
	}
	
	public void Disponible() {
		a.setEstado(new Disponible(a));
		System.out.println("La maquina ahora se encuentra disponible");
	}
}
