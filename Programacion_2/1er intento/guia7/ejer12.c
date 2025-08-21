#include <stdio.h>
#include <stdlib.h>


typedef int TElementoA;

typedef struct nodo{
    TElementoA dato;
    struct nodo *izq,*der;}nodo;

typedef nodo * arbol;

void addnodo(arbol* a, TElementoA e);
int recorre(arbol a,int A,int B);

int main(){
    arbol a;
    int A,B;
       int x;
    addnodo(&a, 30);
    addnodo(&a->izq, 17);
    addnodo(&a->izq->izq, 8);
    addnodo(&a->izq->der, 18);
    addnodo(&a->der, 40);
    addnodo(&a->der->izq, 36);
    addnodo(&a->der->izq->der, 50);

    printf("ingrese un valor de a\n");
    scanf("%d",&A);
    printf("ingrese un valor de b\n");
    scanf("%d",&B);
    printf("la cantidad de elementos entre %d y %d es de %d",A,B,recorre(a,A,B));


    return 0;
}

void addnodo(arbol* a, TElementoA e) {
    *a = (arbol)malloc(sizeof(nodo));
    (*a)->dato = e;
    (*a)->izq = NULL;
    (*a)->der = NULL;
}

int recorre(arbol a,int A, int B){
    if (a!=NULL)
        if (a->dato>B)
            return recorre(a->izq,A,B);
        else if (a->dato<A)
            return recorre(a->der,A,B);
        else
            if (a->dato<B && a->dato>A)
             return 1+recorre(a->izq,A,B)+recorre(a->der,A,B);
            else return recorre(a->izq,A,B)+recorre(a->der,A,B);
}














