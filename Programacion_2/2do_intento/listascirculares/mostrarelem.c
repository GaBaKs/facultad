#include <stdio.h>
#include <stdlib.h>


typedef struct nodo{

    int dato;
    struct nodo * sig;}nodo;


typedef struct nodo * TlistaC;


int main(){


TlistaC LC,auxC;

    if (LC!=NULL)
            auxC=LC->sig;
    while (auxC!=LC){
        printf("%d \t",auxC->dato);
        auxC=auxC->sig;
    }
    printf("%d \t",auxC->dato);


}

void elimina (TlistaC * LC,char palabra[15]){
    Tlista ant,aux;
  if (*LC!=NULL)
    if (strcmp(*LC->dato,palabra)>=0){
        if (strcmp(*LC->dato,palabra)==0)
            *LC->cant--;
         if (*LC->cant==0){
                ant=*LC;
            if (*LC=*LC->sig){           // es unico
                *LC=NULL;
             else
                *LC=*LC->sig;
            free(ant);
         }
    }
        else printf("la palabra no se encuentra en la lista");
    else{
        TlistaC auxC=(*LC)->sig;
        antC=*LC;
        while (auxC!=*LC && strcmp(auxC->dato,palabra)<0){
            antC=auxC;
            auxC=auxC->sig;

        }
        if (strcmp(aux->dato,palabra)==0)
            aux->cant--;
        if (aux->cant==0);
            ant->sig=act->sig;
            free(act);



    }




}
