package ejer7;

public class Delanteros extends Jugadores {

	public Delanteros(String nombre,double potencia,double velocidad) {
		super(nombre,potencia,velocidad);
		
	}

	@Override
	public double indiceDefensa() {
		return this.velocidad*0.5;
	}

	@Override
	public double indiceAtaque() {
		return this.velocidad*this.potencia;
	}

	@Override
	public String toString() {
		return "Delanteros [potencia=" + potencia + ", velocidad=" + velocidad + ", nombre=" + nombre + "]";
	}
	
	 

}
