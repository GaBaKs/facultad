package ejer3;

public class CuentaCorriente extends CuentaBanco{
		double tope;

		public CuentaCorriente(String nombre,int tope) {
			super();
			this.nombre=nombre;
			this.tope=tope;
			
		}
		
		public void extraer(double cant)
		{
			if ((saldo+tope)>=cant)
			{
				saldo-=cant;
			}

				
		}

		public void setTope(double tope) {
			this.tope = tope;
		}

		@Override
		public String toString() {
			return "CuentaCorriente [tope=" + tope + ", saldo=" + saldo + ", nombre=" + nombre + "]";
		}

		
		
		
}
