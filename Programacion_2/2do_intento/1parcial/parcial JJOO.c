#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define ST8 9
#define ST4 5
#define ST3 4

typedef struct nodito{

    int puntos;
    struct nodito * sig;}nodito;
 typedef struct nodito * Sublista;


typedef struct nodo{
    ST8 codgim;
    ST4 codnac;
    ST3 codis;
    Sublista sub;
    struct nodo * sig;}nodo;

typedef struct nodo * Tlista;

int main(){



}

void creaarchivo(Tlista L,ST4 codnac){

    Tlista auxL=L;
    Sublista antS,auxS;
    FILE * arch;
    int min,max,suma=0;
    int cont=0;


    if ((arch=fopen("DEPURAN.TXT","w"))==NULL)
        printf("ocurrio un error con la apertura del archivo");
    else{
        while (auxL!=NULL && strcmp(auxL->codnac,codnac)<=0){

            if (strcmp(auxL->codnac,codnac)==0){
                auxS=auxL->sub;
                min=auxS->puntos;                          //guardo el minimo xq asumo que esta ordenada la lista


                auxL->sub=auxL->sub->sig;
                free(auxS);
                auxS=auxL->sub;
                antS=NULL;
                while (auxS->sig!=NULL){
                        antS=auxS;
                        auxS=auxS->sig;
                }
                max=auxS->puntos;
                ants->sig=NULL;
                free(auxS);
                fprintf(arch,"%s %d %d \n",L->codg,min,max);
                suma=suma+min+max;
                cont+=2;
            }
            auxL=auxL->sig;

        }
            if (cont!=0){
                printf("no hayu gimnastas de la nacionalidad dada");
            else
                printf("el promedio de todas las puntuaciones depuradas es %5.2f ",(float)suma/cont);


            }

    Close(arch);
    }




}



