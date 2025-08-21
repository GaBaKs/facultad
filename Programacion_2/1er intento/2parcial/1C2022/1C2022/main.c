#include <stdio.h>
#include <stdlib.h>












// ejer 2

int verifica(arbol a,pos p){

    if (!nulo(p)){
        if (vocal(a,p)){
            c=hijomasizq(p,a);
            int gradoa=grado(a,c);
            if (gradoa % 2 == 0 && gradoa!=0)
                return 1;
            else
                return verifica(a,hijomasizq(p,a))||verifica(a,hermanoder(p,a));
        }
        else
            return verifica(a,hijomasizq(p,a))||verifica(a,hermanoder(p,a));

    }

    else return 0;


}

int grado(arbol a, pos p){
    int gradoa=0;
    while (!nulo(p) && vocal(a,p)){
        gradoa++;
        p=hermanoder(p,a);
    }
    if (!nulo(p))
            return 0;
    else
        return gradoa;



}


int vocal(arbol a, pos p){
    if (info(p,a)=="a" || info(p,a)=="e" || info(p,a) = "i" || info(p,a)=="o" || info(p,a)== "u")
        return 1;
    else return 0;

}


//ejer 1


#include <stdio.h>
#include <stdlib.h>
int main(){
    arbol a;

    a=NULL;
    incioarbol(&a);
    printf("la suma de los elementos arriba de k es de %d",suma(a,k,0));

}

int suma(arbol a,int k,int niv){
    if (a!=NULL){
        if (niv>k)
           return 0;
        else
            if (grado(a->izq) % 2 != 0)
                return a->dato+suma(a->izq,k,niv+1)+suma(a->der,k,niv);
            else return suma(a->izq,k,niv+1)+suma(a->der,k,niv);
    }
    else return 0;
}


int grado(arbol a){

    if (a!=NULL)
        return 1+grado(a->der)
    else return 0;
}


int suma(arbol a, int K,int niv){

    if (a!=NULL){
         if (niv<k)
            if (grado(a->izq) % 2 ==1)
                return a->dato+suma(a->izq,K,niv+1)+suma(a->der,K,niv);
            else
                return suma(a->izq,K,niv+1)+suma(a->der,K,niv);
        else
            return 0;
    }
    else
        return 0;


    int grado(arbol a){
        if (a!=NULL)
            return 1+grado(a->der);

        else
            return 0;
    }
}
// ejer 3






generavec(vec,N,0,0,mat,&k,0);

void generavec(Tvec vec[],int N, int i, int j,int mat[MAX][],int *k,int grado){
    if (i<N){
        if (j<N && mat[i][i]==1){
                if (mat[i][j]==1)
                    generavec(vec,N,i,j+1,mat,k,grado+1);
                else
                    generavec(vec,N,i,j+1,mat,k,grado);
        }
            else{
                if (mat[i][i]==1){
                    vec[*k].vertice=i+1;
                    vec[*k].grados=grado;
                    *k+=1;
                }
                generavec(vec,N,i+1,0,mat,k,0);
            }

    }
    else{
        for (int h=0;h<(*k);h++){
            printf("vertice: %d\n grado de salida: %d \t",vec[h].vertice,vec[h].grados);

        }
    }

}





