#include <stdio.h>
#include <stdlib.h>
#include "pilas.h"

void generapila(TPila* pila,int i);
void inviertepila(TPila* pila,TElementoP x,int i);

int main(){
    TPila pila;
    TElementoP x;
    int i;
    IniciaP(&pila);
    printf("cuantos datos quiere ingresar a la pila\n");
    scanf("%d",&i);
    generapila(&pila,i);
    inviertepila(&pila,x,i);
return 0;
}


void generapila(TPila* pila,int i){
    TElementoP aux;
   if (i>0){
        printf("ingrese el valor a ingresar a la pila\n");
        scanf("%d",&aux);
        poneP(pila,aux);
        generapila(pila,i-1);
   }
  else printf("termino la carga de la pila goood \n");
}

void inviertepila(TPila* pila,TElementoP x,int i){
        if (i>0){
            sacaP(pila,&x);
            printf("a");
            printf("ida %d \n",x);
            inviertepila(pila,x,i-1);
            x = -x;
            poneP(pila,x);
            printf("vuelta %d \n",consultaP(*pila));
        }
}
