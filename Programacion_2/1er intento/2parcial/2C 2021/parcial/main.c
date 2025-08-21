#include <stdio.h>
#include <stdlib.h>
#define MAX 100


typedef struct nodo{
        int dato;
        struct nodo *izq;
        struct nodo *der;
} NODO;
typedef NODO * arbol;



void claves(arbol a,int cmen,int cmay,int nmen,int nmay);
void addnodo(arbol* a, int e);
void clavemenor(arbol a,int * cmen,int *nmen,int nivact);
void clavemayor(arbol a, int *cmay,int *nmay,int nivact);




int main(){
    arbol a;
    int x;
    a=NULL;




 /* carga arbol ejemplo. Ej 1 */
 addnodo(&a, 15);
 addnodo(&a->izq, 10);
 addnodo(&a->izq->izq, 7);
 addnodo(&a->izq->izq, 25);
 addnodo(&a->izq->der, 12);
 addnodo(&a->izq->der, 12);

 addnodo(&a->der, 20);
 addnodo(&a->der->izq, 16);
 addnodo(&a->der->der, 25);

 claves(a,0,0,0,0);
 return 0;


}

void addnodo(arbol* a, int e) {
    *a = (arbol)malloc(sizeof(NODO));
    (*a)->dato = e;
    (*a)->izq = NULL;
    (*a)->der = NULL;
}


//ejer 1

void claves(arbol a,int cmen,int cmay,int nmen,int nmay){
   if (a!=NULL){
        cmen=10000;
        cmay=0;
        if (a->izq!=NULL)
            clavemenor(a->izq,&cmen,&nmen,1);
        else{
            cmen=a->dato;
            nmen=0;
        }
        if (a->der!=NULL)
            clavemayor(a->der,&cmay,&nmay,1);
        else{
            cmay=a->dato;
            nmay=0;
        }
        printf("la clave menor del ABB es %d en el nivel %d y la clave mayor es %d en el nivel %d.",cmen,nmen,cmay,nmay);
   }
   else
        printf("el arbol es nulo, por lo tanto no hay clave menor y mayor.");
}


void clavemenor(arbol a,int *cmen,int *nmen,int nivact){
    if (a!=NULL){
        if (a->dato<(*cmen) && a->izq!=NULL && a->der!=NULL){
            *cmen=a->dato;
            *nmen=nivact;
        }
        clavemenor(a->izq,cmen,nmen,nivact+1);
        clavemayor(a->der,cmen,nmen,nivact+1);
    }
}



void clavemayor(arbol a, int *cmay,int *nmay,int nivact){
    if (a!=NULL){
        if (a->dato>(*cmay) && a->izq!=NULL && a->der!=NULL){
            *cmay=a->dato;
            *nmay=nivact;
        }
        clavemayor(a->izq,cmay,nivact,nivact+1);
        clavemayor(a->der,cmay,nivact,nivact+1);

    }
}







// ejer 2

int verifica(arbol a,pos p,int k,int niv){
    if (!nulo(p)){
        if (niv==k){
            c=hijomasizq(p,a);
            int grado=0;
            int cmayor=0,cmenor=0;
            while (!nulo(c) || (!cmayor && !cmenor ){
                if (strcmp(info(p,a),info(c,a))>0)
                    cmenor=1;
                if (strcmp(info(p,a),info(c,a))<0)
                    cmayor=1;
                c=hermanoder(c,a);
            }
            if (cmayor && cmenor);
                return verifica(a,hermanoder(p,a),k,niv);
            else return 0;
        }
        else
            return verifica(a,hijomasizq(p,a),k,niv+1) && verifica(a,hermanoder(p,a),k,niv);
    }
    else return 1;
}


// ejer 3


int menorgrado(int mat[][N],int N){
    int i=0,j=0;
    int grado,ver=0,gmin=1000;
    while (i<N){
        grado=0;
        if (mat[i][i]==1){
            while (i>=j){
                    if (mat[i][j]==1)
                        grado++;
                    j++;
            }
            if (grado % 2 == 0 && grado<gmin){
                gmin=grado;
                ver=i;
            }
        }
        i++;
        j=0;
    }
    return ver;
}





