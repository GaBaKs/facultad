package testsdas;

public class Cafetera {
	
	Istate estado;
	String marca;
	Persona cliente;
	Persona operario;
	
	public Cafetera(String marca) {
		this.marca=marca;
		estado=new Disponible(this);
	}

	public void ClientePideCafe() {
		this.estado.preparoCafe();
	}
	
	public void ClientePideTe() {
		this.estado.preparoCafe();
	}
	
	public void OperarioPideCargaAgua() {
		this.estado.CargoAgua();
	}
	
	public void OperarioTerminaUso() {
		this.estado.Disponible();
	}
	
	public void setEstado(Istate estado) {
		this.estado=estado;
	}
}
