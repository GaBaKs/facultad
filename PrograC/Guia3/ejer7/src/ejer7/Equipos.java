package ejer7;
import java.util.ArrayList;

public class Equipos {

	ArrayList <Jugadores> listajugadores= new ArrayList<>();
	
	
	public Equipos() {
		
	}
	
	String agregaDelantero(String nombre, double velocidad, double potencia)
	{
		 if (velocidad>0 && velocidad <=1 && potencia>0 && potencia<=1)
		 {
			 Jugadores newdelantero = new Delanteros(nombre,velocidad,potencia);
			 listajugadores.add(newdelantero);
			return "Se agrego un delantero correctamente";
		 }
		 else return "No se pudo agregar un delantero";
	}	
	String agregaDefensor(String nombre,double velocidad, double potencia)
	{
	   if (velocidad>0 && velocidad <=1 && potencia>0 && potencia<=1)
	   {   
		   Jugadores newDefensor= new Defensores(nombre,velocidad,potencia);
			listajugadores.add(newDefensor);
			return "Se agrego un defensor correctamente";
	   }
	   else return "No se pudo agregar un defensor";
	}
	
	String agregaArquero(String nombre, double velocidad, double potencia,double efectividad)
	{
		 if (velocidad>0 && velocidad <=1 && potencia>0 && potencia<=1)
		 {
			 Jugadores newArquero= new Arqueros(nombre,velocidad,potencia,efectividad);
			 listajugadores.add(newArquero);
			 return "Se agrego un arquero correctamente";
		 }
		 else return "No se pudo agregar un arquero";
	}
	
	void eliminaJugador(Jugador jugador)
	{
		
	}
	
	Iterator<Jugador> getJugadores();
	
	double indiceDefensa();
	
	double indiceAtaque();

	
}
