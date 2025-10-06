package excepciones;


public class Excepciones{
	public static void main(String[] args) throws ValException{
	 int i=0;
	   try { 
		   i=1/0;
		}
	   
	  
	   catch(ValException e) {
		   System.out.println(e+"entro");
	   }
	   catch(RuntimeException e) {
		   System.out.println("CATCH " +e.getMessage());
	   }
	    try {
		   throw new ValException("asdsad");
	   }
	    
	    catch(ValException e) {
			   System.out.println(e+"entro");
		   }
	   finally {
		   System.out.println("TERMINO");
	   }
	System.out.println("asda");
	}
}

