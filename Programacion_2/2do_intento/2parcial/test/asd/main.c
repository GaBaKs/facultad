#include <stdio.h>
#include <stdlib.h>

typedef int TElememtoA;

typedef struct nodo{
    TElememtoA dato;
    struct nodo * izq,*der;}nodo;
typedef struct nodo * arbol;

void addnodo(arbol* a, TElememtoA e);
int contclaves(arbol a);


int main(){
    int k;
    int x;
    arbol a;
 addnodo(&a, 40);
 addnodo(&a->izq, 20);
 addnodo(&a->der, 50);
 addnodo(&a->der->der, 37);

addnodo(&a->izq->izq,3);
addnodo(&a->izq->izq->der,3);
addnodo(&a->izq->izq->der->der,2);
//addnodo(&a->izq->izq->der->der->der,1);
//addnodo(&a->izq->izq->der->der->der->izq,4);
//addnodo(&a->izq->izq->der->der->der->izq->der,3);

 addnodo(&a->der->der->izq, 10);
 addnodo(&a->der->der->izq->der, 12);
 //addnodo(&a->der->der->izq->der->der, 14);
 //addnodo(&a->der->der->izq->der->der->der, 23);
 //addnodo(&a->der->der->izq->der->der->der->izq, 70);
 addnodo(&a->der->der->izq->der->izq, 33);
 addnodo(&a->der->der->izq->der->izq->der, 53);
 //addnodo(&a->der->der->izq->der->izq->der->der, 54);

   // printf("cant de claves que cumplen: %d\n",contclaves2(a));
    //printf("cant de claves que cumplen: %d\n",contclaves(a));
    printf("la cant de nodos que cumplen es %d",gradoparbosque(a));
    return 0;
}


int gradoparbosque(arbol a){
    int gr=0;
    while (a!=NULL){
        gr+=gradoarbol(a);
        a=a->der;
    }
    return gr;

}
int gradoarbol(arbol a){
    arbol hijo;
    int gr=0;
    int contnodos=0;
  if (a!=NULL){
    hijo=a->izq;
    while (hijo!=NULL){
        gr++;
        contnodos+=gradoarbol(hijo);
        hijo=hijo->der;
    }
    if (gr!=0 && gr%2==0)
        return contnodos+1;
    else
        return contnodos;
  }
  else return contnodos;
}

























/*
int contclaves2(arbol a){                    //tarde 9:05 en resolver y 2:10 revisando
arbol aux;
int acumact=0;
 if (a!=NULL){
   if (a->izq!=NULL){
    printf("a= %d",a->dato);
    aux=a->izq;
    while (aux!=NULL){
        acumact+=aux->dato;
        printf("sumo %d\t",aux->dato);
        aux=aux->der;
    }
    if (a->dato>acumact)
        return contclaves2(a->izq)+contclaves2(a->der);
    else
        return 1+contclaves2(a->izq)+contclaves2(a->der);
   }
   else return contclaves2(a->izq)+contclaves2(a->der);
 }
 else return 0;

}
int contclaves(arbol a){
    arbol hijo;
    int suma=0;
    int cont=0;
    if (a!=NULL){
            printf("a %d",a->dato);
        if (a->izq==NULL)
            return 0;
        else{
            hijo=a->izq;
            while (hijo!=NULL){
                suma+=hijo->dato;
                cont=contclaves(hijo);
                printf("sumo %d\t",hijo->dato);
                hijo=hijo->der;
            }
            if (a->dato<suma){
                    printf("CUMPLE %d",a->dato);
                return cont+1;
            }
            else
                return cont;


        }
    }
    else return cont;


}
*/
void addnodo(arbol* a, TElememtoA e) {
    *a = (arbol)malloc(sizeof(nodo));
    (*a)->dato = e;
    (*a)->izq = NULL;
    (*a)->der = NULL;
}

