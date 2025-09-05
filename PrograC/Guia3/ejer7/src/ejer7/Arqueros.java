package ejer7;


public class Arqueros extends Jugadores {

	double efectividad;
	
	public Arqueros(String nombre, double potencia, double velocidad, double efectividad) {
		super(nombre, potencia, velocidad);
		this.efectividad=efectividad;
	}

	@Override
	public double indiceDefensa() {
		return efectividad;
	}

	@Override
	public double indiceAtaque() {
		return 0.1*velocidad*potencia;
	}

	@Override
	public String toString() {
		return "Arqueros [efectividad=" + efectividad + ", potencia=" + potencia + ", velocidad=" + velocidad
				+ ", nombre=" + nombre + "]";
	}

}
