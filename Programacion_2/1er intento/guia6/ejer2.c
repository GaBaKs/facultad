#include <stdio.h>
#include <stdlib.h>

typedef struct nodo{
    int dato;
    struct nodo *sig;}nodo;

    typedef struct nodo * Tlista;

void generalista(Tlista *L,int arreglo[]);
void muestralista(Tlista L);
int main(){
    int arreglo[5];
    Tlista L= NULL;
    arreglo[0]=1;
    arreglo[1]=2;
    arreglo[2]=3;
    arreglo[3]=5;
    arreglo[4]=4;

    generalista(&L,arreglo);
    muestralista(L);

   return 0;
}


   void generalista(Tlista *L,int arreglo[5]){
    Tlista aux;
    for(int i=0;i<5;i++){
        aux = (Tlista) malloc (sizeof(nodo));
        aux->dato = arreglo[i];
        if (*L == NULL){
            aux->sig = NULL;
            *L=aux;   // como en la lista no hay nada, aux pasa a ser el 1er elemento de la lista
        }
        else {
                aux->sig=*L;
                *L=aux;
        }
    }

}

 void muestralista(Tlista L){
    Tlista aux;
    printf("mostrar lista al reves\n");
    aux=L;
    while (aux != NULL){
        printf("%d",aux->dato);
        aux=aux->sig;
    }
 }
