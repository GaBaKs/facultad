package ejer4;

public class Rectangulo {
	int x1,x2,y1,y2;

	public int getX1() {
		return x1;
	}

	public void setX1(int x1) {
		this.x1 = x1;
	}

	public int getX2() {
		return x2;
	}

	public void setX2(int x2) {
		this.x2 = x2;
	}

	public int getY1() {
		return y1;
	}

	public void setY1(int y1) {
		this.y1 = y1;
	}

	public int getY2() {
		return y2;
	}

	public void setY2(int y2) {
		this.y2 = y2;
	}
	
	
	int perimetro()
	{
		return 2*(this.x2-this.x1+this.y2-this.y1);
	}
	
	
	public Rectangulo()
	{
		setX1(-1);
		setX2(1);
		setY1(-1);
		setY2(1);
	}
	
	public Rectangulo(int ancho,int alto)
	{
		setX1(0);
		setX2(ancho);
		setY1(0);
		setY2(alto);
	}
	
	public Rectangulo(int x1,int y1,int x2,int y2)
	{
		setX1(x1);
		setX2(x2);
		setY1(y1);
		setY2(y2);
	}
	
	
	
}
