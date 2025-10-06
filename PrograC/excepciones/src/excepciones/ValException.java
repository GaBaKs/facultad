package excepciones;

public class ValException extends RuntimeException{

		public ValException(String mensaje) {
			super(mensaje);
			
		}

		@Override
		public String toString() {
			return "Hola soy un tostring";
		}
		
		
}


