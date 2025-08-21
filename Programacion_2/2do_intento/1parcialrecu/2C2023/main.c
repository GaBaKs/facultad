#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define ST30 31
#define ST7 8

typedef struct nodito{
    char codp[ST7];     //se repite
    int dest;       //se repite en distintos puestos
    int prodsol;
    int prodenv;        //inicia en 0
    struct nodito * sig;}nodito;

typedef struct nodito * Sublista;

typedef struct nodoC{
    int puesto;         //ordenado no se repite
    char nombre[ST30];
    int prodtotal;
    Sublista sub;
    struct nodoC * sig;}nodoC;

typedef struct nodoC * TlistaC;

typedef struct nodo{

    int idrobot;
    int puesto;
    Tcola C;            // codp y cantdisp
    struct nodo * sig;}nodo;

  typedef struct nodo * Tlista;



void lectura(TlistaC *LC){

    TlistaC antC,actC,nuevoC;
    FILE * arch;
    int puesto,n,i;
    char nombre[ST30];
    char codprod[ST7];
    int dest,cantprod;
    if ((arch=fopen("PEDIDOS.TXT","rt"))==NULL)
        printf("error en la apertura del archivo");
    else{
        fscanf(arch,"%d %s %d",&puesto,nombre,&n);
        while (!feof(arch)){
      if (*LC!=NULL){
        if ((*LC)->puesto==puesto){     // meto en la cabeza
            for (i=0;i<n;i++){
                    fscanf(arch,"%d %s %d",&dest,codprod,cantprod);
                    metosublista(*LC,dest,codprod,cantprod);
                    (*LC)->prodtotal+=cantprod;
            }
        }
        else{


        if ((*LC)->puesto<puesto){          //ingreso a lo ultimo
            nuevoC=(TlistaC) malloc (sizeof(nodoC));
            nuevoC->puesto=puesto;
            strcpy(nuevoC->nombre,nombre);
            nuevoC->prodtotal=0;
            nuevoC->sub=NULL;
            nuevoC->sig=(*LC)->sig;
            (*LC)->sig=nuevoC;
            *LC=nuevoC;
            for (i=0;i<n;i++){
                    fscanf(arch,"%d %s %d",&dest,codprod,cantprod);
                    metosublista(*LC,dest,codprod,cantprod);
                    (*LC)->prodtotal+=cantprod;
            }
        }
         else{
            actC=(*LC)->sig;
            antC=*LC;
            while (actC!=*LC && actC->puesto<puesto){
                antC=actC;
                actC=actC->sig;
            }
            if (actC->puesto!=puesto){      // no existe nodo
                nuevoC=(TlistaC) malloc (sizeof(nodoC));
                nuevoC->puesto=puesto;
                strcpy(nuevoC->nombre,nombre);
                nuevoC->prodtotal=0;
                nuevoC->sub=NULL;
                nuevoC->sig=actC;
                antC->sig=nuevoC;
                actC=nuevoC;
            }
            for (i=0;i<n;i++){
                    fscanf(arch,"%d %s %d",&dest,codprod,cantprod);
                    metosublista(actC,dest,codprod,cantprod);
                    actC->prodtotal+=cantprod;
            }

         }

        }
        //as

      }

    fscanf(arch,"%d %s %d",&puesto,nombre,&n);
    }
    fclose(arch);
    }

}

void metosublista(TlistaC LC,int dest,char codprod[ST7],int cantprod){
    Sublista subn;
    subn=(Sublista) malloc (sizeof(nodito));
    strcpy(subn->codp,codprod);
    subn->dest=dest;
    subn->prodsol=cantprod;
    subn->prodenv=0;
    subn->sig=LC->sub;
    LC->sub=subn;

}












int main()
{
    printf("Hello world!\n");
    return 0;
}
