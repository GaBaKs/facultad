#include <stdio.h>
#include <stdlib.h>
typedef int TelementoA;
typedef struct nodo{
    TelementoA dato;
    struct nodo * izq;
    struct nodo *der;

}nodo;

typedef struct nodo * arbol;

void inserta(arbol *a,TelementoA X);



int main(){
    arbol a;
    TelementoA X=10;
    a=NULL;

    while (X!=0){
        printf("ingrese un valor de X\n");
        scanf("%d",&X);
        if (X!=0)
         inserta(&a,X);
    }
    recorre(a);
    return 0;
}


void recorre(arbol a){
    if (a!=NULL){
        recorre(a->izq);
        printf("%d\n",a->dato);
        recorre(a->der);
    }
}

void inserta(arbol *a,TelementoA X){
    if (*a==NULL){
        (*a)=(arbol)malloc(sizeof(nodo));
        (*a)->dato=X;
        (*a)->der=NULL;
        (*a)->izq=NULL;
    }
    else
        if (X>(*a)->dato)
            inserta(&(*a)->der,X);
        else inserta(&(*a)->izq,X);
}
