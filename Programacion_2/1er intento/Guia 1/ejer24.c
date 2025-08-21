#include <stdio.h>




 void posmatriz(int mat[3] [3],int n,int m);
 void promediocol(int mat[3] [3], int n, int m);
int main(){
    int mat[3] [3] = { {1,1,67}, {1,1,1}, {1,2,3} };
    int n=3;
    int m=3;
    posmatriz(mat,n,m);
    promediocol(mat,n,m);
 return 0;
}

void posmatriz(int mat[3] [3],int n,int m){
  int i=0;
  int j=0;
  int x;
        printf("ingrese un valor para su busqueda \n");
        scanf("%d",&x);
        while ((x!=mat[i][j]) && (i<n)){
          while ((x!=mat[i][j]) && (j<m)) {
                    j++;
                    printf("%d \n",mat[i][j]);
           }
           if (x!=mat[i][j]){
              j=0;
              i++;
           }
        }
         if (i==n)
             printf("el numero ingresado no esta en la matriz\n");
         else
             printf("el numero ingresado se encuentra por primera vez en la fila %d columna %d \n",i+1,j+1);
    }


void promediocol(int mat[3] [3], int n, int m){
    printf("promediocol \n");
    int i=0,j=0;
    int acum=0;

    while (j<m){
        while (i<n){
            acum+=mat[i][j];
            i++;
        }
        i=0;
        printf("promedio de columna %d: %d \n",j+1,acum/n);
        acum=0;
        j++;
    }

}
