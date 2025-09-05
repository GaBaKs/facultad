package ejer7;

public abstract class Jugadores {

	double potencia;
	double velocidad;
	String nombre;
	
	public Jugadores(String nombre,double potencia,double velocidad) {
		super();
		this.nombre=nombre;
		this.potencia=potencia;
		this.velocidad=velocidad;
		
	}
	
	public abstract double indiceDefensa();
	
		
	
	
	public abstract double indiceAtaque();
		
	

}
