#include <stdio.h>
#include <stdlib.h>
#define MAX 100

void generadigrafo(int mat[][MAX]);
int comprueba(int mat[][MAX],int N);
int main(){
    int i=3;
    int j=3;
    int mat[MAX][MAX];
    generadigrafo(mat);
    int N=3;
    if (comprueba(mat,N))
        printf("el grafo G' no es subgrafo de G");
    else printf("el grafo G' es subgrafo de G");
   return 0;
}


int comprueba(int mat[][MAX],int N){
    int x=0;
    int y=0;
    int flag=0;
    while (y<N && !flag){
            while (x<y && !flag){
                    if (mat[x][y]==1 && mat[y][x]==0)
                        flag=1;
                    else x++;
            }
            x=0;
            y++;

    }
    return flag;
}


void generadigrafo(int mat[][MAX]){

    mat[0][0]=0;
    mat[0][1]=1;
    mat[0][2]=0;
    mat[1][0]=1;
    mat[1][2]=1;
    mat[1][1]=0;
    mat[2][1]=1;
    mat[2][2]=0;
    mat[2][0]=0;
}




