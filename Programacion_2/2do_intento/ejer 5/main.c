#include <stdio.h>
#include <stdlib.h>
#include "pilas.h"
#include "colas.h"



typedef struct nodo{
    TCola dato;
    struct nodo * sig;}nodo;

typedef struct nodo * Tlista;

void cargalista(Tlista * L);
void generapila(Tlista L,TPila *P);
TElementoP maximocola(TCola C);
void muestrapila(TPila P);


// abro archivo
//cargo datos a la cola
// miro si la lista esta vacia
// si esta vacia creo 1er nodo, sino sigo hasta el ultimo
// releo arch y reinicio ciclo

int main()
{
TPila P;
Tlista L=NULL;
cargalista(&L);
generapila(L,&P);
muestrapila(P);
return 0;
}

void cargalista(Tlista *L){
    FILE * arch;
    int n;
    TElementoC dato;
    Tlista aux,aux2;
    int contcola=1;
    TCola colaux;
    if ((arch=fopen("datoscola.txt","r"))==NULL)
        printf("error al abrir el archivo");
    else{
        fscanf(arch,"%d",&n);
        while (!feof(arch)){
            IniciaC(&colaux);
            printf("cola numero: %d \n",contcola);
            contcola++;
            for (int i=0;i<n;i++){
                dato= rand() % 21;
                printf("%d \t",dato);
                poneC(&colaux,dato);
            }
            printf("\n");
           aux = (Tlista) malloc (sizeof(nodo));
           aux->dato=colaux;
           aux->sig=NULL;
           if (*L==NULL){
            *L=aux;
           }
           //si la lista no esta vacia
           else{
                aux2=*L;
                while (aux2->sig!=NULL)
                    aux2=aux2->sig;
                aux2->sig=aux;
           }
           fscanf(arch,"%d",&n);
        }
     fclose(arch);
    }
}

TElementoP maximocola(TCola C){
    int max=-200;
    TElementoC aux;
   while (!VaciaC(C)){
    sacaC(&C,&aux);
    if (max<aux)
        max=aux;
   }
    return max;
}

void generapila(Tlista L,TPila * P){
    TElementoP auxP;
    IniciaP(P);
    while (L!=NULL){
        auxP=maximocola(L->dato);
        printf("%d auxp\t",auxP);
        poneP(P,auxP);
        L=L->sig;
    }

}

void muestrapila(TPila P){

    TElementoP aux;
    if (!VaciaP(P)){
        sacaP(&P,&aux);
        muestrapila(P);
        printf("%d muestra \t",aux);
    }

}
