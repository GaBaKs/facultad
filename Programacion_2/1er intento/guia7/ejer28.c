#include <stdio.h>
#include <stdlib.h>



/*void par(arbol A,pos p,int * cant){

    pos c;
    int grado;
    c=Hijomasizq(p,A);
    if (!nulo(c)){
        while(!nulo(c))
            par(A,c,cant);
            grado++;
            c=Hermanoder(p,A);
    }
     *cant=!grado%2;
    }

*/

int nodos(arbol a,pos p){
    pos c;
    if (!nulo(c)){
        return 1+nodos(a,hijomasizq(c,a))+nodos(a,hermanoder(c,a));
    }
    else return 0;
}


void porcentaje(arbol a,pos p,int cont1, int cont2){
    if (!nulo(c)){
        pos c;
        cont1+= (info(p,a) % 2 == 0);
        cont2+=1;
        c=hijomasizq(p,a);
        while (!nulo(c)){
            cont1+=(info(c,a)%2 ==0);
            cont2+=1;
            porcentaje(a,hijomasizq(c,a),cont1,cont2);
            c=hermanoder(c,a);
        }
    }
    printf("%f.2",(float)cont1/cont2);
}


 int grado(arbol a, pos p){
    if (!nulo(p)){
        gradohijo=grado(a,hijomasizq(p,a));
        gradohermano=grado(a,hermanoder(p,a));
        int max=0;
        int i=0;
        pos c= hijomasizq(p,a);
        while (!nulo(c)){
            i++;
            c=hermanoder(c,a);
        }
        max = (gradohijo<gradohermano)?gradohermano:gradohijo;
        return (max<i)? i:max;
    }
    else return 0;
 }


