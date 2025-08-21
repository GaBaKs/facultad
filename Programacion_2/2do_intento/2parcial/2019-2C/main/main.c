#include <stdio.h>
#include <stdlib.h>

typedef int TelememtoA;

typedef struct nodo{

    TelememtoA dato;
    nodo * izq, * der;}nodo;

}
typedef struct nodo * Tarbol;


int main()



int grado(arbol a){

int cont=0;
    while (a!=NULL){
            cont++;
            a+a->der;
    }
    return cont;
}


int suma(arbol a,int alt){    // tarde 8:46 en hacerlo y 1:30 seg revisando

    if (a!=NULL){
        if (a->dato==alt && a->dato==grado(a->izq)){
            return a->dato+suma(a->izq,alt+1)+suma(a->der,alt);
        }
        else suma(a->izq,alt+1)+suma(a->der,alt);
    }
    else return 0;

}


void mayornivel(arbol a,pos p,int cont0,int niv,int nivmax){   // tarde 9 min mas una revision de profe
            if (!nulo(p) && cont0<2){
                if (info(p,a)==0){
                    if (nivmax<niv){
                        nivmax=niv;
                        cont0++;
                    }
                }
                mayornivel(a,hijomasizq(p,a),cont0,niv+1,nivmax);
                mayornivel(a,hermanoder(p,a),cont0,niv,nivmax);
            }
            else
               if (cont0==2)
                printf("el nivel maximo donde hay un 0 es %d",nivmax);
}



