package barcos;

public class Prueba {

	public static void main(String[] args) {
		Barco b2=null;
		Armamentos misil=new Armamento_Misil(200,200,false,Armamentos.Posiciones.PROA);
		Barco b1=new Barco("asd",200.1,misil);
		
		System.out.println(b1);
		try {	
			b2=(Barco)b1.clone();
		}
		catch(CloneNotSupportedException e){
			System.out.println("BOT");
		}
		b2.Armamento.setAlcance(2.0f);
		System.out.println(b2);
		System.out.println(b1);
	}
	
}
