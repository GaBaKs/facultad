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
int verifica(arbol a);
int grado(arbol a);
int recorrearbol(arbol a);

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

    if (verifica(a))
        printf("los arboles cumplen");
    else printf("los arboles no cumplen");


 return 0;

}

void addnodo(arbol* a, TElememtoA e) {
    *a = (arbol)malloc(sizeof(nodo));
    (*a)->dato = e;
    (*a)->izq = NULL;
    (*a)->der = NULL;
}



int grado(arbol a){
    if (a!=NULL)
        return 1+grado(a->der);
    else
        return 0;
}


int recorrearbol(arbol a){
    if (a!=NULL){
        int gizq=recorrearbol(a->izq);
        int gder=recorrearbol(a->der);
        int gact=grado(a->izq);
        int max=(gizq>gder)?gizq:gder;
        return (max>gact)?max:gact;
    }
    else return 0;
}
int verifica(arbol a){
    if (a!=NULL){
        int raiz=grado(a->izq);
        int ab=recorrearbol(a->izq);
        if (raiz==ab)
            return 1&&verifica(a->der);
        else
            return 0;
    }
    else return 0;

}


// ejercicio 2

int gradocrec(arbol a,pos p,int gradoher){
    pos c;
      if (!nulo(hijomasizq(p,a)){
        int gradoact=0;
        c=hijomasizq(p,a);
        while (!nulo(c)){
            gradoact++;
            c=hermanoderecha(c,a);
        }
        if (gradoact>gradoher && nulo(hermanoder(p,a)))
            return 1;
        else
            if (gradoact>gradoher)
                return 1 && gradocrec(a,hermanoder(p,a),gradoact);
            else
                return 0;
      }
    else return 1;  

}

int verifica(arbol a,pos p){
    if (!nulo(p))
        return verifica(a,hijomasizq(p,a)) || verifica (a,hermanoder(p,a)) || gradorec(a,hijomasizq(p,a),0) || gradorec(a,hermanoder(p,a),0));
    else return 0;
}



int gradocrec(arbol a, pos p, int gradoher){
    int gradoact=0;
    pos c;
    if(!nulo(p)){
        c=hijomasizq(p,a)
        while (!nulo(c)){               // saco grado de el nodo p
            gradoact++;
            c=hermanoder(c,a);

        }
        if (gradoact>gradoher){
            return 1 && gradocrec(a,hermanoder(p,a),gradoact)
        }

    }

}





// ejer 3


int nodos(int mat[MAX][MAX],int N,int i, int j,int ent,int sal)

    if (i<N)
        if (j<n)
            if (mat[i][i]==0){
                if (mat[i][j]==1)
                    sal++;
                if (mat[j][i]==1)
                    ent++;
                return nodos(mat,N,i,j+1,ent,sal);
            }
            else
                    return nodos(mat,N,i+1,0,0,0);
       else
            if (ent==sal)
                return 1+nodos(mat,N,i+1,0,0,0);
            else
                return nodos(mat,N,i+1,0,0,0);
   else
        return 0;










