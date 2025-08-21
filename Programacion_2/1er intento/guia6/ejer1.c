#include <stdio.h>


typedef struct nodo{
    car letra;
   struct nodo * sig;}nodo;

typedef struct nodo * Tlista;



int main(){
    Tlista L;
    int k;
    printf("ingrese un valor de k\n");
    scanf("%d",&k);
    esvocal(L,k);

return 0;
}


void esvocal(Tlista L,int k){
    int cont=0;
    int i=0;
    Tlista aux;
    aux=L;
    while (aux != NULL && i<k){
        if (aux->dato=='a')
             cont++;
        i++;
        aux=aux->sig;
    }

}
