#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("Hello world!\n");
    return 0;
}

int recorrobosque(arbol a,int k1,int k2){
    int cont=0;
    int niv=1;
        while (a!=NULL){
            if (niv>=k1 && a->dato<0)
                cont++;
            else
                cont+=recorrearbol(a->izq,k1,k2,niv);
            a+a->der;

        }
    return cont;

}

int recorroarbol(arbol a,int k1,int k2,int niv){

    if (a!=NULL){
        if (niv>=k1 && niv<=k2 && a->dato<0)
                return 1;
            else
                if (niv<=k2)
                  return recorroarbol(a->izq,k1,k2,niv+1)||recorroarbol(a->der,k1,k2,niv);
                else return 0;

    }
    else return 0;
}

int grado(arbol a,pos c){
    int cont=0;
    while(!nulo(c)){
        cont++;
        c=hermanoder(c,a);
    }
    return cont;


}
void maxmin(arbol a, pos p,int *ming,*maxg,int k,int niv){
    pos c;
    int gact;
    if (!nulo(p) && niv==k){
        c=hijomasizq(p,a);
        gact=grado(a,c);
        if (gact>*maxg)
            *maxg=gact;

        if (gact>*ming)
            *ming=gact;
    }
    else
        if (!nulo(p) && niv<k)
            maxmin(a,hijomasizq(p,a),ming,maxg,k,niv+1)
}

void quedevuelve(mat[][N],int N){

    int flag;
    if (flag==1)
        printf("los grafos son inducidos");
    else
        if (!flag)
            printf("ninguno es subgrafo de ninguno");
    else
    if (flag==2)
        printf("g es subgrafo de g prima");
    else
        if (flag==3)
            printf("g prima es subrafo de g");
}

int (mat[][N],int N){               // 0 2 3
    int flag=1;                     // 3 0 6
    int i=0,j=0;                    // 8 3 0
    while (i<N && flag){
        while (j<N && flag){
           if (flag>1)      // es inducido o no
                if (flag==2 && mat[i][j]<mat[j][i])

        }
    }



    }


















