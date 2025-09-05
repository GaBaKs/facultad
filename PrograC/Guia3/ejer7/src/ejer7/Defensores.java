package ejer7;

public class Defensores extends Jugadores{

	public Defensores(String nombre, double potencia, double velocidad) {
		super(nombre, potencia, velocidad);
	}

	@Override
	public double indiceDefensa() {

		return this.velocidad*this.velocidad;
	}

	@Override
	public double indiceAtaque() {
		return potencia*potencia;
	}

	@Override
	public String toString() {
		return "Defensores [potencia=" + potencia + ", velocidad=" + velocidad + ", nombre=" + nombre + "]";
	}

	
}
