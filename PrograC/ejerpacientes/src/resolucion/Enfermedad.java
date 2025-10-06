package resolucion;

public class Enfermedad {
	int tipo;
	String descripcion;
	boolean contagiosa;
	public Enfermedad(int tipo, String descripcion, boolean contagiosa) {
		this.tipo = tipo;
		this.descripcion = descripcion;
		this.contagiosa = contagiosa;
	}
	public int getTipo() {
		return tipo;
	}
	public void setTipo(int tipo) {
		this.tipo = tipo;
	}
	public String getDescripcion() {
		return descripcion;
	}
	public void setDescripcion(String descripcion) {
		this.descripcion = descripcion;
	}
	public boolean isContagiosa() {
		return contagiosa;
	}
	public void setContagiosa(boolean contagiosa) {
		this.contagiosa = contagiosa;
	}
	@Override
	public String toString() {
		return "Enfermedad [tipo=" + tipo + ", descripcion=" + descripcion + ", contagiosa=" + contagiosa + "]";
	}
	
	
}
