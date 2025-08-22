package ejer6;

public class Socio {

		double cuota=500;
		int edad;
		
		public int getEdad() {
			return edad;
		}
		public void setEdad(int edad) {
			this.edad = edad;
		}
		
		public Socio(int edad)
		{
			this.edad=edad;
		}
		
		public double calcularCuota()
		{
			if (edad<=18)
				return 0.75*cuota;			
			else
				if (edad>=65)
					return 0.5*cuota;
				else
					return cuota;
		}
}
