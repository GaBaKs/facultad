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
void asd(arbol a,int *max,int *lvmax,int *min,int *lvmin,int niv);
int main(){
 arbol a;
 int max,lvmax,min,lvmin,niv;
 int x;
 /* carga arbol ejemplo. Ej 1 */
 addnodo(&a, 5);
 addnodo(&a->izq, 8);
 addnodo(&a->izq->izq, 3);
 addnodo(&a->izq->der, 6);

 addnodo(&a->der, 4);
 addnodo(&a->der->izq, 1);
 addnodo(&a->der->izq->der, 2);

 asd(a,0,0,1000,12,1);
 printf("la clave menor de grado dos es %d y esta en el nivel %d\n",min,lvmin);
 printf("la clave mayor de grado dos es %d y esta en el nivel %d\n",max,lvmax);

 return 0;

}

void addnodo(arbol* a, TElememtoA e) {
    *a = (arbol)malloc(sizeof(NODO));
    (*a)->dato = e;
    (*a)->izq = NULL;
    (*a)->der = NULL;
}

void asd(arbol a,int *max,int *lvmax,int *min,int *lvmin,int niv){
    if (a!=NULL)
        asd(a->izq,&max,&lvmax,&min,&lvmin,++niv);
        if (a->izq!=NULL && a->der!=NULL){
            if (a->dato>(*max)){
                *max=a->dato;
                *lvmax=niv;
            }
            else
            if (a->dato<(*min)){
                *min=a->dato;
                *lvmin=niv;

            }
        }
            asd(a->der,&max,&lvmax,&min,&lvmin,++niv);
}

