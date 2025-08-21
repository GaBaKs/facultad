#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define ST30 31
#define ST10 11
#define ST20 21


typedef struct nodo{
    ST30 nomR;
    Tpila P;
    struct nodo * sig;}nodo;
typedef struct nodo * Tlista;

typedef struct nodito{
    ST30 nomR;
    float cant;
    ST10 unidad;
    struct nodito * sig;}nodito
typedef struct nodito * Tsublista;

typedef struct nodoD{

    ST10 rubro;
    ST20 noming;
    Tsublista sub;
    struct nodoD * sig,*ant;}nodoD;
typedef struct nodoD * PnodoD;
typedef struct{
    PnodoD pri,ult;}TlistaD;



int main(){

    }


void creaLD(TlistaD *LD,Tlista L,int * contr,int * menoring){

    PnodoD auxD,nuevoD;
    Tsublista auxS,nuevoS;
    TelementoP datoP;
    Tlista auxL;
    int conting;
    *menoring=1000;
    *contr=0;
    auxL=L;
    while (auxL!=NULL){
        (*contr)++;
        contint=0;
        while (!vacia(auxL->P)){
            conting++;
            SacaP(&(auxL->P),&datoP);
            if (LD->pri==NULL){               //no hay nada en la LD
                   nuevoD=(PnodoD) malloc sizeof(nodoD);
                   strcpy(nuevoD->noming,datoP.noming);
                   strcpy(nuevoD->rubro,datoP.rubro);
                   nuevoS=(Tsublista) malloc sizeof(nodito);
                   nuevoS->cant=datoP.cant;
                   strcpy(nuevoS->nomR,auxL->nomR);
                   strcpy(nuevoS->unidad,datoP.unidad);
                   nuevoD->sub=nuevoS;
            }
            else{
                if (LD->pri )



            }

        }




    }






}

