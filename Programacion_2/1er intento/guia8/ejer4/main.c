#include <stdio.h>
#include <stdlib.h>
#define MAX 100

void generadigrafo(int mat[][MAX]);

int main(){
int i=3;
int j=3;
int mat[MAX][MAX];
generadigrafo(mat);
subyacente(mat,i,j);


}


void generadigrafo(int mat[][MAX]){

    mat[1][1]=0;
    mat[1][2]=1;
    mat[1][3]=0;
    mat[2][1]=0;
    mat[2][2]=1;
    mat[2][3]=1;
    mat[3][1]=1;
    mat[3][2]=0;
    mat[3][3]=0;
}

void subyacente(int mat[][MAX],int i,int j){
    int x,y;

    for (x=1;x<=i;x++){
        for (y=1;y<=j;y++)
            if (mat[x][y]==1){
                printf("%d %d cambio a %d %d \n",x,y,y,x);
                mat[y][x]==1;
            }
    }

}



