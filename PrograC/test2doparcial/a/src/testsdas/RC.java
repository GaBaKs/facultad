package testsdas;


public class RC {

	public LinkedList<Libros> libros=new LinkedList();
	iterator
	
	public synchronized void solicitalibro(Libro libro) {
		
	 while (!this.librodisponible(libro))
		wait();
	
	//saco libro de lista
	 this.libros.notifyall();
	}
	
	
	public synchronized void DevuelveLibro(Libro libro) {
		libros.add(libro);
	}
	
	
	private boolean librodisponible(Libro libro) {
		//recorre iterator
	}
	
	
	
}
