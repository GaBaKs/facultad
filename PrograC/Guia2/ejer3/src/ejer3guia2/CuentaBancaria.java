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
		
		
		
		
		
		
		public double getSaldo() {
			return saldo;
		}

		public void setSaldo(double saldo) {
			this.saldo = saldo;
		}

		public String getTitular() {
			return titular;
		}

		public void setTitular(String titular) {
			this.titular = titular;
		}
		
		
		
		
		
		
}
