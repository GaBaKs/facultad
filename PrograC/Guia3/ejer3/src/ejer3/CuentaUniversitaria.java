package ejer3;

public class CuentaUniversitaria extends CuentaBanco {
	private double diario=0;
	private double limite=1000;
	
	
	public void extraer(double cant)
	{
		if (diario+cant<=limite && cant<=saldo)
			saldo-=cant;
	}
	
	
	
	public CuentaUniversitaria(String nombre) {
		super();
		this.nombre=nombre;
		this.diario=0;
		
	}

	
	public void setDiario(double diario) {
		this.diario = diario;
	}



	@Override
	public String toString() {
		return "CuentaUniversitaria limite=" + limite + ", saldo=" + saldo + ", nombre="
				+ nombre + "]";
	}


	

	
	
}
