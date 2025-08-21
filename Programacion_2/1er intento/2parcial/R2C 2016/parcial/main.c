#include <stdio.h>
#include <stdlib.h>

int main()
{

}

// ejer 1

int cantgrados(arbol a,int k){

    int cont=0;
        while(a!=NULL){
          if (contnodos(a->izq)==k){  // grado de la raiz
                    if (!verifica(a->izq,k,1))
                        cont++;
          }
          else
                if (!verifica(a->izq,k,0))
                    cont++;
          a=a->der;
        }
    return cont;
}

int contnodos(arbol a){
    if (a!=NULL){
        return 1+contnodos(a->der);

    }
    else return 0;


}
int verifica(arbol a,int k,int flag){
    if (a!=NULL){
            int gr=contnodos(a->izq);
        if (gr==k && !flag)
                return 1 && verifica(a->izq,k,1) && verifica(a->der,k,1);
        else
            if (gr==k)
                return 0;
            else
            return verifica(a->izq,k,flag) && verifica(a->der,k,flag);
    }
    else return flag;
  }




  // ejer 2

  int nivelv(arbol a,pos p,int nivel,int fvocal){
    pos c;
 if (!nulo(p)){
   if (!fvocal){
        c=hijomasizq(p,a);
        while (!nulo(c) && !vocal(a,c))
            c=hermanoder(c);
        if (!nulo(c))
            return 1 && nivelv(a,hijomasizq(p,a),nivel+1,0) &&nivelv(a,hermanoder(p,a),nivel,1)

  }
  else return nivelv(a,hijomasizq(p,a),nivel+1,0) && nivelv(a,hermanoder(p,a),nivel,1);
 }
 else return 1;
}











//ejer 3


int mayorv(int mat[MAX][],int N,int i,int j,int vermax,float costmaxprom,int cont,int cost){

    if (j<N){
        if (i<N){
           if (mat[i][j]!=0){
                cost+=mat[i][j];
                cont++;
            }

            return mayorv(mat,N,i+1,j,vermax,costmaxprom,cont,cost);
        }
        else{
            float prom=0;
            if (cont!=0)
             prom=(float)cost/cont;
            if (prom>costmaxprom){
                costmaxprom=prom;
                vermax=j;
            }
            return mayorv(mat,N,0,j+1,vermax,costmaxprom,0,0);
        }
    }
    else return vermax;
}

