package ejer4;

public class Producto {
	int cod;
	String desc;
	int precio;
	
	public int getCod() {
		return cod;
	}
	public void setCod(int cod) {
		this.cod = cod;
	}
	public String getDesc() {
		return desc;
	}
	public void setDesc(String desc) {
		this.desc = desc;
	}
	public int getPrecio() {
		return precio;
	}
	public void setPrecio(int precio) {
		this.precio = precio;
	}
	Producto(int cod,String desc,int precio)
	{
		this.cod=cod;
		this.desc=desc;
		this.precio=precio;
	}
	
}
