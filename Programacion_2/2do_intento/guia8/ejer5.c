#include <stdio.h>
#include <stdlib.h>
#define MAX 100


int main(){

int mat[MAX][MAX];
generadigrafo(mat);
int x;
int N=3;
int gradoent,gradosal;
printf("ingrese el numero de nodo que quiere analizar");
scanf("%d",&x);
gradoent=grado(mat,0,x,N);
gradosal=grado(mat,x,0,N);

printf("el grado de entrada de %d es %d , el grado de salida es %d y el grado del vertice es %d",x,gradoent,gradosal,gradoent-gradosal);
return 0;
}


void generadigrafo(int mat[][MAX]){
    mat[1][1]=0;
    mat[1][2]=3;
    mat[1][0]=0;
    mat[2][1]=8;
    mat[2][2]=1;
    mat[2][0]=45;
    mat[0][1]=1;
    mat[0][2]=2;
    mat[0][0]=0;
}


int grado(int mat[][MAX],int i,int j,int N){
  if (i<N){
    if (mat[i][j]!=0){
            return mat[i][j]+grado(mat,i+1,j,N);
    }
    else
        return grado(mat,i+1,j,N);

  }else return 0;

}
