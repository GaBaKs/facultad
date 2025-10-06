package resolucion;

public class main {

	public static void main(String[] args) {
		Enfermedad enfermedad= new Enfermedad(1,"es terrible",true);
		Paciente p1= new Paciente("martin",21,enfermedad);
		
		try {
			Paciente p2=(Paciente) p1.clone();
			System.out.println(p1);
			p2.enfermedad.setTipo(3);
			System.out.println(p1);
			System.out.println(p2);
		}
		catch(CloneNotSupportedException e) {
			System.out.println("no soporta clones");
		}
	}

}
