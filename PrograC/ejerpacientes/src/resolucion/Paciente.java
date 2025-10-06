package resolucion;

public class Paciente implements Cloneable{
	String nombre;
	int edad;
	Enfermedad enfermedad;
	
	
	
	public Paciente(String nombre, int edad, Enfermedad enfermedad) {
		super();
		this.nombre = nombre;
		this.edad = edad;
		this.enfermedad = enfermedad;
	}

	

	@Override
		public Object clone() throws CloneNotSupportedException{
			Paciente pacienteC=null;
			pacienteC=(Paciente)super.clone();
			return pacienteC;
	}



	@Override
	public String toString() {
		return "Paciente [nombre=" + nombre + ", edad=" + edad + ", enfermedad=" + enfermedad + "]";
	}
	
	
}
