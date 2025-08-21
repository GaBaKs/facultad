package ejer1;

public static void main {
	double saldo;
	string titular,aux;
	
	CuentaBancaria unacuenta = new CuentaBancaria();
	unacuenta.depositar(1250);
	unacuenta.extraer(450);
	saldo=unacuenta.getsaldo();
	unacuenta.setTitular("Juan Perez");
	aux = unacuenta.getTitular;
}
