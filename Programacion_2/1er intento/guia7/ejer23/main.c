#include <stdio.h>
#include <stdlib.h>
typedef int TElememtoA;
typedef struct nodo{
        TElememtoA dato;
        struct nodo *izq;
        struct nodo *der;
} nodo;
typedef nodo * arbol;

void addnodo(arbol* a, TElememtoA e);
int gradoarbol(arbol a,int* gradomax,int grado);

int main(){
 arbol a;
 int x;
 /* carga arbol ejemplo. Ej 1 */
 a=NULL;
 addnodo(&a, 30);
 addnodo(&a->izq, 40);
 addnodo(&a->izq->izq, 20);
 addnodo(&a->izq->der, 50);

 addnodo(&a->izq->der->der, 37);
 addnodo(&a->izq->der->der->izq, 10);
 addnodo(&a->izq->der->der->izq->der, 12);
 addnodo(&a->izq->der->der->izq->der->der, 14);
 addnodo(&a->izq->der->der->izq->der->der->der, 23);
 addnodo(&a->izq->der->der->izq->der->der->der->izq, 70);
 addnodo(&a->izq->der->der->izq->der->izq, 33);
 addnodo(&a->izq->der->der->izq->der->izq->der, 53);
int gradomax=0;
printf("el grado del arbol es de %d",gradoarbol(a,&gradomax,0));
 return 0;

}

void addnodo(arbol* a, TElememtoA e) {
    *a = (arbol)malloc(sizeof(nodo));
    (*a)->dato = e;
    (*a)->izq = NULL;
    (*a)->der = NULL;
}

int gradoarbol(arbol a,int* gradomax,int grado){
    if (a!=NULL){
           printf("grado %d\n",grado);
           grado=1+gradoarbol(a->der,gradomax,grado);
        if (a->izq!=NULL)
                return gradoarbol(a->izq,gradomax,0);
    }
    else return (*gradomax>grado)? *gradomax:grado;

 }
