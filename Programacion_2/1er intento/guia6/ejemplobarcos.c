#include <stdio.h>
#include <string.h>
#include <stdlib.h>


typedef struct nodo{
    char codC[15];
    char dest[15];
    float peso;
    struct nodo * sig;}nodo;
typedef nodo * TlistaC;

typedef struct nodito{
    char codC[15];
    float peso;
    struct nodito * sig;}nodito;
typedef nodito * Sublista;

typedef struct nodoB{
    char codB[15];
    char dest[15];
    float capac;
    struct nodoB * sig;
    Sublista sub;}nodoB;
typedef nodoB * TlistaB;


int main(){

Tlista L;

}



void procesoL(TlistaC *LC;TlistaB LB){

    TlistaC ant,aux,elim;
    TlistaB act;
    float suma;
    Sublista nuevo,actS;
    int despacho;
    ant=NULL;
    aux=*LC;

    while (aux!=NULL){
        despacho=0;
        act=LB;
        while (act!=NULL && !despacho){
            if (strcmp(aux->dest,act->dest)==0){
                suma=0;
                actS=act->sub;
                while (actS!=NULL){
                    suma+=actS->peso;
                    actS=actS->sig;
                }
               if (suma+aux->peso <= act->capac){
                    nuevo = (Sublista) malloc (sizeof(nodito));
                    strcpy(nuevo->codC,aux->codC);
                    nuevo->peso=aux->peso;
                    nuevo->sig=act->sub;
                    act->sub=nuevo;
                    despacho=1;
               }
            }
            act=act->sig;
        }
        if (!despacho){
            ant=aux;
            aux=aux->sig;
        }
        else {
            elim=aux;
            aux=aux->sig;
            if (elim == *LC)
                *LC=(*LC)->sig;
            else
                ant->sig=aux;
            free(elim);

        }
    }
}



}
