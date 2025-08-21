#include <stdio.h>
#include <stdlib.h>

typedef struct nodo{
    int dato;
    struct nodo * sig;}nodo;

typedef struct nodo * Tlista;

void generalista(Tlista *L,int arreglo[]);
void mostrarlista(Tlista L);




int main(){
    int arreglo[5];
    Tlista L= NULL;
    arreglo[0]=1;
    arreglo[1]=2;
    arreglo[2]=3;
    arreglo[3]=5;
    arreglo[4]=4;
    generalista(&L,arreglo);
    mostrarlista(L);
    return 0;
}

 void generalista(Tlista *L,int arreglo[5]){
    Tlista aux,actual;
    for (int i=0;i<5;i++){
        aux = (Tlista) malloc (sizeof(nodo));
        aux->dato=arreglo[i];
            aux->sig=NULL;
        if (*L==NULL)
            *L=aux;

        else {
            actual = *L;
            while (actual->sig != NULL){
                actual=actual->sig;
            }
            actual->sig=aux;
        }
    }
 }
void mostrarlista(Tlista L){
    Tlista aux;

    while (L != NULL){
        aux=L;
        printf("%d",aux->dato);
        L=L->sig;
    }

}
