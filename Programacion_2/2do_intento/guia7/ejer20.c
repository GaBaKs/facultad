#include <stdio.h>
#include <stdlib.h>
typedef int TElememtoA;
typedef struct nodo{
        int dato;
        struct nodo *izq;
        struct nodo *der;
} NODO;
typedef NODO * arbol;

void addnodo(arbol* a, int e);

int main(){
 arbol a;
 int x;
int acum=0;
int cont=0;
float prom=0;
 int k=3;

  addnodo(&a, 30);
 addnodo(&a->izq, 40);
 addnodo(&a->izq->izq, 20);
 addnodo(&a->izq->der, 50);

 addnodo(&a->izq->der->der, 37);
 addnodo(&a->izq->der->der->izq, 10);
 addnodo(&a->izq->der->der->izq->der, 12);
 addnodo(&a->izq->der->der->izq->der->der, 14);
 //addnodo(&a->izq->der->der->izq->der->der->der, 23);
 //addnodo(&a->izq->der->der->izq->der->der->der->izq, 70);
 addnodo(&a->izq->der->der->izq->der->izq, 33);
 addnodo(&a->izq->der->der->izq->der->izq->der, 53);


printf("la cantidad de nodos en niveles impares es de %d \n",nodosimp(a,1));

promedio(a,k,&acum,&cont);

printf("la cant de claves de grado %d k es de %5.2f",k,(float)acum/cont);



 return 0;

}

void addnodo(arbol* a, TElememtoA e) {
    *a = (arbol)malloc(sizeof(NODO));
    (*a)->dato = e;
    (*a)->izq = NULL;
    (*a)->der = NULL;
}
int nodosimp(arbol a,int niv){
    if (a!=NULL && niv % 2 == 1)
        return 1+nodosimp(a->izq,niv+1)+nodosimp(a->der,niv);
    else
        if (a!=NULL)
            return nodosimp(a->izq,niv+1)+nodosimp(a->der,niv);
        else return 0;

}

int grado(arbol a){
    if (a!=NULL)
        return 1+grado(a->der);
    else return 0;
}


void promedio(arbol a,int k,int *acum,int *cont){
    if (a!=NULL){
            if (grado(a->izq)==k){
                (*acum)+=a->dato;
                (*cont)+=1;
            }
                promedio(a->izq,k,acum,cont);
                promedio(a->der,k,acum,cont);
    }
}





