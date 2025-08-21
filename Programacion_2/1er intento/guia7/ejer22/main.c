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
int altura(arbol a);

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

printf("la cantidad de nodos en niveles impares es de %d",altura(a));


 return 0;

}

void addnodo(arbol* a, TElememtoA e) {
    *a = (arbol)malloc(sizeof(nodo));
    (*a)->dato = e;
    (*a)->izq = NULL;
    (*a)->der = NULL;
}



/*int altura(arbol a, int alt){
    if (a==NULL)
            return alt-1;
    else{
        return (altura(a->izq,alt+1)<altura (a->der,alt))? altura(a->der,alt):altura(a->izq,alt+1);
    }
}
*/

int altura(arbol a) {
    if (a == NULL)
        return 0;
    else {
        int altizq = 1 + altura(a->izq);
        int altder = altura(a->der);
        return (altizq > altder)?altizq:altder;
    }
}
