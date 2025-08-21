#include <stdio.h>
#include <stdlib.h>


typedef chat TelementoA;
typedef struct nodo{
        TelementoA dato;
        struct nodo * izq;
        struct nodo *der;}nodo;

typedef struct nodo * arbol;




int main(){




}



void busqueda(arbol a,int maxlevel,char * clave,int levelact){

    if(a!=NULL){
            if (a->izq!=NULL && a->der!=NULL && maxlevel<levelact){
                maxlevel=levelact;
                *clave=a->dato;
            }
                busqueda(a->izq,maxlevel,clave,levelact+1);
                busqueda(a->der,maxlevel,clave,levelact+1);
    }


}



int verifica(arbol a,pos p, int k1, int k2,int nivact){
    pos c;
    if (!nulo(p)){
        int grado=1;
        c=hijomasizq(p,a);
       if (!nulo(c) && nivact<k2 && nivact>k1 && info(c,a)>nivact) {
        while (hermanoder(c,a)!=NULL){
            grado++;
            c=hermanoder(c,a);
        }
        if (info(c,a)>nivact && grado>1)
            return 1+verifica(a,hijomasizq(p,a),k1,k2,nivact+1)+verifica(a,hermanoder(p,a),k1,k2,nivact);
        else
            return verifica(a,hijomasizq(p,a),k1,k2,nivact+1)+verifica(a,hermanoder(p,a),k1,k2,nivact);
       }
      else
            if (!nulo(c))
                return verifica(a,hijomasizq(p,a),k1,k2,nivact+1)+verifica(a,hermanoder(p,a),k1,k2,nivact);
            else return 0;


    }
    else return 0;



}


















