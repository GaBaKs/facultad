package ejer5;
import java.util.ArrayList;


public class Empresa {
	private String nombre;
    private ArrayList<Chofer> choferes = new ArrayList<>();
    private ArrayList<Colectivo> colectivos = new ArrayList<>();
    private ArrayList<Categoria> categorias = new ArrayList<>();
    
    
    public int choferesnocol()
    {
    	int cont=0;
    	for (Chofer c: choferes)
    	{
    		if (c.colectivo==null)
    			cont++;
    	}
    	return cont;
    }
    
    public int cantcolectivos() {
    	return colectivos.size();
    }
    
    public void quecategoria(String categoria)
    {
    	int cont=0;
    	for (Chofer c : choferes)
    	{
    		if (c.categoria.nombrecategoria==categoria)
    			cont++;
    	}
    }
    
    public void choferesueldosup(double sueldo)
    {
  
    	for (Chofer c: choferes)
    	{
    		if (c.categoria.sueldo>sueldo)
    			System.out.println(c);
    	}
   
    }
    
    
    public void sueldomayor(double sueldo)
    {
    	for (Categoria c: categorias)
    	{
    		c.sueldosup(sueldo);
    	}
    }
    
    public void addChofer(Chofer chofer)
    {
    		choferes.add(chofer);
    }
    
    public void addColectivo(Colectivo colectivo)
    {
		colectivos.add(colectivo);
    }
    
    public void addCategoria(Categoria categoria)
    {
		categorias.add(categoria);
    }
    
    Empresa(String nombre)
    {
    	this.nombre=nombre;
    	
    }
}
