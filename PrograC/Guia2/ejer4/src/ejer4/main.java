package ejer4;
import java.util.ArrayList;
public class main {

	public static void main(String[] args) {
		ArrayList <Empleado> empleados = new ArrayList <Empleado>();
		Empleado e1 = new Empleado("martin","223456788","asd@gmail.com");
		empleados.add(e1);
		e1 = new Empleado("martin2","12345667","rty@gmail.com");
		empleados.add(e1);
		
		ArrayList <Producto> productos = new ArrayList <Producto>();
		Producto p1 = new Producto(1234,"desc1",100);
		productos.add(p1);
		p1 = new Producto(2345,"desc2",50);
		productos.add(p1);
		
		
		
		
		Pedido sol = new Pedido(); 
		
		
		
		
	}

}
