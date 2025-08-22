package ejer5;

public class Guerrero {

		String nombre;
		double vitalidad;
		double armadura;
		double x;
		double y;
		
		public String getNombre() {
			return nombre;
		}
		
		public void setNombre(String nombre) {
			this.nombre = nombre;
		}
		
		public double getVitalidad() {
			return vitalidad;
		}
		
		public void setVitalidad(double vitalidad) {
			this.vitalidad = vitalidad;
		}
		
		public double getArmadura() {
			return armadura;
		}
		
		public void setArmadura(double armadura) {
			this.armadura = armadura;
		}
		
		public double getX() {
			return x;
		}
		
		public void setX(double x) {
			this.x = x;
		}
		
		public double getY() {
			return y;
		}
		
		public void setY(double y) {
			this.y = y;
		}
		
		void mover(double inc_x,double inc_y)
		{
			x+=inc_x;
			y+=inc_y;
		}
		
		void recibeDano(double cantidad)
		{
			armadura-=cantidad;
			if (armadura<0)
			{
				vitalidad+=(armadura);
				armadura=0;
			}
		}
}


















