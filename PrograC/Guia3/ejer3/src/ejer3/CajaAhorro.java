package ejer3;

public class CajaAhorro extends CuentaBanco{
	int cantextracciones=0;
	int extraccionesmax;
	@Override
	public void extraer(double cant) {
			if (cantextracciones<cantextracciones && this.saldo>=cant)
			{	
				cantextracciones++;
				this.saldo-=cant;
			}
	}
	
	public CajaAhorro(String nombre,int extraccionesmax)
	{
		super();
		this.nombre=nombre;
		this.extraccionesmax=extraccionesmax;
		
	}

	@Override
	public String toString() {
		return "CajaAhorro "+ "saldo=" + saldo + ", nombre=" + nombre + "]";
	}

	
	
	
}
