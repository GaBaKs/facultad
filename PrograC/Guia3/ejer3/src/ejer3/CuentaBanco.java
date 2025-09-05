package ejer3;

public abstract class CuentaBanco {
		protected double saldo;
		String nombre;
	
		
		public CuentaBanco() {
			super();
			this.saldo = 0;
		}

		public double getSaldo()
		{
			return this.saldo;
		}
		
		public void depositar(double cant)
		{
			saldo+=cant;
		}
		
		public abstract void extraer(double cant);

	
		
		
}
