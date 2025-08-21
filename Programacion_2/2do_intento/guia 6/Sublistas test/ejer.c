#include <stdio.h>
#include <stdlib.h>

typedef struct nodoL{

    char codC[15],dest[15];
    float peso;
    struct nodoL * sig;}nodo;
typedef struct nodo * TlistaL;

typedef struct nodito{
    char codC[15];
    float peso;
    struct nodito * sig;}nodito;

typedef struct nodito * Tsublista;


typedef struct nodoB{
       char codB[15],dest[15];
       float capacidad;
       Tsublista sub;
       struct nodoB * sig;}nodoB;

typedef struct nodo2* TlistaB;


int main(){



}

void envios(TlistaL *L,TlistaB LB){
    int despacho;
    TlistaL actL,antL,elim;
    TlistaB auxB;
    actL=*L;
    antL=NULL;
    float suma;
    Tsublista actS,nuevoS;
    while (actL!= NULL){
        auxB=LB;
        despacho=0;
        while (auxB!=NULL && !despacho){
            if (strcmp(auxB->dest,actL->dest)==0){
                suma=0;
                actS=auxB->sub;
                // recorro sublista
                while (actS!=NULL){
                    suma+=actS->peso;
                    actS=actS->sig;
                }
                if ((suma+actL->peso)<=auxB->capacidad){
                    nuevoS=(Tsublista) malloc sizeof(nodito);
                    strcpy(nuevoS->codC,actL->codC);
                    nuevoS->peso=actL->peso;
                    nuevoS->sig=auxB->sub;
                    auxB->sub=nuevoS;
                    despacho=1;
                }
            }
            auxB=auxB->sig;
        }
            if (despacho){
                elim=actL;
                actL=actL->sig;
                if (elim = *LC)
                    *LC=(*LC)->sig;
                else
                    antL->sig=actL;
                free(elim);
            }
            else
                antL=actL;
                actL=actL->sig;
        }
    }




