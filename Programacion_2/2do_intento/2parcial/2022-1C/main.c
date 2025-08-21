#include <stdio.h>
#include <stdlib.h>

typedef int TelememtoA;
typedef struct nodo{
    TelememtoA dato;
    struct nodo * izq,der;}nodo;

typedef struct nodo * arbol;



int main(){


}


int grado(arbol a){
    int cont=0;

    while (a!=NULL){
        cont++;
        a=a->der;
    }
    return cont;
}


int claves(arbol a,int niv,int k){              //nivel arranca en 1        tarde 7:23 y 4:22 en revisar

    if (a!=NULL && niv<k){
            if (grado(a->izq) % 2 ==1)   // grado impar
                return a->dato+claves(a->izq,niv+1,k)+claves(a->der,niv,k);
            else return claves(a->izq,niv+1,k)+claves(a->der,niv,k);
    }
    else
        return 0;

}

// ejercicio 2


int esvocal(char a){
    a=tolower(a);
    if (a=='a' || a=='e' || a=='i' || a=='o' || a=='u' ||)
        return 1;
    else return 0;
}


int verifica(arbol a,pos p){                    // tarde 11:22 minutos
    pos c;
    int gr=0;
    int flag=0;
    if(!nulo(p) && esvocal(info(p,a))){
        c=hijomasizq(p,a);
       if (!nulo(c)){               //no es hoja
        while (!nulo(c) && !flag){
            gr++;
            if (esvocal(info(c)))
                c=hermanoder(c,a);
            else
                flag=1;
        }
        if (!flag && gr % 2==0)
            return 1;
        else
            return verifica(a,hijomasizq(p,a))||verifica(a,hermanoder(p,a));
       }
       else
            return verifica(a,hermanoder(p,a));



    }
    else
        return 0;

}

typedef struct{
    int grado;}Tvec;


}

void generavec(int mat[][N] ,Tvec vec[N],int N,int i,int j,int *k,int grS){     // invoco con k,i y j = 0
    if (i<N){
        if (j<N){
            if (mat[i][i]==1)          // tiene bucle
                 if (mat[i][j]==1)
                    generavec(mat,N,i,j+1,k,grS+mat[i][j]);
                 else
                    generavec(mat,N,i,j+1,k,grS);
            else
                generavec(mat,N,i+1,0,k,0);
        }
         else{
            if (mat[i][i]==1){
             vec[*k].vert=i+1;
             vec[*k].grado=grS;
            }
              generavec(mat,vec,N,i+1,0,k+1,0);
         }
    }

}



















