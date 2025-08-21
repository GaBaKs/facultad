#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pilas.h>
typedef struct nodito{
    char dest;
    struct nodito * sig;}nodito;
typedef nodo * sublista;

typedef struct nodoD{
    char est;
    char nombre[31];
    sublista sub;
    struct nodoD *ant,*sig;}nodoD;
typedef nodoD * TnodoD;

typedef struct{
    TnodoD pri,ult;}TlistaD;
void actlista()



int main(){
TlistaD LD;


}

void actlista(TlistaD *LD){
 sublista ant,act;
 sublista nuevo2;
 TnodoD antD,actD;
 TnodoD nuevo;
 FILE *arch;
 char cod,codes;
 char nombre[31];
 int cantp;

    if ((arch=fopen("INICIAL.txt","r"))==NULL)
        printf("hubo un error en la apertura del archivo");
    else{
         fscanf("%c %s %d",cod,nombre,cantp);
         while (!feof(arch)){
                antD=NULL;
                if ((LD->pri->est)>cod){
                    nuevo=(TnodoD) malloc (sizeof(nodoD));
                    nuevo->est=cod;
                    strcpy(nuevo->nombre,nombre);
                    nuevo->ant=NULL;
                    nuevo->sub=NULL;
                    LD->pri->ant=nuevo;
                    nuevo->sig=(*LD)->pri;
                    (*LD)->pri=nuevo;
                }
                else
                    if (LD->ult->est<cod){
                        nuevo=(TnodoD) malloc (sizeof(nodoD));
                        nuevo->est=cod;
                        strcpy(nuevo->nombre,nombre);
                        nuevo->sig=NULL;
                        nuevo->sub=NULL;
                        nuevo->ant=(*LD).ult;
                        LD->ult->sig=nuevo;
                        LD->ult=nuevo;
                    }
                    else{
                        antD=NULL;
                        actD=LD->pri;
                        while (actD!=NULL && actD->est<=cod){
                            antD=actD;
                            actD=actD->sig;
                        }
                        if (antD->est!=cod){
                            nuevo=(TnodoD) malloc (sizeof(nodoD));
                            nuevo->est=cod;
                            nuevo->sub=NULL;
                            strcpy(nuevo->nombre,nombre);
                            nuevo->sig=actD;
                            antD->sig=nuevo;
                        }
                    }

                for (int i=0;i<cantp;i++){
                    fscanf("%c",codes);
                    nuevo2=(sublista) malloc (sizeof(nodito));
                    actD=LR->pri;
                    nuevo2->dest=codes;
                    nuevo2->sig=NULL;
                    while (actD->est!=cod)
                        actD=actD->sig;
                    if (actD->sub==NULL)
                        actD->sub=nuevo2;
                    else{
                        act=actD->sub;
                        while (act->sig!=NULL)
                            act=act->sig;
                        act->sig=nuevo2;
                    }
                }
            fscanf("%c %s %d",cod,nombre,cantp);
         }

    }
    close(arch);
}

void viajetren(TlistaD *LD){
    Tpila Pila;
    TnodoD tren;
    sublista ant,sig;
    TelementoP aux;
    int D,cap;
    printf("ingrese la distancia entre cada estacion\n");
    scanf("%d",D);
    printf("ingrese la capacidad del tren\n");
    scanf("%d",cap);
    IniciaP(&Pila);
    tren=LD->pri;
    while
}


