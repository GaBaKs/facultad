package aprenderclone;

public class prueba {

	public static void main(String[] args) {
		try {
			Estudiante es1= new Estudiante(232,12);
			System.out.println(es1);

			
			Estudiante clon= (Estudiante)es1.clone();
			clon.setNombre(23);
			System.out.println(es1);
			System.out.println(clon);
		}
		catch (CloneNotSupportedException e) {
			System.out.println("no puedo clonar botardo");
		}
	}

}
