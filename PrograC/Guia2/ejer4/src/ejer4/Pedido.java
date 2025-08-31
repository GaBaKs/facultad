package ejer4;
import java.util.ArrayList;




public class Pedido {
	Empleado empleado;
	String fecha;
	public static ArrayList <LineaDePedido> lineas= new ArrayList <LineaDePedido>();
	
	public void agregaLineadepedido(LineaDePedido ldp)
	{
		lineas.add(ldp);
	}

	
	
	public Empleado getEmpleado() {
		return empleado;
	}

	public void setEmpleado(Empleado empleado) {
		this.empleado = empleado;
	}

	public String getFecha() {
		return fecha;
	}

	public void setFecha(String fecha) {
		this.fecha = fecha;
	}

	
	

}
