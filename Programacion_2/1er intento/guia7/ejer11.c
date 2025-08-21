#include <stdio.h>
#include <stdlib.h>


typedef int TElementoA;
typedef struct nodo{
    TElementoA dato;
   struct nodo * izq,*der;}nodo;

typedef nodo * arbol;


void addnodo(arbol* a, TElementoA e);
int recorre(arbol a);

int main(){
    arbol a;
    int x;
 addnodo(&a, 30);
 addnodo(&a->izq, 17);
 addnodo(&a->izq->izq, 8);
 addnodo(&a->izq->der, 18);

 addnodo(&a->der, 40);
 addnodo(&a->der->izq, 36);
 addnodo(&a->der->izq->der, 50);

    printf("el valor minimo del ABB es %d",recorre(a));
    return 0;
}

void addnodo(arbol* a, TElementoA e) {
    *a = (arbol)malloc(sizeof(nodo));
    (*a)->dato = e;
    (*a)->izq = NULL;
    (*a)->der = NULL;
}

int recorre(arbol a){
      if (a!=NULL)
        if (a->izq!=NULL)
            return 0+recorre(a->izq);
        else
            return a->dato;
}


