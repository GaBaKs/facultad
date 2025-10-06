package barcos;

public abstract class Armamentos implements Cloneable{
	Float Alcance;
	enum Posiciones {POPA,BABOR,ESTRIBOR,PROA};
	
public void setAlcance(float alcance) {
		this.Alcance=alcance;
	}
	
	public Armamentos(Float alcance) {
		super();
		Alcance = alcance;
	}



	@Override
		public Object clone() throws CloneNotSupportedException{
		 try {
			Armamentos armamentoclon=null;
			armamentoclon=(Armamentos)super.clone();
			return armamentoclon;
		 }
		 catch(CloneNotSupportedException e){
			 System.out.println("No se pudo clonar");
			 return null;
		 }
		 
		 
	}

	@Override
	public String toString() {
		return "Armamentos [Alcance=" + Alcance + "]";
	}
	
	
}
