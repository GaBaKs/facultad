package aprenderclone;

public class Estudiante implements Cloneable{
	private int codigo;
	private int nombre;
	
	public Estudiante(int codigo, int nombre) {
		this.codigo=codigo;
		this.nombre=nombre;
	}


	public void setNombre(int nombre) {
		this.nombre = nombre;
	}
	
	@Override
	public Object clone() throws CloneNotSupportedException{
		return super.clone();
	}

	@Override
	public String toString() {
		return "Estudiante [codigo=" + codigo + ", nombre=" + nombre + "]";
	}
	
	

	
}

	