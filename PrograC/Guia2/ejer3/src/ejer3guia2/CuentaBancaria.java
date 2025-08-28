package ejer3guia2;

public class CuentaBancaria {

		double saldo;
		String titular;
		
		CuentaBancaria(String titular)
		{
			this.titular=titular;
			this.saldo=0;
		}

		void depositar(double monto)
		{
			if (monto<=0)
			
				System.out.println("Sos tonto flaco?");
			else
				{
				this.saldo+=monto;
				}
		}
		
		boolean extraer(double monto)
		{
			if (monto>this.saldo)
				return false;
			else
			{
				saldo-=monto;
				return true;
			}
				
		}
		
		
		
		
		public double getSaldo() {
			return saldo;
		}



		public String getTitular() {
			return titular;
		}

		
		
		
		
}
