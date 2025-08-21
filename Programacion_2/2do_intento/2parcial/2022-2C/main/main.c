#include <stdio.h>
#include <stdlib.h>

typedef char TElememtoA;

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
    printf("ingrese k");
    scanf("%d",&k);
      addnodo(&a, 30);
 addnodo(&a->izq, 40);
 addnodo(&a->izq->izq, 20);
 addnodo(&a->izq->der, 50);
 addnodo(&a->izq->der->der, 37);
 addnodo(&a->izq->der->der->izq, 10);
 addnodo(&a->izq->der->der->izq->der, 40);
 addnodo(&a->izq->der->der->izq->der->der, 14);
 //addnodo(&a->izq->der->der->izq->der->der->der, 23);
 //addnodo(&a->izq->der->der->izq->der->der->der->izq, 70);
 //addnodo(&a->izq->der->der->izq->der->izq, 33);
 //addnodo(&a->izq->der->der->izq->der->izq->der, 53);

    cumple(a,k);
    return 0;
}



void cumple(arbol a, int k){
    int niv=1;
    if (a==NULL)
        printf("el arbol esta vacio");
    else
    if (verifica(a,niv,k))
        printf("el arbol dado cumple con lo pedido");
     else
        printf("el arbol dado no cumple con lo pedido");
}

int verifica(arbol a,int niv, int k){
    if (a!=NULL){
        if (niv==k-1){      // entro a padre
            if (a->izq!=NULL){      // tiene hijo a izquierda
                    if (a->der!=NULL){
                        if (a->der->dato>a->izq->dato && a->izq->dato>a->dato){
                            return 1;
                        }
                        else
                            return 0;
                    }
                     else
                        if (a->izq->dato>a->dato)
                            return 1;
                        else
                            return 0;

            }
            else
                return 1;
        }
        else
            return verifica(a->izq,niv+1,k)&&verifica(a->der,niv+1,k);

        }
        else return 1;

}

void addnodo(arbol* a, TElememtoA e) {
    *a = (arbol)malloc(sizeof(nodo));
    (*a)->dato = e;
    (*a)->izq = NULL;
    (*a)->der = NULL;
}




int clavemayor(arbol a,pos p,int G){            //
    pos c;int gr=0;int submax;int mayor=-1
         if (!nulo(p)){
            c=hijomasizq(p,a);
            while (!nulo(c)){
                gr++;
                submax=clavemayor(a,c,G);
                if (submax>mayor)
                    mayor=submax;
                c=hermanoder(c,a);
            }
            if (gr==G || gr==2*G && info(p,a)>mayor)
                mayor=info(p,a);
         }
        return mayor;
}



int subgrafo(int mat[][N],int N,int i,int j){
        if (j>i){
            if (mat[i][j]==1)
                if (mat[j][i]==1)
                    return subgrafo(mat,N,i,j-1);
                else
                    return 0;
            else
                return subgrafo(mat,N,i,j-1);
        }
        else
            if(i>0)
                return subgrafo(mat,N,i-1,N);
            else
                return 1;

    }


int subgrafo(mat[][N],int N){
    int i,j;
    j=N;
    i=N;
    int flag=0;
   while (i>=0 && !flag){
    while (j>i && !flag)){
        if (mat[i][j]==1){
            if (mat[j][i]!=1)
                flag=1;
        }
        j--;
    }
    j=N;
    i--;
   }
    return flag;


    }


















