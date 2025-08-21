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

int main(){
 arbol a;
 int x;
 addnodo(&a, 40);
 addnodo(&a->izq, 20);
 addnodo(&a->der, 50);
 addnodo(&a->der->der, 37);
/*
addnodo(&a->izq->izq,3);
addnodo(&a->izq->izq->der,3);
addnodo(&a->izq->izq->der->der,2);
addnodo(&a->izq->izq->der->der->der,1);
addnodo(&a->izq->izq->der->der->der->izq,4);
addnodo(&a->izq->izq->der->der->der->izq->der,3);

*/

 addnodo(&a->der->der->izq, 10);
 addnodo(&a->der->der->izq->der, 12);
 //addnodo(&a->der->der->izq->der->der, 14);
 //addnodo(&a->der->der->izq->der->der->der, 23);
 //addnodo(&a->der->der->izq->der->der->der->izq, 70);
 addnodo(&a->der->der->izq->der->izq, 33);
 addnodo(&a->der->der->izq->der->izq->der, 53);
 //addnodo(&a->der->der->izq->der->izq->der->der, 54);

 if (flag(a))

  printf("cumple");
  else
    printf("no cumple\t");


 verificabosque(a);
 return 0;
}
int comp(arbol a, int max){
  int x;
  if(a!=NULL){
    x = gr(a->izq);
    if(x>max)
      return 0;
    else
      return comp(a->izq,max)&&comp(a->der,max);
  }
  else
    return 1;
}

int verifica(arbol a){
    int gradoraiz=grado(a->izq);
    int gradomax=gradoraiz;
    gradomaximo(a->izq,&gradomax,gradoraiz);
    if (gradoraiz==gradomax)
            return 1;
    else return 0;

}

