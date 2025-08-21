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
int recorre(arbol a,int niv);


int main(){
 arbol a;
 int x;
 int niv=1;
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

printf("la cantidad de nodos en niveles impares es de %d",recorre(a,niv));


 return 0;

}

void addnodo(arbol* a, TElememtoA e) {
    *a = (arbol)malloc(sizeof(nodo));
    (*a)->dato = e;
    (*a)->izq = NULL;
    (*a)->der = NULL;
}



int recorre(arbol a,int niv){

    if (a!=NULL){
        if (niv % 2 == 1){
                printf("%d\t",a->dato);
            return 1+recorre(a->der,niv)+recorre(a->izq,niv+1);
        }
        else return recorre(a->der,niv)+recorre(a->izq,niv+1);
    }
    else return 0;
}




