#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct nodo{
    char dato[20];
    int cont;
 struct nodo * sig;}nodo;

typedef struct nodo * Tlista;

void generalista(Tlista *L);
void muestralista(Tlista L);



int main(){
    Tlista L;
    generalista(&L);
    muestralista(L);
    return 0;
}




void generalista(Tlista *L){
    FILE *arch;
    Tlista aux;
    Tlista recorre,ant;
    *L=NULL;
   if ((arch=fopen("ejer3.txt","r"))==NULL)
        printf("fallo al abrir el archivo.");
   else {
       aux = (Tlista) malloc (sizeof(nodo));
        while (feof(arch)==0){
            fscanf(arch,"%s",aux->dato);
            if (*L==NULL || strcmp(aux->dato,(*L)->dato)<0){    // cambio el 1er nodo o lo creo
                aux->sig=*L;
                aux->cont=1;
                *L=aux;
                aux = (Tlista) malloc (sizeof(nodo));
            }
         else {     //cambio otro nodo no se cual
                recorre=*L;  //analizar
                ant=NULL;
                while ((recorre != NULL && strcmp(recorre->dato,aux->dato)<0)){ //el dato a ingresar es mas chico que el nodo actual
                    ant=recorre;
                    recorre=recorre->sig;
                }
                if (recorre!=NULL){
                    if (strcmp(ant->dato,aux->dato)==0){
                        ant->cont++;
                    printf("contador: %d",ant->cont)
                }
                else {
                            aux->cont=1;
                            aux->sig=recorre;
                            ant->sig=aux;
                            aux = (Tlista) malloc (sizeof(nodo));
                    }


         }
        }
  fclose(arch);
}
}
void muestralista(Tlista L){
    printf("muestra lista:");
 while (L != NULL){
    printf("palabra: %s apariciones: %d \n",L->dato,L->cont);
    L=L->sig;

 }


}


