#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "colas.h"
#define ST30 31
#define ST7 8


typedef struct nodito{
    char codprod[ST7];
    int dest;
    int cantprodsol;
    int cantprodenv;
    struct nodito * sig;}nodito;
 typedef struct nodito * sublista;   



typedef struct nodoC{
    int idpuesto;
    char nombreprep[ST30];
    int cantprosol;
    sublista sub;
    struct nodoC * sig;}nodoC;
typedef struct nodoC* TlistaC;


typedef struct nodo{
    int idrobot;
    int idpuesto;
    Tcola C;
    struct nodo * sig;}nodo;

typedef struct nodo * Tlista;    



//inciso a

void actualizaLC(TlistaC *LC){
    FILE * arch;
    TlistaC antC,actC,nuevo;
    sublista antS,actS;

    if ((arch=fopen("PEDIDOS.TXT","r"))==NULL)
        printf("ocurrio un problema al abrir el archivo");
    else{
        while (!feof(arch)){
            nuevo=(TlistaC) malloc sizeof(nodoC);
           fscanf(arch,"%d %s %d",nuevo->idpuesto,nomprepact,&cantprod);
           if (*LC==NULL){
             nuevo->idpuesto=idpuestoact;
             strcpy(nuevo->nomprep,nomprepact);
             nuevo->cantprodsol=cantprod;
             for (i=0;i<cantprod;i++){
                fscanf(arch,"%d %s %d",&destact,codprod,&cantprodact);



             }
           }


    }



}
