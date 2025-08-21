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
 int x,bol=0;
 /* carga arbol ejemplo. Ej 1 */
 addnodo(&a, 5);
 addnodo(&a->izq, 8);
 addnodo(&a->izq->izq, 3);
 addnodo(&a->izq->der, 6);

 addnodo(&a->der, 4);
 addnodo(&a->der->izq, 1);
 addnodo(&a->der->izq->der, 2);

  printf("la suma de los elementos es %d \n",sumaelem(a));
  printf("la cantidad de hojas es %d \n",canth(a));
  esta(a,9,&bol);
  if (!bol)
    printf("el valor ingresado no se encuentra");
 return 0;

}

void addnodo(arbol* a, TElememtoA e) {
    *a = (arbol)malloc(sizeof(NODO));
    (*a)->dato = e;
    (*a)->izq = NULL;
    (*a)->der = NULL;
}

int sumaelem(arbol a){
    if (a!=NULL && a->dato % 3 == 0)
        return a->dato+sumaelem(a->izq)+sumaelem(a->der);
    else
       if (a!=NULL)
         return sumaelem(a->izq)+sumaelem(a->der);
        else
            return 0;
}


int canth(arbol a){
    if (a!=NULL && a->izq==NULL && a->der==NULL)
        return 1;
    else
        if (a!=NULL)
            return canth(a->izq)+canth(a->der);
        else
            return 0;

}

void esta(arbol a,int z,int *bol){
    if (a!=NULL && a->dato==z){
        printf("el valor %d se encuentra en el arbol",z);
        *bol=1;
    }
    else
       if (a!=NULL && !(*bol)){
        esta(a->izq,z,bol);
        esta(a->der,z,bol);
       }
}



