#include <stdio.h>
#include <stdlib.h>
typedef int TElememtoA;
typedef struct nodo{
        TElememtoA dato;
        struct nodo *izq;
        struct nodo *der;
} NODO;
typedef NODO * arbol;

void addnodo(arbol* a, TElememtoA e);
int sumaelem(arbol a);
int canth(arbol a);
void busca(arbol a,int z);

int main(){
 arbol a;
 int x,z;
 addnodo(&a, 5);
 addnodo(&a->izq, 8);
 addnodo(&a->izq->izq, 3);
 addnodo(&a->izq->der, 1);
 addnodo(&a->der, 4);
 addnodo(&a->der->izq, 1);
 addnodo(&a->der->izq->der,2);
 addnodo(&a->der->izq->izq,3);
printf("la suma de sus elementos es de %d \n",sumaelem(a));
printf("la cantidad de hojas es de %d \n",canth(a));
printf("ingrese un valor de Z\n");
scanf("%d",z);
busca(a,z);

 return 0;

}

int sumaelem(arbol a){
    if (a!=NULL){
        if ((a->dato % 3)==0)
            return a->dato+sumaelem(a->izq)+sumaelem(a->der);
        else return sumaelem(a->izq)+sumaelem(a->der);
    }
    else return 0;
}

int canth(arbol a){
    if (a!=NULL){
        if ((a->izq==NULL) && (a->der==NULL))
            return 1+canth(a->izq)+canth(a->der);
        else return canth(a->izq)+canth(a->der);

    }
    else return 0;

}

void busca(arbol a,int z){
    if (a!=NULL){
       busca(a->izq,z);
        if (a->dato==z)
           printf("el valor %d se encuentra en el arbol.\n",z);
        busca(a->der,z);

    }
}
void addnodo(arbol* a, TElememtoA e) {
    *a = (arbol)malloc(sizeof(NODO));
    (*a)->dato = e;
    (*a)->izq = NULL;
    (*a)->der = NULL;
}
